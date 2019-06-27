from django.db import models

class TimeStampModel(models.Model):
    created_date = models.DateTimeField(auto_now=True)
    updated_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True 


class Content(TimeStampModel):
    title = models.CharField(max_length=255)
    description = models.TextField() 
    thumbnail = models.ImageField()
    category = models.ManyToManyField('Category')
    
    def __str__(self):
        return self.title

    class Meta:
        pass 


class Resource(TimeStampModel):
    resource_name = models.CharField(max_length=255)
    content = models.ForeignKey("Content", on_delete=models.CASCADE)
    resource = models.FileField(upload_to="uploads/resource")
    
    def __str__(self):
        return self.resource_name

    



class Category(TimeStampModel):
    category_name = models.CharField(max_length=255)

    def __str__(self):
        return self.category_name