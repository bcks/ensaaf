from django import forms

class ContactForm(forms.Form):
    from_email = forms.EmailField(required=False)
    referer = forms.CharField(required=False)
    message = forms.CharField(widget=forms.Textarea, required=True)
