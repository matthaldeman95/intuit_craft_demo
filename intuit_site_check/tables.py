import django_tables2 as tables
from .models import DataPoint

class DataPointTable(tables.Table***REMOVED***:
    class Meta:
        model = DataPoint
        attrs = {'class': "paleblue"***REMOVED***