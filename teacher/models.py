from django.db import models

# Create your models here.
class User(models.Model):
	firstname=models.CharField(max_length=70,null=True)
	lastname=models.CharField(max_length=70,null=True)
	profilepic=models.ImageField(default="default.png",null=True,blank=True)
	email=models.EmailField(unique=True,max_length=200,null=True)
	phone=models.CharField(max_length=70,null=True)
	room=models.CharField(max_length=70,null=True)
	subjects=models.CharField(max_length=200,null=True)

	def isExists(self):
		if User.objects.filter(email = self.email):
			return True

		return  False

	@staticmethod
	def get_user_by_id(ids):
		return User.objects.filter(id__in =ids)		