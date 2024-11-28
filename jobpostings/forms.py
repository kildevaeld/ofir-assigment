from django import forms
from django.utils.translation import gettext as _


from .models import Category


class JobPostingFilterForm(forms.Form):
    """
    JobPosting list filters
    """
    category = forms.ModelChoiceField(
        queryset = Category.objects.all(),
        required = False,
        widget=forms.Select(attrs={'class': 'select'}),
    )
    q = forms.CharField(
        required = False,
        label = _("Søg"),
        widget = forms.TextInput(attrs={'class': 'input', 'placeholder': _("Indtast søgning")})
    )
    
    template_name = "forms/filter-form.html"
