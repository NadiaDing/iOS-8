from django.contrib import admin
from survey.models import Survey, Question, Choice, SurveyAnswer, QuestionAnswer
# Register your models here.

admin.site.register(Survey)
admin.site.register(Question)
admin.site.register(Choice)
admin.site.register(SurveyAnswer)
admin.site.register(QuestionAnswer)