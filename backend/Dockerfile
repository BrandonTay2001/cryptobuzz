FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Copy requirements file
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY . .

# Set environment variables
ENV PYTHONUNBUFFERED=1

# Expose port (Cloud Run will override this with the PORT environment variable)
EXPOSE 8080

# Run the application with Gunicorn
CMD exec gunicorn --bind :$PORT --workers $(python -c "import multiprocessing; print(max(1, multiprocessing.cpu_count() * 2 - 1))") --threads 8 --timeout 0 app:app