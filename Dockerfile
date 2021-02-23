FROM python:3.8-slim

COPY . /app
WORKDIR /app

RUN pip install poetry
RUN poetry export --without-hashes --dev -f requirements.txt -o requirements.txt
RUN pip install -r requirements.txt
ADD . /app/
RUN pip install gunicorn
EXPOSE 80
WORKDIR /app/src

ENTRYPOINT ["gunicorn", "-w", "4", "-b", ":80", "wsgi:app"]