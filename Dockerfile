FROM python:3.6
ENV PYTHONUNBUFFERED 1
RUN mkdir /jubilee
WORKDIR /jubilee
COPY requirements.txt /jubilee/
RUN pip install -r requirements.txt

COPY . /jubilee/
