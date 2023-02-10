from django.contrib import admin
from .models import Choice, Question

# Register your models here.


# This class nest the choice info inside the Question
class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3


# To nest the choice inside this class must call the inlines[call_to_coice]
class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [ChoiceInline]
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    list_filter = ['pub_date']
    search_fields = ['question_text']

admin.site.register(Question, QuestionAdmin)
