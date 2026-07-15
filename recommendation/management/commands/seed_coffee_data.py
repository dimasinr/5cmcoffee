from django.core.management.base import BaseCommand
from recommendation.models import MenuKopi

class Command(BaseCommand):
    help = 'Seeds the database with initial coffee menu data from menu.md'

    def handle(self, *args, **kwargs):
        # Mapping:
        # aroma  : Sedang=2, Kuat=3
        # jenis  : Arabica=1, Robusta=2, Blend=3
        # kafein : Sedang=2, Tinggi=3
        # susu   : Ya=True, Tidak=False
        # suhu   : Ya(panas)=True, Tidak(dingin)=False

        coffee_data = [
            {
                "nama_menu": "5cm Coffee",
                "kemanisan": 3,
                "kepahitan": 3,
                "keasaman": 2,
                "body": 3,
                "aroma": 2,   # Sedang
                "jenis": 1,   # Arabica
                "kafein": 2,  # Sedang
                "susu": True,
                "suhu": False,  # Tidak panas = dingin
                "description": "Racikan otentik ala 5CM — perpaduan sempurna antara espresso pekat, susu segar, dan resep rahasia kami yang creamy, seimbang, dan bikin nagih di setiap tegukan."
            },
            {
                "nama_menu": "Affogato",
                "kemanisan": 4,
                "kepahitan": 3,
                "keasaman": 2,
                "body": 3,
                "aroma": 2,   # Sedang
                "jenis": 2,   # Robusta
                "kafein": 2,  # Sedang
                "susu": True,
                "suhu": False,
                "description": "Sensasi klasik Italia: satu scoop es krim vanila lembut disiram double espresso panas, menciptakan perpaduan magis antara pahit, manis, dan creamy yang meleleh di lidah."
            },
            {
                "nama_menu": "Banana Coffee",
                "kemanisan": 4,
                "kepahitan": 2,
                "keasaman": 2,
                "body": 3,
                "aroma": 2,   # Sedang
                "jenis": 1,   # Arabica
                "kafein": 2,  # Sedang
                "susu": True,
                "suhu": False,
                "description": "Espresso berpadu mesra dengan banana foam yang lembut dan sentuhan karamel alami — manisnya buah menyatu segar dengan kekuatan kopi sejati."
            },
            {
                "nama_menu": "Cheeseway",
                "kemanisan": 4,
                "kepahitan": 2,
                "keasaman": 2,
                "body": 4,
                "aroma": 2,   # Sedang
                "jenis": 2,   # Robusta
                "kafein": 2,  # Sedang
                "susu": True,
                "suhu": False,
                "description": "Espresso creamy dengan cheese foam lembut dan taburan keju parut di atasnya — perpaduan gurih dan nikmat yang membuat setiap tegukan terasa mewah."
            },
            {
                "nama_menu": "Coffee Caramelo",
                "kemanisan": 5,
                "kepahitan": 2,
                "keasaman": 2,
                "body": 3,
                "aroma": 2,   # Sedang
                "jenis": 1,   # Arabica
                "kafein": 2,  # Sedang
                "susu": True,
                "suhu": False,
                "description": "Manisnya karamel meleleh sempurna bersama espresso dan susu segar, menghadirkan aroma karamel yang menggoda di setiap seruputan."
            },
            {
                "nama_menu": "Coffee Matcha",
                "kemanisan": 3,
                "kepahitan": 2,
                "keasaman": 2,
                "body": 3,
                "aroma": 2,   # Sedang
                "jenis": 2,   # Robusta
                "kafein": 2,  # Sedang
                "susu": True,
                "suhu": False,
                "description": "Perpaduan unik antara espresso pekat dan matcha creamy — dua dunia rasa bertemu dalam satu cangkir yang menyegarkan dan penuh karakter."
            },
            {
                "nama_menu": "Coffee Salted Caramel",
                "kemanisan": 4,
                "kepahitan": 2,
                "keasaman": 2,
                "body": 4,
                "aroma": 2,   # Sedang
                "jenis": 1,   # Arabica
                "kafein": 2,  # Sedang
                "susu": True,
                "suhu": False,
                "description": "Kombinasi manis dan gurih yang pas: espresso dipadukan salted caramel premium untuk sensasi rasa kaya yang memanjakan lidah."
            },
            {
                "nama_menu": "Con Heilo",
                "kemanisan": 4,
                "kepahitan": 2,
                "keasaman": 2,
                "body": 3,
                "aroma": 2,   # Sedang
                "jenis": 2,   # Robusta
                "kafein": 2,  # Sedang
                "susu": True,
                "suhu": False,
                "description": "Es kopi susu ala Vietnam dengan sentuhan krim lembut yang menyegarkan — bold, creamy, dan pas menemani hari yang panas."
            },
            {
                "nama_menu": "Creamy Pop Delight",
                "kemanisan": 5,
                "kepahitan": 2,
                "keasaman": 2,
                "body": 4,
                "aroma": 2,   # Sedang
                "jenis": 1,   # Arabica
                "kafein": 2,  # Sedang
                "susu": True,
                "suhu": False,
                "description": "Es kopi creamy dengan foam lembut dan topping renyah yang playful — kesegaran menyenangkan di setiap tegukan."
            },
            {
                "nama_menu": "Cremix Butterscotch",
                "kemanisan": 5,
                "kepahitan": 2,
                "keasaman": 2,
                "body": 3,
                "aroma": 2,   # Sedang
                "jenis": 2,   # Robusta
                "kafein": 2,  # Sedang
                "susu": True,
                "suhu": False,
                "description": "Espresso, susu, dan sirup butterscotch beraroma buttery yang manis memikat — kelembutan rasa karamel klasik dalam sajian modern."
            },
            {
                "nama_menu": "Double Espresso",
                "kemanisan": 1,
                "kepahitan": 5,
                "keasaman": 3,
                "body": 5,
                "aroma": 3,   # Kuat
                "jenis": 1,   # Arabica
                "kafein": 3,  # Tinggi
                "susu": False,
                "suhu": True,
                "description": "Dua shot espresso murni dengan karakter kopi pekat dan aftertaste panjang — pilihan tepat bagi pecinta kopi sejati yang menginginkan kekuatan penuh."
            },
            {
                "nama_menu": "Flat White",
                "kemanisan": 2,
                "kepahitan": 4,
                "keasaman": 2,
                "body": 4,
                "aroma": 2,   # Sedang
                "jenis": 1,   # Arabica
                "kafein": 2,  # Sedang
                "susu": True,
                "suhu": True,
                "description": "Double espresso dipadukan steamed milk yang halus dan foam tipis nan lembut — keseimbangan sempurna antara kekuatan kopi dan kelembutan susu."
            },
            {
                "nama_menu": "Hot Macchiato",
                "kemanisan": 1,
                "kepahitan": 5,
                "keasaman": 2,
                "body": 5,
                "aroma": 3,   # Kuat
                "jenis": 1,   # Arabica
                "kafein": 2,  # Sedang
                "susu": True,
                "suhu": True,
                "description": "Single espresso dengan sentuhan milk foam lembut di atasnya — sederhana namun penuh karakter, klasik yang tak lekang waktu."
            },
            {
                "nama_menu": "Iced Americano",
                "kemanisan": 1,
                "kepahitan": 4,
                "keasaman": 3,
                "body": 3,
                "aroma": 3,   # Kuat
                "jenis": 1,   # Arabica
                "kafein": 3,  # Tinggi
                "susu": False,
                "suhu": False,
                "description": "Double espresso bertemu air dingin, menghadirkan rasa bersih, tegas, dan menyegarkan — kopi hitam favorit yang selalu jadi andalan."
            },
            {
                "nama_menu": "Iced Cappuccino",
                "kemanisan": 3,
                "kepahitan": 3,
                "keasaman": 2,
                "body": 3,
                "aroma": 2,   # Sedang
                "jenis": 1,   # Arabica
                "kafein": 2,  # Sedang
                "susu": True,
                "suhu": False,
                "description": "Espresso, susu dingin, dan foam tebal nan ringan berpadu sempurna — klasik Italia dalam sajian segar yang memanjakan."
            },
            {
                "nama_menu": "Iced Cold Brew",
                "kemanisan": 2,
                "kepahitan": 3,
                "keasaman": 1,
                "body": 3,
                "aroma": 2,   # Sedang
                "jenis": 1,   # Arabica
                "kafein": 2,  # Sedang
                "susu": False,
                "suhu": False,
                "description": "Diseduh dingin selama 12–24 jam untuk menghasilkan rasa halus dan keasaman rendah — kesegaran kopi murni tanpa kompromi."
            },
            {
                "nama_menu": "Iced Hazelnut Latte",
                "kemanisan": 4,
                "kepahitan": 2,
                "keasaman": 2,
                "body": 3,
                "aroma": 2,   # Sedang
                "jenis": 3,   # Blend
                "kafein": 2,  # Sedang
                "susu": True,
                "suhu": False,
                "description": "Latte lembut dengan sirup hazelnut beraroma nutty dan manis — kehangatan rasa kacang yang menyatu sempurna dengan kopi susu segar."
            },
            {
                "nama_menu": "Iced Latte",
                "kemanisan": 4,
                "kepahitan": 2,
                "keasaman": 2,
                "body": 3,
                "aroma": 2,   # Sedang
                "jenis": 1,   # Arabica
                "kafein": 2,  # Sedang
                "susu": True,
                "suhu": False,
                "description": "Es kopi susu dengan rasio susu lebih banyak dan foam tipis nan lembut — pilihan ringan dan creamy untuk menemani aktivitas harianmu."
            },
            {
                "nama_menu": "Iced Mocha Latte",
                "kemanisan": 5,
                "kepahitan": 2,
                "keasaman": 2,
                "body": 3,
                "aroma": 2,   # Sedang
                "jenis": 1,   # Arabica
                "kafein": 2,  # Sedang
                "susu": True,
                "suhu": False,
                "description": "Perpaduan manis espresso, susu, dan cokelat creamy — sensasi mocha klasik yang memanjakan setiap pecinta rasa manis."
            },
            {
                "nama_menu": "Japanese Style",
                "kemanisan": 1,
                "kepahitan": 3,
                "keasaman": 3,
                "body": 2,
                "aroma": 2,   # Sedang
                "jenis": 2,   # Robusta
                "kafein": 2,  # Sedang
                "susu": False,
                "suhu": False,
                "description": "Manual brew di atas es dengan cita rasa bersih dan aroma kompleks — teknik seduh presisi ala Jepang untuk pengalaman ngopi yang berbeda."
            },
            {
                "nama_menu": "Kopi Tubruk",
                "kemanisan": 1,
                "kepahitan": 4,
                "keasaman": 2,
                "body": 5,
                "aroma": 3,   # Kuat
                "jenis": 1,   # Arabica
                "kafein": 3,  # Tinggi
                "susu": False,
                "suhu": True,
                "description": "Kopi tradisional Nusantara tanpa filter dengan body tebal dan karakter kuat — cita rasa otentik yang menghubungkan setiap tegukan dengan warisan kopi Indonesia."
            },
            {
                "nama_menu": "Piccolo Coffee",
                "kemanisan": 2,
                "kepahitan": 4,
                "keasaman": 2,
                "body": 4,
                "aroma": 2,   # Sedang
                "jenis": 3,   # Blend
                "kafein": 2,  # Sedang
                "susu": True,
                "suhu": True,
                "description": "Espresso dengan sedikit steamed milk — kuat namun tetap lembut, sajian mungil dengan rasa yang membekas."
            },
            {
                "nama_menu": "Single Espresso",
                "kemanisan": 1,
                "kepahitan": 5,
                "keasaman": 3,
                "body": 5,
                "aroma": 3,   # Kuat
                "jenis": 1,   # Arabica
                "kafein": 2,  # Sedang
                "susu": False,
                "suhu": True,
                "description": "Satu shot espresso dengan crema tebal dan rasa intens — murni, singkat, dan penuh kekuatan bagi pecinta kopi sejati."
            },
            {
                "nama_menu": "V60 Pour Over",
                "kemanisan": 1,
                "kepahitan": 3,
                "keasaman": 3,
                "body": 2,
                "aroma": 2,   # Sedang
                "jenis": 1,   # Arabica
                "kafein": 2,  # Sedang
                "susu": False,
                "suhu": True,
                "description": "Manual brew V60 dengan rasa clean dan aroma kompleks — seni menyeduh kopi yang menghadirkan karakter biji kopi secara utuh."
            },
            {
                "nama_menu": "Vanilla Sweet Coffee",
                "kemanisan": 5,
                "kepahitan": 2,
                "keasaman": 2,
                "body": 3,
                "aroma": 2,   # Sedang
                "jenis": 3,   # Blend
                "kafein": 2,  # Sedang
                "susu": True,
                "suhu": False,
                "description": "Espresso, susu, dan vanilla yang lembut memanjakan — manis hangat dan nyaman di setiap tegukan."
            },
            {
                "nama_menu": "Vietnamese Sweet Drip",
                "kemanisan": 5,
                "kepahitan": 4,
                "keasaman": 2,
                "body": 5,
                "aroma": 3,   # Kuat
                "jenis": 2,   # Robusta
                "kafein": 3,  # Tinggi
                "susu": True,
                "suhu": False,
                "description": "Vietnam drip dengan susu kental manis yang bold dan creamy — perpaduan klasik Vietnam yang kaya rasa dan menggoda."
            },
        ]

        for item in coffee_data:
            obj, created = MenuKopi.objects.get_or_create(
                nama_menu=item['nama_menu'],
                defaults=item
            )
            if created:
                self.stdout.write(self.style.SUCCESS(f'Created: {item["nama_menu"]}'))
            else:
                self.stdout.write(f'Already exists: {item["nama_menu"]}')

        self.stdout.write(self.style.SUCCESS('Successfully seeded coffee data.'))
