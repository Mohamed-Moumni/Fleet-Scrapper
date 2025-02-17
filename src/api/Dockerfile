FROM python:3.11

ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY . .

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

CMD ["gunicorn", "api.wsgi:application", "--bind", "0.0.0.0:8000"]
