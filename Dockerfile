# Use a lightweight Python image
FROM python:3.9-slim

# Set environment variables
ENV PYTHONUNBUFFERED=1

# Install required system tools
RUN apt-get update && apt-get install -y --no-install-recommends build-essential python3-pip

# Set the working directory
WORKDIR /app

# Copy the requirements file and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application files
COPY taxonomic_analysis.py taxonomic_data.csv ./

# Create and set permissions for the output directory
RUN mkdir -p /app/output && chmod 777 /app/output

# Default command to run the Python script
CMD ["python", "taxonomic_analysis.py"]

