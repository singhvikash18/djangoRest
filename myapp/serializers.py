from rest_framework import serializers
from .models import Emplyoee

class EmplyoeeSerializers(serializers.ModelSerializer):
    class Meta:
        model = Emplyoee
        fields = ['id','fullname','email','created']