FROM python:3.8-slim

COPY . /app
WORKDIR /app

RUN pip install poetry
RUN poetry export --without-hashes -f requirements.txt -o requirements.txt
RUN pip install -r requirements.txt
ADD . /app/
RUN pip install gunicorn
WORKDIR /app/src

# Entrypoint for Local test, use with docker run -it --rm -p 8000:80 <name_of_image>
#ENTRYPOINT ["gunicorn","-b",":80","wsgi:app"]

# Entrypoint for Heroku
ENTRYPOINT ["gunicorn","wsgi:app"]