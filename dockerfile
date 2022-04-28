# Pull base image
FROM python:3.10

# Set environment varibles
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /./

# Install dependencies
RUN pip install pipenv
RUN pipenv install --system --dev

COPY /./

EXPOSE 8000