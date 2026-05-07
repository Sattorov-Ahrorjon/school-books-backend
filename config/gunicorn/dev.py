# Django loyihasini ishga tushirish uchun port va host
bind = "0.0.0.0:8001"

workers = 2

# Ish jarayonlari turi (sync, gevent, eventlet)
worker_class = "sync"  # Tezlikni oshirish uchun gevent yoki eventletni sinab ko'rishingiz mumkin

# Maksimal xotira ishlatish (megabaytlar, masalan 128MB)
limit_request_line = 4094
limit_request_fields = 100
limit_request_field_size = 8190

# Ishchilarning qayta yuklash rejimi (faqat ishlab chiqish uchun)
reload = False

# Tizim resurslarini optimallashtirish uchun sozlamalar
timeout = 30  # Sekundda vaqt tugashi
keepalive = 2  # Ishchi so'rovni kutish vaqti

# Gunicornning maxsus nomi
proc_name = "django_school_books_gunicorn"
