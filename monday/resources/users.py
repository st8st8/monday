from monday.resources.base import BaseResource
from monday import query_joins
import json


class UserResource(BaseResource):
    def __init__(self, token):
        super().__init__(token)

    def fetch_users(self, **kwargs):
        query = query_joins.get_users_query(**kwargs)
        return json.loads(self.client.execute(query))
