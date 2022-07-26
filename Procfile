web: gunicorn core.wsgi:application --log-file - --log-level debug
worker: celery -A core worker -B --loglevel=info
