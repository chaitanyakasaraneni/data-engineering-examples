
FROM python:3.7.10
LABEL maintainer="Chaitanya Kasaraneni <chaitanya.kasaraneni0@gmail.com>"

ADD . /services

WORKDIR /services
ADD . /utils
ADD . /services/publishData_toPub.py
ADD . /services/subscribeData_toStorage.py
RUN pip install -r requirements.txt

CMD [ "python", "services/publishData_toPub.py"]