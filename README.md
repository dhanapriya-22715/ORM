# Ex02 Django ORM Web Application
# Date:29-11-2024
# AIM
To develop a Django application to store and retrieve data from a bank loan database using Object Relational Mapping(ORM).


## DESIGN STEPS
## STEP 1:
Clone the problem from GitHub

## STEP 2:
Create a new app in Django project

## STEP 3:
Enter the code for admin.py and models.py

## STEP 4:
Execute Django admin and create details for 10 Bank loan

# PROGRAM
```
admin.py 
from .models import Customer, Loan

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'phone_number')

@admin.register(Loan)
class LoanAdmin(admin.ModelAdmin):
    list_display = ('customer', 'loan_type', 'loan_amount', 'interest_rate', 'tenure_months', 'issue_date')
 

models.pyfrom django.db import models

class Customer(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Loan(models.Model):
    LOAN_TYPES = [
        ('Personal', 'Personal Loan'),
        ('Home', 'Home Loan'),
        ('Car', 'Car Loan'),
        ('Education', 'Education Loan'),
    ]

    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='loans')
    loan_type = models.CharField(max_length=50, choices=LOAN_TYPES)
    loan_amount = models.DecimalField(max_digits=12, decimal_places=2)
    interest_rate = models.DecimalField(max_digits=5, decimal_places=2)
    tenure_months = models.IntegerField()
    issue_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.loan_type} - {self.loan_amount} for {self.customer}"

```
# OUTPUT
![Screenshot (33)](https://github.com/user-attachments/assets/13be2fef-0a8f-42bd-b43a-e32a12e84b5f)
![Screenshot (34)](https://github.com/user-attachments/assets/a0de5c4b-70e4-471b-898c-63ca51b89db2)


# RESULT
Thus the program for creating a database using ORM hass been executed successfully
