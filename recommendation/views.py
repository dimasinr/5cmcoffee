from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout, get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from .forms import PreferenceForm, UserRegistrationForm, UserEditForm, MenuForm
from .models import MenuKopi, Preferensi, Rekomendasi
from .services.recommendation_engine import get_recommendations

User = get_user_model()

def register_view(request):
    if request.user.is_authenticated:
        return redirect('recommendation:form')
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('recommendation:form')
    else:
        form = UserRegistrationForm()
    return render(request, 'recommendation/register.html', {'form': form})

def login_view(request):
    if request.user.is_authenticated:
        if request.user.is_staff:
            return redirect('recommendation:admin_menu')
        return redirect('recommendation:form')
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('username') 
            password = form.cleaned_data.get('password')
            user = authenticate(username=email, password=password)
            if user is not None:
                login(request, user)
                if user.is_staff:
                    return redirect('recommendation:admin_menu')
                return redirect('recommendation:form')
    else:
        form = AuthenticationForm()
    return render(request, 'recommendation/login.html', {'form': form})

@login_required
def logout_confirm(request):
    if request.method == 'POST':
        logout(request)
        return redirect('recommendation:login')
    return render(request, 'recommendation/logout.html')

def home(request):
    if request.user.is_authenticated:
        return redirect('recommendation:form')
    return redirect('recommendation:login')

@login_required
def recommendation_form(request):
    if request.method == 'POST':
        form = PreferenceForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user_prefs = {
                'kemanisan': int(data['kemanisan']),
                'kepahitan': int(data['kepahitan']),
                'keasaman': int(data['keasaman']),
                'body': int(data['body']),
                'aroma': int(data['aroma']),
                'susu': bool(data['susu']),
                'suhu': bool(data['suhu']),
                'jenis_kopi': int(data['jenis_kopi']),
                'kafein': int(data['kafein']),
            }

            results = get_recommendations(user_prefs, k=3)

            if results:
                # Simpan Preferensi
                pref = Preferensi.objects.create(
                    id_user=request.user,
                    kemanisan=user_prefs['kemanisan'],
                    kepahitan=user_prefs['kepahitan'],
                    keasaman=user_prefs['keasaman'],
                    body=user_prefs['body'],
                    aroma=user_prefs['aroma'],
                    susu=user_prefs['susu'],
                    suhu=user_prefs['suhu'],
                    jenis_kopi=user_prefs['jenis_kopi'],
                    kafein=user_prefs['kafein'],
                )

                # Simpan Rekomendasi
                # Hapus rekomendasi lama untuk user ini jika ada
                Rekomendasi.objects.filter(id_user=request.user).delete()
                
                for i, res in enumerate(results):
                    Rekomendasi.objects.create(
                        id_user=request.user,
                        id_menu=res['menu'],
                        nilai_jarak=res['distance'],
                        ranking=i + 1
                    )

                request.session['recommendation_results_ids'] = [r['menu'].id_menu for r in results]
                request.session['recommendation_results_data'] = [
                    {'id': r['menu'].id_menu, 'similarity': r['similarity'], 'distance': r['distance']}
                    for r in results
                ]
                
                return redirect('recommendation:result')
            else:
                messages.error(request, 'Belum ada data menu kopi.')
    else:
        form = PreferenceForm()

    return render(request, 'recommendation/recommendation_form.html', {'form': form})

@login_required
def recommendation_result(request):
    result_data = request.session.get('recommendation_results_data')
    if not result_data:
        return redirect('recommendation:form')

    results = []
    for item in result_data:
        try:
            menu = MenuKopi.objects.get(id_menu=item['id'])
            results.append({
                'menu': menu,
                'similarity': item['similarity'],
                'distance': item['distance'],
            })
        except MenuKopi.DoesNotExist:
            pass

    if not results:
        return redirect('recommendation:form')

    return render(request, 'recommendation/recommendation_result.html', {
        'results': results,
    })

@login_required
def coffee_detail(request, pk):
    menu = get_object_or_404(MenuKopi, pk=pk)
    return render(request, 'recommendation/coffee_detail.html', {'menu': menu})

# Admin Views
@login_required
def admin_menu(request):
    if not request.user.is_staff:
        return redirect('recommendation:form')
    menus = MenuKopi.objects.all()
    return render(request, 'recommendation/admin_menu.html', {'menus': menus})

@login_required
def admin_menu_add(request):
    if not request.user.is_staff:
        return redirect('recommendation:form')
    if request.method == 'POST':
        form = MenuForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Menu berhasil ditambahkan.')
            return redirect('recommendation:admin_menu')
    else:
        form = MenuForm()
    return render(request, 'recommendation/admin_menu_form.html', {'form': form, 'title': 'Tambah Menu'})

@login_required
def admin_menu_edit(request, pk):
    if not request.user.is_staff:
        return redirect('recommendation:form')
    menu = get_object_or_404(MenuKopi, pk=pk)
    if request.method == 'POST':
        form = MenuForm(request.POST, request.FILES, instance=menu)
        if form.is_valid():
            form.save()
            messages.success(request, 'Menu berhasil diperbarui.')
            return redirect('recommendation:admin_menu')
    else:
        form = MenuForm(instance=menu)
    return render(request, 'recommendation/admin_menu_form.html', {'form': form, 'title': 'Edit Menu', 'menu': menu})

@login_required
def admin_menu_delete(request, pk):
    if not request.user.is_staff:
        return redirect('recommendation:form')
    menu = get_object_or_404(MenuKopi, pk=pk)
    menu.delete()
    messages.success(request, 'Menu berhasil dihapus.')
    return redirect('recommendation:admin_menu')

@login_required
def admin_users(request):
    if not request.user.is_staff:
        return redirect('recommendation:form')
    users = User.objects.all()
    return render(request, 'recommendation/admin_users.html', {'users': users})

@login_required
def admin_user_add(request):
    if not request.user.is_staff:
        return redirect('recommendation:form')
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Pengguna berhasil ditambahkan.')
            return redirect('recommendation:admin_users')
    else:
        form = UserRegistrationForm()
    return render(request, 'recommendation/admin_user_form.html', {'form': form, 'title': 'Tambah Pengguna'})

@login_required
def admin_user_edit(request, pk):
    if not request.user.is_staff:
        return redirect('recommendation:form')
    user = get_object_or_404(User, pk=pk)
    if request.method == 'POST':
        form = UserEditForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Pengguna berhasil diperbarui.')
            return redirect('recommendation:admin_users')
    else:
        form = UserEditForm(instance=user)
    return render(request, 'recommendation/admin_user_form.html', {'form': form, 'title': 'Edit Pengguna', 'edit_user': user})

@login_required
def admin_user_delete(request, pk):
    if not request.user.is_staff:
        return redirect('recommendation:form')
    user_to_delete = get_object_or_404(User, pk=pk)
    if user_to_delete == request.user:
        messages.error(request, 'Anda tidak dapat menghapus akun Anda sendiri.')
    else:
        user_to_delete.delete()
        messages.success(request, 'Pengguna berhasil dihapus.')
    return redirect('recommendation:admin_users')
