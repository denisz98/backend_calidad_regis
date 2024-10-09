from rest_framework import serializers
import os


class CustomSerializer(serializers.ModelSerializer):
    file_fields = []

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        for file_field in self.file_fields:
            if file_field in representation:
                file_path = getattr(instance, file_field)
                if file_path:
                    file_name = os.path.basename(file_path.name)
                    representation[file_field] = file_name
                else:
                    representation[file_field] = None
        return representation
