"""
WSGI config for myvoting project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myvoting.settings')

application = get_wsgi_application()



# ssh -i n_evote.pem ubuntu@ec2-16-171-226-173.eu-north-1.compute.amazonaws.com



# [Unit]
# Description=gunicorn daemon
# Requires=gunicorn.socket
# After=network.target

# [Service]
# User=ubuntu
# Group=www-data
# WorkingDirectory=/home/ubuntu/vote_test
# ExecStart=/home/ubuntu/vote_test/myprojectenv/bin/gunicorn \
#           --access-logfile - \
#           --workers 3 \
#           --bind unix:/run/gunicorn.sock \
#           myvoting.wsgi:application

# [Install]
# WantedBy=multi-user.target


# server {
#     listen 80;
#     server_name server_domain_or_IP;
# }


# server {
#     listen 80;
#     server_name 16.171.226.173;

#     location = /favicon.ico { access_log off; log_not_found off; }
#     location /static/ {
#         root /home/ubuntu/vote_test;
#     }

#     location / {
#         include proxy_params;
#         proxy_pass http://unix:/run/gunicorn.sock;
#     }
# }