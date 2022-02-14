# !/usr/bin/env python
# coding=utf-8
import requests
import time
import json
import sys
import pytz
import datetime
import re
import random
from io import StringIO

# Python版本 3.6, 该脚本仅供分享交流和学习, 不允许用于任何非法途径, 否则后果自负, 作者对此不承担任何责任
# 20210812魔改，仅保留网页签到功能，精简消息
# 20210124更新: 添加WPS小程序会员群集结功能 (如需仅执行群集结功能, 请将执行方法由'index.main_handler'更改为'index.wps_massing' ); 添加并优化企业微信推送功能; 优化推送逻辑
# 请依次修改 25-32行中的需要修改的部分内容以实现推送功能
# 请依次修改 36-37, 42, 44, 46行中的需要修改的部分内容以实现签到功能
# 邀请用户签到可以额外获得会员, 每日可邀请最多10个用户, 已预置了12个小号用于接受邀请和会员群集结功能, 49-72行invite_sid信息可选删改
# 如群集结失败,请在相应49-72行处修改或相应位置前后增加invite_sid信息, 修改时注意逗号及保留双引号

# 参考以下代码解决https访问警告
# from requests.packages.urllib3.exceptions import InsecureRequestWarning,InsecurePlatformWarning
# requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
# requests.packages.urllib3.disable_warnings(InsecurePlatformWarning)

# 初始化信息
pusher = 1 # SERVER酱填1, 企业微信推送填2(推荐使用)
SCKEY = ''
corpid = ''
agentid = ''
corpsecret = ''
pushusr = '@all' # 企业微信推送用户,默认'@all'为应用全体用户
img_url = 'https://s3.ax1x.com/2021/01/23/s7GOTP.png' # 微信图文消息提醒图片地址
wxpusher_type = 1 # 企业微信推送文本消息填1, 图文消息填2(推荐选择)


summary_msg=1    #是否提示积分信息，1 提示，否则不提示
info_msg=1       #是否提示会员信息，1 提示，否则不提示
data = {
    "wps_checkin": [

        #多账号，有几个账号复制几行
        #{"name": "账号1","sid": ""},
        #{"name": "账号2","sid": ""},
        #{"name": "账号3","sid": ""},
{"name": "1","sid": "V02SqTXMAobjqKwUIQ"},
{"name": "2","sid": "V02SqTXMAobjqKwUIQ"},
{"name": "3","sid": "V02SqTXMAobjqKwUIQ"},
{"name": "4","sid": "V02SqTXMAobjqKwUIQ"},
{"name": "5","sid": "V02SqTXMAobjqKwUIQ"},


    ]
}



# 初始化日志
sio = StringIO('WPS签到日志\n')
sio.seek(0, 2)  # 将读写位置移动到结尾
dio = StringIO('')
#dio.seek(0, 2)
s = requests.session()
tz = pytz.timezone('Asia/Shanghai')
nowtime = datetime.datetime.now(tz).strftime("%Y-%m-%d %H:%M:%S")
sio.write("--- "+nowtime+" ---")

# 微信推送
def pushWechat(desp,nowtime):
    ssckey = SCKEY
    send_url='https://sc.ftqq.com/' + ssckey + '.send'
    if '失败' in desp :
        params = {
            'text': 'WPS签到提醒' + nowtime,
            'desp': desp
            }
    else:
        params = {
            'text': 'WPS签到提醒' + nowtime,
            'desp': desp
            }
    requests.post(send_url,params=params)

class WXPusher:
    def __init__(self, usr=None, digest=None, desp=None):
        self.base_url = 'https://qyapi.weixin.qq.com/cgi-bin/gettoken?'
        self.req_url = 'https://qyapi.weixin.qq.com/cgi-bin/message/send?access_token='
        self.media_url = 'https://qyapi.weixin.qq.com/cgi-bin/media/upload?access_token={access_token}&type=file'
        self.corpid = corpid     # 填写企业ID
        self.corpsecret = corpsecret     # 应用Secret
        self.agentid = int(agentid)          # 填写应用ID，是个整型常数,就是应用AgentId
        if usr is None:
            usr = '@all'
        self.usr = usr
        if '失败' in desp:
            self.title = 'WPS签到提醒'
        else:
            self.title = 'WPS签到提醒'
        self.msg = desp
        self.digest = digest
        content = self.msg
        content = content.replace('\n          ---', '\n<code>          ---')
        content = content.replace('---↓\n', '---↓</code>\n')
        self.content = '<pre>' + content + '</pre>'  # content.replace('\n','<br/>')

    def get_access_token(self):
        urls = self.base_url + 'corpid=' + self.corpid + '&corpsecret=' + self.corpsecret
        resp = requests.get(urls).json()
        access_token = resp['access_token']
        return access_token

    # 上传临时素材,返回素材id
    def get_ShortTimeMedia(self):
        url = self.media_url
        ask_url = url.format(access_token=self.get_access_token())
        f = requests.get(img_url).content
        r = requests.post(ask_url, files={'file': f}, json=True)
        return json.loads(r.text)['media_id']

    def send_message(self):
        data = self.get_message()
        req_urls = self.req_url + self.get_access_token()
        res = requests.post(url=req_urls, data=data)
        print(res.text)

    def get_message(self):
        if wxpusher_type == 1:
            data = {
                "touser": self.usr,
                "toparty": "@all",
                "totag": "@all",
                "msgtype": "text",
                "agentid": self.agentid,
                "text": {
                    "content": self.msg
                },
                "safe": 0,
                "enable_id_trans": 0,
                "enable_duplicate_check": 0,
                "duplicate_check_interval": 1800
            }
        elif wxpusher_type == 2:

            data = {
                "touser": self.usr,
                "toparty": "@all",
                "totag": "@all",
                "msgtype": "mpnews",
                "agentid": self.agentid,
                "mpnews": {
                    "articles": [
                        {
                            "title": self.title,
                            "thumb_media_id": self.get_ShortTimeMedia(),  # 填写图片media_id
                            "author": "WPS推送助手",
                            "content_source_url": "",
                            "content": self.content,
                            "digest": self.digest
                        }
                    ]
                },
                "safe": 0,
                "enable_id_trans": 0,
                "enable_duplicate_check": 0,
                "duplicate_check_interval": 1800
            }
        data = json.dumps(data)
        return data


# wps网页签到
def wps_webpage_clockin(sid: str):
    sio.write("wps网页签到：")
    if len(sid) == 0:
        sio.write("签到失败: 用户sid为空, 请重新输入\n")
        return 0
    elif "*" in sid or sid[0] != "V":
        sio.write("签到失败: 用户sid错误, 请重新输入\n")
        return 0

    url = "https://vip.wps.cn/sign/v2"
    headers = {
        "Cookie": "wps_sid=" + sid,
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2486.0 Safari/537.36 Edge/13.10586"
    }
    data = {
        "platform": "8",
        "captcha_pos": "137.00431974731889, 36.00431593261568",
        "img_witdh": "275.164",
        "img_height": "69.184"
    }  # 带验证坐标的请求
    data0 = {"platform": "8"}  # 不带验证坐标的请求
    yz_url = "https://vip.wps.cn/checkcode/signin/captcha.png?platform=8&encode=0&img_witdh=275.164&img_height=69.184"

    req = requests.post(url=url, headers=headers, data=data)
    #print(req.text)
    if not ("msg" in req.text):
        # 判断wps_sid是否失效
        sio.write("wps_sid无效\n")
        return 0
    else:
        sus = json.loads(req.text)["result"]  # 第一次：不带验证码的请求结果
        #sio.write("免验证签到-->" + sus + '\n')  # 判断第一次请求
        if sus == "error":
            if json.loads(req.text)["msg"] == "10003":
                sio.write('今日已签到\n')
                return 2
            for n in range(50):
                requests.get(url=yz_url, headers=headers)
                req = requests.post(url=url, headers=headers, data=data)
                sus = json.loads(req.text)["result"]
                #sio.write(str(n + 1) + "尝试验证签到-->" + sus + "\n")
                time.sleep(random.randint(0, 5)/10)
                if sus == "ok":
                    break
        if sus == "error":
            sio.write('失败，验证未通过！\n')
        else:
            sio.write('成功！\n')
        return 1


# 主函数
def main():
    # sio.write("\n            ===模拟WPS签到===")
    sid = data['wps_checkin']

    for item in sid:

        sio.write("\n\n---为 {} 签到---↓\n".format(item['name']))
        dio.write("{}签到摘要↓\n".format(item['name']))

        b0 = wps_webpage_clockin(item['sid'])
        if b0 == 1:
            # 获取当前网页签到信息
            dio.write("wps网页签到成功\n")
        elif b0 == 2:
            dio.write("今日已签到\n")
        else:
            dio.write("wps网页签到失败\n")
            desp = sio.getvalue()
            digest = dio.getvalue()
            if digest[-2:] == '\n\n':
                digest = digest[0:-2]


        # 获取当前用户信息
        if summary_msg==1:
            sio.write('当前用户信息：')
            summary_url = 'https://vip.wps.cn/2019/user/summary'
            r = s.post(summary_url, headers={'sid': item['sid']})
            resp = json.loads(r.text)
            sio.write('会员积分:{}，稻米数量:{}\n'.format(resp['data']['integral'], resp['data']['wealth']))
        if info_msg==1:
            userinfo_url = 'https://vip.wps.cn/userinfo'
            r = s.get(userinfo_url, headers={'sid': item['sid']})
            resp = json.loads(r.text)
            if len(resp['data']['vip']['enabled']) > 0:
                sio.write('会员信息：\n')
                for i in range(len(resp['data']['vip']['enabled'])):
                    sio.write('{}, 过期时间:{}\n'.format(resp['data']['vip']['enabled'][i]['name'], datetime.datetime.fromtimestamp(
                        resp['data']['vip']['enabled'][i]['expire_time']).strftime("%Y-%m-%d")))
                    dio.write('{}, 过期时间:{}\n'.format(resp['data']['vip']['enabled'][i]['name'],
                                                            datetime.datetime.fromtimestamp(resp['data']['vip']['enabled'][i]['expire_time']).strftime("%Y/%m/%d")))

    desp = sio.getvalue()
    digest = dio.getvalue()
    if digest[-2:] == '\n\n':
        digest = digest[0:-2]
    if pusher == 1:
        pushWechat(desp, nowtime)
    elif pusher == 2:
        desp = desp.replace('\n\n', '\n')
        digest = digest.replace('\n\n', '\n')
        push = WXPusher(pushusr, digest, desp)
        push.send_message()
    print(desp)
    return desp


def main_handler(event, context):
    return main()


if __name__ == '__main__':
    main()
