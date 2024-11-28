from django.contrib import admin

from .models import Candidate, JobPosting, Application, Category


admin.site.register(Candidate)
admin.site.register(JobPosting)
admin.site.register(Application)
admin.site.register(Category)