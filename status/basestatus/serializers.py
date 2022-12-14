from dataclasses import field
from rest_framework.serializers import ModelSerializer
from basestatus.models import Note

class NoteSerializer(ModelSerializer):
    class Meta:
        model = Note
        fields = '__all__'