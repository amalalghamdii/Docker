FROM python:alpine
WORKDIR /
RUN mkdir /home/data
RUN mkdir /home/output
COPY . /
CMD python dockerpro.py 

