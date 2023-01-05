from django.db import models
from helpers.models import TrackingModel
from  authentication.models import User


class Todo(TrackingModel):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=250)
    descriptio = models.TextField()
    is_complete=models.BooleanField(default=False)
    
    
    def __str__(self):
        return self.title
    
    
    


    
    
    
