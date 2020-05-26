from marshmallow import Schema, fields, validate


class UserSchema(Schema):
    name = fields.Str(required=True, allow_none=False, )
    username = fields.Str(required=True, allow_none=False, )
    twitter_username = fields.Str(required=True, allow_none=True)
    github_username = fields.Str(required=True, allow_none=True)
    website_url = fields.URL(required=True, allow_none=True)
    profile_image = fields.URL(required=True, allow_none=True)
    profile_image_90 = fields.URL(required=True, allow_none=True)










