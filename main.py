import datetime, time
import sys
import requests


if __name__ == '__main__':
    url = 'https://api.stackexchange.com/'
    uri = '2.3/questions'

    to_date = int(datetime.datetime.today().timestamp())
    from_date = datetime.datetime.today().date() - datetime.timedelta(days=1)
    from_date = int(time.mktime(from_date.timetuple()))
    page = 1
    count = 0
    params = {
        'fromdate': from_date,
        'todate': to_date,
        'order': 'desc',
        'sort': 'creation',
        'tagged': 'python',
        'site': 'stackoverflow',
        'pagesize': '100'
    }

    while True:
        params['page'] = page
        response = requests.get(url+uri, params=params)
        if not response.ok:
            print(f'Request error {response.status_code}: {response.reason}')
            sys.exit()

        questions = response.json()
        questions_list = questions['items']
        print(questions_list[0].keys())
        for q in questions_list:
            count += 1
            print(f"{count}."
                  f" {datetime.datetime.fromtimestamp(q['creation_date'])}:"
                  f" {q['title']}")

        if questions['has_more']:
            page += 1
        else:
            break

    print('===')
    print(f'Questions received: {count}')
