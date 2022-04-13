FROM python:3.9

COPY . /app

WORKDIR /app

RUN pip install --upgrade pip
RUN pip install --trusted-host pypi.python.org -r requirements.txt

ENV PORT 8080
EXPOSE 8080
CMD univort main:app --host 0.0.0.0 --port 8080