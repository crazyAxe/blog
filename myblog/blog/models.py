from django.db import models
# Create your models here.


# normal visitors, just can comment the blog
class User(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField()
    password = models.CharField(max_length=20)
    image = models.ImageField()

    def __str__(self):
        return self.name


# blog's author
class Author(User):
    admin = models.BooleanField(default=1)


class Type(models.Model):
    tag = models.CharField(max_length=20)

    def __str__(self):
        return self.tag


class Blog(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    blog_type = models.ManyToManyField(Type)
    headline = models.CharField(max_length=50)
    blog_content = models.TextField(max_length=2000)
    create_time = models.DateTimeField(auto_now=True)
    digest = models.TextField(max_length=200, null=True)

    def __str__(self):
        return self.headline


class Comments(models.Model):
    visitor_name = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.TextField(max_length=200)
    pud_date = models.DateTimeField()

    def __str__(self):
        return self.comment

