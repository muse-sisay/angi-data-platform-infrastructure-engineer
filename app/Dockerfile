FROM python:3.10.12-alpine3.18

COPY requirements.txt main.py /app

RUN python3 -m pip install -r /app/requirements.txt

WORKDIR /app

ENTRYPOINT ["python3",  "main.py"]