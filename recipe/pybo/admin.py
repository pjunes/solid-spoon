from django.contrib import admin
from .models import Question

# Register your models here.
class QuetionAdmin(admin.ModelAdmin):
    search_fields = ['subject']

admin.site.register(Question, QuetionAdmin)