from django.db import models


class Notice(models.Model) :
    id = models.CharField(max_length = 10, primary_key=True)
    name = models.CharField(max_length = 255)
    date = models.CharField(max_length = 10)
    url = models.CharField(max_length = 255)

    class Meta : 
        ordering = ['-id'] #역순으로 정렬