from django.db import models
from django.utils.translation import gettext as _


class Candidate(models.Model):
    name = models.CharField(_("Name"), max_length=100)
    email = models.EmailField(_("Email"), max_length=254, unique = True)
    registration_date = models.DateTimeField(_("Registration date"), auto_now=False, auto_now_add=True)

    def __str__(self):
        return self.name


class Category(models.Model):
    title = models.CharField(_("title"), max_length=100, unique = True)
    
    def __str__(self):
        return self.title
    

class JobPosting(models.Model):
    title = models.CharField(_("Title"), max_length = 100, db_index = True)
    company = models.CharField(_("Company"), max_length = 100)
    location = models.CharField(_("Location"), max_length = 50)
    posted_date = models.DateTimeField(_("Posted date"), auto_now_add=True)
    description = models.TextField(_("Description of the job"))
    summary = models.TextField(_("Summery"))
    logo_url = models.URLField(_("Logo URL"))
    
    category = models.ForeignKey(Category, verbose_name=_("Category"), on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Application(models.Model):
    application_date = models.DateTimeField(_("Application date"), auto_now=False, auto_now_add=False)
    status = models.CharField(_("Status of application"), max_length=50)

    jobposting = models.ForeignKey(JobPosting, verbose_name=_("Jobposition"), on_delete=models.CASCADE)
    candidate = models.ForeignKey(Candidate, verbose_name=_("Candidate"), on_delete=models.CASCADE)
    
    