from django.contrib import admin
from training.models import *

# Register your models here.

admin.site.register(Module)
admin.site.register(Topics)
admin.site.register(ClassRoom)
admin.site.register(OngoingModule)
admin.site.register(Assignment)
admin.site.register(AssignmentReport)
admin.site.register(AssignmentReportComment)

