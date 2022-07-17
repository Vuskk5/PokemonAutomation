from typing import Iterator, TypeVar, Generic, Type

from pydantic import BaseModel
from requests_toolbelt import sessions

from core.request import APIResponse
from models.utility import APIResource, APIResourceList

ResourceListType = TypeVar('ResourceListType', bound=APIResourceList)
ResourceType = TypeVar('ResourceType', bound=APIResource)


class Endpoint(Generic[ResourceType, ResourceListType]):
    def __init__(self,
                 session: sessions.BaseUrlSession,
                 service_uri: str,
                 resource_type: Type[BaseModel],
                 resource_list_type: Type):
        self.session = session
        self.service_uri = service_uri
        self.resource_type: ResourceType = resource_type
        self.resource_list_type: ResourceListType = resource_list_type

    def paginator(self, limit: int = 20) -> Iterator[APIResponse[ResourceListType]]:
        api_response: APIResponse[ResourceListType] = self.list(limit=limit, offset=0)
        yield APIResponse(response=api_response.response,
                          data_type=self.resource_list_type)

        while api_response.data().next:
            response = self.session.get(api_response.data().next)
            api_response = APIResponse(response=response,
                                       data_type=self.resource_list_type)
            yield api_response

    def __getitem__(self, id_or_name: str) -> APIResponse[ResourceType]:
        return self.get(id_or_name)

    def get(self, id_or_name: str) -> APIResponse[ResourceType]:
        response = self.session.get(f'{self.service_uri}/{id_or_name}')
        return APIResponse(response=response,
                           data_type=self.resource_type)

    def list(self, limit: int, offset: int) -> APIResponse[ResourceListType]:
        response = self.session.get(self.service_uri, params={'limit': limit, 'offset': offset})
        return APIResponse(response=response,
                           data_type=self.resource_list_type)
