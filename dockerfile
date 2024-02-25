root@localhost:~/py# cat Dockerfile

# Use the official Python base image
FROM --platform=linux/amd64 python:3.9-rc-slim-buster as pythonbaseimage

# Copy pip file to container
COPY Pipfile .
COPY Pipfile.lock .

# Install any required system dependencies
RUN pip install pipenv \
 && PIPENV_VENV_IN_PROJECT=1 PIPENV_SITE_PACKAGES=1 pipenv install --deploy --dev --system

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements file and install Python dependencies
FROM pythonbaseimage
COPY --from=pythonbaseimage /.venv /.venv
ENV PATH="/.venv/bin:$PATH"

# Copy your application code into the container
COPY . .

# Expose any required ports
RUN mkdir /app/allure-results