from django.contrib import admin

from .models import Question, Choice
# Register your models here.

# this overrides the default site_header in the copied template
admin.site.site_header = 'My First Django Admin'

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    search_fields = ['question_text']
    list_filter = ['pub_date']
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    fieldsets = [
        ('Date information', {'fields': ['pub_date']}),
        (None,               {'fields': ['question_text']}),
    ]
    inlines = [ChoiceInline]

admin.site.register(Question, QuestionAdmin)
