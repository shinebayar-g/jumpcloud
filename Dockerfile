FROM python:3.7-alpine
WORKDIR /app
COPY src .
RUN pip install -r requirements.txt --no-cache-dir
ENTRYPOINT ["python", "app.py"]