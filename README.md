# 🏦 Alke Wallet

![Python](https://img.shields.io/badge/Python-3.13-blue?style=for-the-badge&logo=python&logoColor=white)
![Django](https://img.shields.io/badge/Django-6.0-green?style=for-the-badge&logo=django&logoColor=white)
![SQLite](https://img.shields.io/badge/SQLite-Database-lightblue?style=for-the-badge&logo=sqlite&logoColor=white)
![GitHub](https://img.shields.io/badge/GitHub-Repositorio-black?style=for-the-badge&logo=github&logoColor=white)

Billetera digital desarrollada con Django para gestionar clientes,
cuentas y transacciones financieras de forma segura y sencilla.

---

## 🚀 Tecnologías utilizadas

- **Python 3.13**
- **Django 6.0**
- **SQLite** (desarrollo)
- **PostgreSQL** (producción)
- **HTML/CSS** (templates)

---

## ⚙️ Instalación y configuración local

### 1. Clonar el repositorio

git clone https://github.com/CarobethPaez/alke_wallet.git
cd alke_wallet


### 2. Crear y activar el entorno virtual

python -m venv venv
venv\Scripts\activate  # Windows


### 3. Instalar dependencias

pip install django


### 4. Aplicar migraciones

cd alke_wallet
python manage.py migrate


### 5. Crear superusuario

python manage.py createsuperuser


### 6. Correr el servidor

python manage.py runserver


---

## 📋 Funcionalidades

- ✅ Registro y gestión de clientes
- ✅ Operaciones CRUD completas
- ✅ Panel de administración `/admin`
- ✅ Login y autenticación de usuarios
- ✅ Protección CSRF en formularios
- ✅ Archivos estáticos con CSS personalizado

---

## 🗂️ Estructura del proyecto
alke_wallet/
├── core/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── gestion/
│   ├── migrations/
│   ├── templates/
│   │   ├── gestion/
│   │   │   ├── cliente_list.html
│   │   │   ├── cliente_form.html
│   │   │   └── cliente_confirm_delete.html
│   │   └── registration/
│   │       └── login.html
│   ├── admin.py
│   ├── models.py
│   ├── urls.py
│   └── views.py
├── static/
│   └── css/
│       └── estilos.css
├── manage.py
└── README.md

---

## 🔗 URLs disponibles

| URL | Descripción |
|-----|-------------|
| `/admin/` | Panel de administración |
| `/accounts/login/` | Inicio de sesión |
| `/gestion/clientes/` | Lista de clientes |
| `/gestion/clientes/nuevo/` | Crear cliente |
| `/gestion/clientes/<id>/editar/` | Editar cliente |
| `/gestion/clientes/<id>/eliminar/` | Eliminar cliente |

---

## 👩‍💻 Autora

**Carobeth Páez**  
[![GitHub](https://img.shields.io/badge/GitHub-CarobethPaez-black?style=flat&logo=github)](https://github.com/CarobethPaez)

---

