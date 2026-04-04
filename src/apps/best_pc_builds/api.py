from django_bolt import BoltAPI

from config.components.bolt import openapi_config

api = BoltAPI(openapi_config=openapi_config)


@api.get('/')
async def hello():
    return {'message': 'Hello, World!'}
