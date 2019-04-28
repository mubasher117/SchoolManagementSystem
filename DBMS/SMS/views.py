from django.shortcuts import render
from django.shortcuts import get_object_or_404, render,redirect
from django.http import HttpResponseRedirect
from .models import Person, Student, Login, Request
# Create your views here.

def index(request):
    return render(request, 'SMS/index.html')

def articles(request):
    return render(request, 'SMS/articles.html')

def contact_us(request):
    return render(request, 'SMS/contact-us.html')

def site_map(request):
    return render(request, 'SMS/sitemap.html')

def about(request):
    return render(request, 'SMS/about-us.html')

def student(request, student_id):
        
        return render(request, 'SMS/AcademicDetail.html', {'StudentId' : student_id})

def login(request):
        incorrect_password = True
        if request.method == 'POST':
                print ("logged")
                name = request.POST.get('inputEmail')
                password = request.POST.get('inputPassword')
                print (name)
                print (password)
                
                """
                current_user = get_object_or_404(Login, username = name)
                """
                try :
                        current_user = Login.objects.get(username = name, password = password)
                        if current_user.role == 'Student':
                                return redirect('/sms/student/' + str(current_user.personid.id) )
                        else :
                                return redirect('/sms/teacher/' + str(current_user.personid.id))
                except:
                        incorrect_password = True
                        return render(request,'sms/login.html', {'incorrectPassword' :incorrect_password})
                """
                if current_user != None :

                else:

                if current_user.username == name and current_user.password == password:
                        if current_user.Role == 'Student':
                                return redirect('/sms/student/' + name )
                                
                        
                if name == 't@t.com' and password == '1234':
                        return redirect('/sms/student/' )
                else:
                        incorrect_password = True
                        return render(request,'sms/login.html', {'incorrectPassword' :incorrect_password})
                        """
        else:
                return render(request,'sms/login.html', {'incorrectPassword' :incorrect_password})  
        

def view_student_timetable(request,student_id):
    return render(request, 'SMS/TimeTable.html', {'StudentId' : student_id})

def view_student_academic_detail(request, student_id):
    return render(request, 'SMS/AcademicDetail.html', {'StudentId' : student_id})

def view_date_sheet(request, student_id):
    return render(request, 'SMS/DateSheet.html', {'StudentId' : student_id})

def view_result(request,student_id):
    return render(request, 'SMS/Result.html', {'StudentId' : student_id})

def send_student_request(request, student_id):
        if request.method == 'POST':
                Student = Person.objects.get(id = student_id)
                description = request.POST.get('Description')
                new_request = Request(personid = Student, description = description)
                new_request.save()
                return render(request, 'SMS/Request.html', {'StudentId' : student_id})
        else:
                return render(request, 'SMS/Request.html', {'StudentId' : student_id})

def upload_student_assignment(request,student_id):
    return render(request, 'SMS/Assignments.html', {'StudentId' : student_id})

def view_student_fee(request, student_id):
    return render(request, 'SMS/Fee.html', {'StudentId' : student_id})


def teacher_dashboard(request,teacher_id):
        return render(request, 'SMS/indexT.html', {'TeacherId' : teacher_id})

def teacher_upload_assignments(request, teacher_id):
        return render(request, 'SMS/AssignmentsT.html', {'TeacherId' : teacher_id})


def teacher_attendance(request,teacher_id):
        return render(request, 'SMS/AttendanceT.html', {'TeacherId' : teacher_id})


def teacher_payroll(request,teacher_id):
        return render(request, 'SMS/payroll.html', {'TeacherId' : teacher_id})


def teacher_request(request,teacher_id):
        
        if request.method == 'POST':
                Teacher = Person.objects.get(id = teacher_id)
                description = request.POST.get('Description')
                new_request = Request(personid = Teacher, description = description)
                new_request.save()
                return render(request, 'SMS/IndexT.html', {'TeacherId' : teacher_id})


        else:
                return render(request, 'SMS/Request.html', {'TeacherId' : teacher_id})
        
def teacher_timetable(request,teacher_id):
        return render(request, 'SMS/TimetableT.html', {'TeacherId' : teacher_id})

def teacher_result(request,teacher_id):
        return render(request, 'SMS/ResultT.html', {'TeacherId' : teacher_id})