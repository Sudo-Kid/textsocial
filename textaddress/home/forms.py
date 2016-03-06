from django import forms


class TextMessage(forms.Form):
        message = forms.CharField(max_length=140)
