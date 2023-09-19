from django.db import models
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager
# Create your models here.
class UserManager(BaseUserManager):
    def create_user(self,email,username,first_name=None,last_name=None,password=None,password2=None):
        if not email:
            raise ValueError("Users must have an email")
    
        user = self.model(
            email=self.normalize_email(email),
            first_name=first_name,
            last_name=last_name,
            username=username
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self,email,username,password):
        user=self.create_user(
            email,
            password=password,
            
            username=username
        )
        user.is_admin=True
        user.save(using=self._db)
        return user
    
class User(AbstractBaseUser):
    email=models.EmailField(verbose_name='email address',max_length=250,unique=True)
    first_name=models.CharField(max_length=250,null=True,blank=True)
    last_name=models.CharField(max_length=250,null=True,blank=True)
    username=models.CharField(max_length=250)
    is_admin = models.BooleanField(default=False)
    is_active= models.BooleanField(default=True)
    objects=UserManager()

    USERNAME_FIELD="email"
    REQUIRED_FIELDS=['username']

    def __str__(self) :
        return self.email
    

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return self.is_admin

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin
    

class Profile(AbstractBaseUser):
    name=  models.CharField(max_length=250)
    place= models.CharField(max_length=250)
    phone=models.IntegerField()
    email=models.EmailField(max_length=250)

    def __str__(self) :
        return self.place