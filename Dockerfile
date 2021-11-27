# FROM alpine:3.9
FROM continuumio/anaconda3
COPY . /app
EXPOSE 5000
WORKDIR /app
# RUN apk add --update \
#     python3 \
#     python-dev \
#     py-pip \
#     build-base \
#   && pip3 install virtualenv \
# #   && pip install --upgrade pip \
#   && rm -rf /var/cache/apk/*
# RUN pip3 install wheel setuptools \
#     pip3 install -r requirements.txt
RUN \
    # apk add --update python3 python3-dev py-pip build-base && \
    # apk add build-base && \
    pip3 install wheel setuptools \
    && pip3 install -r requirements.txt \
    && rm -rf /var/cache/apk/*
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "5000"]