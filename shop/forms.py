from django import forms
from django.forms import ModelForm
from django.db import models
from .models import Category, Shop, Article
from user.models import User


class ShopForm(ModelForm):
    class Meta:
        model = Shop
        exclude = ('user', 'market')
        #ields = '__all__'


class CategoryForm(ModelForm):
    class Meta:
        model = Category
        fields = '__all__'

class ArticleForm(ModelForm):
    class Meta:
        model = Article
        fields = '__all__'