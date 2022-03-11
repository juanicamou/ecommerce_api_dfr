from django.urls import path
from apps.products.api.views.general_views import MeasureUnitListAPIView, IndicatorListAPIView, ProductCategoryListAPIView

urlpatterns = [
    path('measure_units/', MeasureUnitListAPIView.as_view(), name = 'measure_units'),
    path('indicators/', IndicatorListAPIView.as_view(), name = 'indicators'),
    path('product_categories/', ProductCategoryListAPIView.as_view(), name = 'product_categories'),
   
]
