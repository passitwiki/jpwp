from django.contrib import admin

# Register your models here.
from questions.models import Question, Answer

admin.site.register(Question)
admin.site.register(Answer)
