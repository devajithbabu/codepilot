from django.urls import path

from rest_framework.authtoken.views import ObtainAuthToken

from exams.views import AssesmentListCreateView,AssesmentRetrieveUpdateDeleteView

urlpatterns=[
    path('assesment/',AssesmentListCreateView.as_view()),

    path('token/',ObtainAuthToken.as_view()),
    path('assesment/<int:pk>/',AssesmentRetrieveUpdateDeleteView.as_view()),
]