# graphene-cookbook
Graphene Öğreniyorum

```python
echo "# graphene-cookbook" >> README.md
git init
git add README.md
git commit -m "ilk commit"
git branch -M main
git remote add origin https://github.com/form90/graphene-cookbook.git
git push -u origin main


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

py manage.py migrate
py manage.py makemigrations

```
>>>>>>> 586e2490abd2a3206c39ea41b1da1af3d1af5b34
