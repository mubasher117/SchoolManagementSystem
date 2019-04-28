from django.contrib import admin
from django.db import models
# Register your models here.
from .models import Classes, Section
from .models import Person, Student, Teacher, Request, Fee, Salary, Classcourses


admin.site.site_header = 'School Management Admin'
admin.site.index_title = 'SMS Administration'

class StudentAdmin(admin.ModelAdmin):
    pass
admin.site.register(Student,StudentAdmin)


class TeacherAdmin(admin.ModelAdmin):
    pass
admin.site.register(Teacher,TeacherAdmin)

class PersonAdmin(admin.ModelAdmin):
    pass

admin.site.register(Person,PersonAdmin)


class SectionAdmin(admin.StackedInline):
    model = Section
    
class ClassAdmin(admin.ModelAdmin):
    inlines = [SectionAdmin]

admin.site.register(Classes,ClassAdmin)


class RequestAdmin(admin.ModelAdmin):
    pass
admin.site.register(Request,RequestAdmin)

class FeeAdmin(admin.ModelAdmin):
    pass

admin.site.register(Fee,FeeAdmin)

class SalaryAdmin(admin.ModelAdmin):
    pass

admin.site.register(Salary,SalaryAdmin)



"""
class myClassAdmin(admin.ModelAdmin):
    def get_model_perms(self, request):
        
        Return empty perms dict thus hiding the model from admin index.
        
        return {}
    change_form_template = 'adminApp/changeClass.html'
    def change_view(self, request, object_id, form_url='', extra_context=None):
        extra_context = extra_context or {}
        print(object_id)
        depId = Class.objects.get(pk=object_id).DepartmentId
        extra_context['osm_data'] = Section.objects.filter(
            ClassId=object_id, DepartmentId=depId)
        return super().change_view(
            request, object_id, form_url, extra_context=extra_context,
        )

        """