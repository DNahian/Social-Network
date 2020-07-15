from django.shortcuts import render
from django.views.generic import TemplateView
from home.forms import HomeForm


class HomeView(TemplateView):
    template_name = 'home.html'

    def get(self, request):
        form = HomeForm()
        return render(request, self.template_name, {'form': form})
