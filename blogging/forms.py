# -*- coding: utf-8 -*-
from django.forms import ModelForm

from blogging.models import Post


class PostForm(ModelForm):

    class Meta:
        model = Post
        fields = '__all__'
        exclude = ['author']