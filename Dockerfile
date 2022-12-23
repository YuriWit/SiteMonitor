FROM python:3.10.4
WORKDIR /app
COPY requirements.txt requirements.txt
COPY app.py app.py
RUN mkdir last_status
RUN pip3 install -r requirements.txt
CMD python3 ./app.py