#!/usr/bin/env bash
# Web static Deployment automation.


sudo apt update -y
sudo apt install nginx -y

sudo mkdir -p /data/web_static/releases/test
sudo mkdir -p /data/web_static/shared
echo "<html>
        <head>
                <title>Faker</title>
        </head>
        <body>
                <p1>I am Fake</p1>
        </body>
</html>" > /data/web_static/releases/test/index.html

sudo ln -sf /data/web_static/releases/test/ /data/web_static/current
sudo chown -R ubuntu:ubuntu /data
sudo sed -i '/listen 80 default_server/a location /hbnb_static/ { alias /data/web_static/current/;}' /etc/nginx/sites-available/default
sudo service nginx restart
