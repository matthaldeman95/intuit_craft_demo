import django_tables2 as tables
from .models import DataPoint


class DataPointTable(tables.Table):
    class Meta:
        model = DataPoint
        attrs = {'class': "paleblue"}
