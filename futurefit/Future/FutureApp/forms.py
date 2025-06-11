from django import forms
from .models import NewsletterSubscription, ContactUs, StudyAbroadFormSubmission, GetInTouchFormSubmission, ProgramApplication

class NewsletterSubscriptionForm(forms.ModelForm):
    class Meta:
        model = NewsletterSubscription
        fields = ['email']





class ContactUsForm(forms.ModelForm):
    class Meta:
        model = ContactUs
        fields = ['first_name', 'last_name', 'email', 'message']
        widgets = {
            'first_name': forms.TextInput(attrs={'placeholder': 'First Name', 'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'placeholder': 'Last Name', 'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Email Address', 'class': 'form-control'}),
            'message': forms.Textarea(attrs={'placeholder': 'Your Message', 'rows': 5, 'class': 'form-control'}),
        }
        labels = {
            'first_name': 'First Name',
            'last_name': 'Last Name',
            'email': 'Email Address',
            'message': 'Your Message',
        }



class StudyAbroadForm(forms.ModelForm):
    class Meta:
        model = StudyAbroadFormSubmission
        fields = ['first_name', 'last_name', 'email', 'country_code', 'phone_number', 'course_of_interest', 'level_of_study_of_interest', 'uploaded_file']

    def clean_uploaded_file(self):
        uploaded_file = self.cleaned_data.get('uploaded_file')
        if uploaded_file:
            if uploaded_file.size > 10 * 1024 * 1024:  # 10MB limit
                raise forms.ValidationError("File size must be under 10MB.")
            allowed_types = [
                'application/pdf',
                'application/msword',
                'application/vnd.openxmlformats-officedocument.wordprocessingml.document',
                'image/jpeg',
                'image/png',
            ]
            if uploaded_file.content_type not in allowed_types:
                raise forms.ValidationError("File type not supported. Allowed types: PDF, DOC, DOCX, JPG, PNG.")
        return uploaded_file


class GetInTouchForm(forms.ModelForm):
    class Meta:
        model = GetInTouchFormSubmission
        fields = ['first_name', 'last_name', 'email', 'country_code', 'phone_number', 'purpose', 'message']

class ProgramApplicationForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Add placeholder/empty label for dropdown
        self.fields['program_name'].empty_label = "Select a program..."

    class Meta:
        model = ProgramApplication
        fields = ['full_name', 'email', 'phone', 'program_name', 'cover_letter', 'resume']



