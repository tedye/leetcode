import requests, re, os
from bs4 import BeautifulSoup

class leetcode_submission_crawler(object):
    '''
    leetcode_submission_crawler will try to login with credentials provided and then
    scan througth all items in the problem list table, finally download all accepted
    solutions in submission pages.
    '''
    def __init__(self, login_url, username, password, headers, cookies, data):
        print('LeetCode Submission Clawer Initialization...\n')
        self.login_url = login_url
        self.username = username
        self.password = password
        self.headers = headers
        self.cookies = cookies
        self.data = data
        self.session = requests.session()
        self.problem_url_list = []
        print('Initialization Done!\n')

        print('Trying to login...\n')
        if self.log_in():
            print('Login Succuess!\n')

            print('Try to read algorithm problem list...\n')
            if self.get_leetcode_algorithm_url():
                print('Problem list url collection. Done!\n')
            else:
                print('Failed to collect problem list urls.\n')
        else:
            print('Login Failed!\n')

    def log_in(self):
        response = self.session.post(self.login_url, data = self.data, headers = self.headers, cookies = self.cookies)
        # print(response.text)
        if 'Sign out' in str(response.text):
            return True
        return False

    def get_leetcode_algorithm_url(self):
        response = self.session.get('https://leetcode.com/problemset/algorithms/')
        response.encode = 'utf-8'
        soup = BeautifulSoup(response.text)
        problem_list = soup.findAll('table',{'id': 'problemList'})
        tb = problem_list[0].find('tbody')
        url_prefix = 'https://leetcode.com'
        trs = tb.findAll('tr')
        for row in trs:
            tds = row.findAll('td')
            print('found', tds[1].text.strip(), tds[2].text.strip())
            self.problem_url_list += [tds[1].text.strip(), tds[2].text.strip(), url_prefix + tds[2].find('a')['href']],
        if self.problem_url_list:
            return True
        else:
            return False

    def file_writer(self, file_name, text_str):
        with open(file_name,'w') as f:
            f.write(text_str)
    

    def get_leetcode_submission_records(self, languange = 'python'):
        if not self.problem_url_list:
            print('no url list exist!\n')
        for number, name, url in self.problem_url_list:
            if len(number) == 1:
                countNumber = '00'+number
            elif len(number) == 2:
                countNumber = '0'+number
            else:
                countNumber = number
            print('access problem '+countNumber+' '+name)
            submission_url = url + 'submissions/'
            response = self.session.get(submission_url)
            response.encoding = 'utf-8'
            tbs = BeautifulSoup(response.text).findAll('table')
            if not tbs:
                print('no sumission history for '+ name)
                continue

            print('open submission history...\n')
            sumission_history = tbs[0].findAll('tbody')[0]
            for i, row in enumerate(sumission_history.findAll('tr')):
                entry = row.findAll('td')[2].find('a')
                accept_status = entry.find('strong').text
                href = entry['href']
                if accept_status != 'Accepted':
                    continue
                solution_url = 'https://leetcode.com/' + href
                solution_response = self.session.get(solution_url)
                # print(solution_response.text)
                solution_response.encoding = 'utf-8'
                directory = 'leetcode.' + countNumber+'.'+name
                if not os.path.exists(directory):
                    os.makedirs(directory)

                print('accepted solution found...('+str(i)+')')
                solution_html = BeautifulSoup(solution_response.text)
                script = str(solution_html.findAll('script')[-5].text)
                for line in script.split('\n'):
                    target = 'vm.code.'+languange
                    if target in line:
                        text_str = eval(line[len(target)+7:-1])
                        # print(text_str)
                        file_name = directory+'/leetcode.' + countNumber+'.'+name+'.submission'+str(i)+'.py'
                        print('writing file to ./'+file_name)
                        self.file_writer(file_name, text_str)
                        break

if __name__ == '__main__':
    #----------------------------------------------------------------------------------------------#
    login_url = 'https://leetcode.com/accounts/login/'
    username = 'your_username'
    password = 'your_password'
    # for headers, cookies and data, you should also use your own.
    # to get these, please follow the steps in my blog:
    # http://yefangliang.com/?p=5931
    #----------------------------------------------------------------------------------------------#
    headers = {
        'Referer': "https://leetcode.com/accounts/login/",
        'Content-Type': 'application/x-www-form-urlencoded',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; LCJB; rv:11.0) like Gecko',
        'Host': 'leetcode.com'
    }

    cookies = {
        '__atuvc': '0%7C17%2C0%7C18%2C0%7C19%2C0%7C20%2C1%7C21',
        '_gat': '1',
        'csrftoken': 'xr9BWUq5xVtgec4HOWfPE3sr1PzXMU7X',
        '_ga': 'GA1.2.1699599603.1427126517'
    }

    data = dict(
        login=username, 
        password=password,
        csrfmiddlewaretoken='xr9BWUq5xVtgec4HOWfPE3sr1PzXMU7X')
    #----------------------------------------------------------------------------------------------#
    test_clawer = leetcode_submission_crawler(login_url, username, password, headers, cookies, data)
    test_clawer.get_leetcode_submission_records(languange='python')

