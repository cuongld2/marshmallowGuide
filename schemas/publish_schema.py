import re

from marshmallow import Schema, fields, validate

from schemas.user_schema import UserSchema


class PublishSchema(Schema):
    regex_for_published_date = r"Jan?|Feb?|Mar?|Apr?|May|Jun?|Jul?|Aug?|Sep?|Oct?|Nov?|Dec?\s+\d{1,2}"
    regex_for_path = r"^(.+)\/([^/]+)$"
    user_schema = UserSchema()

    type_of = fields.Str(required=True, allow_none=False, )
    id = fields.Int(required=True, allow_none=False, )
    title = fields.Str(required=True, allow_none=False)
    description = fields.Str(required=True, allow_none=False)
    readable_publish_date = fields.Str(required=True, allow_none=False,
                                       validate=validate.Regexp(regex_for_published_date))
    slug = fields.Str(required=True, allow_none=False, )
    path = fields.Str(required=True, allow_none=False, validate=validate.Regexp(regex_for_path))
    url = fields.Str(required=True, allow_none=False, validate=validate.URL(error="Not a valid URL for url field"))
    comments_count = fields.Int(required=True, allow_none=False)
    positive_reactions_count = fields.Int(required=True, allow_none=False)
    collection_id = fields.Int(required=True, allow_none=True)
    published_timestamp = fields.DateTime(required=True, allow_none=False)
    cover_image = fields.URL(required=True, allow_none=True)
    social_image = fields.URL(required=True)
    canonical_url = fields.URL(required=True)
    created_at = fields.DateTime(required=True, allow_none=False)
    edited_at = fields.DateTime(required=True, allow_none=True)
    crossposted_at = fields.DateTime(required=True, allow_none=True)
    published_at = fields.DateTime(required=True, allow_none=False)
    last_comment_at = fields.DateTime(required=True, allow_none=True)
    tag_list = fields.List(fields.Str, required=True, allow_none=True)
    tags = fields.Str(required=True, allow_none=True)
    user = fields.Nested(user_schema)


