from django.db import models
from attributes.models import Options



class ProductQuerySet(models.query.QuerySet):
    def active(self):
        return self.filter(source="data1.sav")

 



class ProductManager(models.Manager):
    def all(self, *args, **kwargs):
       return self.get_queryset().active()
    
    def get_queryset(self):
        return ProductQuerySet(self.model, using=self._db)




class Result(models.Model):
     answer_id = models.IntegerField(primary_key=True)
     respondent_id=models.IntegerField()
     parametres=models.ManyToManyField(Options, related_name="all_param")
     attribute = models.ForeignKey(Options, on_delete=models.CASCADE, related_name="cur_param")
     result=models.IntegerField()
     source=models.CharField(max_length=200)
     date_field=models.DateField(null=True, blank=True)
     objects = ProductManager()



     #def __str__(self):
     #   return self.result

     def res_data(self):
        return (self.result, self.date_field)
     
     def get_all_data(self):   
     	return 
