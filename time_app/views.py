from django.contrib.auth.mixins import LoginRequiredMixin
from django import forms
from django.contrib.auth.models import User
from django.shortcuts import render
from django.views import View

from time_app.models import UserTime


# Create your views here.

class UserTimeForm(forms.ModelForm):
    user = forms.ModelChoiceField(widget=forms.HiddenInput(), queryset=User.objects.all())
    day = forms.DateField(widget=forms.TextInput(attrs={"type": "date"}))
    start_time = forms.TimeField(widget=forms.TextInput(attrs={"type": "time"}))
    end_time = forms.TimeField(widget=forms.TextInput(attrs={"type": "time"}))

    class Meta:
        model = UserTime
        fields = "__all__"


class TimeView(LoginRequiredMixin, View):
    def get(self, request):
        context = {}
        form = UserTimeForm(initial={'user': request.user})
        context["form"] = form
        return render(request, "time_app/time_view.html", context)

    def post(self, request):
        context = {}
        form = UserTimeForm(request.POST)
        if form.is_valid():
            form.save()
            context['saved'] = True
        else:
            context['saved'] = False
            context['form'] = form
        return render(request, "time_app/time_view.html", context)

