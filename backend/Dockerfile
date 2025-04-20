FROM python:3.10

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the app source and the wait script
COPY run.py .
COPY wait_for_db.py .
COPY app/ ./app

# Wait for DB to be ready before starting Flask
CMD ["sh", "-c", "python wait_for_db.py && python run.py"]

EXPOSE 5000
