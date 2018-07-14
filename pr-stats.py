import argparse
import calendar
from datetime import datetime
import getpass
import requests


def get_config():
    parser = argparse.ArgumentParser()
    parser.add_argument('-v', '--version', action='version',
                        version='%(prog)s 1.0', help='Show version')
    parser.add_argument('-d', '--dayweek', default=False, action='store_true',
                        dest='d', help='Day of the week opened.')
    parser.add_argument('-n', '--daynum', default=False, action='store_true',
                        dest='n', help='Number of days opened.')
    parser.add_argument('-u', '--user', default=False, action='store_true',
                        dest='u', help='User who opened.')
    parser.add_argument('-c', '--comment', default=False, action='store_true',
                        dest='c', help='Show all comments.')
    parser.add_argument('-a', '--add', default=False, action='store_true',
                        dest='a', help='Number of lines added..')
    parser.add_argument(metavar='user', dest='user')
    parser.add_argument(metavar='repo', dest='repo')

    config = parser.parse_args().__dict__
    config['login'] = input("Enter your login: ")
    config['password'] = getpass.getpass()

    url = 'https://api.github.com/repos/' + config['user'] + '/' + \
          config['repo'] + '/pulls?page=1&per_page=100'
    history = requests.get(url, auth=(config['login'], config['password'])).json()

    return config, history


def day_week(history):
    for i in history:
        title = i['title']
        day = i['created_at'][:10]
        day = datetime.strptime(day, '%Y-%m-%d').date()
        dayweek = calendar.day_name[day.weekday()]
        print(title, day, '-', dayweek)


def number_days(history):
    for i in history:
        title = i['title']
        day = i['created_at'][:10]
        day = datetime.strptime(day, '%Y-%m-%d').date()
        ndays = (datetime.now().date() - day).days
        print(title, day, '-', ndays, 'day(s)')


def user_opened(history):
    for i in history:
        title = i['title']
        user = i['user']['login']
        print(title, 'opened by', user)


def get_comments(history, config):
    for i in history:
        number = str(i['number'])
        url = 'https://api.github.com/repos/' + config['user'] + '/' + \
              config['repo'] + '/pulls/' + number + '/comments?page=1&per_page=100'
        history2 = requests.get(url, auth=(config['login'], config['password'])).json()
        print('Comments for ', i['title'], ':', sep='')
        for j in history2:
            print(j['path'], ':', j['user']['login'], ': ', j['body'], sep='')


def lines_added(history, config):
    for i in history:
        number = str(i['number'])
        url = 'https://api.github.com/repos/' + config['user'] + '/' + \
              config['repo'] + '/pulls/' + number + '?page=1&per_page=100'
        history2 = requests.get(url, auth=(config['login'], config['password'])).json()
        print(i['title'], ': ', history2['additions'], ' lines were added', sep='')


conf, hist = get_config()
if conf['d']:
    day_week(hist)
if conf['n']:
    number_days(hist)
if conf['u']:
    user_opened(hist)
if conf['c']:
    get_comments(hist, conf)
if conf['a']:
    lines_added(hist, conf)
