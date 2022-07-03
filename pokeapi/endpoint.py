from typing import Iterator, TypeVar, Generic, Type

from pydantic import BaseModel
from requests_toolbelt import sessions

ResourceListType = TypeVar('ResourceListType')
ResourceType = TypeVar('ResourceType')


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

    def paginator(self, limit: int = 20) -> Iterator[ResourceListType]:
        resource_list: ResourceListType = self.list(limit=limit, offset=0)
        yield resource_list

        while resource_list.next:
            response = self.session.get(resource_list.next)
            resource_list = self.resource_list_type(**response.json())
            yield resource_list

    def __getitem__(self, id_or_name: str) -> ResourceType:
        return self.get(id_or_name)

    def get(self, id_or_name: str) -> ResourceType:
        response = self.session.get(f'{self.service_uri}/{id_or_name}')
        return self.resource_type(**response.json())

    def list(self, limit: int, offset: int) -> ResourceListType:
        response = self.session.get(self.service_uri, params={'limit': limit, 'offset': offset})
        return self.resource_list_type(**response.json())
