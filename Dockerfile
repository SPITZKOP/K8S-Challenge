# Use a base image
FROM python:3.9

# Set the working directory inside the container
WORKDIR .

# Copy the requirements file and install dependencies
COPY requirements.txt .
RUN pip install psycopg2

# Install the postgre client
RUN apt-get update && apt-get install -y postgresql-client

# Copy the rest of the application code
COPY app.py .
COPY templates templates


# Set the entry point for the container

# Expose a port (if required)
EXPOSE 5000

ENV FLASK_APP=app.py
ENV PYTHONUNBUFFERED=1
ENV PYTHONIOENCODING=UTF-8

# Set the entry point command
CMD ["flask", "run", "--host=0.0.0.0"]