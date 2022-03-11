from apps.products.models import MeasureUnit, ProductCategory, Indicator
from rest_framework import serializers

class MeasureUnitSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = MeasureUnit
        exclude = ('state','created_date', 'modified_date', 'deleted_date') # These fields are for internal use, they are used only if a logical elimination is done.


class ProductCategorySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = ProductCategory
        exclude = ('state','created_date', 'modified_date', 'deleted_date') # These fields are for internal use, they are used only if a logical elimination is done.


class IndicatorSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Indicator
        exclude = ('state','created_date', 'modified_date', 'deleted_date') # These fields are for internal use, they are used only if a logical elimination is done.