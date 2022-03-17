// [rule: 315]


// 百度315速报
const request = require('request');

const options = {
    url: 'https://www.baidu.com/s?ie=utf-8&f=8&rsv_bp=1&tn=baidu&wd=315&oq=%25E5%25A4%25AE%25E8%25A7%2586&rsv_pq=87dcc52b004bfb4c&rsv_t=947aNVRWF43EksSeDQ%2FD20D86bsgm%2BpbTo5TTQIqTnN%2FP7M0VKd%2F1aX5xyw&rqlang=cn&rsv_enter=1&rsv_dl=tb&rsv_btype=t&inputT=574&rsv_sug3=10&rsv_sug1=8&rsv_sug7=100&rsv_sug2=0&rsv_sug4=574',
    method: 'get',
    headers: {
        cookie: 'BDUSS=FxdE43NnU0cUlzNVdzSGxveHNyTUNMTzJGT0NsQ3BJN1ZJOTBuYTNZOEtyfnBmSVFBQUFBJCQAAAAAAAAAAAEAAAAvKy8VxP3EvtPqAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAoi018KItNfUn; BDUSS_BFESS=FxdE43NnU0cUlzNVdzSGxveHNyTUNMTzJGT0NsQ3BJN1ZJOTBuYTNZOEtyfnBmSVFBQUFBJCQAAAAAAAAAAAEAAAAvKy8VxP3EvtPqAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAoi018KItNfUn; BIDUPSID=910D47C0003CB7F226EF06BF8C87AB98; PSTM=1609426059; __yjs_duid=1_b4045a55f4f25b210e28c026af4082681621657186645; BD_UPN=12314753; BAIDUID=B9DCC7A8DF84E4296E311F3BB83E06ED:FG=1; BAIDUID_BFESS=B9DCC7A8DF84E4296E311F3BB83E06ED:FG=1; channel=baidusearch; COOKIE_SESSION=62731_0_4_4_15_2_1_0_4_2_0_1_62854_0_124_0_1647394115_0_1647393991|9#0_0_1647413668|1|1; BD_HOME=1; delPer=0; BD_CK_SAM=1; PSINO=5; sug=3; sugstore=0; ORIGIN=0; bdime=21110; RT="z=1&dm=baidu.com&si=4amupax36ve&ss=l0uclpda&sl=2&tt=25p&bcn=https://fclog.baidu.com/log/weirwood?type=perf&ld=2jh"; H_PS_PSSID=35839_35970_35104_31254_34813_34584_35802_35315_26350_36112_35878_36061; H_PS_645EC=81f6J7/ru+O80WUP5YWF0t6FiKAeQCupnWCk3Ip99XKXH7eA/hwJeOZCnhQ; BA_HECTOR=250h0k01a52l8la4291h355u00q; baikeVisitId=e0dab26c-3af6-4799-8bff-3c7fb9c80e26; BDSVRTM=20',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36',
    }
}

const nodeList = [];

request(options, (error, response)=>{
    if (error) {
        sendText('查找错误，请使用浏览器确实搜索结果');
    }else{
        let body = response.body;
        body = body.replace(/\n/g, '');
        body = body.replace(/\r/g, '');

        let data = body.match(/{"title":"晚会曝光名单",(.*?)<div/)[1];

        let nodeDesc = data.match(/"nodeDesc":"(.*?)"/g);
        let nodeName = data.match(/"nodeName":"(.*?)"/g);
        let nodeUrl = data.match(/"nodeUrl":"(.*?)"/g);
        nodeDesc.forEach((val,index) => {
            let item = 'No.' + index + ' ' + nodeName[index].match(/"nodeName":"(.*?)"/)[1] + '\n' + val.match(/"nodeDesc":"(.*?)"/)[1] + '\n' + nodeUrl[index].match(/"nodeUrl":"(.*?)"/)[1];
            nodeList.push(item);
        });
        sendText(nodeList.join('\n'));
    }
})

