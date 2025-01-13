Inicia o projeto

python -m venv venv                     (cria o ambiente virtual)
. venv/bin/activate                     (ativa o ambiente virtual)
pip install django                      (instala o Django)
django-admin startproject project .     (cria o projeto)
python manage.py startapp contact       (cria o app contact)

Configur o GIT

git config --global user.name 'Seu nome'
git config --global user.email 'seu_email@gmail.com'
git config --global init.defaultBranch main
# Configure o .gitignore
git init
git add .
git commit -m 'Mensagem'
git remote add origin URL_DO_GIT

Migrando a base de dados do Django

python manage.py makemigrations
python manage.py migrate

Criando e modificando a senha de um super usuário Django

python manage.py createsuperuser
python manage.py changepassword USERNAME