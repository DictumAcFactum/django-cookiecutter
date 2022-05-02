#!/bin/sh
echo $HTPASSWD > /etc/nginx/.htpasswd
esh -o /etc/nginx/conf.d/nginx.conf /etc/nginx/nginx.conf.esh
exec nginx -g 'daemon off;'