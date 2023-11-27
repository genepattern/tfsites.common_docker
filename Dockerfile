FROM python:3.9.7

RUN mkdir -p /build

COPY tfsites-webportal /build/tfsites-webportal 


ENV PYTHONPATH "${PYTHONPATH}:/build/tfsites-webportal"
RUN pip install pandas Bio matplotlib
RUN apt-get update && apt-get install bedtools && apt-get clean

COPY 05-integrateGenomeAnnotations.GENEPATTERN.py /build/tfsites-webportal/05-integrateGenomeAnnotations/05-integrateGenomeAnnotations.GENEPATTERN.py

