from django.db import models


class Attributes(models.Model):
    Attribute = models.IntegerField()
    Attribute_Label = models.CharField(max_length=200)
    Standard_variable_attr=models.CharField(max_length=30, null=True, blank=True)		


    def __str__(self):
        return self.Attribute_Label


class Options(models.Model):
    Option_Code = models.IntegerField()
    Option_Label = models.CharField(max_length=200)
    Attribute = models.ForeignKey(Attributes, on_delete=models.CASCADE)
    connections=models.ManyToManyField("self", blank=True)
    type= models.IntegerField()
    Standard_variable_option=models.CharField(max_length=30, null=True, blank=True)	

    def __str__(self):
        return self.Option_Label + " (" + self.Attribute.Attribute_Label + ")"

# Create your models here.
