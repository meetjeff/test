# OpenAPI
## /
###### -GET-
**Swagger UI**  

## /api/hello
###### -GET-
question1-a 

**Input Parameters :**
* No parameters

**Success Example**
```yaml
"Hello!"
```

## /api/item
###### -POST-
question1-b

**Input Parameters :**
* item_name　　　&thinsp;( string )

**Success Example**  
```yaml
{
  "result": "success"
}
```

## /api/spec
###### -GET-
question1-c 

**Input Parameters :**
* No parameters

**Success Example**
```yaml
"definitions:\n  AddResponse:\n    properties:\n      sum:\n        example: 123\n        type: number\n    type: object\n  ConvertResponse:\n    properties:\n      text:\n        example: textstring\n        type: string\n    type: object\n  PostRequest:\n    properties:\n      item_name:\n        type: string\n    required:\n    - item_name\n    type: object\n  PostResponse:\n    properties:\n      result:\n        example: success\n        type: string\n    type: object\ninfo:\n  title: \"Jeff - \\u5F8C\\u7AEF\\u8003\\u8A66(Python)\"\n  version: v1\npaths:\n  /api/hello:\n    get:\n      description: question1-a\n      parameters: []\n      responses: {}\n      tags:\n      - question1\n  /api/item:\n    post:\n      description: question1-b\n      parameters:\n      - in: body\n        name: body\n        required: false\n        schema:\n          $ref: '#/definitions/PostRequest'\n      responses:\n        '200':\n          description: ''\n          schema:\n            $ref: '#/definitions/PostResponse'\n      tags:\n      - question1\n  /api/spec:\n    get:\n      description: question1-c\n      parameters: []\n      responses: {}\n      tags:\n      - question1\n  /question2/add:\n    get:\n      description: A function with two parameters, a and b. The return value is a+b.\n      parameters:\n      - in: query\n        name: a\n        required: true\n        type: number\n      - in: query\n        name: b\n        required: true\n        type: number\n      responses:\n        '200':\n          description: ''\n          schema:\n            $ref: '#/definitions/AddResponse'\n      tags:\n      - question2\n  /question3/convert:\n    get:\n      description: Convert a ASCII numbers string to TEXT. The text matches a regular\n        expression, '[a-zA-Z]+'gm\n      parameters:\n      - in: query\n        name: ASCII_numbers\n        required: true\n        type: string\n      responses:\n        '200':\n          description: ''\n          schema:\n            $ref: '#/definitions/ConvertResponse'\n      tags:\n      - question3\n  /question4/sayHello:\n    get:\n      description: Only a single instance of a program is running.\n      parameters:\n      - in: query\n        name: name\n        required: true\n        type: string\n      - in: query\n        name: message\n        required: true\n        type: string\n      responses: {}\n      tags:\n      - question4\nswagger: 2.0.0\n"
```
