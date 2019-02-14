from django.db import models


class Subject(models.Model):
    subject = models.CharField(max_length=200)
    #pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.subject


class Grade(models.Model):
    subject = models.ManyToManyField(Subject)
    name = models.CharField(max_length=200)
    #votes = models.IntegerField(default=0)

    def __str__(self):
        return self.name


class Thought(models.Model):
    subject = models.ForeignKey(Subject,on_delete=models.CASCADE)
    thought = models.CharField(max_length=200)
    #votes = models.IntegerField(default=0)

    def __str__(self):
        return self.thought


class Process(models.Model):
    subject = models.ForeignKey(Subject,on_delete=models.CASCADE)
    process = models.CharField(max_length=200)
    #votes = models.IntegerField(default=0)

    def __str__(self):
        return self.process


class Standard(models.Model):
    subject = models.ForeignKey(Subject,on_delete=models.CASCADE)
    standard = models.CharField(max_length=400)
    grade = models.ForeignKey(Grade, on_delete=models.CASCADE)
    thought = models.ForeignKey(Thought, on_delete=models.CASCADE)

    def __str__(self):
        return self.standard

class Dba(models.Model):
    subject = models.ForeignKey(Subject,on_delete=models.CASCADE)
    dba = models.CharField(max_length=400)
    standard = models.ForeignKey(Standard, on_delete=models.CASCADE)
    grade = models.ForeignKey(Grade, on_delete=models.CASCADE)
    thought = models.ForeignKey(Thought, on_delete=models.CASCADE)

    def __str__(self):
        return self.dba

class Learning(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    learning = models.CharField(max_length=400)
    standard = models.ForeignKey(Standard, on_delete=models.CASCADE)
    grade = models.ForeignKey(Grade, on_delete=models.CASCADE)
    thought = models.ForeignKey(Thought, on_delete=models.CASCADE)
    dba = models.ForeignKey(Dba, on_delete=models.CASCADE)
    process = models.ForeignKey(Process, on_delete=models.CASCADE, default=None)

    def __str__(self):
        return self.learning

class CriticalPoint(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    criticalpoint = models.CharField(max_length=400)
    standard = models.ForeignKey(Standard, on_delete=models.CASCADE)
    grade = models.ForeignKey(Grade, on_delete=models.CASCADE)
    thought = models.ForeignKey(Thought, on_delete=models.CASCADE)
    dba = models.ForeignKey(Dba, on_delete=models.CASCADE)
    process = models.ForeignKey(Process, on_delete=models.CASCADE, default=None)


    def __str__(self):
        return self.criticalpoint


