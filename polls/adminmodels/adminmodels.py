from django.contrib import admin
from polls import models

class ChoicesInline(admin.TabularInline):
    model = models.Choices
    extra = 3

class QuestionsAdminModel(admin.ModelAdmin):
    fieldsets = [('Question', {'fields': ['question_text', 'pub_date']}),]
    inlines = [ChoicesInline]
    list_display = ('question_text', 'was_published_recently', 'pub_date')
    list_filter = ('pub_date',)
    search_fields = ['question_text']