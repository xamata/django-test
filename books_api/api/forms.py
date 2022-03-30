from django import forms
from .models import Company


class CreateCompanyMutationForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = [
            "title",
            "cover",
            # "year_published",
            # "review",
            # "cover",
        ]
