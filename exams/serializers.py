from rest_framework import serializers

from exams.models import Assesment

from problem.models import Question

from django.db.models import Sum

from problem.serializers import QuestionSerializer

class AssesmentSerializer(serializers.ModelSerializer):

    greetings = serializers.SerializerMethodField(read_only=True)

    question_count = serializers.SerializerMethodField(read_only=True)

    total_marks=serializers.SerializerMethodField(read_only=True)

    questions=serializers.SerializerMethodField(read_only=True)

    class Meta:

        model=Assesment

        fields = "__all__"

        read_only_fields = ["id","endtime","createdby"]

    def get_greetings(self,obj):

        return "good morning"    

    def get_question_count(self,obj):

        return Question.objects.filter(assesment=obj).count()

    def get_total_marks(self,obj):

        return Question.objects.filter(assesment=obj).values("score").aggregate(total=Sum("score")).get("total")

    def get_questions(self,obj):

        question_objects=Question.objects.filter(assesment=obj)

        serializer_inst=QuestionSerializer(question_objects,many=True)

        return serializer_inst.data
        