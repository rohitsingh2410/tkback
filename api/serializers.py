from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from django.contrib.auth.hashers import make_password
from .models import Categories,Leads


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id','username','password')
        extra_kwargs = {'password':{'write_only':True,'required':True }}

        def create(self,validated_data):
            user = User.objects.create_user(**validated_data)
            Token.objects.create(user=user)
            print(user)
            return user
        
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Categories
        fields = ['category_name']


class LeadsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Leads
        fields = ['customer_name','customer_username','customer_phone','lead_converted','lead_time','lead_category','lead_isactive']