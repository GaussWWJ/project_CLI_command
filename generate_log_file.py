import random
import os
from datetime import datetime

def randomaize_ip_addr():
    return ".".join(str(random.randint(0, 255)) for _ in range(4))


def randomize_methods_codes(list):
    return random.choice(list)


methods=["GET", "POST", "PUT", "PATCH", "DELETE"]
codes=["200", "201", "400", "401", "403", "404", "500", "501", "502", "503"]

long_list = randomize_methods_codes(methods) + ' ' + randomize_methods_codes(codes) + ' ' + randomaize_ip_addr()
print(f"{randomize_methods_codes(methods)} {randomize_methods_codes(codes)} {randomaize_ip_addr()}")


log_time = datetime.now()
print (log_time.year)

