import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'fbvProject.settings')
django.setup()
from faker import Faker
from myApp.models import Employee
f = Faker()
def populate(n):
    for i in range(n):
        feno = f.random_int(min =1, max =20)
        fename = f.name()
        fesal = f.random_int(min = 1000, max =100000)
        feaddr = f.address()
        e = Employee.objects.get_or_create(eno = feno, ename = fename, esal = fesal, eaddr = feaddr)

populate(20)
