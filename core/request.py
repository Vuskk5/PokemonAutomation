from json import JSONDecodeError
from typing import TypeVar, Generic

import pydantic
import requests


ContentType = TypeVar('ContentType', bound=pydantic.BaseModel)


class APIResponse(requests.Response, Generic[ContentType]):
    def __init__(self, response: requests.Response, data_type: ContentType):
        super().__init__()

        self.response = response
        self.data_type = data_type

        for key, value in response.__dict__.items():
            self.__dict__[key] = value

    def data(self) -> ContentType:
        return self.data_type.construct(**self.response.json())
