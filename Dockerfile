FROM python:3.8

WORKDIR /code

COPY build/app/requirements.txt .
COPY .env .
RUN useradd -ms /bin/bash admin

RUN pip install --upgrade pip
RUN pip install python-multipart
RUN pip install -r requirements.txt

COPY build/app .
RUN chown -R admin:admin /code
RUN chmod 755 /code
USER admin

CMD [ "python", "./server.py" ]
