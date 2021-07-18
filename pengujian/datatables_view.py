from django_datatables_view.base_datatable_view import BaseDatatableView
from django.utils.html import escape
from .models import DataPengujian
from django.db.models import Q

import functools
import operator

class DataPengujianTables(BaseDatatableView):
    # The model we're going to show
    model = DataPengujian
    columns = ['data_uji_id', 'cf_combine', 'kelas', 'target']    # define the columns that will be returned

    # define column names that will be used in sorting
    # order is important and should be same as order of columns
    # displayed by datatables. For non sortable columns use empty
    # value like ''

    order_columns = ['data_uji_id', 'cf_combine', 'kelas', 'target'] 
    # set max limit of records returned, this is used to protect our site if someone tries to attack our site
    # and make it return huge amount of data
    max_display_length = 500


    def render_column(self, row, column):
        # # We want to render user as a custom column
        if column == 'target':
            # escape HTML for security reasons
            return escape('{0}'.format(row.data_uji.target))
        else:
            return super(DataPengujianTables, self).render_column(row, column)

    def filter_queryset(self, qs):
        # use parameters passed in GET request to filter queryset

        # simple example:
        search = self.request.GET.get('search[value]', None)
        lookups = [
            'data_uji_id__istartswith',
            'cf_combine__istartswith',
            'target__istartswith',
            'kelas__istartswith',
        ]

        or_queries = [Q(**{lookup: search}) for lookup in lookups]


        if search:
            qs = qs.filter(functools.reduce(operator.or_, or_queries))

        # more advanced example using extra parameters
        # filter_customer = self.request.GET.get('customer', None)

        # if filter_customer:
        #     customer_parts = filter_customer.split(' ')
        #     qs_params = None
        #     for part in customer_parts:
        #         q = Q(customer_firstname__istartswith=part)|Q(customer_lastname__istartswith=part)
        #         qs_params = qs_params | q if qs_params else q
        #     qs = qs.filter(qs_params)
        return qs