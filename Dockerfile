FROM ubuntu:22.04
RUN apt-get update && \
    apt-get -y install python3 socat python3-pip && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /home/nobody
COPY src .

COPY .env .
RUN export $(cat .env | xargs)

USER nobody
EXPOSE 10000
CMD socat TCP-LISTEN:10000,reuseaddr,fork EXEC:"python3 -u app.py"