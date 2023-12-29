# usage: docker build -t tvsi-backend:IMAGE_VERSION .
FROM python:3.10-slim
MAINTAINER ChenYong
ENV LANG en_US.UTF-8
ENV opt /opt
WORKDIR ${opt}
ADD . .
RUN pip3 install -U -i https://mirrors.aliyun.com/pypi/simple/ pip
RUN pip3 install -U -i https://mirrors.aliyun.com/pypi/simple/ -r requirements.txt
CMD ["/bin/sh", "runserver.sh"]
