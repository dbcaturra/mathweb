from django.contrib import admin

from .models import Subject, Grade, Thought, Process, Standard, Dba, Learning, CriticalPoint

from django.db import models


class SubjectAdmin(admin.ModelAdmin):
    fields = ['subject']

class GradeAdmin(admin.ModelAdmin):
    fields = ['name', 'subject']
    list_display = ('get_subject', 'name')
    
    def get_subject(self, obj):
        return [i["subject"] for i in obj.subject.values('subject').values().values()]

admin.site.register(Subject, SubjectAdmin)
admin.site.register(Grade, GradeAdmin)
admin.site.register(Thought)
admin.site.register(Process)
admin.site.register(Standard)
admin.site.register(Dba)
admin.site.register(Learning)
admin.site.register(CriticalPoint)



