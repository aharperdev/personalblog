bind = "0.0.0.0:8000"
module = "personalblog.wsgi:application"

workers = 3
worker_connections = 500
threads = 3

certfile = "/etc/letsencrypt/live/blog.aharper.codes/fullchain.pem"
keyfile = "/etc/letsencrypt/live/blog.aharper.codes/privkey.pem"
