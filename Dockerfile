FROM python:2.7

RUN mkdir /opt/dashboarder
WORKDIR /opt/dashboarder

ADD requirements.txt /opt/dashboarder/
RUN pip install -r requirements.txt
ADD . /opt/dashboarder