from django.contrib import admin
from .models import NewsUpdate, NewsletterSubscription, ContactUs, Store, StudyAbroadFormSubmission, GetInTouchFormSubmission, ProgramApplication

admin.site.register(NewsUpdate)
admin.site.register(NewsletterSubscription)
admin.site.register(StudyAbroadFormSubmission)
admin.site.register(GetInTouchFormSubmission)
admin.site.register(ProgramApplication)
@admin.register(ContactUs)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'created_at')
    search_fields = ('first_name', 'last_name', 'email')
    list_filter = ('created_at',)

@admin.register(Store)
class StoreAdmin(admin.ModelAdmin):
    list_display = ('name', 'price')
