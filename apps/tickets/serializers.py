from rest_framework import serializers
from .models import Ticket, ImageUpload


class TicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        fields = ["id", "user", "num_images", "status", "created_at", "updated_at"]
        read_only_fields = ["id", "user", "status", "created_at", "updated_at"]

    def create(self, validated_data):
        validated_data["user"] = self.context["request"].user
        return super().create(validated_data)


class ImageUploadSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImageUpload
        fields = ["id", "ticket", "image_url", "uploaded_at"]
        read_only_fields = ["id", "uploaded_at"]
