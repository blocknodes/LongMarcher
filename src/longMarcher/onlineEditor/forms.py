from django import forms

class FileForm(forms.Form):
    content = forms.CharField(widget=forms.Textarea(attrs={"rows":55, "cols":265}))
