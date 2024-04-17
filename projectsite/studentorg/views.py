from django.shortcuts import render
from django.views.generic.list import ListView
from studentorg.models import Organization

class HomepageView(ListView):
    model = Organization
    context_object_name = 'home'
    template_name = "home.html"

class OrganizationnList(ListView) : 
    model = Organization
    context_object_name = 'organzation'
    template_name = 'organization'
    paginate_by = 5
# Create your views here.


class OrganizationCreateView (CreateView):
model = Organization
form_class = OrganizationForm template_name = 'org_add.html'
success_url = reverse_lazy( 'organization-list')