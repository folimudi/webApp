from rest_framework import serializers
from list.models import Brother, Guest

class BrotherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brother
        fields = ('brother_id', 'first_n', 'last_n', 'status')

    def create(self, validated_data):
        return Brother.objects.create(**validated_data);

    def update(self, instance, args):
        instance.brother_id = validated_data.get('brother_id', instance.brother_id)
        instance.first_n = validated_data.get('first_n', instance.first_n)
        instance.last_n = validated_data.get('last_n', instance.last_n)
        instance.status = validated_data.get('status', instance.status)
        instance.save()
        return instance

class GuestSerializer(serializers.ModelSerializer):
    """docstring for GuestSerializer."""
    class Meta:
        model = Guest
        fields = ('first_n', 'last_n', 'gender','blacklisted' , 'host')
    def create(self, validated_data):
        return Guest.object.create(**validated_data)

    def update(self, instance, validated_data):
        instance.first_n = serializers.CharField(max_length = 30)
    	instance.last_n = serializers.CharField(max_length= 30)
    	instance.gender = serializers.CharField(max_length=1, choices=GENDER)
    	instance.blacklisted = serializers.BooleanField(default=False)
    	instance.host = models.ManyToManyField(Brother)
