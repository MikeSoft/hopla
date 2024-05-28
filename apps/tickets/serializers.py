from rest_framework import serializers
from .models import Ticket, ImageUpload


class ImageUploadSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImageUpload
        fields = ["id", "ticket", "image", "uploaded_at"]
        read_only_fields = ["id", "uploaded_at"]


class TicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        fields = ["id", "user", "num_images", "status", "created_at", "updated_at"]
        read_only_fields = [
            "id",
            "user",
            "status",
            "created_at",
            "updated_at",
            "images",
        ]

    def get_images(self, obj):
        return ImageUploadSerializer(obj.images.all(), many=True).data

    def create(self, validated_data):
        validated_data["user"] = self.context["request"].user
        return super().create(validated_data)
