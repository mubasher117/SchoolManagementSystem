from django.db import models


class Assigncourse(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    teacherid = models.ForeignKey('Teacher', models.DO_NOTHING, db_column='TeacherId')  # Field name made lowercase.
    courseid = models.ForeignKey('Courses', models.DO_NOTHING, db_column='CourseId')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'AssignCourse'


class Assignsalary(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    designation = models.CharField(db_column='Designation', max_length=50)  # Field name made lowercase.
    salary = models.CharField(db_column='Salary', max_length=50)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'AssignSalary'


class Assignmentsubmit(models.Model):
    assignmentid = models.IntegerField(db_column='AssignmentId', primary_key=True)  # Field name made lowercase.
    studentid = models.ForeignKey('Student', models.DO_NOTHING, db_column='StudentId')  # Field name made lowercase.
    assignment = models.CharField(db_column='Assignment', max_length=50)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'AssignmentSubmit'


class Assignmentupload(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    teacherid = models.ForeignKey('Teacher', models.DO_NOTHING, db_column='TeacherId')  # Field name made lowercase.
    sectionid = models.ForeignKey('Section', models.DO_NOTHING, db_column='SectionId')  # Field name made lowercase.
    courseid = models.ForeignKey('Courses', models.DO_NOTHING, db_column='CourseId')  # Field name made lowercase.
    assignment = models.CharField(db_column='Assignment', max_length=50)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'AssignmentUpload'


class Attendance(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    personid = models.ForeignKey('Person', models.DO_NOTHING, db_column='PersonId')  # Field name made lowercase.
    status = models.BooleanField(db_column='Status')  # Field name made lowercase.
    date = models.DateField(db_column='Date')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Attendance'


class Classcourses(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    classid = models.ForeignKey('Classes', models.DO_NOTHING, db_column='ClassId')  # Field name made lowercase.
    courseid = models.ForeignKey('Courses', models.DO_NOTHING, db_column='CourseId')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ClassCourses'


class Classes(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=50)  # Field name made lowercase.
    fee = models.IntegerField(db_column='Fee')  # Field name made lowercase.
    def __str__(self):
        return self.name
    class Meta:
        managed = False
        db_table = 'Classes'


class Courses(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    coursecode = models.CharField(db_column='CourseCode', max_length=50)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Courses'


class Datesheet(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    classid = models.ForeignKey(Classes, models.DO_NOTHING, db_column='ClassId')  # Field name made lowercase.
    courseid = models.ForeignKey(Courses, models.DO_NOTHING, db_column='CourseId')  # Field name made lowercase.
    date = models.DateTimeField(db_column='Date')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DateSheet'


class Fee(models.Model):
    challanid = models.AutoField(db_column='ChallanId', primary_key=True)  # Field name made lowercase.
    month = models.CharField(max_length = 8, db_column = 'Month')  # Field name made lowercase.
    classid = models.ForeignKey(Classes, models.DO_NOTHING, db_column='ClassId', related_name= '+')  # Field name made lowercase.
    duedate = models.DateField(db_column='DueDate')  # Field name made lowercase.
    def __str__(self):
        if self.month == None:
            self.month = "N/A"
        return str(self.classid) + " "  + self.month

    class Meta:
        managed = False
        db_table = 'Fee'


class Login(models.Model):
    personid = models.ForeignKey('Person', models.DO_NOTHING, db_column='PersonId')  # Field name made lowercase.
    username = models.CharField(db_column='UserName', primary_key=True, max_length=50)  # Field name made lowercase.
    password = models.CharField(db_column='Password', max_length=50)  # Field name made lowercase.
    role = models.CharField(db_column='Role', max_length=50)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Login'


class Person(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    firstname = models.CharField(db_column='FirstName', max_length=50)  # Field name made lowercase.
    lastname = models.CharField(db_column='LastName', max_length=50, blank=True, null=True)  # Field name made lowercase.
    contact = models.CharField(db_column='Contact', max_length=50, blank=True, null=True)  # Field name made lowercase.
    email = models.CharField(db_column='Email', max_length=50, blank=True, null=True)  # Field name made lowercase.
    dateofbirth = models.DateTimeField(db_column='DateOfBirth')  # Field name made lowercase.
    gender = models.BooleanField(db_column='Gender')  # Field name made lowercase.
    def __str__(self):
        return self.firstname + " " + self.lastname

    class Meta:
        managed = False
        db_table = 'Person'


class Request(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    personid = models.ForeignKey(Person, models.DO_NOTHING, db_column='PersonId')  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=50)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Request'
    def __str__(self):
        return self.description

class Result(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    courseid = models.ForeignKey(Courses, models.DO_NOTHING, db_column='CourseId')  # Field name made lowercase.
    studentid = models.ForeignKey('Student', models.DO_NOTHING, db_column='StudentId')  # Field name made lowercase.
    evaluationname = models.CharField(db_column='EvaluationName', max_length=50)  # Field name made lowercase.
    marks = models.IntegerField(db_column='Marks')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Result'
    def __str__(self):
        return self.evaluationname

class Salary(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    teacherid = models.ForeignKey('Teacher', models.DO_NOTHING, db_column='TeacherId')  # Field name made lowercase.
    assignsalaryid = models.ForeignKey(Assignsalary, models.DO_NOTHING, db_column='AssignSalaryId', related_name= '+')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Salary'


class Section(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    classid = models.ForeignKey(Classes, models.DO_NOTHING, db_column='ClassId')  # Field name made lowercase.
    teacherid = models.ForeignKey('Teacher', models.DO_NOTHING, db_column='TeacherId')  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=50)  # Field name made lowercase.
    strength = models.IntegerField(db_column='Strength')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Section'


class Student(models.Model):
    id = models.ForeignKey(Person, models.DO_NOTHING, db_column='Id', primary_key=True, related_name= '+')  # Field name made lowercase.
    registrationno = models.CharField(db_column='RegistrationNo', max_length=50)  # Field name made lowercase.

    def __str__(self):
        return self.registrationno
    class Meta:
        managed = False
        db_table = 'Student'


class Studentsection(models.Model):
    studentid = models.IntegerField(db_column='StudentId', primary_key=True)  # Field name made lowercase.
    sectionid = models.ForeignKey(Section, models.DO_NOTHING, db_column='SectionId')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'StudentSection'


class Teacher(models.Model):
    id = models.ForeignKey(Person, models.DO_NOTHING, db_column='Id', primary_key=True, related_name= '+')  # Field name made lowercase.
    designation = models.CharField(db_column='Designation', max_length=50)  # Field name made lowercase.
    
    def __str__(self):
        return self.id.firstname
    class Meta:
        managed = False
        db_table = 'Teacher'


class Timetable(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    datetime = models.DateTimeField(db_column='DateTime')  # Field name made lowercase.
    assigncourseid = models.ForeignKey(Assigncourse, models.DO_NOTHING, db_column='AssignCourseId')  # Field name made lowercase.
    sectionid = models.ForeignKey(Section, models.DO_NOTHING, db_column='SectionId')  # Field name made lowercase.
    
    class Meta:
        managed = False
        db_table = 'TimeTable'