FROM python:3.9.7

RUN mkdir -p /build

COPY tfsites-webportal /build/tfsites-webportal 


ENV PYTHONPATH "${PYTHONPATH}:/build/tfsites-webportal"
RUN pip install pandas Bio matplotlib
RUN apt-get update && apt-get install bedtools && apt-get clean


RUN chmod a+x /build/tfsites-webportal/*.sh
