from django.core.management.base import BaseCommand
from ofertas.models import Category, Product
class Command(BaseCommand):
    help = "Cria categorias e produtos de demonstração."
    def handle(self, *args, **kwargs):
        demo = {
          "Tecnologia":("💻",[("Fone Bluetooth Pro","Som para sua playlist sem enrolação.","Shopee","79.90","119.90",True),("Teclado Mecânico Gamer","Para dar um upgrade no setup.","Mercado Livre","129.90","179.90",True),("Mouse Gamer RGB","Um acessório para completar seu espaço.","Amazon","89.90","119.90",False)]),
          "Games":("🎮",[("Controle Wireless","Para jogar com mais liberdade.","Mercado Livre","99.90","149.90",True)]),
          "Academia":("🏋️",[("Garrafa Esportiva","Para levar água ao treino.","Shopee","39.90","59.90",False)]),
          "Casa":("🏠",[("Organizador de Mesa","Ajuda a manter tudo no lugar.","Shopee","34.90","54.90",False)]),
          "Acessórios":("📱",[("Suporte para Celular","Praticidade para apoiar o celular.","Shopee","29.90","49.90",False)])
        }
        for name,(icon,items) in demo.items():
            cat,_=Category.objects.get_or_create(name=name,defaults={"icon":icon})
            for title,desc,platform,price,old,featured in items:
                Product.objects.get_or_create(name=title,defaults={"description":desc,"category":cat,"platform":platform,"current_price":price,"old_price":old,"featured":featured,"affiliate_url":"https://example.com/troque-pelo-seu-link"})
        self.stdout.write(self.style.SUCCESS("Dados demonstrativos adicionados. Troque os links no painel /admin."))
