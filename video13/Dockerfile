FROM python:3.7

ENV PYTHONUNBUFFERED=1
COPY conf/requirements.txt andrey-django/
WORKDIR andrey-django/
RUN pip3 install -r requirements.txt
CMD ["uwsgi", "--master", "--ini", "/opt/conf/mysite_uwsgi.ini"]

#ENV PYTHONUNBUFFERED=1
#RUN pip3 install -r /opt/app/conf/requirements.txt
#CMD ["uwsgi", "--master", "--ini", "/opt/conf/mysite_uwsgi.ini"]