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
definitions:
  AddResponse:
    properties:
      sum:
        example: 123
        type: number
    type: object
  ConvertResponse:
    properties:
      text:
        example: textstring
        type: string
    type: object
  PostRequest:
    properties:
      item_name:
        type: string
    required:
    - item_name
    type: object
  PostResponse:
    properties:
      result:
        example: success
        type: string
    type: object
info:
  title: "Jeff - \u5F8C\u7AEF\u8003\u8A66(Python)"
  version: v1
paths:
  /api/hello:
    get:
      description: question1-a
      parameters: []
      responses: {}
      tags:
      - question1
  /api/item:
    post:
      description: question1-b
      parameters:
      - in: body
        name: body
        required: false
        schema:
          $ref: '#/definitions/PostRequest'
      responses:
        '200':
          description: ''
          schema:
            $ref: '#/definitions/PostResponse'
      tags:
      - question1
  /api/spec:
    get:
      description: question1-c
      parameters: []
      responses: {}
      tags:
      - question1
  /question2/add:
    get:
      description: A function with two parameters, a and b. The return value is a+b.        
      parameters:
      - in: query
        name: a
        required: true
        type: number
      - in: query
        name: b
        required: true
        type: number
      responses:
        '200':
          description: ''
          schema:
            $ref: '#/definitions/AddResponse'
      tags:
      - question2
  /question3/convert:
    get:
      description: Convert a ASCII numbers string to TEXT. The text matches a regular       
        expression, '[a-zA-Z]+'gm
      parameters:
      - in: query
        name: ASCII_numbers
        required: true
        type: string
      responses:
        '200':
          description: ''
          schema:
            $ref: '#/definitions/ConvertResponse'
      tags:
      - question3
  /question4/sayHello:
    get:
      description: Only a single instance of a program is running.
      parameters:
      - in: query
        name: name
        required: true
        type: string
      - in: query
        name: message
        required: true
        type: string
      responses: {}
      tags:
      - question4
swagger: 2.0.0
```
