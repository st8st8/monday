import json

from monday.resources.base import BaseResource
from monday import query_joins


class GroupResource(BaseResource):
    def __init__(self, token):
        super().__init__(token)

    def get_groups_by_board(self, board_ids):
        query = query_joins.get_groups_by_board_query(board_ids=board_ids)
        return json.loads(self.client.execute(query))

    def get_items_by_group(self, board_id, group_id):
        query = query_joins.get_items_by_group_query(board_id=board_id, group_id=group_id)
        return json.loads(self.client.execute(query))

    def create_group(self, board_id, group_name):
        query = query_joins.create_group_query(board_id=board_id, group_name=group_name)
        return json.loads(self.client.execute(query))

    def duplicate_group(self, board_id, group_id):
        query = query_joins.duplicate_group_query(board_id=board_id, group_id=group_id)
        return json.loads(self.client.execute(query))

    def archive_group(self, board_id, group_id):
        query = query_joins.archive_group_query(board_id=board_id, group_id=group_id)
        return json.loads(self.client.execute(query))

    def delete_group(self, board_id, group_id):
        query = query_joins.delete_group_query(board_id=board_id, group_id=group_id)
        return json.loads(self.client.execute(query))
