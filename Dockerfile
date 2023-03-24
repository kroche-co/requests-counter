FROM python:3.9-slim-buster

WORKDIR /app

COPY requirements.txt ./
RUN pip install \
    --quiet \
    --no-cache-dir \
    --requirement requirements.txt

COPY . .

CMD [ "python", "-u", "counter.py" ]
