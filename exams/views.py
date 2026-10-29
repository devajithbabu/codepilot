from django.shortcuts import render,get_object_or_404

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions,authentication

from exams.serializers import AssesmentSerializer
from exams.models import Assesment
from exams.permissions import IsOwner

from datetime import datetime,timedelta

# Create your views here.

class AssesmentListCreateView(APIView):

    authentication_classes=[authentication.TokenAuthentication]
    permission_classes=[permissions.IsAuthenticated]

    def get(self,request):

        qs=Assesment.objects.filter(createdby=request.user)

        serializer_inst = AssesmentSerializer(qs,many=True)

        return Response(data=serializer_inst.data)

    def post(self,request):

        form_data = request.data

        serializer_inst = AssesmentSerializer(data=form_data)

        if serializer_inst.is_valid():
            # start_time = serializer_inst.validated_data['starttime']
            # duration = serializer_inst.validated_data['duration']

            # start = datetime.combine(datetime.today(), start_time)

            # end = start + timedelta(minutes=duration)

            serializer_inst.save(
                createdby=request.user,
                
            )

            return Response(data=serializer_inst.data)

        else:

            return Response(data=serializer_inst.errors)

class AssesmentRetrieveUpdateDeleteView(APIView):

    authentication_classes=[authentication.TokenAuthentication]
    permission_classes=[IsOwner]

    def get(self,request,pk=None):

        instance = get_object_or_404(Assesment,id=pk)

        self.check_object_permissions(request,instance)

        serializer_instance = AssesmentSerializer(instance)

        return Response(data=serializer_instance.data)

    def put(self,request,pk=None):

        instance = get_object_or_404(Assesment,id=pk)

        self.check_object_permissions(request,instance)

        form_data = request.data

        serializer_instance = AssesmentSerializer(data=form_data,instance=instance)

        if serializer_instance.is_valid():

            serializer_instance.save()

            return Response(data=serializer_instance.validated_data)
        
        else:

            return Response(data=serializer_instance.errors)

    def delete(self,request,pk=None):

        instance = get_object_or_404(Assesment,id=pk)

        self.check_object_permissions(request,instance)

        instance.delete()

        return Response(data={"message":"deleted"})