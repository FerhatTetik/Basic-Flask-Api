# Flask CRUD API

Bu proje, Flask ve SQLAlchemy kullanarak basit bir CRUD (Create, Read, Update, Delete) API uygulamasıdır. Kullanıcı bilgilerini veritabanında yönetmek için temel CRUD işlevlerini sağlar.

## İçindekiler

- [Özellikler](#özellikler)
- [Kurulum](#kurulum)
- [Kullanım](#kullanım)
  
## Özellikler

- Kullanıcı ekleme
- Tüm kullanıcıları listeleme
- Kullanıcı bilgilerini güncelleme
- Kullanıcı silme

## Kurulum

Projeyi yerel makinenizde çalıştırmak için aşağıdaki adımları izleyin:

1. Bu depoyu klonlayın:

    ```sh
    git clone https://github.com/kullanıcı_adı/Api_deneme_5.git
    cd Api_deneme_5
    ```

2. Sanal ortam oluşturun ve etkinleştirin:

    Windows:

    ```sh
    python -m venv venv
    venv\Scripts\activate
    ```

    Mac/Linux:

    ```sh
    python3 -m venv venv
    source venv/bin/activate
    ```

3. Gerekli bağımlılıkları yükleyin:

    ```sh
    pip install -r requirements.txt
    ```

4. Veritabanı yapılandırmasını güncelleyin ve veritabanını oluşturun:


## Kullanım

API'yi çalıştırmak için aşağıdaki komutu kullanın:

```sh
python app.py
