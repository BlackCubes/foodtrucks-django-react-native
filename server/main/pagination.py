from collections import OrderedDict

from rest_framework import pagination
from rest_framework.response import Response


class CustomPageNumberPagination(pagination.PageNumberPagination):
    """
    """
    page_size = 1
    page_size_query_param = 'count'
    max_page_size = 100
    page_query_param = 'p'

    def get_paginated_response(self, data):
        return Response(OrderedDict([
            ('results', data),
            ('meta_data', OrderedDict([
                ('count', self.page.paginator.count),
                ('next', self.get_next_link()),
                ('previous', self.get_previous_link())
            ]))
        ]))
