FROM python:3.8

WORKDIR /code

COPY app/requirements.txt .

RUN pip install --upgrade pip
RUN pip install python-multipart
RUN pip install -r requirements.txt

COPY app/ .

CMD [ "python", "./server.py" ]
