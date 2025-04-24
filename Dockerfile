FROM python:3.8-slim-buster

# Install system dependencies
RUN apt update -y && apt install -y \
    awscli \
    build-essential \
    gcc \
    libzstd-dev

WORKDIR /app

# Copy project files
COPY . /app

# Install Python dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
RUN pip install --upgrade accelerate
RUN pip uninstall -y transformers accelerate
RUN pip install transformers accelerate

# Command to run the application
CMD ["python3", "app.py"]