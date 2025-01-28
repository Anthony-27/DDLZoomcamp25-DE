FROM python:3.9.1

# Install dependencies
RUN apt-get update && apt-get install -y wget

# Install Python libraries
RUN pip install pandas sqlalchemy psycopg2

# Set working directory
WORKDIR /app

# Copy the script
COPY ingest_data.py ingest_data.py

# Set the entrypoint
ENTRYPOINT [ "python", "ingest_data.py" ]