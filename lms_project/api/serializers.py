from rest_framework import serializers
from lms_app.models import AddBook

class BookSerializers(serializers.ModelSerializer):
    class Meta:
        model = AddBook
        fields = '__all__'
        