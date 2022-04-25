#腾讯视频双签
#server_key 为server 密钥，kutui_key 为酷推密钥
#添加参数移动到138--142行，抓取pc_cookie和refresh_url参数方法：
#电脑登陆--- F12 --- network --- 过滤关键字auth_refresh --- 复制完整auth_refresh链接和COOKIE分别填入参数
#app_cookie参数自行手机抓包抓取cookie
import time
import json
import requests

'''
参数
'''
#pushType：0Service酱推送；pushType：1酷推推送；pushType：2企业微信推送
pushType = 1
pc_cookie = ''
app_cookie = ''
refresh_url = ''
server_key = ''
kutui_key = ''
corpid = ''
agentid = ''
corpsecret = ''
pushusr = '@all' # 企业微信推送用户,默认'@all'为应用全体用户

def refresh_cookie(params):
    """
    cookies处理并转为字典
    :param params: auth_refresh?后字符串
    :param cookie: cookies字符串
    :return: 返回元组形式，(params, cookie)
    """
    #params_dict = dict([p.split("=", 1) for p in params.split("&")])
    app_ck = []
    a = params['app'].split(";")
    for item in a:
        if item not in '':
            app_ck.append(item.split("=",1))
    app_auth = 'vqq_vusession' if params['app'].find('vqq_vusession') >= 0 else ('vusession' if params['app'].find('vusession') >= 0 else '')
    pc_auth = 'vqq_vusession' if params['pc'].find('vqq_vusession') >= 0 else ('vusession' if params['pc'].find('vusession') >= 0 else '')
    print('app端验证字段：'+app_auth)
    print('网页端验证字段：'+pc_auth)
    ck_params = {'ckdict':dict(app_ck),'a_auth': app_auth,'p_auth':pc_auth}
    params.update(ck_params)
    res = get_cookie(params)
    return res

# 刷新cookie
def get_cookie(params):
    try:
        res = ''
        refresh_url = params['url']
        ckparams = {
            "Referer":"https://v.qq.com",
            "Cookie": params['pc']
        }
        response = requests.get(refresh_url, headers=ckparams)
        #获取新的cookie
        cookie = requests.utils.dict_from_cookiejar(response.cookies)
        params['ckdict'][params['a_auth']] = cookie[params['p_auth']]
        for key in params['ckdict']:
            res += key +"=" + params['ckdict'][key] + ";"
        #print("新的cookie：\n"+res)
        return res
    except Exception as e:
        print('刷新vqq_vusession失败，异常代码：'+'\n'+str(e))
        res += '\nPC端COOKIE失效'
        return res
# 一次签到
def one_sign(ck):
    try:
        msg = ''
        onesign_url = 'https://vip.video.qq.com/fcgi-bin/comm_cgi?name=hierarchical_task_system&cmd=2'
        params = {
            'Cookie': ck
        }
        res = requests.get(onesign_url, headers=params).text
        jsondata=res.replace("QZOutputJson=(","").replace(");","")
        jsonlload=json.loads(str(jsondata))
        #一次签到判断
        if 'Account Verify Error' in res:
            print('一签失败，COOKIE失效')
            msg += '\n一签失败，COOKIE失效 '
        elif jsonlload["checkin_score"] == 0:
            print('无需重复一次签到')
            msg += '\r重复的一次签到'
        else:
            print('一次签到完成,获得V值 '+str(jsonlload["checkin_score"]))
            msg += '\n一签成功[获得V值 '+ str(jsonlload["checkin_score"])+']'
    except Exception as e:
        print('一签失败，异常代码：'+'\n'+str(e))
        msg += '\n一签失败，异常代码：'+'\n'+str(e)
    return msg

# 二次签到
def second_sign(ck):
    try:
        msg = ''
        secend_sign_score = []
        secendsign_url = 'http://v.qq.com/x/bu/mobile_checkin'
        params = {
            "Cookie": ck
        }
        res = requests.get(secendsign_url, headers=params)

        #V值查询
        score_info = requests.get('https://vip.video.qq.com/fcgi-bin/comm_cgi?name=get_score_flow&score_type=1&size=6&index=0',headers=params).text
        score_info_data = score_info.replace("QZOutputJson=(","").replace(");","")
        score_info_jsonlload = json.loads(str(score_info_data))
        #print('访问结果：'+ str(len(score_info_jsonlload.get('score_flow'))))
        for i in range(0,len(score_info_jsonlload.get('score_flow'))-1):
            if 'si106197' in score_info_jsonlload.get('score_flow')[i]['bill_no']:
                secend_sign_score.append(score_info_jsonlload.get('score_flow')[i]['score'])

        #print(res.text)
        if 'Unauthorized' in res:
            print ('二签失败，COOKIE失效')
            msg += '\n二签失败，COOKIE失效 '
        else:
            msg += '\n二签成功[获得V值 '+str(secend_sign_score[0])+']'
            print ('二次签到完成,获得V值 '+str(secend_sign_score[0]))
    except Exception as e:
        print('二签失败，异常代码：'+'\n'+str(e))
        msg += '\n二签失败，异常代码：'+'\n'+str(e)
    return msg

# 微信推送
def pushWechat(key,desp):
    try:
        send_url='https://sc.ftqq.com/' + key + '.send'
        params = {
            'text': '腾讯视频签到' ,
            'desp': desp
        }
        requests.post(send_url,params=params)
    except Exception as e:
        print('server酱通知失败，异常代码：'+'\n'+str(e))

# 酷推推送
def pushKuchat(key,desp):
    try:
        send_url='https://push.xuthus.cc/ww/' + key + '?'
        params = {
            'c': '【腾讯视频签到】' + desp
        }
        requests.post(send_url,params=params)
    except Exception as e:
        print('酷推通知失败，异常代码：'+'\n'+str(e))

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
            self.title = '腾讯视频签到提醒'
        else:
            self.title = '腾讯视频签到提醒'
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
        
# 主函数
def main():
    '''
    执行签到
    '''
    params = {'pc':pc_cookie,'app':app_cookie,'url':refresh_url}
    ck = refresh_cookie(params)
    msg1 = one_sign(ck)
    msg2 = second_sign(ck)
    msg = msg1+msg2
    if pushType==1:
        pushKuchat(kutui_key,msg)
    elif pushType==0:
        pushWechat(server_key,msg)

def main_handler(event, context):
    return main()

if __name__ == '__main__':
    main()