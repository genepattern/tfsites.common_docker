FROM python:3.9.7

RUN mkdir -p /build

COPY tfsites-webportal /build/tfsites-webportal 

ENV PYTHONPATH="${PYTHONPATH}:/build/tfsites-webportal"

RUN apt update && \
    DEBIAN_FRONTEND=noninteractive apt install -y --no-install-recommends \
    libc6 \
    bedtools \
    vim && \
    apt clean && \
    rm -rf /var/lib/apt/lists/* 
    
RUN pip install pandas Bio matplotlib seaborn markdown psutil jinja2 numpy==1.26.4

RUN chmod a+x /build/tfsites-webportal/*.sh

# Font installation
ENV DEBIAN_FRONTEND=noninteractive
RUN apt-get update && \
    apt-get install -y --no-install-recommends fonts-dejavu-core software-properties-common && \
    sed -i 's/main/main contrib non-free/' /etc/apt/sources.list && \
    apt-get update && \
    apt-get install -y --no-install-recommends ttf-mscorefonts-installer && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/* /var/cache/apt/archives/* && \
    rm ~/.cache/matplotlib -rf