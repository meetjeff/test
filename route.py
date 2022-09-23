from route_model import PostRequest,PostResponse,AddRequest,AddResponse,ConvertRequest,ConvertResponse,decoratorRequest
from flask_apispec import use_kwargs, MethodResource, marshal_with, doc
import requests
import yaml
import threading

class Hello(MethodResource):
    @doc(description = "question1-a", tags = ['question1'])
    def get(self):
        return "Hello!"

class Item(MethodResource):
    @doc(description = "question1-b", tags = ['question1'])
    @use_kwargs(PostRequest,location = "json")
    @marshal_with(PostResponse, code = 200)
    def post(self,**kwargs):        
        input = {}
        input["item_name"] = kwargs['item_name']
        # 執行功能如新增資料
        message = {}
        if input != {}:
            message["result"] = "success"
        else:
            message["result"] = "failure"    
        return message

class Spec(MethodResource):
    @doc(description = "question1-c", tags = ['question1'])
    def get(self):
        spec = yaml.dump(requests.get("http://localhost:5000/json").json())
        print(spec)
        return spec

class Add(MethodResource):
    @doc(description = "A function with two parameters, a and b. The return value is a+b.", tags = ['question2'])
    @use_kwargs(AddRequest, location = "query")
    @marshal_with(AddResponse, code = 200)
    def get(self,**kwargs):
        res = {}
        res["sum"] = sum((kwargs['a'],kwargs['b']))
        return res

class Convert(MethodResource):
    @doc(description = "Convert a ASCII numbers string to TEXT. The text matches a regular expression, '[a-zA-Z]+'gm", tags = ['question3'])
    @use_kwargs(ConvertRequest, location = "query")
    @marshal_with(ConvertResponse, code = 200)
    def get(self,**kwargs):
        s = kwargs["ASCII_numbers"]
        t = ''
        i = 0
        while i < len(s)-1:
            if int(s[i:i+2]) in range(65,91) or int(s[i:i+2]) in range(97,100):
                t += chr(int(s[i:i+2]))
                i += 2
            else:
                t += chr(int(s[i:i+3]))
                i += 3
        res = {}
        res["text"] = t
        return res

def lockdecorator(func):
    lock = threading.Lock()
    def warp(self,**kwargs):
        lock.acquire()
        res = func(self,**kwargs)
        lock.release()
        return res
    return warp
    
#透過threading模組的鎖將sayHello程式碼資源鎖定，執行完成後才釋放，如此可確保function一次只給一個程序啟動

class sayHello(MethodResource):
    @doc(description = "Only a single instance of a program is running.", tags = ['question4'])
    @use_kwargs(decoratorRequest, location = "query")
    @lockdecorator
    def get(self, **kwargs):
        return f"Hi, {kwargs['name']}. Your message: {kwargs['message']}"