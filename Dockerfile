FROM ubuntu:15.10

RUN locale-gen en_US en_US.UTF-8
ENV LANG en_US.UTF-8

RUN apt-get update && \
    apt-get install -y --force-yes \
        sudo wget software-properties-common python3 python3-setuptools python3-dev python3-lxml libpq-dev git mercurial \
        build-essential libboost-all-dev autoconf antlr swig libjpeg8 libjpeg-dev libfreetype6 libfreetype6-dev zlib1g-dev libxml2-dev libxslt1-dev \
        libcairo2 libpango1.0-0 libgdk-pixbuf2.0-0 libffi-dev shared-mime-info libcurl4-openssl-dev && \
    apt-get purge python3-pip && easy_install3 pip && \
    apt-get install -y --force-yes libcurl4-gnutls-dev && \
    apt-get install -y --force-yes libcurl4-openssl-dev



COPY . /home/r
WORKDIR /home/r

RUN cd ..

RUN wget https://github.com/Apination/cn/archive/master.tar.gz && \
    tar xzf master.tar.gz


RUN pip3 install -r requirements.txt


CMD python3 -u worker.py
