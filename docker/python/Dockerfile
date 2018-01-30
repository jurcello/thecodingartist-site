FROM python:3
RUN useradd -ms /bin/bash admin
ENV PYTHONUNBUFFERED 1
ENV DJANGO_ENVIRONMENT production
RUN mkdir /code
RUN mkdir -p /media/codingartist && mkdir -p /databases/coding_artist
RUN chown -R admin:admin /media/codingartist && chown -R admin:admin /databases/coding_artist
WORKDIR /code
COPY ./codingartist/requirements.txt /code/
RUN pip install -r requirements.txt && pip install uwsgi
COPY ./codingartist /code/
COPY ./docker/python/uwsgi.ini /home/admin/

WORKDIR /code
USER admin
CMD ["uwsgi", "/home/admin/uwsgi.ini" ]