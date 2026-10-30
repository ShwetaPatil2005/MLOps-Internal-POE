
FROM python:3.13-slim

WORKDIR /app

COPY requirements-app.txt .
RUN python -m pip install --no-cache-dir --index-url https://pypi.org/simple Flask==3.1.3 Werkzeug==3.1.9

COPY hello.py .

EXPOSE 5000

CMD ["python", "hello.py"]
