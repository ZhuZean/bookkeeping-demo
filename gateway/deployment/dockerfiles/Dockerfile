FROM nginx:1.19.0-alpine AS gateway-base

COPY gateway/deployment/dockerfiles/default.conf /etc/nginx/conf.d/default.conf
COPY gateway/deployment/dockerfiles/nginx.conf /etc/nginx/nginx.conf
RUN mkdir -p /data/nginx/cache

EXPOSE 80
