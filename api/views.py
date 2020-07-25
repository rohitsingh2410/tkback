from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import action
from django.contrib.auth.models import User
from .serializers import UserSerializer,CategorySerializer,LeadsSerializer
from .models import Categories,Leads
from rest_framework import viewsets,status
from rest_framework.decorators import api_view


from django.contrib.auth.hashers import make_password



# Create your views here.

class UserViewSet(viewsets.ModelViewSet):
    def perform_create(self, serializer):
        password = make_password(self.request.data['password'])

        serializer.save(password=password)

    def perform_update(self, serializer):
        password = make_password(self.request.data['password'])

        serializer.save(password=password)
    queryset = User.objects.all()
    serializer_class = UserSerializer

#Update & Retrieve Caegories.
@api_view(['GET', 'POST'])
def categories(request):
    if request.method == 'POST':
        # Sample input:
        data = request.data 
        category_name = data['category_name']
        Categories.objects.create(category_name=category_name)

        return Response({"True"})
    elif request.method == 'GET':
        category_data = Categories.objects.all()
        serial_data = CategorySerializer(category_data,many = True)

    return Response(serial_data.data)


#Insert & Retrieve Leads.
@api_view(['GET', 'POST'])
def leads(request):
    if request.method == 'POST':
        # Sample input:
        data = request.data 
        if len(data)<1:
            return Response({"Fields Missing"},status=400)
        #category_name = data['category_name']
        leadmodel=Leads.objects.create(**data)
        leadmodel.save()

        return Response({"True"})
    elif request.method == 'GET':
        lead_data = Leads.objects.all()
        serial_data = LeadsSerializer(lead_data,many = True)

    return Response(serial_data.data)
