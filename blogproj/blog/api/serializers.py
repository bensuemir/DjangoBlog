from rest_framework import serializers
from django.contrib.auth.models import User
from blog.models import Post

class PostSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        queryset=User.objects.all(), slug_field='username', required=True
    )

    class Meta:
        model = Post
        fields = ['id', 'title', 'content', 'date_posted', 'author']

    def create(self, validated_data):
        author_username = validated_data.pop('author')
        author = User.objects.get(username=author_username)
        post = Post.objects.create(author=author, **validated_data)
        return post

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.content = validated_data.get('content', instance.content)
        instance.date_posted = validated_data.get('date_posted', instance.date_posted)
        author_username = validated_data.get('author', instance.author.username)
        instance.author = User.objects.get(username=author_username)
        instance.save()
        return instance

    def validate(self, data):
        if data['title'] == data['content']:
            raise serializers.ValidationError('Title and Content cannot be the same.')
        return data
    
    def validate_title(self, value):
        if len(value) < 3:
            raise serializers.ValidationError(f'Title must be at least 2 characters. Your number of characters is {len(value)}.')
        return value
