from django.conf import settings
from apps.QLA.models import School, Country
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.db import models
from django.core.validators import RegexValidator
import re
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

gender = settings.GENDER
type_of_user = settings.TYPE_OF_USER


class UserAccountManager(BaseUserManager):
    use_in_migrations = True

    def create_user_super(self, email, firstname, lastname, password=None):
        if not email:
            raise ValueError('User must have an email')
        email = self.normalize_email(email)
        user = self.model(
            email=email,
            firstname=firstname,
            lastname=lastname,
        )
        user.is_active = True
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, firstname, lastname, School, Country, password=None):
        if not email:
            raise ValueError('User must have an email')
        email = self.normalize_email(email)
        user = self.model(
            email=email,
            firstname=firstname,
            lastname=lastname,
            School=School,
            Country=Country
        )
        user.is_active = True
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, firstname, lastname, password):
        user = self.create_user_super(email, firstname, lastname, password)
        user.is_staff = True
        user.is_superuser = True
        user.is_active = True
        user.save(using=self._db)
        return user


# Here we can add more domain, they would be whitelisted by default only @edu.com/.pk is valid
# domain_validator = RegexValidator(
#     regex=r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.+-]+\.(edu|edu.pk|)$',
#     message='Domain not valid',
#     code='invalid_domain',
# )


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True
                              # , validators=[domain_validator]
                              )
    username = models.CharField(max_length=100, null=True, blank=True)
    date_of_birth = models.DateField(default=None, null=True)
    firstname = models.CharField(max_length=100, null=True, blank=True)
    lastname = models.CharField(max_length=100, null=True, blank=True)
    is_active = models.BooleanField(default=False)
    gender = models.CharField(max_length=100, choices=gender)
    type_of_user = models.CharField(max_length=100, choices=type_of_user, default='TBD')
    pic = models.ImageField(upload_to="media/profile_pictures", blank=True, null=True)
    School = models.ForeignKey(School, on_delete=models.DO_NOTHING, blank=True, null=True)
    Country = models.ForeignKey(Country, on_delete=models.DO_NOTHING, blank=True, null=True)
    is_staff = models.BooleanField(default=False)  # For help in login to admin
    AccountOwner = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['firstname', 'lastname']

    objects = UserAccountManager()

    def get_short_name(self):
        return self.email

    def __str__(self):
        return self.email

    # def save(self, *args, **kwargs):
    #     # print(self.email)
    #     for x in emailValidator:
    #         result = re.search(x, self.email)
    #         print(result, "result")
    #         if result is None:
    #             raise ValidationError(
    #                 _('%(value)s is not an valid email domain, use Edu domain'),
    #                 params={'value': self.email},
    #             )
    #         else:
    #             print(self.email, "else")
