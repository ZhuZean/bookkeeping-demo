FROM node:lts-alpine as build-stage
WORKDIR /app
COPY web/. ./
RUN npm install
COPY . .
RUN npm run build

# production image
FROM nginx:stable-alpine as release-stage

COPY --from=build-stage /app/dist /usr/share/nginx/html/

COPY web/deployment/dockerfiles/nginx.conf /etc/nginx/conf.d/default.conf

EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]