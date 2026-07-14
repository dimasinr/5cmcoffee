import random
from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from recommendation.models import Preferensi, Rekomendasi, MenuKopi
from recommendation.services.recommendation_engine import get_recommendations

User = get_user_model()

class Command(BaseCommand):
    help = 'Seeds the database with 300 Indonesian youth/slang users, each with 3 preferences and 9 recommendations.'

    def handle(self, *args, **kwargs):
        # Lists of trendy/youthful Indonesian names and slang descriptors
        first_names = [
            "Adit", "Bagas", "Daffa", "Farel", "Gavin", "Kevin", "Naufal", "Raka", "Rafi", "Reza",
            "Alya", "Bella", "Cinta", "Diva", "Elsa", "Fira", "Gita", "Hana", "Jihan", "Keisha",
            "Laras", "Nabila", "Salsa", "Tiara", "Zara", "Chika", "Rachel", "Jessica", "Amanda", "Brandon",
            "Darren", "Kenzo", "Devano", "Arka", "Zayyan", "Gathan", "Reyhan", "Athalla", "Verrel", "Natasha",
            "Syifa", "Lyodra", "Keisya", "Mahalini", "Ziva", "Ghea", "Salma", "Rony", "Paul", "Nyoman",
            "Bimo", "Diki", "Fajar", "Gilang", "Indra", "Kiki", "Lutfi", "Yusuf", "Zain", "Aldo",
            "Angga", "Arya", "Bintang", "Cakra", "Dimas", "Edo", "Fahri", "Haikal", "Iqbal",
            "Jody", "Leo", "Mario", "Nico", "Oki", "Pandu", "Rama", "Satria", "Tio",
            "Umar", "Vino", "Wahyu", "Xavier", "Yoga", "Zack", "Ayu", "Citra", "Dhea", "Eka",
            "Febby", "Gaby", "Hilda", "Intan", "Jenny", "Kartika", "Lia", "Maya", "Niken", "Olga",
            "Pipit", "Queen", "Rini", "Santi", "Tari", "Uli", "Vivi", "Wulan", "Yani", "Zelda"
        ]
        
        last_names = [
            "Pratama", "Putra", "Putri", "Wijaya", "Kusuma", "Laksana", "Hidayat", "Santoso", "Wibowo", "Siregar",
            "Sinaga", "Ginting", "Nasution", "Sitorus", "Manurung", "Simanjuntak", "Siahaan", "Pohan", "Lubis", "Pane"
        ]

        # Generate unique names
        generated_names = set()
        while len(generated_names) < 300:
            first = random.choice(first_names)
            second = random.choice(last_names)
            
            # Add sometimes a third part to make it even more unique/fun
            if random.random() < 0.2:
                third = random.choice(last_names)
                name = f"{first} {second} {third}"
            else:
                name = f"{first} {second}"
                
            generated_names.add(name)

        names_list = list(generated_names)
        random.shuffle(names_list)

        self.stdout.write("Generating 300 users...")

        menus = list(MenuKopi.objects.all())
        if not menus:
            self.stdout.write(self.style.ERROR("Error: MenuKopi table is empty. Run seed_coffee_data first."))
            return

        users_created = 0
        for i in range(300):
            nama = names_list[i]
            # Create a cool/slangy email
            clean_name = nama.lower().replace(" ", ".")
            email = f"{clean_name}{random.randint(10, 99)}@gmail.com"
            
            # Ensure unique email
            while User.objects.filter(email=email).exists():
                email = f"{clean_name}{random.randint(100, 999)}@gmail.com"

            # Create User
            user = User.objects.create_user(
                email=email,
                nama=nama,
                password="password123"
            )
            users_created += 1

            # Create 3 Preferences
            last_pref_dict = None
            for p in range(3):
                pref_dict = {
                    'kemanisan': random.randint(1, 5),
                    'kepahitan': random.randint(1, 5),
                    'keasaman': random.randint(1, 5),
                    'body': random.randint(1, 5),
                    'aroma': random.randint(1, 3),
                    'susu': random.choice([True, False]),
                    'suhu': random.choice([True, False]),
                    'jenis_kopi': random.choice([1, 2, 3]),
                    'kafein': random.choice([1, 2, 3]),
                }
                Preferensi.objects.create(
                    id_user=user,
                    kemanisan=pref_dict['kemanisan'],
                    kepahitan=pref_dict['kepahitan'],
                    keasaman=pref_dict['keasaman'],
                    body=pref_dict['body'],
                    aroma=pref_dict['aroma'],
                    susu=pref_dict['susu'],
                    suhu=pref_dict['suhu'],
                    jenis_kopi=pref_dict['jenis_kopi'],
                    kafein=pref_dict['kafein']
                )
                last_pref_dict = pref_dict

            # Create 9 Recommendations based on the last preference
            recommendations = get_recommendations(last_pref_dict, k=9)
            for rank, rec in enumerate(recommendations):
                Rekomendasi.objects.create(
                    id_user=user,
                    id_menu=rec['menu'],
                    nilai_jarak=rec['distance'],
                    ranking=rank + 1
                )

        self.stdout.write(self.style.SUCCESS(f"Successfully generated {users_created} users, {users_created * 3} preferences, and {users_created * 9} recommendations."))
