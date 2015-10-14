import requests
def get_login_requests(login_url, user_id, password):
    s = requests.session()
    data = dict(login=user_id, password=password,
                csrfmiddlewaretoken='xr9BWUq5xVtgec4HOWfPE3sr1PzXMU7X')
    cookies = {
        '__atuvc': '0%7C17%2C0%7C18%2C0%7C19%2C0%7C20%2C1%7C21',
        '_gat': '1',
        'csrftoken': 'xr9BWUq5xVtgec4HOWfPE3sr1PzXMU7X',
        '_ga': 'GA1.2.1699599603.1427126517'
    }
    headers = {
        'Referer': "https://leetcode.com/accounts/login/",
        'Content-Type': 'application/x-www-form-urlencoded',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; LCJB; rv:11.0) like Gecko',
        'Host': 'leetcode.com'
    }
    respose = s.post(login_url, data=data, headers=headers,
               cookies=cookies)
    print(respose.headers)
    print(respose.text)


if __name__ == '__main__':
    login_url = 'https://leetcode.com/accounts/login/'
    r = requests.get(login_url)
    cookies = r.cookies['csrftoken']
    print(r.cookies['csrftoken'])
    get_login_requests(login_url, input('username>'),input('password>') )
    print('Login Succeeded!')