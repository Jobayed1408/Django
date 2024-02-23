from django.db import models

# Create your models here.
class TaskModel(models.Model): 
    # CATEGORY = (
    #     ('Mystery', 'Mystery'),
    #     ('Thriller', 'Triller'),
    #     ('Sci-Fi', 'Sci-Fi'),
    #     ('Humor', 'Humor'),
    #     ('Horror', 'Horror'), 
    # )
    id = models.IntegerField(primary_key = True)
    taskTitle  = models.CharField(max_length=50)
    taskDescription = models.CharField(max_length=250)
    is_completed = models.BooleanField() 
    


    
