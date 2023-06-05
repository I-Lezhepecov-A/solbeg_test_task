FROM python:3.9-buster
ENV PYTHONUNBUFFERED 1

WORKDIR /opt/app
COPY shipments_backend/requirements.txt /tmp/
# COPY .env /tmp/
RUN apt update && \
    pip install --upgrade pip && \
    pip install -r /tmp/requirements.txt

COPY shipments_backend /opt/app
# COPY . .
EXPOSE 8000
# RUN python manage.py migrate ;python manage.py seed_directions ;python manage.py seed_transporters ;python manage.py seed_shipments
# ENTRYPOINT []
CMD python manage.py runserver 8000