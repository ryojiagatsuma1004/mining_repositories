FROM fedora:latest

WORKDIR /workspace

RUN dnf install -y \
        glibc \
        procps \
        freetype \
        libXext \
        libXrender \
        libXtst \
        libXi \
        unzip \
        curl \
        git \
        python3 \
        python3-pip && \
    dnf clean all
