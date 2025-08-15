from django.shortcuts import render
from django.views.generic import TemplateView

from ambadmin.models import *

# Create your views here.

class BlogView(TemplateView):
    # template = "./templates/blog.html"

    def __init__(self):
        self.page = None

    def get_template_names(self):
        return ["blog.html"]

    def dispatch(self, request, id, *args, **kwargs):
        self.page = Page.objects.get(id=id)
        return super().dispatch(request, **kwargs)

    def get(self, request, **kwargs):
        context = {"page":self.page}
        return self.render_to_response(context)



