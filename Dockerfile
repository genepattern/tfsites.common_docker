FROM python:3.9.7

RUN mkdir -p /build

COPY tfsites-webportal /build/tfsites-webportal 

RUN pip install pandas Bio matplotlib



