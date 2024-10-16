bind = "0.0.0.0:8000"
module = "personalblog.wsgi:application"

workers = 3
worker_connections = 500
threads = 3

certfile = "/etc/letsencrypt/live/your_domain.com/fullchain.pem"
keyfile = "/etc/letsencrypt/live/your_domain.com/privkey.pem"
