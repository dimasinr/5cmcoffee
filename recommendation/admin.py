from django.contrib import admin
from django.utils.html import format_html
from django.contrib.auth import get_user_model
from .models import MenuKopi, Preferensi, Rekomendasi

User = get_user_model()

@admin.register(User)
class MyUserAdmin(admin.ModelAdmin):
    list_display = ('email', 'nama', 'is_staff')
    search_fields = ('email', 'nama')

@admin.register(MenuKopi)
class MenuKopiAdmin(admin.ModelAdmin):
    list_display = (
        'nama_menu', 'kemanisan', 'kepahitan', 'keasaman',
        'body', 'aroma', 'susu', 'suhu',
        'jenis', 'kafein', 'image_preview'
    )
    list_filter = ('aroma', 'kafein', 'susu', 'suhu', 'jenis')
    search_fields = ('nama_menu', 'description')

    def image_preview(self, obj):
        if obj.image:
            return format_html(
                '<img src="{}" width="50" height="50" style="border-radius:5px; object-fit:cover;" />',
                obj.image.url
            )
        return "-"
    image_preview.short_description = "Gambar"

@admin.register(Preferensi)
class PreferensiAdmin(admin.ModelAdmin):
    list_display = ('id_user', 'created_at', 'kemanisan', 'kepahitan')

@admin.register(Rekomendasi)
class RekomendasiAdmin(admin.ModelAdmin):
    list_display = ('id_user', 'id_menu', 'nilai_jarak', 'ranking')
