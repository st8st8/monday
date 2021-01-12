"""
monday.client
~~~~~~~~~~~~~~~~~~

:copyright: (c) 2019 by Christina D'Astolfo.
:license: Apache2, see LICENSE for more details.
"""

from .__version__ import __version__
from . import resources


class MondayClient:
    def __init__(self, token):
        """
        :param token: API Token for the new :class:`BaseResource` object.
        """
        self.items = resources.ItemResource(token=token)
        self.updates = resources.UpdateResource(token=token)
        self.tags = resources.TagResource(token=token)
        self.boards = resources.BoardResource(token=token)
        self.users = resources.UserResource(token=token)
        self.groups = resources.GroupResource(token=token)
        self.column_values = resources.ColumnValueResource(token=token)

    def __str__(self):
        return f'MondayClient {__version__}'

    def __repr__(self):
        return f'MondayClient {__version__}'
