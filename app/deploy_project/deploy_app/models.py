from django.db import models

# Create your models here.

class SeatingSection(models.Model):
	ID = models.IntegerField()
class Table(models.Model):
	tableNumber = models.IntegerField()
	section = models.ForeignKey(SeatingSection, on_delete=models.CASCADE)

class StaffMember(models.Model):
	firstName = models.CharField(max_length=15)
	ID = models.IntegerField()
	working = models.BooleanField(default=False)

class Chef(StaffMember):
	headChef = models.BooleanField(default=False)

class Server(StaffMember):
	currentTables = models.CharField(max_length=14)

class Support(StaffMember):
	POSITION = [
		('H', 'Host'),
		('FR', 'Food Runner'),
		('B', 'Busser'),
	]
	position = models.CharField(max_length = 2, choices=POSITION)
