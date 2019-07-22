from django.conf.urls import include
from django.urls import path
from rest_framework import routers

from grandchallenge.cases.views import ImageViewSet
from grandchallenge.patients.views import PatientViewSet
from grandchallenge.reader_studies.views import (
    ReaderStudyViewSet,
    QuestionViewSet,
    AnswerViewSet,
)
from grandchallenge.studies.views import StudyViewSet
from grandchallenge.worklists.views import WorklistViewSet
from grandchallenge.workstations.views import SessionViewSet

app_name = "api"

router = routers.DefaultRouter()
router.register(r"patients", PatientViewSet, basename="patient")
router.register(r"studies", StudyViewSet, basename="study")
router.register(r"worklists", WorklistViewSet, basename="worklist")
router.register(r"cases/images", ImageViewSet, basename="image")
router.register(r"workstations/sessions", SessionViewSet)

router.register(
    r"reader-studies/answers", AnswerViewSet, basename="reader-studies-answer"
)
router.register(
    r"reader-studies/questions",
    QuestionViewSet,
    basename="reader-studies-question",
)
router.register(r"reader-studies", ReaderStudyViewSet, basename="reader-study")


urlpatterns = [
    # Do not namespace the router.urls without updating the view names in
    # the serializers
    path("v1/", include(router.urls)),
    path("auth/", include("rest_framework.urls", namespace="rest_framework")),
]
