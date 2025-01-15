from django.db import models

from django.db import models

class Contact(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100) 
    email = models.EmailField()
    phone_number = models.CharField(max_length=15) 
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} {self.surname}"




class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Work(models.Model):
    image = models.ImageField(upload_to='work_images/')
    title = models.CharField(max_length=200)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    date = models.DateField()
    

    def __str__(self):
        return self.title



