FROM mcr.microsoft.com/playwright/python:v1.41.2-jammy

ARG ENV

ENV ENV=$ENV

COPY . ./e2e/
WORKDIR /e2e

RUN pip install --upgrade pip
RUN pip install -r requirements.txt