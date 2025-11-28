import requests
import json
from config import url , rules
from notification import send_sms


def get_rates():
    response =requests.get(url)
    if response.status_code==200:
        return json.loads(response.text)
    return None


def archive(filename, rates):
    with open(f'/home/zahrasadeghi/Documents/7learn project/exchange/exchange/archive/{filename}.json', 'w') as f:
        f.write(json.dumps(rates))


def send_mail(timestamp , rates):
    subject = f'{timestamp} rates'
    if rules['email']['preferred'] is not none:
        tmp = dict()
        for exc in rules['email']['preferred']:
            tmp[exc] = rates[exc]
        rates = tmp
    text = json.dumps(rates)


def check_notify_rules(rates):
    preferred = rules['notification']['preferred']
    msg = ''
    for exc in preferred:
        print(rates[exc])
        print(preferred[exc]['min'])
        if rates[exc] <= preferred[exc]['min']:
            msg+= f'{exc} reached min'
            
        if rates[exc] >= preferred[exc]['max']:
            msg+= f'{exc} reached max'
    print(f'massage is {msg}')


def send_notification(msg):
    send_sms(msg)


if __name__=="__main__":

    res = get_rates()

    if rules['archive']:
        archive(res['timestamp'] , res['rates'])

    if rules['email']['enable']:
        send_mail(res['timestamp'] , res['rates'])

    if rules['notification']['enable']:
        notification_msg =  check_notify_rules(res['rates'])
        if notification_msg !='':
            send_notification(notification_msg)