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
    
    def __str__(self):
        return self.title 


class Resource(TimeStampModel):
    resource_name = models.CharField(max_length=255)
    resource_type = models.ForeignKey("ContentType", on_delete=models.CASCADE)
    resource = models.FileType(upload_to="uploads/resource")
    
    def __str__(self):
        return self.content_name