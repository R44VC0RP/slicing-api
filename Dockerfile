FROM python:3.12-slim

# Update and install required packages
RUN apt-get update && \
    apt-get install -y \
    prusa-slicer

# Install requirements
COPY requirements.txt /requirements.txt
RUN python3 -m pip install -r requirements.txt

# Copy application
COPY app.py /app.py

CMD ["python3", "/app.py"]