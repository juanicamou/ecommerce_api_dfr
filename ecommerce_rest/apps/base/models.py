from operator import mod
from pyexpat import model
from tabnanny import verbose
from django.db import models


class BaseModel(models.Model):

    id = models.AutoField(primary_key=True)
    state = models.BooleanField('State', default=True)
    created_date = models.DateField('Creation date', auto_now=False, auto_now_add=True)
    modified_date = models.DateField('Modification date', auto_now=True, auto_now_add=False)
    deleted_date = models.DateField('Removal date.', auto_now=True, auto_now_add=False)

    class Meta:
        abstract = True
        verbose_name = 'Base Model'
        verbose_name_plural = 'Base Models'