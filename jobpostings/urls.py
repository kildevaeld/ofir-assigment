from django.urls import path, include
from rest_framework import routers

from . import views, api

router = routers.DefaultRouter()
router.register(r'jobs', api.JobPostingViewSet)
router.register(r'categories', api.CategoryViewSet)


urlpatterns = [
    path("", views.IndexView.as_view(), name = 'job-list'),
    path("job/<int:pk>", views.JobPostingDetailView.as_view(), name = "job-detail"),
    path("api/", include(router.urls))
]


