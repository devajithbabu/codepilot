from django.urls import path

from evaluation.views import SubmissionStartView,AnswerCreateView,SubmissionRetrieveView

urlpatterns=[
                path("assesment/<int:pk>/submission/",SubmissionStartView.as_view()),
                path('submission/<int:pk>/answer/',AnswerCreateView.as_view()),
                path('submission/<int:pk>/',SubmissionRetrieveView.as_view()),
]