from django.contrib.auth.base_user import BaseUserManager


class CustomUserManager(BaseUserManager):
    """
    Prilagođeni manager za Racun klasu koji stvara Django korisnika
    s identifikacijom putem emaila umjesto usernamea
    """
    def create_user(self, email, password, **extra_fields):
        """
        Stvaranje i spremanje korisnika s emailom i lozinkom
        """
        if not email:
            raise ValueError('Email ne smije biti prazan')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):
        """
        Stvaranje i spremanje administratora s emailom i lozinkom
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superkorisnik mora imati is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superkorisnik mora imati is_superuser=True.')
        return self.create_user(email, password, **extra_fields)