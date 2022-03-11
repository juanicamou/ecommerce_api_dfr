from distutils.command.upload import upload
from statistics import mode
from tkinter import CASCADE
from tokenize import blank_re
from unicodedata import category
from django.db import models
from simple_history.models import HistoricalRecords

from apps.base.models import BaseModel

# Measure Unit

class MeasureUnit(BaseModel):
    description = models.CharField('Description', max_length=50, blank=False, null=False, unique=True)
    historical = HistoricalRecords

    @property
    def _history_user(self):
        return self.changed_by

    @_history_user.setter
    def _history_user(self, value):
        self.changed_by = value

    
    class Meta:
        verbose_name = 'Measure Unit'
        verbose_name_plural = 'Measure Units'

    def __str__(self):
        return self.description

# Product Category

class ProductCategory(BaseModel):
    description = models.CharField('Description', max_length=50, blank=False, null=False, unique=True)
    historical = HistoricalRecords

    @property
    def _history_user(self):
        return self.changed_by

    @_history_user.setter
    def _history_user(self, value):
        self.changed_by = value

    
    class Meta:
        verbose_name = 'Product Category'
        verbose_name_plural = 'Product Categories'

    def __str__(self):
        return self.description

# Offer indicator.

class Indicator(BaseModel):
    discount_value = models.PositiveSmallIntegerField(default=0)
    category_product = models.ForeignKey(ProductCategory, on_delete=models.CASCADE, verbose_name='Product Category')
    historical = HistoricalRecords

    @property
    def _history_user(self):
        return self.changed_by

    @_history_user.setter
    def _history_user(self, value):
        self.changed_by = value

    
    class Meta:
        verbose_name = 'Offer Indicator'
        verbose_name_plural = 'Offer Indicators'

    def __str__(self):
        return f'Category {self.category_product} offer: {self.discount_value}%'

# Product

class Product(BaseModel):
    
    name = models.CharField('Product Name', max_length=150, unique=True, blank=False, null=False)
    description = models.TextField('Product Description', blank=False, null=False)
    measure_unit = models.ForeignKey(MeasureUnit, on_delete=models.CASCADE, verbose_name='Measure Unit', null = True)
    product_category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE, verbose_name='Category Product', null = True)
    image = models.ImageField('Product Image', upload_to='products/', blank=True, null=True)

    historical = HistoricalRecords

    @property
    def _history_user(self):
        return self.changed_by

    @_history_user.setter
    def _history_user(self, value):
        self.changed_by = value

    
    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'

    def __str__(self):
        return self.name
