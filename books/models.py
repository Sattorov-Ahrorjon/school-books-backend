from django.db import models


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Class(BaseModel):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Category(BaseModel):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Book(BaseModel):
    name = models.CharField(max_length=100)
    image = models.FileField(upload_to='books/images/')
    about = models.TextField()
    publication = models.DateField()
    file = models.FileField(upload_to='books/files/')
    class_name = models.ForeignKey(to=Class, on_delete=models.CASCADE)
    category = models.ForeignKey(to=Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
