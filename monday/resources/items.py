import json

from monday.resources.base import BaseResource
from monday import query_joins


class ItemResource(BaseResource):
    def __init__(self, token):
        super().__init__(token)

    def create_item(self, board, group, item_name, column_values=None):
        query = query_joins.mutate_item_query(board, group, item_name, column_values)
        return json.loads(self.client.execute(query))

    def create_subitem(self, parent_item_id, subitem_name, column_values=None):
        query = query_joins.mutate_subitem_query(parent_item_id, subitem_name, column_values)
        return json.loads(self.client.execute(query))

    def fetch_items_by_column_value(self, board, column=None, value=None):
        query = query_joins.get_item_query(board, column, value)
        return json.loads(self.client.execute(query))

    def fetch_items_by_id(self, ids):
        query = query_joins.get_item_by_id_query(ids)
        return json.loads(self.client.execute(query))

    def move_item_to_group(self, item_id, group_id):
        query = query_joins.move_item_to_group_query(item_id, group_id)
        return json.loads(self.client.execute(query))

    def archive_item(self, item_id):
        query = query_joins.archive_item_query(item_id)
        return json.loads(self.client.execute(query))

    def change_item_value(self, board, item_id, column, value):
        query = query_joins.update_item_query(board, item_id, column, value)
        return json.loads(self.client.execute(query))

    def change_multiple_column_values(self, board, item_id, column_values):
        query = query_joins.update_multiple_column_values_query(board, item_id, column_values)
        return json.loads(self.client.execute(query))

    def add_file_to_column(self, item_id, column_id, file):
        query = query_joins.add_file_to_column_query(item_id, column_id)
        return json.loads(self.file_upload_client.execute(query, variables={'file': file}))
