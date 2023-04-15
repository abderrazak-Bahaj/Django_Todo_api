from .models import TodoItem
from rest_framework import serializers

class TodoItemSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()
    def get_image(self, obj):
        request = self.context.get('request')
        if obj.image:
            return request.build_absolute_uri(obj.image.url)
        return None
    class Meta:
        model = TodoItem
        fields = ['title', 'content', 'completed', 'image']

