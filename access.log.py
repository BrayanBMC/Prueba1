import random
from datetime import datetime

ips = ["192.168.1.1", "192.168.1.2", "192.168.1.3", "192.168.1.4", "192.168.1.5", "192.168.1.6", "192.168.1.7",
        "192.168.1.8", "192.168.1.9"]
statuses = [200, 404]
urls = ["/index.html", "/notfound", "/login"]

with open("access.log", "w") as file:
    for _ in range(50):
        ip = random.choice(ips)
        status = random.choice(statuses)
        url = random.choice(urls)
        size = random.randint(100, 5000)
        log = f'{ip} - - [{datetime.now().strftime("%d/%b/%Y:%H:%M:%S +0000")}] "GET {url} HTTP/1.1" {status} {size}\n'
        file.write(log)
