# Ofertas do Luis — Django
Catálogo de ofertas com administração de produtos e rastreamento de cliques.

## Instalar no Windows (terminal do VS Code)
Execute um comando por vez, na pasta do projeto:
```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py seed_demo
python manage.py runserver
```
Se a ativação for bloqueada pelo PowerShell, rode `Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass` e tente ativar novamente.

Acesse o site em http://127.0.0.1:8000/ e o painel em http://127.0.0.1:8000/admin/.
No painel, entre em Produtos para cadastrar nome, preço, link afiliado, imagem, categoria e publicar. Os cliques que passam pelos botões são registrados em Cliques registrados.

Os produtos de demonstração têm links falsos `example.com`: substitua-os antes de divulgar. O registro de cliques não comprova venda/comissão e os preços não são atualizados automaticamente. Para publicar na internet, configure chave secreta, DEBUG=0, ALLOWED_HOSTS, HTTPS, hospedagem, banco de produção, backups e política de privacidade. Não compartilhe suas credenciais do admin.
