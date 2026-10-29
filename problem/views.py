from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework import authentication,permissions
from rest_framework.response import Response
from rest_framework.generics import RetrieveAPIView,UpdateAPIView,DestroyAPIView


from exams.models import Assesment

from problem.serializers import QuestionSerializer
from problem.models import Question

# Create your views here.

class QuestionCreateView(APIView):

    authentication_classes=[authentication.TokenAuthentication]
    permission_classes=[permissions.IsAdminUser]

    def post(self,request,pk=None):

        assesment_id=pk

        assesment_object= Assesment.objects.get(id=assesment_id)

        form_data=request.data

        serializer_inst = QuestionSerializer(data=form_data)

        if serializer_inst.is_valid():

            serializer_inst.save(createdby=request.user,assesment=assesment_object)

            return Response(data=serializer_inst.data)

        else:

            return Response(data=serializer_inst.errors)


class QuestionRetrieveUpdateDeleteView(RetrieveAPIView,UpdateAPIView,DestroyAPIView):

    serializer_class=QuestionSerializer

    queryset=Question.objects.all()