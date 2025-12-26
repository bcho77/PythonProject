from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100, label='Your Name')
    email = forms.EmailField(label='Your Email')
    message = forms.CharField(widget=forms.Textarea, label='Your Message')
    # subject = forms.CharField(max_length=150, label='Subject')# Optional field for subject
    # phone = forms.CharField(max_length=15, label='Phone Number', required=False)  # Optional field for phone number
    # attachment = forms.FileField(label='Attachment', required=False)  # Optional file upload field
    