from django.db import models

# Creating AuthorDetails Table

class AuthorDeatils(models.Model):
    Author_id = models.AutoField(primary_key=True)
    AuthorName = models.CharField(max_length=50)

    def AuthorSave(self):
        self.save()


    def __str__(self):
        return self.AuthorName

# creating BookDetails Table
# class BookDetails(models.Model):
#     Book_id=models.AutoField(primary_key=True)
#     Author_id=models.ForeignKey(AuthorDeatils, on_delete=models.CASCADE)
#     BookName=models.CharField(max_length=120)
#     Genre=models.CharField(max_length=60)
#     Desc=models.TextField()
#
#     def BookSave(self):
#         self.save()
#
#     def __str__(self):
#         return self.BookName


# creating PublicationDetails Table
class PublicationDetails(models.Model):
    Pub_id = models.AutoField(primary_key = True)
    PubName = models.CharField(max_length = 120)


    def PublicationSave(self):
        self.save()

    def __str__(self):
        return self.PubName

#creating Bookdetails Table

class BookDetails(models.Model):
    Pub_id = models.ForeignKey(PublicationDetails, on_delete= models.CASCADE)
    Author_id = models.ForeignKey(AuthorDeatils, on_delete= models.CASCADE)
    BookName = models.CharField(max_length = 60)
    Genre = models.CharField(max_length=60)
    Launch_Year = models.PositiveIntegerField()
    Desc = models.TextField()

    def BookSave(self):
        self.save()
