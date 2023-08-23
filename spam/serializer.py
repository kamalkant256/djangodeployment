from rest_framework import serializers
from spam.models import UserMaster




class RegisterSerializer(serializers.Serializer):
    name = serializers.CharField(max_length =200)
    email = serializers.EmailField(max_length =200)
    mobile = serializers.CharField(max_length =200)
    
    
    class Meta:
        model = UserMaster
        fields = "__all__"
    