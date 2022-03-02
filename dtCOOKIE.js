module.exports = {
    "id": "dt",
    "name": "读特",
    "keys": ["dturl","dturl2","dturl3","dturl4","dturl5"],
    "author": "@tom",
    "settings": [{
      "id": "dtSuffix",
      "name": "当前账号",
      "val": "1",
      "type": "number",
      "desc": "当前抓取ck记录的账号序号，如：1、2、3、4"
    }, {
      "id": "dtCount",
      "name": "账号个数",
      "val": "3",
      "type": "number",
      "desc": "3"
    }, {
      "id": "dtXH",
      "name": "循环获取ck",
      "val": "0",
      "type": "number",
      "desc": "0关闭，1打开，默认关闭"
    }, {
      "id": "dtTXTX",
      "name": "txtx",
      "val": "0",
      "type": "number",
      "desc": "0关闭，1打开，默认关闭"
    }, {
      "id": "dtSC",
      "name": "sc",
      "val": "0",
      "type": "number",
      "desc": "0关闭，1打开，默认关闭"
    }, {
      "id": "dtnotifyttt",
      "name": "推送控制",
      "val": "1",
      "type": "number",
      "desc": "0关闭，1推送,默认12点以及23点推送"
    }, {
      "id": "dtnotifyInterval",
      "name": "通知控制",
      "val": "2",
      "type": "number",
      "desc": "0关闭，1为 所有通知，2为 12，23 点通知，3为 6，12，18，23 点通知"
    }, {
      "id": "dtMinutes",
      "name": "推送-通知 分钟控制",
      "val": "10",
      "type": "number",
      "desc": "推送以及通知控制在什么分钟段，可设置0-59,默认0到10"
    }],
    "repo": "https://raw.githubusercontent.com/xl2101200/-/main/dt.js",
    "icons": ["https://raw.githubusercontent.com/xl2101200/-/main/tom/tom.jpg", "https://raw.githubusercontent.com/xl2101200/-/main/tom/tom.jpg"],
    "script": "https://raw.githubusercontent.com/xl2101200/-/main/dt.js",
    "icon": "https://raw.githubusercontent.com/xl2101200/-/main/tom/tom.jpg",
    "favIcon": "mdi-star-outline",
    "favIconColor": "grey",
    "datas": [{
      "key": "dturl",
      "val": "https://plus.dutenews.com/api/v2/auth/logindute?app_version=6.3.1&clientid=1&device_id=6C0D10E6-B79E-43D1-85CB-9F22D179AB8B&device_model=iPhone&device_version=iPhone&ip=192.168.123.4&memberid=760819&mobile=15108968441&nickname=Li&sign=67426ad504346fb3171fd4d688ec120b&siteid=10001&system_name=iOS&system_version=14.1&thumb=https%3A//thirdwx.qlogo.cn/mmopen/vi_32/xU7Pickem2iaTiaeuKicl5vheMOiajY7iaREgplxn0dMic3a7uV1yiacxDQREvaSytB7WKLeBpDxMgQoic1GXYic7zibuZEaA/132&time=1633967082000&type=ios"
    }, {
      "key": "dturl2",
      "val": "https://plus.dutenews.com/api/v2/auth/logindute?app_version=6.3.1&clientid=1&device_id=6C0D10E6-B79E-43D1-85CB-9F22D179AB8B&device_model=iPhone&device_version=iPhone&ip=192.168.123.4&memberid=760839&mobile=19907679180&nickname=199%2A%2A%2A180&sign=f6a9460f97a1f08b4cd8307ac85a3f72&siteid=10001&system_name=iOS&system_version=14.1&time=1633970362000&type=ios"
    }, {
      "key": "dturl3",
      "val": "https://plus.dutenews.com/api/v2/auth/logindute?app_version=6.3.1&clientid=1&device_id=6C0D10E6-B79E-43D1-85CB-9F22D179AB8B&device_model=iPhone&device_version=iPhone&ip=192.168.123.4&memberid=760822&mobile=17330828408&nickname=173%2A%2A%2A408&sign=8f6d2183bf336900e2b75651cfa45e54&siteid=10001&system_name=iOS&system_version=14.1&time=1633970581000&type=ios"
    }, {
      "key": "dturl4",
      "val": ""
    }, {
      "key": "dturl5",
      "val": ""
    }],
    "sessions": [],
    "isLoaded": true
  }
  
