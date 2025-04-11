# Use an official Python runtime as a parent image
FROM python:3.12
LABEL authors="MykytaChernetskyi"

# Prevents Python from writing pyc files to disc
ENV PYTHONDONTWRITEBYTECODE 1
# Prevents Python buffering stdout and stderr
ENV PYTHONUNBUFFERED 1

WORKDIR /code

# Install dependencies
COPY requirements.txt /code/
RUN pip install --upgrade pip && pip install -r requirements.txt

# Copy project files
COPY . /code/

# Perform static build when building an image
RUN python manage.py collectstatic --noinput

RUN chmod +x /code/docker/event/entrypoint.sh

# Open port
EXPOSE 8000

# Run the application using gunicorn for production
ENTRYPOINT ["/code/docker/event/entrypoint.sh"]
