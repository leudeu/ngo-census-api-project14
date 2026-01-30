FROM python:3.10-alpine
WORKDIR /app
COPY app/ .
RUN pip install flask --no-cache-dir
EXPOSE 5000
CMD ["python", "app.py"]
