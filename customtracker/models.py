from django.db import models
from django.contrib.auth.models import User
#from django.contrib.auth.models import authenticate


# need users, items, measure words
#user = User.objects.create_user('john', 'lennon@thebeatles.com', 'johnpassword')
#user = User.objects.create_user('john', 'secret')
#user.save()

# tables
# ---------------
# username, 
# item_names 
# measure_words
Class AppUser(models.Model):
    username = models.CharField(max_length=50)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.CharField(max_length=100)
    #this should be done by base class
    #password = 
    # one to many?
    items = models.ManyToManyField(Item)
    preferred_mw = models.ManyToManyField(MeasureWord, through='Pairings')
    # preferred measure words? fk lookup on items

Class Item(model.Model):
    name = models.CharField(max_length=100)

Class MeasureWord(model.Model):
    name = models.CharField(max_length=100)

Class Pairings:
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    measure_word = models.ForeignKey(MeasureWord, on_delete=models.CASCADE)

Class Session(model.Model):
    # date
    # username fk
    # item fk
    # amount
    # measure word fk 

#measure words 

# session =>
# item, date, "level" (aka length or amount depending on measure word), username
