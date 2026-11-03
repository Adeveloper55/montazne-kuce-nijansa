# Build context = repository root
# Serves static Homely/Nijansa site on port 80
FROM nginx:1.27-alpine

COPY homely/nginx.conf /etc/nginx/conf.d/default.conf
COPY homely/ /usr/share/nginx/html/

RUN rm -f /usr/share/nginx/html/Dockerfile \
          /usr/share/nginx/html/nginx.conf \
          /usr/share/nginx/html/docker-compose.yml \
          /usr/share/nginx/html/.dockerignore \
          /usr/share/nginx/html/package.json \
          /usr/share/nginx/html/package-lock.json 2>/dev/null || true

EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]
