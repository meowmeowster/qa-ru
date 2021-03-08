FROM python:3.8

WORKDIR /code

COPY build/app/requirements.txt .
COPY .env .

RUN pip install --upgrade pip
RUN pip install python-multipart
RUN pip install -r requirements.txt

COPY build/app .
RUN chmod 777 /code

CMD [ "python", "./server.py" ]
