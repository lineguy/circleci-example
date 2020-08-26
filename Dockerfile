FROM nginx:latest

# Copy index into nginx
COPY ./index.html /usr/share/nginx/html/index.html

# Set version variable inside container
ARG commit
ENV COMMIT_SHA=$commit

