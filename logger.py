import datetime
import json
import psutil
import time


class Logger(object):
    'Class for writing system information in log file'
    def __init__(self):
        f = open("config.ini", "r")
        config = f.read()
        f.close()
        config = config.split()

        self.count = 0
        self.format = config[3]
        self.interval = float(config[6]) * 60

        if self.format != 'json':
            list = ['Count      ', 'Date      ', 'Time            ',
                    'CPU', 'Mem', 'Swp', 'Disc', 'Net', '\n']
            title = ' '.join(list)
            f = open("log.txt", "w")
            f.write(title)
        else:
            f = open("log.txt", "w")
        f.close()

    def get_info(self):
        self.count += 1
        self.date = str(datetime.datetime.now().date())
        self.time = str(datetime.datetime.now().time())
        self.cpu = psutil.cpu_percent(interval=1, percpu=False)
        self.memory = psutil.virtual_memory().percent
        self.virtual_memory = psutil.swap_memory().percent
        self.disk = psutil.disk_usage('/').percent
        self.network = len(psutil.net_connections())

    def write_txt(self):
        list = ['SNAPSHOT']
        list.append(str(self.count) + ':')
        list.append(self.date)
        list.append(self.time + ':')
        list.append(str(self.cpu))
        list.append(str(self.memory))
        list.append(str(self.virtual_memory))
        list.append(str(self.disk))
        list.append(str(self.network))
        list.append('\n')
        log = ' '.join(list)
        f = open("log.txt", "a")
        f.write(log)
        f.close()

    def write_json(self):
        log = json.dumps({
            'SNAPSHOT': self.count,
            'Date': self.date,
            'Time': self.time,
            'CPU': self.cpu,
            'Memory': self.memory,
            'Virtual memory': self.virtual_memory,
            'IO information': self.disk,
            'Network': self.network
        }, indent=4)
        f = open("log.txt", "a")
        f.write(log + '\n')
        f.close()

    def sleep(self):
        time.sleep(self.interval)


log = Logger()

while True:
    log.get_info()
    if log.format == 'json':
        log.write_json()
    else:
        log.write_txt()
    log.sleep()
