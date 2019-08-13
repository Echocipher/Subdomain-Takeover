import json
import requests
import dns.resolver
import sys,getopt

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
        opts,args = getopt.getopt(argv,'hu:')
    except:
        print('[*]Usage:python subdomain_takeover.py -u <target>')
        sys.exit(2)
    for opt,arg in opts:
        if opt == '-h':
            print('[*]Usage:python subdomain_takeover.py -u <target>')
            sys.exit()
        elif opt == '-u':
            subdomain = arg
            cname = cname_get(subdomain)
            sub_check(cname,subdomain)

if __name__ == '__main__':
    main(sys.argv[1:])
