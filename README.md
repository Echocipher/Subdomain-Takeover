[![Python 3.7](https://img.shields.io/badge/python-3.7-yellow.svg)](https://www.python.org/)
# Subdomain-Takeover

**一个子域名接管检测工具**

![](https://github.com/Echocipher/Subdomain-Takeover/blob/master/pic/title.png)


## 版权 ##

author：Echocipher

mail：echocipher@163.com

blog：https://echocipher.github.io

## 关于Subdomain-Takerover

本项目是我为[OneForAll](https://github.com/shmilylty/OneForAll)准备的一个模块，为方便使用，特意提取出来单独使用，用于检测子域名接管风险，相关内容可以在[Subdomain-Takeover](https://echocipher.github.io/2019/08/14/Subdomain-takeover/)查看，目前支持以下服务检测：

> Github, Heroku, Unbounce, Tumblr, Shopify, Instapage, Desk, Campaignmonitor, Cargocollective, Statuspage, Amazonaws, Cloudfront, Bitbucket, Smartling, Acquia, Fastly, Pantheon, Zendesk, Uservoice, Ghost, Freshdesk, Pingdom, Tilda, Wordpress, Teamwork, Helpjuice, Helpscout, Cargo, Feedpress, Surge, Surveygizmo, Mashery, Intercom, Webflow, Kajabi, Thinkific, Tave, Wishpond, Aftership, Aha, Brightcove, Bigcartel, Activecompaign, Compaignmonitor, Acquia, Proposify, Simplebooklet, Getresponse, Vend, Jetbrains, Azure

并且支持以下服务自动接管：

> Github

由于恰好与个人需求重叠，便提上了日程，目前还处在开发阶段，由于是为已有框架写的一个模块，目前框架内已有并发部分，因此此处只是简单的功能函数，代码会慢慢完善，日后会与个人其他项目结合，优化期间如果您有什么好的建议或遇到了BUG，请联系我：echocipher@163.com，期待与您的交流。

## 使用说明 ##

```
git clone https://github.com/Echocipher/Subdomain-Takeover.git
cd Subdomain-Takeover/
pip install -r requirements.txt
python subdomain_takeover.py -u <target>
python subdomain_takerover.py -u <target> -c True
```
其中`-h`参数可以查看帮助，`-u`参数后面跟待检测目标，`-c`参数为自动接管功能选项，非必选选项，当它的值为True时，可以完成自动接管的操作（目前仅支持Github），**注意：默认情况下，不允许使用`-c`参数，本函数仅作为安全人员对已有授权项目完成测试工作和学习交流使用，如作他用所承受的法律责任一概与作者无关，下载使用即代表同意作者观点**

如果选择使用自动接管功能，则需要对`config.yml`进行配置：

```
tokens: 
  - name: github
    user: Github用户名
    token: Github Token值
Repo: 
  - name: my.subdomain.takerover
```

其中`user`为我们在Github注册的用户名，`token`为我们在Github上的个人访问令牌，要确保此令牌有创建存储库、引用、修改内容等权限，你可以在这里创建令牌：https://github.com/settings/tokens


## 运行截图 ##
![usage](https://github.com/Echocipher/Subdomain-Takeover/blob/master/pic/help.jpg)
![check](https://github.com/Echocipher/Subdomain-Takeover/blob/master/pic/check.jpg)
![auto_takeover](https://github.com/Echocipher/Subdomain-Takeover/blob/master/pic/takeover.jpg)

## 使用视频 ##

https://youtu.be/BXcOrS21KGs

## 开发日志 ##

- 2019/08/13 初步功能完成。
- 2019/08/14 相关知识总结完成，指纹优化。
- 2019/08/15 Github自动接管完成。
- 2019/08/16 Github自动接管，已支持全自动接管

## 待完成 ##

1. ~~指纹完善，服务商识别优化~~（2019/08/14）
2. ~~自动接管~~（2019/08/15）
3. ~~相关知识整理总结~~（2019/08/14 详情请访问[Subdomain-Takeover](https://echocipher.github.io/2019/08/14/Subdomain-takeover/)）
4. 判断逻辑完善
5. 支持多个目标检测，多进程+协程的实现
6. 全站爬虫模块的联动
7. Broken Link Hijacking
8. 域名监控服务
9. ~~视频录制~~ （2019/08/16）

## 感谢 ##

1. 感谢[SubOver](https://github.com/Ice3man543/SubOver)、[subjack](https://github.com/haccer/subjack/)提供的指纹列表，以及[OneForAll](https://github.com/shmilylty/OneForAll)项目中各位师傅的积极交流。
2. 感谢IFBBPROkyle师傅以及群主大人提供的域名。
2. 感谢我的女朋友，假如没有你的陪伴，我应该早写完了。

## 说明 ##

本项目仅进行漏洞探测工作，无漏洞利用、攻击性行为，开发初衷仅为方便安全人员对授权项目完成测试工作和学习交流使用，**请使用者遵守当地相关法律，勿用于非授权测试，如作他用所承受的法律责任一概与作者无关，下载使用即代表使用者同意上述观点**。

附《[中华人民共和国网络安全法](http://www.npc.gov.cn/npc/xinwen/2016-11/07/content_2001605.htm)》。
