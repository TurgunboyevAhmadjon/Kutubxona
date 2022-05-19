from django.db import models

class Student(models.Model):
    ism = models.CharField(max_length=30)
    guruh = models.CharField(max_length=10)
    guvohnoma = models.CharField(max_length=10, blank=True)
    kitob_soni = models.PositiveSmallIntegerField(default=0)

    def __str__(self):
        return f"{self.ism} {self.guruh} {self.guvohnoma} {self.kitob_soni}"
class Muallif(models.Model):
    Jins = (
        ('Erkak', 'Erkak'),
        ('Ayol', 'Ayol'),
    )
    ism = models.CharField(max_length=50)
    yosh = models.PositiveSmallIntegerField()
    tirik = models.BooleanField(default=True)
    jins = models.CharField(choices=Jins, max_length=10)

    def __str__(self):
        return f"{self.ism} "
# {self.yosh} {self.tirik} {self.jins}
class Kitob(models.Model):
    JANR = (
        ("Badiiy", "Badiiy"),
        ("Ilmiy", "Ilmiy"),
        ("Hujjatli", "Hujjatli"),
        ("Detektiv", "Detektiv"),
            )
    nom = models.CharField(max_length=30)
    sahifa = models.PositiveSmallIntegerField(default=200)
    janr = models.CharField(max_length=12, choices=JANR)
    sana = models.DateField()
    muallif = models.ForeignKey(Muallif, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f"{self.muallif}"

class Record(models.Model):
    sana = models.DateField()
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    kitob = models.ForeignKey(Kitob, on_delete=models.CASCADE)
    qaytardi = models.CharField(max_length=5, choices=(("Ha", "Ha"), ("Yo'q", "Yo'q")))
    qaytarish_sana = models.DateField(null=True)

    def __str__(self):
        return f"{self.student.ism}, {self.kitob.nom}"

class Speciality(models.Model):
    name = models.CharField(max_length=30)
    code = models.IntegerField()
    start_date = models.DateField(null=True)
    is_active = models.CharField(max_length=15)
    def str(self):
        return self.name

class Teacher(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    degree =  models.CharField(max_length=20)
    def str(self):
        return f"{self.first_name} {self.last_name}"

class Subject(models.Model):
    name = models.CharField(max_length=30)
    speciality = models.ManyToManyField(Speciality)
    teachers = models.ManyToManyField(Teacher)
    def str(self):
        return self.name