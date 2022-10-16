FROM python:3.8

WORKDIR /aplicacion

COPY ./requirements.txt ./requirements.txt

RUN pip3 install -r requirements.txt

COPY ./miPrueba .

EXPOSE 5000

VOLUME ["./miPrueba","./aplicacion"]


CMD ["python","manage.py","runserver","0.0.0.0:5000"]