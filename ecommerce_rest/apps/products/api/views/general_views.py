
from apps.base.api import GeneralListApiView
from apps.products.api.serializers.general_serializers import MeasureUnitSerializer, IndicatorSerializer, ProductCategorySerializer

class MeasureUnitListAPIView(GeneralListApiView): # ListAPIView only allows GET.
    serializer_class = MeasureUnitSerializer

class IndicatorListAPIView(GeneralListApiView): 
    serializer_class = IndicatorSerializer

class ProductCategoryListAPIView(GeneralListApiView): 
    serializer_class = ProductCategorySerializer