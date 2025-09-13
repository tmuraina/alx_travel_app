from rest_framework import serializers
from .models import Listing

class ListingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Listing
        fields = ['id', 'title', 'description', 'location', 'price_per_night', 'created_at', 'updated_at', 'host']
        read_only_fields = ['id', 'created_at', 'updated_at']