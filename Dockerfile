FROM debian:latest

RUN apt-get update && apt-get install -y \
    build-essential \
    libssl-dev \
    git

RUN git clone https://github.com/katmagic/Shallot.git

WORKDIR /Shallot

RUN ./configure && make
