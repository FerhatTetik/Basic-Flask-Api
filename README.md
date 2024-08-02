# Api_deneme_5

Api_deneme_5, Flask kullanarak geliştirilmiş bir CRUD API ve basit bir kullanıcı arayüzü sunan bir web uygulamasıdır. Uygulama, kullanıcılar ve kitaplar üzerinde işlem yapmayı sağlar ve JWT (JSON Web Token) ile kimlik doğrulama sunar.

## Özellikler

- **Kullanıcı Yönetimi**: Kullanıcı ekleme, güncelleme, silme ve listeleme.
- **Kitap Yönetimi**: Kitap ekleme, güncelleme, silme ve listeleme.
- **JWT Kimlik Doğrulama**: Kullanıcı girişi ve çıkışı için JWT tabanlı kimlik doğrulama.
- **Bootstrap Tabanlı Arayüz**: Bootstrap kullanılarak stilize edilmiş modern bir kullanıcı arayüzü.

## Proje Yapısı
Api_deneme_5/
├── app/
│ ├── init.py
│ ├── auth.py
│ ├── config.py
│ ├── models/
│ │ ├── init.py
│ │ ├── models.py
│ ├── db/
│ │ ├── users.py
│ │ ├── books.py
│ │ ├── init.py
│ └── templates/
│ ├── home_page.html
│ ├── users_list.html
│ ├── add_user.html
│ ├── update_user.html
│ ├── books_list.html
│ ├── add_book.html
│ └── update_book.html
└── app.py


## Kurulum

1. **Gereksinimler**: Python 3.8 veya üstü, PostgreSQL veritabanı.

2. **Sanal Ortam Oluşturma**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # macOS/Linux
   venv\Scripts\activate     # Windows
3. **Gereksinimleri Yükleme**:
    pip install -r requirements.txt
4. **Veritabanı Oluşturma**:
    Veritabanı bağlantı ayarlarını app/config.py dosyasındaki SQLALCHEMY_DATABASE_URI değişkeninde güncelleyin.

    class Config:
    SQLALCHEMY_DATABASE_URI = 'postgresql://<kullanıcı_adı>:<şifre>@<host>:<port>/<veritabanı_adı>'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JWT_SECRET_KEY = 'your_jwt_secret_key'
    JWT_TOKEN_LOCATION = ['cookies']
    JWT_COOKIE_CSRF_PROTECT = False

5. **Veritabanı Tablolarını Oluşturma**:
    flask db upgrade

6. **Veritabanı Tablolarını Oluşturma**:
    flask db migrate

## Kullanım
*Ana Sayfa: / - Uygulamanın ana sayfası, kimlik doğrulama gerektirir.
*Kullanıcılar:
    *Listeleme: /users
    *Ekleme: /users/add
    *Güncelleme: /users/update/<int:id>
    *Silme: /users/delete/<int:id>
*Kitaplar:
    *Listeleme: /books
    *Ekleme: /books/add
    *Güncelleme: /books/update/<int:id>
    *Silme: /books/delete/<int:id>
    *Giriş ve Çıkış:
*Giriş: /login
    *Çıkış: /logout
    *Konfigürasyon
JWT ayarları 'app/config.py' dosyasında yapılır:

    class Config:
    SQLALCHEMY_DATABASE_URI = 'postgresql://<kullanıcı_adı>:<şifre>@<host>:<port>/<veritabanı_adı>'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JWT_SECRET_KEY = 'your_jwt_secret_key'
    JWT_TOKEN_LOCATION = ['cookies']
    JWT_COOKIE_CSRF_PROTECT = False
