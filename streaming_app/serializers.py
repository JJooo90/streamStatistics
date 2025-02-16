from rest_framework import serializers
from .models import Chzzk
from .models import stremerVideo


# class ChzzkSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Chzzk
#         fields = '__all__'

class stremerVedio_Serializer(serializers.ModelSerializer):
    class Meta:
        model=stremerVideo
        fields='__all__'