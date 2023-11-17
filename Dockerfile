FROM python:3.12

ENV PYTHONUNBUFFERED = 1

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

EXPOSE 8000

COPY django.sh django.sh

ENTRYPOINT [ "sh", "django.sh"]

# CMD ["python", "manage.py", "runserver", "0.0.0.0:80"]
