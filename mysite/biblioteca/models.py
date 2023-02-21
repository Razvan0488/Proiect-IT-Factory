from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=200)
    origin = models.CharField(max_length=100)
    date_of_birth = models.DateTimeField()
    def __str__(self):
        return f"Author(name={self.name},origin={self.origin},date of birth = {self.date_of_birth})"
    def __repr__(self):
        return self.__str__()

class Book(models.Model):
    title = models.CharField(max_length=100)
    published_year = models.IntegerField(null=True)
    number_of_pages = models.IntegerField()
    genre = models.CharField(max_length=100)
    cover = models.CharField(max_length=1000,null = True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE,null= True)

    def __str__(self):
        return f"Book(title={self.title},published_date={self.published_year},number_of_pages = {self.number_of_pages}," \
               f"genre= {self.genre},author ={self.author.name})"

    def __repr__(self):
        return self.__str__()
