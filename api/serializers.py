from rest_framework import serializers
from blog import models

class BlogSerializer(serializers.ModelSerializer):
    
    class Meta:
        fields = [
            'title', 
            'text', 
            'image', 
            'tags', 
            'status'
    ]

    model = models.Blog