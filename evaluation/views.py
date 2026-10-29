from django.shortcuts import render,get_object_or_404

from rest_framework.views import APIView
from rest_framework import authentication,permissions
from rest_framework.response import Response
from rest_framework import serializers

from problem.models import Question

from evaluation.serializers import SubmissionSerializer,AnswerSerializer
from evaluation.permissions import IsStudentUser
from evaluation.models import Submission

from exams.models import Assesment

# Create your views here.

class SubmissionStartView(APIView):

    authentication_classes=[authentication.TokenAuthentication]
    permission_classes=[IsStudentUser]

    def post(self,request,pk=None):

        assesment_id=pk

        assesment_obj=get_object_or_404(Assesment,id=assesment_id)

        instance = Submission.objects.create(assesment=assesment_obj,student=request.user)

        serializer_inst=SubmissionSerializer(instance)

        return Response(data=serializer_inst.data)

class AnswerCreateView(APIView):

    authentication_classes=[authentication.TokenAuthentication]
    permission_classes=[IsStudentUser]

    def post(self,request,pk=None):

        submission_id = pk

        submission_obj=get_object_or_404(Submission,id=submission_id)

        form_data=request.data

        #validation starts
        assesment_obj=submission_obj.assesment

        assesment_questions=Question.objects.filter(assesment=assesment_obj).values_list("id",flat=True)

        question=form_data.get("question")

        if question not in assesment_questions:

            raise serializers.ValidationError("invalid question,question not exists in assesment")
        #validation ends

        serializer_inst=AnswerSerializer(data=form_data)

        if serializer_inst.is_valid():

            serializer_inst.save(submission=submission_obj)

            return Response(data=serializer_inst.data)

        else:

            return Response(data=serializer_inst.errors)

class SubmissionRetrieveView(APIView):

    authentication_classes=[authentication.TokenAuthentication]
    permission_classes=[permissions.IsAdminUser]

    def get(self,request,pk=None):

        instance=get_object_or_404(Submission,id=pk)

        serializer_inst=SubmissionSerializer(instance)

        return Response(data=serializer_inst.data)

