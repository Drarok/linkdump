from django import forms

from .models import Link


class LinkForm(forms.ModelForm):
    class Meta:
        model = Link
        fields = ['url', 'title']

    url = forms.URLField(label='URL', max_length=2000)
    title = forms.CharField(label='Title', max_length=2000, required=False)
