from apps.products.models import MeasureUnit, ProductCategory, Indicator
from rest_framework import serializers

class MeasureUnitSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = MeasureUnit
        exclude = ('state',) # This field is for internal use, it is used only if a logical elimination is done.


class ProductCategorySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = ProductCategory
        exclude = ('state',) # This field is for internal use, it is used only if a logical elimination is done.


class IndicatorSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Indicator
        exclude = ('state',) # This field is for internal use, it is used only if a logical elimination is done.