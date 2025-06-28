from django.db import models
from django.utils import timezone

class NewsUpdate(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    cover_image = models.ImageField(upload_to='news/', null=True, blank=True)
    date_published = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.title


class NewsletterSubscription(models.Model):
    email = models.EmailField(unique=True)
    date_subscribed = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email


class ContactUs(models.Model):
    first_name = models.CharField(max_length=100, null=True, blank=True)
    last_name = models.CharField(max_length=100, null=True, blank=True)
    email = models.EmailField()
    message = models.TextField()
    
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Store(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='store_images/')
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    slug = models.SlugField(unique=True, blank=True, null=True)
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
            super().save(*args, **kwargs)

    def __str__(self):
            return self.name



COUNTRY_CODES = [
    ('+1', '+1 (USA)'),
    ('+44', '+44 (UK)'),
    ('+234', '+234 (Nigeria)'),
    ('+91', '+91 (India)'),
    ('+86', '+86 (China)'),
    ('+49', '+49 (Germany)'),
    ('+33', '+33 (France)'),
    ('+81', '+81 (Japan)'),
    ('+61', '+61 (Australia)'),
    ('+27', '+27 (South Africa)'),
    ('+55', '+55 (Brazil)'),
    ('+52', '+52 (Mexico)'),
    ('+7', '+7 (Russia)'),
    ('+82', '+82 (South Korea)'),
    ('+39', '+39 (Italy)'),
    ('+34', '+34 (Spain)'),
    ('+31', '+31 (Netherlands)'),
    ('+46', '+46 (Sweden)'),
    ('+47', '+47 (Norway)'),
    ('+41', '+41 (Switzerland)'),
]

# Choices for purposes in Get In Touch form
PURPOSE_CHOICES = [
    ('Partnership', 'Partnership'),
    ('General Enquiries', 'General Enquiries'),
    ('Energy Solutions Enquiries', 'Energy Solutions Enquiries'),
]

LEVEL_OF_STUDY_CHOICES = [
    ('Diploma', 'Diploma'),
    ('Undergraduate', 'Undergraduate'),
    ('Postgraduate', 'Postgraduate'),
    ('PhD', 'PhD'),
]

PROGRAM_CHOICES = [
        ('AI_ML', 'Artificial Intelligence (AI) and Machine Learning (ML) Essentials'),
        ('EMBEDDED', 'Embedded System'),
        ('3D_PRINT', '3D Design and Printing'),
        ('PYTHON_DJANGO', 'Python and Django enabled web application for content management'),
    ]


class StudyAbroadFormSubmission(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    country_code = models.CharField(max_length=5, choices=COUNTRY_CODES)
    phone_number = models.CharField(max_length=20)
    uploaded_file = models.FileField(upload_to='study_abroad_uploads/', null=True, blank=True)
    course_of_interest = models.TextField(null=True, blank=True)
    level_of_study_of_interest = models.CharField(
        max_length=20,
        choices=LEVEL_OF_STUDY_CHOICES,
        null=True,
        blank=True
    )
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.email}"


class GetInTouchFormSubmission(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    country_code = models.CharField(max_length=5, choices=COUNTRY_CODES)
    phone_number = models.CharField(max_length=20)
    purpose = models.CharField(max_length=50, choices=PURPOSE_CHOICES)
    message = models.TextField()

    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.first_name} - {self.purpose}"



class ProgramApplication(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    program_name = models.CharField(max_length=50, choices=PROGRAM_CHOICES)
    cover_letter = models.TextField(blank=True, null=True)
    resume = models.FileField(upload_to='resumes/')
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.full_name} - {self.program_name}"


        