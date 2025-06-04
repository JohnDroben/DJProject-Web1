# Django Приложение с двумя страницами

Этот проект демонстрирует создание Django приложения с двумя разными страницами: `/data` и `/test`.

## Установка и запуск

1. Клонируйте репозиторий:
```bash
git clone <repo-url>
cd <project-directory>
```

2. Создайте виртуальное окружение и установите зависимости:
```bash
python -m venv venv
source venv/bin/activate  # Linux/MacOS
venv\Scripts\activate     # Windows
pip install django
```

3. Примените миграции:
```bash
python manage.py migrate
```

4. Запустите сервер разработки:
```bash
python manage.py runserver
```

## Использование

После запуска сервера откройте в браузере:

- **Страница данных**: http://127.0.0.1:8000/data/  
  Отображает: "Страница данных: Здесь отображаются важные данные."

- **Тестовая страница**: http://127.0.0.1:8000/test/  
  Отображает: "Тестовая страница: Проверка работы приложения!"

## Структура проекта

```
Starwars/
├── main/                  # Основное приложение
│   ├── migrations/         # Миграции базы данных
│   ├── __init__.py
│   ├── admin.py            # Админ-панель
│   ├── apps.py             # Конфигурация приложения
│   ├── models.py           # Модели данных
│   ├── tests.py            # Тесты
│   ├── urls.py             # URL-адреса приложения
│   └── views.py            # Обработчики страниц
│
├── Starwars/                # Настройки проекта
│   ├── __init__.py
│   ├── asgi.py             # ASGI-конфигурация
│   ├── settings.py         # Основные настройки
│   ├── urls.py             # Главные URL-адреса
│   └── wsgi.py             # WSGI-конфигурация
│
├── manage.py               # Управление проектом
└── README.md               # Этот файл
```

## Основные файлы

### `main/views.py`
```python
from django.http import HttpResponse

def data_page(request):
    return HttpResponse("Страница данных: Здесь отображаются важные данные.")

def test_page(request):
    return HttpResponse("Тестовая страница: Проверка работы приложения!")
```

### `main/urls.py`
```python
from django.urls import path
from . import views

urlpatterns = [
    path('data/', views.data),
    path('test/', views.test),
]
```

### `Starwars/urls.py`
```python
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),  # Подключение URL приложения
]
```

### `Starwars/settings.py`
```python
INSTALLED_APPS = [
    ...
    'main',  # Зарегистрированное приложение
]
```

## Дальнейшее развитие

1. Добавьте HTML-шаблоны:
```bash
mkdir -p main/templates/main
touch myapp/templates/main/data.html
touch myapp/templates/main/test.html
```

2. Используйте шаблоны в представлениях:
```python
from django.shortcuts import render

def data_page(request):
    return render(request, 'main/data.html', {'title': 'Страница данных'})
```

3. Добавьте статические файлы (CSS, JS):
```python
# settings.py
STATIC_URL = '/static/'
```

```bash
mkdir main/static
```

## Автор

[Георгий Дробенюк]

## Лицензия

Этот проект лицензирован по MIT License - подробности см. в файле LICENSE.
