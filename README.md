[![Python 3.7](https://img.shields.io/badge/python-3.7-yellow.svg)](https://www.python.org/)
# Subdomain-Takeover

**一个子域名接管检测工具**

![](https://github.com/Echocipher/Subdomain-Takeover/blob/master/pic/title.png)


## 版权 ##

author：Echocipher

mail：echocipher@163.com

blog：https://echocipher.github.io

## 关于Subdomain-Takerover

本项目是我为[OneForAll](https://github.com/shmilylty/OneForAll)准备的一个模块，为方便使用，特意提取出来可以单独使用，，用于检测子域名接管风险，相关内容可以在我的博客中查看（待完成），目前支持以下服务检测：

> Github, Heroku, Unbounce, Tumblr, Shopify, Instapage, Desk, Campaignmonitor, Cargocollective, Statuspage, Amazonaws, Cloudfront, Bitbucket, Smartling, Acquia, Fastly, Pantheon, Zendesk, Uservoice, Ghost, Freshdesk, Pingdom, Tilda, Wordpress, Teamwork, Helpjuice, Helpscout, Cargo, Feedpress, Surge, Surveygizmo, Mashery, Intercom, Webflow, Kajabi, Thinkific, Tave, Wishpond, Aftership, Aha, Brightcove, Bigcartel, Activecompaign, Compaignmonitor, Acquia, Proposify, Simplebooklet, Getresponse, Vend, Jetbrains, Azure

由于恰好与个人需求重叠，便提上了日程，目前还处在开发阶段，由于是为已有框架写的一个模块，目前框架内已有并发部分，因此此处只是简单的功能函数，代码会慢慢完善，日后会与个人其他项目结合，优化期间如果您有什么好的建议或遇到了BUG，请联系我：echocipher@163.com，期待与您的交流。

## 使用说明 ##

```
git clone https://github.com/Echocipher/Subdomain-Takeover.git
cd Subdomain-Takeover/
pip install -r requirements.txt
python subdomain_takeover.py -u <target>
```

![usage](https://github.com/Echocipher/Subdomain-Takeover/blob/master/pic/usage.png)

## 开发日志 ##

- 2019/08/13 初步功能完成。
- 2019/08/14 相关知识总结完成。

## 待完成 ##

1. 指纹完善，服务商识别优化
2. 自动接管
3. ~~相关知识整理总结~~（2019/08/14 详情请访问[Subdomain-Takeover](https://echocipher.github.io/2019/08/14/Subdomain-takeover/)）
4. 判断逻辑完善
5. 支持多个目标检测，多进程+协程的实现
6. 全站爬虫模块的联动
7. Broken Link Hijacking
8. 域名监控服务

## 感谢 ##

1. 感谢[SubOver](https://github.com/Ice3man543/SubOver)提供的指纹列表，以及[OneForAll](https://github.com/shmilylty/OneForAll)项目中各位师傅的积极交流。
2. 感谢IFBBPROkyle师傅提供的域名。
2. 感谢我的女朋友，假如没有你的陪伴，我应该早写完了。

## 说明 ##

本项目仅进行漏洞探测工作，无漏洞利用、攻击性行为，开发初衷仅为方便安全人员对授权项目完成测试工作和学习交流使用，**请使用者遵守当地相关法律，勿用于非授权测试，如作他用所承受的法律责任一概与作者无关，下载使用即代表使用者同意上述观点**。

附《[中华人民共和国网络安全法](http://www.npc.gov.cn/npc/xinwen/2016-11/07/content_2001605.htm)》。
