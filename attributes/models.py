from django.db import models
from django.conf import settings

class ProductQuerySet(models.query.QuerySet):
    def active(self):
        return self.filter(source="data1.sav")

 



class ProductManager(models.Manager):
    def all(self, *args, **kwargs):
       return self.get_queryset().active()
    
    def get_queryset(self):
        return ProductQuerySet(self.model, using=self._db)


class Attributes(models.Model):
    Attribute = models.IntegerField()
    Attribute_Label = models.CharField(max_length=200)
    Standard_variable_attr=models.CharField(max_length=30, null=True, blank=True)		
    Standard_question_wording_attr=models.CharField(max_length=250, null=True, blank=True)	
    objects = ProductManager()

    def __str__(self):
        return self.Attribute_Label



class Options(models.Model):
    Option_Code = models.IntegerField()
    Option_Label = models.CharField(max_length=200)
    Attribute = models.ForeignKey(Attributes, on_delete=models.CASCADE)
    connections=models.ManyToManyField("self", blank=True)
    type= models.IntegerField()
    Standard_variable_option=models.CharField(max_length=30, null=True, blank=True)	
    Standard_question_wording_option=models.CharField(max_length=250, null=True, blank=True)	

    def __str__(self):
        return self.Option_Label + " (" + self.Attribute.Attribute_Label + ")"

class Labels(models.Model):
    Code = models.IntegerField()
    Label = models.CharField(max_length=200)
    Attribute = models.ForeignKey(Options, on_delete=models.CASCADE)
    objects = ProductManager()

    def __str__(self):
        return self.Label

class Setting(models.Model):
	user = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True, on_delete=models.CASCADE)
	sortings= models.ManyToManyField(Options)

	def __str__(self):
		return str(self.id)

# Create your models here.
