from rest_framework import serializers

from targets.models import Target

class TargetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Target
        fields = [
            'id',
            'user_id',
            'months',
            'title',
            'completed',
            'description',
            'price',
            'pros',
            'minuses',
            'images',
            'updated_at',
            'created_at'
        ]