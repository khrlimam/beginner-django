from django.contrib import admin
import models
from polls.adminmodels import adminmodels

# Register your models here.
admin.site.register(models.Questions, adminmodels.QuestionsAdminModel)