from pydantic import BaseModel
from tracardi.domain.entity import Entity


class TwitterCredentials(BaseModel):
    consumer_key: str
    consumer_secret: str
    access_token: str
    access_token_secret: str


# class TwitterUser(BaseModel):
#     id: str
#     screen_name: str
#     location: str = None
#     lang: str = None
#     description: str = None


class Config(BaseModel):
    source: Entity
    type: str = 'tweet'
    message: str
