from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status

from rest_framework.viewsets import ModelViewSet
from spam.models import UserMaster
from spam.serializer import RegisterSerializer
# Create your views here.


class Register(ModelViewSet):
    serializer_class = RegisterSerializer
    http_method_names = ['post','get']
    queryset = UserMaster.objects.all()
    
    def create(self,request):
        print(request.data,'fffffff')
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            # serializer.save()
            data =serializer.data
            context = {'status':True, 'message':'Enabled successfully',"data":data}
            return Response(context, status=status.HTTP_200_OK)
        else:
                context = {'status':True, 'message':'Disabled successfully',"data":data}
                return Response(context, status=status.HTTP_200_OK)
        