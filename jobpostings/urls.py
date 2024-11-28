from django.urls import path, include
from rest_framework import routers

from . import views, api

router = routers.DefaultRouter()
router.register(r'jobs', api.JobPostingViewSet)

urlpatterns = [
    path("", views.IndexView.as_view(), name = "jobposting-list"),
    path("api/", include(router.urls))
]


