from django.contrib import admin
from .models import Question,Choice,Authour
from django.db import models


# class QuestionAdmin(admin.ModelAdmin):
#     fields = ['pub_date', 'question_text']   # reorder the fields or ignore some fields
    
    # list_display = ['question_text']   # reorder the fields or ignore some fields
    # ordering = ['question_text']

#-------------------- good concept -------------------
# # break multiple field into multple segment
@admin.register(Authour)   #register with admin using annotation
class AuthourAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['name']}),
        ('writer information', {'fields': ['writer']}),
    ]
# admin.site.register(Authour, AuthourAdmin)   # other way of registration with admin
# admin.site.register(Question, QuestionAdmin)
# admin.site.register(Choice)



#  ------------another good concept ---------------------

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    list_display = ('pub_date', 'question_text')   # field to be displayed
    list_display_links = ('question_text',)   # rmake the fields to link
    list_editable = ('pub_date',)   # means u can change this field there only
    list_filter = ('pub_date',)
    search_fields = ('question_text',)

    fieldsets = [
        (None,               {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [ChoiceInline]

admin.site.register(Question, QuestionAdmin)


admin.site.site_header =  "DOCUMENTATION APP"
admin.site.index_title =  "DOCUMENTATION APP INDEX"
