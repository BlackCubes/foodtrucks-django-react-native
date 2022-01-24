from collections import OrderedDict

from rest_framework import pagination
from rest_framework.response import Response


class CustomPageNumberPagination(pagination.PageNumberPagination):
    """
    A custom PageNumberPagination to be used for all API apps with a list of data.
    If there is a list of data, the `meta_data` key would be inserted to the JSON output
    that is an object with keys of `total_count` (total count of the list of data for all
    pages), `next` (a hyperlink for the next result, or `None`), and `previous` (a hyperlink
    for the previous result, or `None`. `None` for the initial start).

    Default count per page: 10.

    Query param to change the count per page: `count`.

    Maximum amount of pages: 100.
    """
    page_size = 10
    page_size_query_param = 'count'
    max_page_size = 100

    def get_paginated_response(self, data):
        return Response(OrderedDict([
            ('results', data),
            ('meta_data', OrderedDict([
                ('total_count', self.page.paginator.count),
                ('next', self.get_next_link()),
                ('previous', self.get_previous_link())
            ]))
        ]))
