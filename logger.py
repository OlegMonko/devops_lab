import datetime
import json
import psutil
import time

def logtxt(i):
    if i == 1:
        list = ['Count', 'Date', 'Time', 'CPU', 'Mem', 'Swap', 'Disc', 'Net', '\n']
        title = '    '.join(list)
        f = open("log.txt", "w")
        f.write(title)
        f.close()

    list = ['SNAPSHOT']
    list.append(str(i))
    list.append(str(datetime.datetime.now()))
    list.append(str(psutil.cpu_percent(interval=1, percpu=False)))
    list.append(str(psutil.virtual_memory().percent))
    list.append(str(psutil.swap_memory().percent))
    list.append(str(psutil.disk_usage('/').percent))
    list.append(str(len(psutil.net_connections())))
    list.append('\n')
    log = ' '.join(list)

    f = open("log.txt", "a")
    f.write(log)
    f.close()


def logjson(i):
    log = json.dumps({
        'SNAPSHOT': i,
        'Date': str(datetime.datetime.now().date()),
        'Time': str(datetime.datetime.now().time()),
        'CPU': psutil.cpu_percent(interval=1, percpu=False),
        'Memory': psutil.virtual_memory().percent,
        'Virtual memory': psutil.swap_memory().percent,
        'IO information': psutil.disk_usage('/').percent,
        'Network': len(psutil.net_connections())
    }, indent=4)

    if i == 1:
        f = open("log.txt", "w")
    else:
        f = open("log.txt", "a")
    f.write(log + '\n')
    f.close()


f=open("config.ini", "r")
config = f.read()
f.close()
config=config.split()
format = config[3]
interval = float(config[6]) * 60
i = 1

while True:
    if format == 'json':
        logjson(i)
    else:
        logtxt(i)

    i += 1
    time.sleep(interval)
