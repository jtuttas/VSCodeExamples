FROM microsoft/powershell:ubuntu16.04

RUN apt-get update && \
    apt-get -y upgrade && \
	apt-get install -y krb5-multidev && \
    apt-get install -y libkrb5-dev && \
 	apt-get install -y gss-ntlmssp

EXPOSE 5985 5986 