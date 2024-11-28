from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.list import ListView
from django.views.generic.edit import FormMixin
from django.views.generic import TemplateView, DetailView


from .models import JobPosting
from .forms import JobPostingFilterForm


class IndexView(ListView, FormMixin):
    model = JobPosting
    template_name = "index.html"
    partial_template = "partials/list.html"
    queryset = JobPosting.objects.order_by('title')
    form_class = JobPostingFilterForm
    
    def get_template_names(self):
        """
        We return different templates depending on comming from a normal get or
        an htmx.
        get
        """
        if self.request.htmx:
            return self.partial_template
        return self.template_name
    
    def get_queryset(self):
        """
        We parse the query parameters and use them for filtering the job list
        """    
        form = self.get_form()
        if self.request.GET:
            form = self.form_class(self.request.GET)
            
        query = super().get_queryset()
        
        if form.is_valid():
            data = form.cleaned_data
            if data['category']:
                query = query.filter(category__title = data['category'])
            if data['q']:
                query = query.filter(title__icontains = data['q'])
        
        return query[:7]
    
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.GET and not self.request.htmx:
            context["form"] = self.form_class(self.request.GET)
        return context
    
    

class JobPostingDetailView(DetailView):
    model = JobPosting
    template_name = "details.html"    
    context_object_name = 'job'
