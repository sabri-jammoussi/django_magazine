FROM python:3.10.10
RUN pip install --upgrade pip  
ENV DockerHOME=/home/app/webapp  
RUN mkdir -p $DockerHOME  
COPY . $DockerHOME  
WORKDIR $DockerHOME  
RUN pip install -r requirements.txt  
EXPOSE 8000
CMD python manage.py runserver 