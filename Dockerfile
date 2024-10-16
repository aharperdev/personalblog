FROM nikolaik/python-nodejs:python3.10-nodejs20-slim

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV DEBUG 0

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN mkdir /static

COPY ./entrypoint.sh /
ENTRYPOINT [ "sh", "/entrypoint.sh" ]