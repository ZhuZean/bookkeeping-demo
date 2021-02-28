# Django
FROM python:3.8
ENV PYTHONUNBUFFERED 1

RUN mkdir -p /backend/logs
RUN touch /backend/logs/debug.log
WORKDIR /backend
