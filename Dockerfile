FROM ubuntu:18.04
ENTRYPOINT []
RUN apt-get update && apt-get install -y python3 python3-pip && python3 -m pip install --no-cache --upgrade pip && pip3 install --no-cache rasa==1.5.3
ADD . /nona-app/
RUN chmod +x /nona-app/start_services.sh
CMD /nona-app/start_services.sh