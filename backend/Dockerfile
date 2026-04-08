FROM python:3.11-slim


RUN apt-get update && \
    apt-get install -y ca-certificates && \
    update-ca-certificates


WORKDIR /app

COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install --trusted-host pypi.org --trusted-host files.pythonhosted.org fastapi uvicorn sqlalchemy psycopg2-binary
RUN pip install --no-cache-dir -r requirements.txt

COPY app ./app

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8001"]