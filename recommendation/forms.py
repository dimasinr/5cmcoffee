from django import forms
from django.contrib.auth import get_user_model
from .models import MenuKopi, Preferensi

User = get_user_model()

LEVEL_CHOICES = [(i, str(i)) for i in range(1, 6)]
AROMA_CHOICES = [(1, 'Ringan'), (2, 'Sedang'), (3, 'Kuat')]
CAFFEINE_CHOICES = [(1, 'Rendah'), (2, 'Sedang'), (3, 'Tinggi')]
COFFEE_TYPE_CHOICES = [(1, 'Arabica'), (2, 'Robusta'), (3, 'Blend')]

class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'w-full border border-coffee-200 rounded-xl px-4 py-2 bg-cream-50 focus:ring-2 focus:ring-coffee-300 outline-none'}))
    password_confirm = forms.CharField(label='Konfirmasi Password', widget=forms.PasswordInput(attrs={'class': 'w-full border border-coffee-200 rounded-xl px-4 py-2 bg-cream-50 focus:ring-2 focus:ring-coffee-300 outline-none'}))

    class Meta:
        model = User
        fields = ['nama', 'email']
        labels = {
            'nama': 'Nama Lengkap',
            'email': 'Alamat Email',
        }
        widgets = {
            'nama': forms.TextInput(attrs={'class': 'w-full border border-coffee-200 rounded-xl px-4 py-2 bg-cream-50 focus:ring-2 focus:ring-coffee-300 outline-none'}),
            'email': forms.EmailInput(attrs={'class': 'w-full border border-coffee-200 rounded-xl px-4 py-2 bg-cream-50 focus:ring-2 focus:ring-coffee-300 outline-none'}),
        }

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        password_confirm = cleaned_data.get("password_confirm")

        if password and password_confirm and password != password_confirm:
            raise forms.ValidationError("Password tidak cocok.")
        return cleaned_data

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user

class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['nama', 'email', 'is_staff']
        widgets = {
            'nama': forms.TextInput(attrs={'class': 'w-full border border-coffee-200 rounded-xl px-4 py-2 bg-cream-50 focus:ring-2 focus:ring-coffee-300 outline-none'}),
            'email': forms.EmailInput(attrs={'class': 'w-full border border-coffee-200 rounded-xl px-4 py-2 bg-cream-50 focus:ring-2 focus:ring-coffee-300 outline-none'}),
            'is_staff': forms.CheckboxInput(attrs={'class': 'w-4 h-4 text-coffee-600 border-coffee-300 rounded focus:ring-coffee-500'}),
        }

class MenuForm(forms.ModelForm):
    class Meta:
        model = MenuKopi
        fields = [
            'nama_menu', 'kemanisan', 'kepahitan', 'keasaman', 
            'body', 'aroma', 'susu', 'suhu', 
            'jenis', 'kafein', 'description', 'image'
        ]
        widgets = {
            'nama_menu': forms.TextInput(attrs={'class': 'w-full border border-coffee-200 rounded-xl px-4 py-2 bg-cream-50'}),
            'description': forms.Textarea(attrs={'class': 'w-full border border-coffee-200 rounded-xl px-4 py-2 bg-cream-50', 'rows': 3}),
            'kemanisan': forms.NumberInput(attrs={'type': 'range', 'min': '1', 'max': '5', 'class': 'w-full'}),
            'kepahitan': forms.NumberInput(attrs={'type': 'range', 'min': '1', 'max': '5', 'class': 'w-full'}),
            'keasaman': forms.NumberInput(attrs={'type': 'range', 'min': '1', 'max': '5', 'class': 'w-full'}),
            'body': forms.NumberInput(attrs={'type': 'range', 'min': '1', 'max': '5', 'class': 'w-full'}),
            'aroma': forms.Select(choices=AROMA_CHOICES, attrs={'class': 'w-full border border-coffee-200 rounded-xl px-4 py-2 bg-cream-50'}),
            'jenis': forms.Select(choices=COFFEE_TYPE_CHOICES, attrs={'class': 'w-full border border-coffee-200 rounded-xl px-4 py-2 bg-cream-50'}),
            'kafein': forms.Select(choices=CAFFEINE_CHOICES, attrs={'class': 'w-full border border-coffee-200 rounded-xl px-4 py-2 bg-cream-50'}),
            'image': forms.FileInput(attrs={'class': 'w-full text-sm text-coffee-500 file:mr-4 file:py-2 file:px-4 file:rounded-full file:border-0 file:text-sm file:font-semibold file:bg-coffee-50 file:text-coffee-700 hover:file:bg-coffee-100'}),
        }

class PreferenceForm(forms.Form):
    kemanisan = forms.IntegerField(
        min_value=1, max_value=5,
        label="Tingkat Kemanisan",
        initial=3,
        widget=forms.NumberInput(attrs={'type': 'range', 'min': '1', 'max': '5', 'step': '1', 'class': 'pref-slider'})
    )
    kepahitan = forms.IntegerField(
        min_value=1, max_value=5,
        label="Tingkat Kepahitan",
        initial=3,
        widget=forms.NumberInput(attrs={'type': 'range', 'min': '1', 'max': '5', 'step': '1', 'class': 'pref-slider'})
    )
    keasaman = forms.IntegerField(
        min_value=1, max_value=5,
        label="Tingkat Keasaman",
        initial=3,
        widget=forms.NumberInput(attrs={'type': 'range', 'min': '1', 'max': '5', 'step': '1', 'class': 'pref-slider'})
    )
    body = forms.IntegerField(
        min_value=1, max_value=5,
        label="Body / Kekentalan",
        initial=3,
        widget=forms.NumberInput(attrs={'type': 'range', 'min': '1', 'max': '5', 'step': '1', 'class': 'pref-slider'})
    )
    aroma = forms.ChoiceField(
        choices=AROMA_CHOICES,
        label="Aroma",
        initial=2,
        widget=forms.RadioSelect(attrs={'class': 'pref-radio'})
    )
    susu = forms.BooleanField(
        required=False,
        label="Dengan Susu",
        widget=forms.CheckboxInput(attrs={'class': 'pref-toggle'})
    )
    suhu = forms.BooleanField(
        required=False,
        label="Disajikan Panas",
        widget=forms.CheckboxInput(attrs={'class': 'pref-toggle'})
    )
    jenis_kopi = forms.ChoiceField(
        choices=COFFEE_TYPE_CHOICES,
        label="Jenis Biji Kopi",
        initial=1,
        widget=forms.RadioSelect(attrs={'class': 'pref-radio'})
    )
    kafein = forms.ChoiceField(
        choices=CAFFEINE_CHOICES,
        label="Level Kafein",
        initial=2,
        widget=forms.RadioSelect(attrs={'class': 'pref-radio'})
    )
