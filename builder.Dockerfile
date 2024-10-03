FROM debian:12

RUN apt update && \
    apt install -y git make dosfstools sudo && \
    rm -rf /var/lib/apt/lists/* \

WORKDIR /workspace
