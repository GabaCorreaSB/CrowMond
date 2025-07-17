FROM python:3.10-slim

RUN apt-get update && apt-get install -y crowdsec sudo

COPY . /app
WORKDIR /app

RUN pip install psycopg2-binary

CMD ["python", "exporter.py"]
