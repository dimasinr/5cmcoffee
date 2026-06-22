from django.core.management.base import BaseCommand
from recommendation.models import MenuKopi

class Command(BaseCommand):
    help = 'Seeds the database with initial coffee menu data'

    def handle(self, *args, **kwargs):
        coffee_data = [
            {
                "nama_menu": "Latte",
                "kemanisan": 4,
                "kepahitan": 2,
                "keasaman": 2,
                "body": 3,
                "aroma": 2,
                "susu": True,
                "suhu": True,
                "jenis": 1,
                "kafein": 2,
                "description": "Kopi espresso dengan rasio susu yang lebih banyak dan lapisan foam tipis di atasnya. Memiliki rasa yang creamy dan manis alami dari susu."
            },
            {
                "nama_menu": "Americano",
                "kemanisan": 1,
                "kepahitan": 4,
                "keasaman": 3,
                "body": 2,
                "aroma": 3,
                "susu": False,
                "suhu": True,
                "jenis": 1,
                "kafein": 2,
                "description": "Espresso yang ditambahkan air panas. Menghasilkan kopi hitam yang kuat dengan aroma khas espresso, namun dengan kepekatan yang lebih rendah."
            },
            {
                "nama_menu": "Cappuccino",
                "kemanisan": 3,
                "kepahitan": 3,
                "keasaman": 2,
                "body": 4,
                "aroma": 3,
                "susu": True,
                "suhu": True,
                "jenis": 1,
                "kafein": 2,
                "description": "Kombinasi klasik espresso, susu steamed, dan foam tebal. Keseimbangan sempurna antara rasa kopi yang kuat dan kelembutan susu."
            },
            {
                "nama_menu": "Espresso",
                "kemanisan": 1,
                "kepahitan": 5,
                "keasaman": 4,
                "body": 5,
                "aroma": 3,
                "susu": False,
                "suhu": True,
                "jenis": 1,
                "kafein": 3,
                "description": "Kopi pekat yang diekstraksi dengan tekanan tinggi. Sangat kuat, pahit, dengan crema kental di bagian atas."
            },
            {
                "nama_menu": "Flat White",
                "kemanisan": 3,
                "kepahitan": 3,
                "keasaman": 2,
                "body": 3,
                "aroma": 2,
                "susu": True,
                "suhu": True,
                "jenis": 1,
                "kafein": 2,
                "description": "Mirip dengan latte, namun dengan lapisan microfoam yang sangat tipis, menonjolkan rasa kopi lebih kuat dari latte."
            },
            {
                "nama_menu": "Mocha",
                "kemanisan": 5,
                "kepahitan": 2,
                "keasaman": 1,
                "body": 4,
                "aroma": 2,
                "susu": True,
                "suhu": True,
                "jenis": 1,
                "kafein": 2,
                "description": "Kombinasi espresso, susu hangat, dan cokelat. Sangat cocok untuk pecinta kopi manis dengan sentuhan cokelat."
            },
            {
                "nama_menu": "Cold Brew",
                "kemanisan": 2,
                "kepahitan": 2,
                "keasaman": 1,
                "body": 3,
                "aroma": 2,
                "susu": False,
                "suhu": False,
                "jenis": 1,
                "kafein": 3,
                "description": "Kopi yang diseduh dengan air dingin selama 12-24 jam. Menghasilkan rasa yang halus, tidak terlalu asam, dan sangat menyegarkan."
            },
            {
                "nama_menu": "V60",
                "kemanisan": 2,
                "kepahitan": 2,
                "keasaman": 4,
                "body": 2,
                "aroma": 3,
                "susu": False,
                "suhu": True,
                "jenis": 1,
                "kafein": 2,
                "description": "Metode seduh manual pour-over yang menonjolkan profil rasa asli biji kopi, biasanya memiliki keasaman dan aroma yang kompleks."
            },
            {
                "nama_menu": "Vanilla Latte",
                "kemanisan": 5,
                "kepahitan": 2,
                "keasaman": 1,
                "body": 3,
                "aroma": 2,
                "susu": True,
                "suhu": True,
                "jenis": 1,
                "kafein": 2,
                "description": "Latte klasik dengan tambahan sirup vanilla. Sangat manis, creamy, dan aromatik."
            },
            {
                "nama_menu": "Caramel Latte",
                "kemanisan": 5,
                "kepahitan": 2,
                "keasaman": 1,
                "body": 3,
                "aroma": 2,
                "susu": True,
                "suhu": True,
                "jenis": 1,
                "kafein": 2,
                "description": "Latte dengan tambahan sirup karamel. Memberikan rasa manis dan buttery dari karamel."
            },
            {
                "nama_menu": "Hazelnut Latte",
                "kemanisan": 5,
                "kepahitan": 2,
                "keasaman": 1,
                "body": 3,
                "aroma": 2,
                "susu": True,
                "suhu": True,
                "jenis": 1,
                "kafein": 2,
                "description": "Latte dengan sirup hazelnut, memberikan aroma nutty yang khas dan rasa manis."
            },
            {
                "nama_menu": "Macchiato",
                "kemanisan": 2,
                "kepahitan": 4,
                "keasaman": 3,
                "body": 4,
                "aroma": 3,
                "susu": True,
                "suhu": True,
                "jenis": 1,
                "kafein": 3,
                "description": "Espresso dengan sedikit foam susu di atasnya. Cukup kuat dan pekat."
            },
            {
                "nama_menu": "Affogato",
                "kemanisan": 4,
                "kepahitan": 3,
                "keasaman": 2,
                "body": 4,
                "aroma": 2,
                "susu": True,
                "suhu": False,
                "jenis": 1,
                "kafein": 2,
                "description": "Sajian unik berupa es krim vanilla yang disiram dengan espresso panas."
            },
            {
                "nama_menu": "Piccolo",
                "kemanisan": 3,
                "kepahitan": 3,
                "keasaman": 2,
                "body": 3,
                "aroma": 2,
                "susu": True,
                "suhu": True,
                "jenis": 1,
                "kafein": 2,
                "description": "Versi lebih kecil dari latte, disajikan dengan ristretto (espresso pendek) sehingga rasa kopinya lebih terasa dibandingkan latte biasa."
            },
            {
                "nama_menu": "Irish Coffee",
                "kemanisan": 3,
                "kepahitan": 3,
                "keasaman": 2,
                "body": 4,
                "aroma": 3,
                "susu": True,
                "suhu": True,
                "jenis": 1,
                "kafein": 2,
                "description": "Kopi panas, gula, dan sedikit wiski, ditambah krim kocok. (Disimulasikan non-alkohol untuk resep ini, fokus pada creaminess)."
            }
        ]

        for item in coffee_data:
            obj, created = MenuKopi.objects.get_or_create(nama_menu=item['nama_menu'], defaults=item)
            if created:
                self.stdout.write(self.style.SUCCESS(f'Created {item["nama_menu"]}'))
            else:
                self.stdout.write(f'{item["nama_menu"]} already exists')

        self.stdout.write(self.style.SUCCESS('Successfully seeded coffee data.'))
