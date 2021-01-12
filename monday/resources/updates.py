from monday.resources.base import BaseResource
from monday import query_joins


class UpdateResource(BaseResource):
    def __init__(self, token):
        super().__init__(token)

    def create_update(self, item_id, update_value):
        query = query_joins.create_update_query(item_id, update_value)
        return self.client.execute(query)

    def fetch_updates(self, limit, page=None):
        query = query_joins.get_update_query(limit, page)
        return self.client.execute(query)

