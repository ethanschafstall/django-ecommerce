from django.db import models

class User(models.Model):
    
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=99)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    account_creation_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
    def account_info(self):
        return f"{self.account_creation_date}"
