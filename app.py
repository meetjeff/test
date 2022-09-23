from flask import Flask
from flask_restful import Api
from apispec import APISpec
from apispec.ext.marshmallow import MarshmallowPlugin
from flask_apispec.extension import FlaskApiSpec
from route import Hello, Item, Spec, Add, Convert, sayHello

app = Flask(__name__)
api = Api(app)
app.config.update({
    'APISPEC_SPEC': APISpec(
        title='Jeff - 後端考試(Python)',
        version='v1',
        plugins=[MarshmallowPlugin()],
        openapi_version='2.0.0'
    ),
    'APISPEC_SWAGGER_URL': '/jsonspec', 
    'APISPEC_SWAGGER_UI_URL': '/', 
    'JSON_AS_ASCII': False
})

docs = FlaskApiSpec(app)

api.add_resource(Hello, '/api/hello')
docs.register(Hello)
api.add_resource(Item, '/api/item')
docs.register(Item)
api.add_resource(Spec, '/api/spec')
docs.register(Spec)
api.add_resource(Add, '/question2/add')
docs.register(Add)
api.add_resource(Convert, '/question3/convert')
docs.register(Convert)
api.add_resource(sayHello, '/question4/sayHello')
docs.register(sayHello)


if __name__ == '__main__':
    app.run(debug = True)