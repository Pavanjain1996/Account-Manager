from django.db import models

class Account(models.Model):
    user = models.CharField(max_length=30,default='')
    account = models.CharField(max_length=30)
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
    pin = models.CharField(max_length=30,default='')

    def __str__(self):
        return self.account

class BankAccount(models.Model):
    user = models.CharField(max_length=30,default='')
    name = models.CharField(max_length=30,default='Pavan Jain')
    bank = models.CharField(max_length=30)
    account_no = models.CharField(max_length=30)
    IFSC = models.CharField(max_length=30)
    atm_card_no = models.CharField(max_length=30)
    cvv = models.CharField(max_length=5)
    atm_pin = models.CharField(max_length=5)
    card_expiry = models.CharField(max_length=5)
    net_banking_id = models.CharField(max_length=30)
    signin_password = models.CharField(max_length=30)
    transaction_password = models.CharField(max_length=30)
    mob_banking_pin = models.CharField(max_length=30)

    def __str__(self):
        return self.bank
