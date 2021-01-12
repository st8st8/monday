import json

from monday.resources.base import BaseResource
from monday import query_joins


class BoardResource(BaseResource):
    def __init__(self, token):
        super().__init__(token)

    def fetch_boards(self, **kwargs):
        query = query_joins.get_boards_query(**kwargs)
        return json.loads(self.client.execute(query))

    def fetch_boards_by_id(self, board_ids):
        query = query_joins.get_boards_by_id_query(board_ids)
        return json.loads(self.client.execute(query))

    def fetch_items_by_board_id(self, board_ids):
        query = query_joins.get_board_items_query(board_ids)
        return json.loads(self.client.execute(query))

    def fetch_columns_by_board_id(self, board_ids):
        query = query_joins.get_columns_by_board_query(board_ids)
        return json.loads(self.client.execute(query))
