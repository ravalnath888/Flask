# Python image
FROM python:3.11-slim-buster

# Working directory
WORKDIR /app

# Copy requirements and install
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy all frontend code
COPY . .

# Flask environment variables
ENV FLASK_APP=App.py
ENV FLASK_RUN_HOST=0.0.0.0
ENV FLASK_RUN_PORT=3000

# Expose port
EXPOSE 3000

# Run Flask app
CMD ["flask", "run"]
