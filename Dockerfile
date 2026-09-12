FROM python:3.12-slim

# Install Chromium and required system dependencies
RUN apt-get update && apt-get install -y \
    chromium \
    chromium-driver \
    && rm -rf /var/lib/apt/lists/*

# Set working directory
WORKDIR /app

# Copy dependency file first
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy framework
COPY . .

# Run tests by default
CMD ["pytest", "--env", "qa", "--headless", "-n", "2", "-v", "--html=reports/report.html", "--self-contained-html"]