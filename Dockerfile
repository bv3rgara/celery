FROM python:3
ENV PYTHONUNBUFFERED=1
WORKDIR /usr/src/app
COPY requeriments.txt ./
RUN pip install -r requeriments.txt