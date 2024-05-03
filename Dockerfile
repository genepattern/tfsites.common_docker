FROM python:3.9.7

RUN mkdir -p /build

COPY tfsites-webportal /build/tfsites-webportal 


ENV PYTHONPATH "${PYTHONPATH}:/build/tfsites-webportal"
RUN pip install pandas Bio matplotlib
RUN apt-get update && apt-get install bedtools && apt-get clean

#COPY 05-integrateGenomeAnnotations.GENEPATTERN.py /build/tfsites-webportal/05-integrateGenomeAnnotations/05-integrateGenomeAnnotations.GENEPATTERN.py
#COPY 08-compareSeqs.GENEPATTERN.py /build/tfsites-webportal/08-compareSeqs/08-compareSeqs.py
#COPY 11-visualizeGenotypeSnvEffects.GENEPATTERN.py /build/tfsites-webportal/11-visualizeGenotypeSnvEffects/11-visualizeGenotypeSnvEffects.py

#COPY 14-analyzeGwas.GENEPATTERN.py /build/tfsites-webportal/14-analyzeGwas/14-analyzeGwas.py
#COPY 15-analyzeEqtl.GENEPATTERN.py /build/tfsites-webportal/15-analyzeEqtl/15-analyzeEqtl.py
#COPY 13-annotateAndVisualizeInSilicoSnvs.GENEPATTERN.py /build/tfsites-webportal/13-annotateAndVisualizeInSilicoSnvs/13-annotateAndVisualizeInSilicoSnvs.py


RUN chmod a+x /build/tfsites-webportal/*.sh
