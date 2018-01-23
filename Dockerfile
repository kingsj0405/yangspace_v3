FROM python:3
 ENV PYTHONUNBUFFERED 1
 # Tools for I18N
 RUN apt-get update && apt-get install -y gettext libgettextpo-dev
 # Make 
 RUN mkdir /YangSpace
 WORKDIR /YangSpace
 # Install dependencies
 ADD requirements.txt /YangSpace/
 RUN pip install -r requirements.txt
 # Copy all code
 ADD . /YangSpace/
