# -*- coding: utf-8 -*-

from rest_framework import serializers

from blogging.models import Post, Category
from bloggers.serializers import AuthorSerializer


class PostListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = ['title','image', 'summary', 'release_date']


class PostSerializer(serializers.ModelSerializer):

    user = AuthorSerializer(read_only=True)

    class Meta:
        model = Post
        fields = '__all__'

    def validate(self, data):
        """
        Check that image or video have something.
        """
        image = data.get('image', None)
        url = data.get('url', None)
        if (image == '' or image == None) and  (url == '' or url == None):
            raise serializers.ValidationError("Image or video must be set.")
        return data