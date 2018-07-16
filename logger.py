import configparser
import datetime
import json
import psutil
import time
import yaml


class Logger(object):
    """Class for writing system information in log file"""
    def __init__(self):
        config = configparser.ConfigParser()
        config.read('config.ini')

        self.count = 0
        self.format = config['common']['output']
        self.interval = float(config['common']['interval']) * 60
        print(self.format, self.interval)
        if self.format == 'txt':
            lst = ['Count      ', 'Date      ', 'Time            ',
                   'CPU', 'Mem', 'Swp', 'Disc', 'Net', '\n']
            title = ' '.join(lst)
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
        lst = ['SNAPSHOT']
        lst.append(str(self.count) + ':')
        lst.append(self.date)
        lst.append(self.time + ':')
        lst.append(str(self.cpu))
        lst.append(str(self.memory))
        lst.append(str(self.virtual_memory))
        lst.append(str(self.disk))
        lst.append(str(self.network))
        lst.append('\n')
        lg = ' '.join(lst)
        f = open("log.txt", "a")
        f.write(lg)
        f.close()

    def write_json(self):
        lg = json.dumps({
            'SNAPSHOT': self.count,
            'Timestamp': {
                'Date': self.date,
                'Time': self.time
            },
            'Status': {
                'CPU': self.cpu,
                'Memory': self.memory,
                'Virtual memory': self.virtual_memory,
                'IO information': self.disk,
                'Network': self.network
            }}, indent=4)
        f = open("log.txt", "a")
        f.write(lg + '\n')
        f.close()

    def sleep(self):
        time.sleep(self.interval)


class LoggerYaml(Logger):
    """Added writing in YAML"""
    def write_yaml(self):
        lg = yaml.dump({
            'SNAPSHOT': self.count,
            'Date': self.date + self.time,
            'Status': {
                'CPU': self.cpu,
                'Memory': self.memory,
                'Virtual memory': self.virtual_memory,
                'IO information': self.disk,
                'Network': self.network
            }}, default_flow_style=False)
        f = open("log.txt", "a")
        f.write(lg + '\n')
        f.close()


log = LoggerYaml()

while True:
    log.get_info()
    if log.format == 'json':
        log.write_json()
    elif log.format == 'yaml':
        log.write_yaml()
    else:
        log.write_txt()
    log.sleep()
