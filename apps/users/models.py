from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin
from django.utils.translation import gettext_lazy as _

class UserManager(BaseUserManager):
    def create_user(self, email, password=None):
        if not email:
            raise ValueError(_('Users must have an phone_number'))

        user = self.model(
            email=email,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None):
        user = self.create_user(
            email,
            password=password,
        )

        user.is_admin = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin):
    CHOICES = (
        ('oz', _('O\'zbek')),
        ('en', _('Ingliz')),
    )
    email = models.EmailField(unique=True, verbose_name=_("Email"))
    name = models.CharField(max_length=50, null=True, blank=True, verbose_name=_("Ism"))
    username = models.CharField(max_length=50, null=True, unique=True, verbose_name=_("Foydalanuvchi nomi"))
    language = models.CharField(choices=CHOICES, max_length=3, verbose_name=_("Til"))
    description = models.TextField(null=True, blank=True, verbose_name=_("Qo'shimcha ma'lumot"))
    create_at = models.DateTimeField(auto_now_add=True, verbose_name=_("Qo'shilgan vaqti"))
    is_active = models.BooleanField(default=True, verbose_name=_("Holati"))
    is_admin = models.BooleanField(default=False, verbose_name=_("Adminmi?"))

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return str(self.name)

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    class Meta:
        verbose_name = _("Foydalanuvchi")
        verbose_name_plural = _("Foydalanuvchilar")

    @property
    def is_staff(self):
        return self.is_admin

########################
