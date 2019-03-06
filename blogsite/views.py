from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views import View

app_name = 'blogsite'
class Index(View):
    template_name = "blogsite/index.html"

    def get(self, request):
        context_dict = {}
        return render(request, self.template_name, context_dict)


class PostFormClass(View):
    template_name = "blogsite/postform.html"

    def post(self, *args, **kwargs):
        return HttpResponseRedirect(reverse("index"))

    def get(self, request):
        context_dict = {}
        return render(request, self.template_name, context_dict)
