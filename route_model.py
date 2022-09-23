from marshmallow import Schema, fields

class PostRequest(Schema):
    item_name = fields.Str(doc="item_name", required = True)

class PostResponse(Schema):
    result = fields.Str(example="success")

class AddRequest(Schema):
    a = fields.Float(doc="integer_a", required = True)
    b = fields.Float(doc="integer_b", required = True)

class AddResponse(Schema):
    sum = fields.Float(example=123)

class ConvertRequest(Schema):
    ASCII_numbers = fields.Str(doc="ASCII_numbers", required = True)

class ConvertResponse(Schema):
    text = fields.Str(example="textstring")

class decoratorRequest(Schema):
    name = fields.Str(doc="name", required = True)
    message = fields.Str(doc="message", required = True)
