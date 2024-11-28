from django.urls import path, include
from rest_framework import routers

from . import views, api

router = routers.DefaultRouter()
router.register(r'jobs', api.JobPostingViewSet)

urlpatterns = [
    path("", views.IndexView.as_view(), name = 'job-list'),
    path("job/<int:pk>", views.JobPostingDetailView.as_view(), name = "job-detail"),
    path("api/", include(router.urls))
]


