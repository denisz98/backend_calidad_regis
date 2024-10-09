from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin
from simple_history.models import HistoricalRecords


class UserManager(BaseUserManager):
    def _create_user(self, username,rol, email, name,last_name, password, is_staff, is_superuser, **extra_fields):
        user = self.model(
            username = username,
            rol = rol,
            email = email,
            name = name,
            last_name = last_name,
            is_staff = is_staff,
            is_superuser = is_superuser,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self.db)
        return user

    def create_user(self, username,rol, email, name,last_name, password=None, **extra_fields):
        return self._create_user(username,rol, email, name,last_name, password, False, False, **extra_fields)

    def create_superuser(self, username,rol, email, name,last_name, password=None, **extra_fields):
        return self._create_user(username,rol, email, name,last_name, password, True, True, **extra_fields)

class User(AbstractBaseUser):
    username = models.CharField(max_length = 255, unique = True)
    rol = models.CharField('Rol', max_length = 255)
    email = models.EmailField('Correo Electrónico',max_length = 255, unique = True,)
    name = models.CharField('Nombres', max_length = 255, blank = True, null = True)
    last_name = models.CharField('Apellidos', max_length = 255, blank = True, null = True)
    # image = models.ImageField('Imagen de perfil', upload_to='perfil/', max_length=255, null=True, blank = True)
    is_active = models.BooleanField(default = True)
    is_staff = models.BooleanField(default = False)
    objects = UserManager()

    def has_perm(self, perm, obj=None):
        """
        Return True if the user has the specified permission. Query all
        available auth backends, but return immediately if any backend returns
        True. Thus, a user who has permission from a single auth backend is
        assumed to have permission in general. If an object is provided, check
        permissions for that object.
        """
        # Active superusers have all permissions.
        if self.is_active and self.is_staff:
            return True

        return False

    def has_module_perms(self, app_label):
        return True

    class Meta:
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['rol','email','name','last_name']

    def __str__(self):
        return f'{self.name} {self.last_name}'
