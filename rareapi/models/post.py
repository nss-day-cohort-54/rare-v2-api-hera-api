from django.db import models

class Post(models.Model):

    user = models.ForeignKey("RareUser", on_delete=models.CASCADE)
    category = models.ForeignKey("Category", on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    publication_date = models.DateField()
    image_url = models.CharField(max_length=500)
    content = models.CharField(max_length=150)
    approved = models.BooleanField()
    
    @property
    def is_authorized(self):
        return self.__is_authorized
    
    @is_authorized.setter
    def is_authorized(self,value):
        self.__is_authorized = value
    