FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY . .

EXPOSE 8666

CMD ["python", "manage.py", "runserver", "0.0.0.0:8666"]
