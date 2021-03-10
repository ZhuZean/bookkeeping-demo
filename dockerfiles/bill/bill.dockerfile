# Django
FROM python:3.8
ENV PYTHONUNBUFFERED 1

RUN mkdir -p /bill/logs
RUN touch /bill/logs/debug.log
WORKDIR /bill
