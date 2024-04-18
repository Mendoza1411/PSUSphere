from django.forms import Modelform
from django import forms
from .models import organization

class OrganzationForm(ModelFOrm):
    class Meta:
        model = Organization
        fields = "__all__"
