FROM ubuntu:latest
RUN apt-get update && apt-get install -y --no-install-recommends openssl netcat-openbsd lftp python3 python3-pip && pip3 install pycurl
COPY FTPS /FTPS
CMD ["sleep", "infinity"]
