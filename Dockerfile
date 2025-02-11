FROM python:3.9.7

RUN mkdir -p /build

COPY tfsites-webportal /build/tfsites-webportal 

RUN mkdir /phenix_installer
COPY phenix-installer-1.21.2-5419-intel-linux-2.6-x86_64-centos6.tar.gz /phenix_installer/phenix-installer-1.21.2-5419-intel-linux-2.6-x86_64-centos6.tar.gz

ENV PYTHONPATH="${PYTHONPATH}:/build/tfsites-webportal"

RUN export PYTHONPATH="${PYTHONPATH}:/build/tfsites-webportal" && \
    apt-get install libc6 && \
    cd /phenix_installer && \
    tar xvf phenix-installer-1.21.2-5419-intel-linux-2.6-x86_64-centos6.tar.gz && \
    pwd && \
    ls -alrt 
RUN  cd /phenix_installer/phenix-installer-1.21.2-5419-intel-linux-2.6-x86_64-centos6  && \
    ./install

RUN pip install pandas Bio matplotlib
RUN apt-get update && apt-get install bedtools && apt-get clean


RUN chmod a+x /build/tfsites-webportal/*.sh
