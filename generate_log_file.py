import random
import os
from datetime import datetime

def randomaize_ip_addr(): 
    return ".".join(str(random.randint(0, 255)) for _ in range(4))

def randomize_methods_codes(list):
    return random.choice(list)

methods=["GET", "POST", "PUT", "PATCH", "DELETE"]
codes=["200", "201", "400", "401", "403", "404", "500", "501", "502", "503"]

file_log_name = f"{datetime.now().strftime('%Y_%m_%d')}_request.log"

with open(file_log_name, 'a') as file:

    for _ in range(0, 5):
        log_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        long_list = f'{log_time} {randomize_methods_codes(methods)} {randomize_methods_codes(codes)} {randomaize_ip_addr()}\n'
        file.write(long_list)

