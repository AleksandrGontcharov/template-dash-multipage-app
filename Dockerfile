FROM python:3.8-slim
COPY . /app
WORKDIR /app

RUN echo '******* Installing POETRY ********'
RUN pip install poetry

RUN echo '******* Creating requirements.txt file from Poetry********'
RUN poetry export --without-hashes --dev -f requirements.txt -o requirements.txt

RUN echo '******* Installing requirements.txt********'
RUN pip install -r requirements.txt
ADD . /app/

RUN echo '******* Change the entrypoint .py file to app.run_server(host='0.0.0.0', port=80, debug=True)********'
ENTRYPOINT [ "python" ]
CMD ["template_dash_multipage_app/index.py"]