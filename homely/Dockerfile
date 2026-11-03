# Static site — Montažne kuće Nijansa
FROM nginx:1.27-alpine

# Custom nginx config for domain + clean URLs
COPY nginx.conf /etc/nginx/conf.d/default.conf

# Site files (this folder is the web root)
COPY . /usr/share/nginx/html

# Do not ship deploy/helper junk into the image
RUN rm -f /usr/share/nginx/html/Dockerfile \
          /usr/share/nginx/html/nginx.conf \
          /usr/share/nginx/html/docker-compose.yml \
          /usr/share/nginx/html/.dockerignore \
          /usr/share/nginx/html/package.json \
          /usr/share/nginx/html/package-lock.json 2>/dev/null || true

EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]
