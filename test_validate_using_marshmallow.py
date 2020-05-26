import requests

from schemas.publish_schema import PublishSchema


def test_validate_publish_schema():
    publish_schema = PublishSchema()
    json = requests.get('https://dev.to/api/articles?tag=Java').json()
    for each_object in json:
        publish_schema.load(each_object)
