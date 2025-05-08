FROM python:3.12

WORKDIR /app
COPY . /app

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

ENV FLASK_APP=app:create_app
CMD ["flask", "run", "--host=0.0.0.0", "--port=5000"]
