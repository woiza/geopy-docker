FROM python:3

RUN pip install geopy
RUN pip install matplotlib
RUN pip install osmapi
RUN git clone https://github.com/gaulinmp/pyroutelib2
RUN mv /pyroutelib2/* .
