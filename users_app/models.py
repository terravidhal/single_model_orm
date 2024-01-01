from django.db import models

# Create your models here.
class Users(models.Model):
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    email = models.EmailField(max_length=254)
    age = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True) 

    def __str__(self):
        return f"<Users object: {self.first_name} ({self.id})>"
    


 # Users_shell Commands : 

""" 

python manage.py shell

>>> from users_app.models import Users
>>> Users.objects.all()
<QuerySet []>

>>> Users.objects.create(first_name = "terra", last_name = "vidhal", email = "terravidhal@yahoo.com", age = 15)
<Users: Users object (1)>

>>> Users.objects.create(first_name = 'nick', last_name = 'santora', email = "nicksantora@gmail.com", age = 25)
<Users: Users object (2)>

>>> Users.objects.create(first_name = 'mark', last_name = 'evans', email = "markevans@gmail.com", age = 12)
<Users: Users object (3)>

>>> Users.objects.all()
<QuerySet [<Users: <Users object: terra (1)>>, <Users: <Users object: nick (2)>>, <Users: <Users object: mark (3)>>]>

>>> Users.objects.last()
<Users: <Users object: mark (3)>>

>>> Users.objects.first()
<Users: <Users object: terra (1)>>

 user_to_update = Users.objects.get(id=3)
>>> user_to_update.first_name = "Pancakes"
>>> user_to_update.save()
>>> Users.objects.last()
<Users: <Users object: Pancakes (3)>>

user_to_delete = Users.objects.get(id=2)
>>> user_to_delete.delete()
(1, {'users_app.Users': 1})
>>> Users.objects.all()
<QuerySet [<Users: <Users object: terra (1)>>, <Users: <Users object: Pancakes (3)>>]>


>>> Users.objects.all().order_by("last_name")
<QuerySet [<Users: <Users object: Pancakes (3)>>, <Users: <Users object: terra (1)>>]>

>>> Users.objects.all().order_by("-last_name")
<QuerySet [<Users: <Users object: terra (1)>>, <Users: <Users object: Pancakes (3)>>]>

 """      