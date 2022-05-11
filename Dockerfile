FROM ubuntu
RUN apt-get update && \
       apt-get install -y  curl wget  git  python3 python3-pip sudo dos2unix
ADD roman.py /root/roman.py
CMD [ "python3","./root/roman.py" ]

