from django.db import models
from datetime import date


CHOICES = (
    ('testing', 'Testing'),
    ('developement', 'Developement'),
    ('others', 'Others'),
)

REASON = (
    ('sick leave', 'Sick Leave'),
    ('casual leave', 'Casual Leave'),
    ('personal', 'Personal'),
    ('others', 'Others'),
)

typ = (
    ('full day', 'Full Day'),
    ('half day', 'Half Day'),
)



class Leave(models.Model):
    name = models.CharField(max_length=40)
    department = models.CharField(max_length=15, choices=CHOICES, default='testing')
    reason = models.CharField(max_length=15, choices=REASON, default='sick leave')
    from_date = models.DateField(null=True,blank=True,default=str(date.today()))
    to_date = models.DateField(null=True,blank=True,default=str(date.today()))
    leave_type = models.CharField(max_length=10, choices=typ, default='full day')
    leave_days = models.CharField(max_length=2, default='1')
    phone_number = models.CharField(max_length=10)
    Person_in_charge = models.CharField(max_length=40)
    status = models.CharField(max_length=1, default='0')
