# graphene-cookbook
Graphene Öğreniyorum

```editorconfig
echo "# graphene-cookbook" >> README.md
git init
git add README.md
git commit -m "ilk commit"
git branch -M main
git remote add origin https://github.com/form90/graphene-cookbook.git
git push -u origin main
```
#### Sanal ortam, django ve projeyi kur
```python
virtualenv env
.\env\Scripts\activate
pip3 install --user --upgrade pip veya
D:\Hugo\PROJE\cookbook\env\Scripts\python.exe -m pip install --upgrade pip
pip3 install "graphene-django>=2.0"
django-admin startproject cookbook .
cd cookbook
django-admin startapp malzemeler
py manage.py migrate
py manage.py makemigrations
```
#### cookbook/settings.py
```python
INSTALLED_APPS = [
    ...
    # Install the ingredients app
    "cookbook.malzemeler",
]

```
#### Veritabanı güncelle
```python
py manage.py migrate
py manage.py makemigrations

```
### Modeli tanımlıyoruz
#### cookbook/malzemeler/models.py
```python
from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Malzemeler(models.Model):
    name = models.CharField(max_length=100)
    notes = models.TextField()
    category = models.ForeignKey(
        Category, related_name="malzemelers", on_delete=models.CASCADE
    )

    def __str__(self):
        return self.name
```
Bunu çalıştırmayı unutma
```python
py manage.py migrate
py manage.py makemigrations
```
Test verileri ```cookbook/malzemeler/fixtures/malzemelers.json``` klasörüne yüklendi.

```py .\manage.py loaddata .\cookbook\malzemeler\fixtures\malzemelers.json```
çıktı: Installed 6 object(s) from 1 fixture(s)