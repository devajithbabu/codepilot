from django.urls import path

from problem.views import QuestionCreateView,QuestionRetrieveUpdateDeleteView

urlpatterns=[
                path('assesment/<int:pk>/question/',QuestionCreateView.as_view()),
                path('assesment/<int:pk>/',QuestionRetrieveUpdateDeleteView.as_view()),
]