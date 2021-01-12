from monday.resources.base import BaseResource
from monday import query_joins
import json


class TagResource(BaseResource):
    def __init__(self, token):
        super().__init__(token)

    def fetch_tags(self, tag_ids=None):
        query = query_joins.get_tags_query(tag_ids)
        return json.loads(self.client.execute(query))

