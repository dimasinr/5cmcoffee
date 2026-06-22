from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

class UserManager(BaseUserManager):
    def create_user(self, email, nama, password=None):
        if not email:
            raise ValueError('Email wajib diisi')
        user = self.model(
            email=self.normalize_email(email),
            nama=nama,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, nama, password=None):
        user = self.create_user(email, nama, password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

class User(AbstractBaseUser, PermissionsMixin):
    id_user = models.AutoField(primary_key=True)
    nama = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['nama']

    class Meta:
        db_table = 'user'
        verbose_name = 'User'
        verbose_name_plural = 'User'

    def __str__(self):
        return self.nama

class MenuKopi(models.Model):
    id_menu = models.AutoField(primary_key=True)
    nama_menu = models.CharField(max_length=100)
    kemanisan = models.IntegerField(help_text="Skala 1-5")
    kepahitan = models.IntegerField(help_text="Skala 1-5")
    keasaman = models.IntegerField(help_text="Skala 1-5")
    body = models.IntegerField(help_text="Skala 1-5")
    aroma = models.IntegerField(help_text="Skala 1-3")
    susu = models.BooleanField(default=False, help_text="0/1")
    suhu = models.BooleanField(default=True, help_text="0=dingin, 1=panas")
    jenis = models.IntegerField(help_text="Kategori")
    kafein = models.IntegerField(help_text="Level")
    description = models.TextField(blank=True, null=True) # Tambahan untuk UI
    image = models.ImageField(upload_to='coffee_images/', blank=True, null=True) # Tambahan untuk UI

    class Meta:
        db_table = 'menu_kopi'
        verbose_name = 'Menu Kopi'
        verbose_name_plural = 'Menu Kopi'

    def __str__(self):
        return self.nama_menu

class Preferensi(models.Model):
    id_preferensi = models.AutoField(primary_key=True)
    id_user = models.ForeignKey(User, on_delete=models.CASCADE, db_column='id_user')
    kemanisan = models.IntegerField()
    kepahitan = models.IntegerField()
    keasaman = models.IntegerField()
    body = models.IntegerField()
    aroma = models.IntegerField()
    susu = models.BooleanField()
    suhu = models.BooleanField()
    jenis_kopi = models.IntegerField()
    kafein = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'preferensi'
        verbose_name = 'Preferensi'
        verbose_name_plural = 'Preferensi'

class Rekomendasi(models.Model):
    id_rekomendasi = models.AutoField(primary_key=True)
    id_user = models.ForeignKey(User, on_delete=models.CASCADE, db_column='id_user')
    id_menu = models.ForeignKey(MenuKopi, on_delete=models.CASCADE, db_column='id_menu')
    nilai_jarak = models.FloatField()
    ranking = models.IntegerField()

    class Meta:
        db_table = 'rekomendasi'
        verbose_name = 'Rekomendasi'
        verbose_name_plural = 'Rekomendasi'
