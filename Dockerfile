FROM ubuntu:19.10

RUN apt-get update \
  && apt-get install -y wget ca-certificates \ 
  build-essential cmake pkg-config \
  git curl vim python3-dev python3-pip \
  && cd /usr/local/bin \
  && ln -s /usr/bin/python3 python


#    && pip3 install ptvsd \
COPY requirements.txt /tmp/
RUN ["mkdir", "src"]
RUN pip3 install --requirement /tmp/requirements.txt
COPY . /tmp/
COPY requirements.txt /tmp/
COPY conf/.jupyter /root/.jupyter
COPY run_jupyter.sh /

# Jupyter port
EXPOSE 8888

# Store notebooks in this mounted directory
VOLUME /src

CMD ["/run_jupyter.sh"]