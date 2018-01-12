from django.db import models
from attributes.models import Options

# Create your models here.

class Result(models.Model):
     answer_id = models.IntegerField(primary_key=True)
     parametres=models.ManyToManyField(Options, related_name="all_param")
     attribute = models.ForeignKey(Options, on_delete=models.CASCADE, related_name="cur_param")
     result=models.IntegerField()
     source=models.CharField(max_length=200)

     def __str__(self):
        return self.attribute.Option_Label + " = " + str(self.result)
