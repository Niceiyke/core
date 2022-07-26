web: gunicorn core.wsgi:application --log-file - --log-level debug
heroku ps:scale web=1
python manage.py migrate
echo 'worker: python manage.py celery worker --loglevel=info' >> Procfile
echo 'celery_beat: python manage.py celery beat --loglevel=info' >> Procfile
git mv Procfile Procfile.real
echo 'web: env > .env; env PYTHONUNBUFFERED=true honcho start -f Procfile.real 2>&1' > Procfile
