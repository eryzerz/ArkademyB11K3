# ARKADEMY BOOTCAMP BATCH 11 KLOTER 3

Segala berkas yang terdapat pada repository ini merupakan jawaban dari technical test, berisi 6 soal algoritma dan 1 soal project yang mengimplementasikan CRUD (Create, Read, Update, dan Delete)

## Requirements for Problem 1 - 6

```bash
python == 3.7.X
```

## Nomor 1 - problem_1.py

REST merupakan singkatan dari Representational State Transfer. REST menggunakan HTTP untuk melakukan operasi CRUD.

JSON merupakan file yang digunakan untuk pertukaran data, terkenal karena mudah dibaca dan diolah oleh manusia dan juga mudah diolah oleh mesin.

JSON pada REST API memiliki kegunaan untuk mengirimkan data antara server dan browser. Misalnya saat mengirimkan sebuah query menggunakan GET request, server akan memberikan respon dengan file berformat JSON. 


## Requirements for Problem 7
```bash
django==2.1.8
django-bootstrap-modal-forms==1.4.1
django-widget-tweaks==1.4.2
selenium==3.14.0
pytz==2018.5
```

## Stacks

Front-end :
```bash
HTML, CSS, Bootstrap, JS
```
Back-end : 
```bash
Python, Django, SQLite3
```

## Usage - problem_7

Clone this repository to your local
```bash
git clone https://github.com/eryzerz/ArkademyB11K3.git
cd problem_7
```
Create virtual environment, I prefer to use pipenv
```bash
pipenv install -r requirements.txt
pipenv shell
```
Migrate data
```bash
python manage.py migrate
```
Create admin account
```bash
python manage.py createsuperuser
```
Once again, migrate new data but now you need to make migrations first
```bash
python manage.py makemigrations
python manage.py migrate
```
Run this command to start development server
```bash
python manage.py runserver
```
Open localhost:8000 on your browser

## UI and Queries

![Image of main page](https://github.com/eryzerz/ArkademyB11K3/blob/master/problem_7/Index.PNG)

![Image of add data page](https://github.com/eryzerz/ArkademyB11K3/blob/master/problem_7/add-data.PNG)

![Image of edit data page](https://github.com/eryzerz/ArkademyB11K3/blob/master/problem_7/edit-data.PNG)

![Image of delete data page](https://github.com/eryzerz/ArkademyB11K3/blob/master/problem_7/delete-data.PNG)

![Image of queries](https://github.com/eryzerz/ArkademyB11K3/blob/master/problem_7/queries.PNG)
