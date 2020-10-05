# image base
FROM python:3.8.5-alpine

# estableciendo direcetorio de trabajo
WORKDIR /usr/src/app

# agregando e instalando requirements
COPY ./requirements.txt /usr/src/app/requirements.txt
RUN pip install -r requirements.txt

# agregando app
COPY . /usr/src/app

# ejecutando server
CMD python manage.py run -h 0.0.0.0
