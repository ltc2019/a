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
#pc_cookie = 'pgv_pvid=4350930314; ptui_loginuin=445189089@qq.com; RK=PTDE3PpOZW; ptcz=5f76a5eb1e3db5757c49ee8e4ab11dcb42b307870bfdd535e6daf113cea827f7; _ga=GA1.2.1498284914.1626146807; _tc_unionid=ef1cafde-9c24-4a8e-82c6-898602720822; tvfe_boss_uuid=fac866c1f5a65f0e; video_guid=8fdf91d03338669c; video_platform=2; pgv_info=ssid=s4111661202; idt=1627613462; _qpsvr_localtk=0.06855174740742398; main_login=qq; vqq_access_token=F865379EBC43DFD0E50516BA64A0B9C3; vqq_appid=101483052; vqq_openid=C4E6C84213C9661EF1277EE01C914DBA; vqq_vuserid=398866370; vqq_refresh_token=760AE9805DC34CB6110AA1D9B5A5C0A5; login_time_init=2021-7-30 11:30:50; _gid=GA1.2.1430440278.1627634560; vqq_vusession=-xT2lKTIptR_DjIULB0OIQ..; vqq_next_refresh_time=5998; vqq_login_time_init=1627635716; login_time_last=2021-7-30 17:2:1'
pc_cookie = 'tvfe_boss_uuid=a6b6e5308698bfb3; pgv_pvid=8943719576; video_guid=898c8dff9e4f09a4; video_platform=2; pgv_info=ssid=s7934007880; RK=VaHMjvpFf2; ptcz=2610ce91f4f6251c8c1c9422042ce789b8307635a3215a10048b2bbd208ab943; main_login=qq; vqq_access_token=122F6C98970120D9E99CD9FA55A1806F; vqq_appid=101483052; vqq_openid=C4E6C84213C9661EF1277EE01C914DBA; vqq_vuserid=398866370; vqq_vusession=NB7n7rHSLzWYDxVArJyN-w..; vqq_refresh_token=6251DFBE43AAA058B3426492B0129C09; login_time_init=2022-4-15 16:10:10; vqq_next_refresh_time=6546; vqq_login_time_init=1650010263; login_time_last=2022-4-15 16:11:7'
#app_cookie = 'vuserid=398866370; usid=; us_stamp=1627631263417; ussn=0; ctime=1627631263475; zdtime=0; vusession=8XM-6SqDRQoT1RsQVOrdsw..; video_platform=3; video_appid=1000005; vdevice_qimei36=d23c9c735d3b986ee75855f410001e714c04; video_omgid=6927eb89507d44453dd8fd4ad7b51b7a56d00010215b04; guid=195145cd361211eb89cd6c92bf48bcb2; vcuid=; vqq_appid=101795054; vqq_openid=DE3E4B7206863E4DB5D91229D69F8099; vqq_access_token=CA3F21D48376D6A7A0352669BC3849FD; vqq_vuserid=398866370; vqq_vusession=8XM-6SqDRQoT1RsQVOrdsw..; app_ver=8.4.16; main_login=qq; appuser=5E87D975BBC0E64A; o_minduid=LLkXMkII-XPC7G1mntRT8Y9zLYM-RJHz; LWVLturn=874; LMobPlaySpeedturn=702; LWPBturn=392; lv_material_group=; LWDFturn=5'
app_cookie = 'app_ver=8.5.55.25623; call_type=1; ctime=1650009676000; guid=e146c5d5a0ba11e99d19a042d48ad00a; ip=183.254.33.203; isDarkMode=0; latitude=19.991943; logitude=110.318948; main_login=qq; plat_bucketid=104; recommend_setting_code=31; recommend_switch_value=1; teenGuardSessionCode=95A71EDB9DF1C1570AF92E32C602EB524FDBFDB992EB6BA0C7C8C2BDC51B8CE1019DD8DDA0753D881FB9F7CDD806F5FDC5A6D846040C2060756169A6387BDA4153DF891B10914C9FD13E375D30A36F76BD1F481C25512180C32587FD2E428C6E0A7B9CB077172C2D26AEFA10; us_stamp=1650009634000; usid=1650009634000969; ussn=1629428465000202; vdevice_qimei36=13494a064babf17ace923ed5000012914717; video_appid=1000005; video_omgid=0e5d13105e1010401f08a4dd71167f1487ee0010114607; video_platform=5; vqq_access_token=0A6CAB2AE4F42FBB5DB491D86168A781; vqq_appid=101795054; vqq_openid=DE3E4B7206863E4DB5D91229D69F8099; vqq_vuserid=398866370; vqq_vusession=N6NCsuVHB5XoKo74335gbQ..; zdtime=1650009676421; pgv_pvid=c5df9ec10f342d60; tvfe_boss_uuid=736bb68aecaf195c'
#refresh_url = 'https://access.video.qq.com/user/auth_refresh?vappid=11059694&vsecret=fdf61a6be0aad57132bc5cdf78ac30145b6cd2c1470b0cfe&type=qq&g_tk=&g_vstk=1017072402&g_actk=644542650&callback=jQuery191013038248406855635_1640655973564&_=1640655973565'
refresh_url = 'https://access.video.qq.com/user/auth_refresh?vappid=11059694&vsecret=fdf61a6be0aad57132bc5cdf78ac30145b6cd2c1470b0cfe&type=qq&g_tk=&g_vstk=1590903146&g_actk=672521368&callback=jQuery19107048022589522371_1650010299553&_=1650010299554'
server_key = 'SCU155684Tc6f3e58f5364acbfe72c66ed604a73ba60117a0028464'
kutui_key = 'f9a1e470a613b5baf4d438c379fcd1cf'
corpid = 'wwb54eed90599056a5'
agentid = '1000002'
corpsecret = 'pX2_W3e-r7-9OdJ6YwAIPPREb7lIlrzlr8Mef9cX15k'
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