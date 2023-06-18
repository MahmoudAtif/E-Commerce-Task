from rest_framework import serializers


class OrderInputSerilaizer(serializers.Serializer):
    """Order Input Serilaizer"""
    
    state = serializers.CharField()
    city = serializers.CharField()
