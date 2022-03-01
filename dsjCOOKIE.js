//要么自己填写，要么复制自己的boxjs会话 粘贴


module.exports = {
    "id": "dsj",
    "name": "电视家APP",
    "keys": ["dsjheader", "dsjheader2", "dsjheader3"],
    "author": "@ziye",
    "settings": [{
        "id": "dsjSuffix",
        "name": "当前账号",
        "val": "1",
        "type": "number",
        "desc": "当前抓取ck记录的账号序号，如：1、2、3、"
    }, {
        "id": "dsjCount",
        "name": "账号个数",
        "val": "3",
        "type": "number",
        "desc": "指定任务最多跑几个账号，根据抓取的账号数据个数来设值"
    }, {
        "id": "dsjXH",
        "name": "循环获取CK",
        "val": "0",
        "type": "number",
        "desc": "0关闭 1开启,默认关闭"
    }, {
        "id": "dsjXYZ",
        "name": "执行概率",
        "val": "100",
        "type": "number",
        "desc": "0不执行 可设置0-100,默认百分百"
    }, {
        "id": "dsjTXTX",
        "name": "余额提醒",
        "val": "5",
        "type": "number",
        "desc": "0不提醒 可设置0,5,10,20,25,30,50,100"
    }, {
        "id": "dsjZDTX",
        "name": "自动提现",
        "val": "99",
        "type": "number",
        "desc": "0不提现 可设置0,5,10,20,25,30,50,99  99由上到下提现 "
    }, {
        "id": "dsjnotifyttt",
        "name": "推送控制",
        "val": "1",
        "type": "number",
        "desc": "0关闭，1推送,默认12点以及23点推送"
    }, {
        "id": "dsjnotifyInterval",
        "name": "通知控制",
        "val": "2",
        "type": "number",
        "desc": "0关闭，1为 所有通知，2为 12，23 点通知，3为 6，12，18，23 点通知 "
    }, {
        "id": "dsjMinutes",
        "name": "推送-通知 分钟控制",
        "val": "59",
        "type": "number",
        "desc": "推送以及通知控制在什么分钟段，可设置0-59,默认0到10"
    }],
    "repo": "https://cdn.jsdelivr.net/gh/ziye888/JavaScript@main/Task/dsj.js",
    "icons": ["https://cdn.jsdelivr.net/gh/ziye888/JavaScript@main/Task/dsj.png", "https://cdn.jsdelivr.net/gh/ziye888/JavaScript@main/Task/dsj.png"],
    "script": "https://cdn.jsdelivr.net/gh/ziye888/JavaScript@main/Task/dsj.js",
    "icon": "https://cdn.jsdelivr.net/gh/ziye888/JavaScript@main/Task/dsj.png",
    "favIcon": "mdi-star-outline",
    "favIconColor": "grey",
    "datas": [{
    "key": "dsjheader",
    "val": "e5cca5b0df1eecad1b953eee43bac70f&TTJRM1lUazROREUxT0dZek5UYzFNVFV5TXpkbU5qaG1NRFZqWW1RMU9XTT18MTYzMTc1MzAzNTA4OTE3NDk4MnxlYmE4Nzg0NDhmYzhjNzNlNTVjM2RhMzk1NTJmYjc3NjFkZGQ2NTJi"
  }, {
    "key": "dsjheader2",
    "val": "eea6ca5e3e2ff91b9a11e554107c0a5b&WXpsbU1ERmxOR1F5WkdFM1lUUmxaV1ZoTWpKbVpEUmlNREkzTXpWak1ERT18MTYzNTM1Njc5Nzk2MDMwNjEzN3w0MjgwOTg4MTE5MGYyNGE4MDdkZDUyMjMzZDNkYzgxNWE3MTU5YjI2"
  }, {
    "key": "dsjheader3",
    "val": "ca7a5270634546aa349f42a0ed0b4728&TlRrM05EbGhNakV3TnpnellUY3laalJoT0RBeU1UTXdOak5qTlRrME1EQT18MTYzMzEwNTAzODIzNDEzNDYwN3xhMzY4MzIzMjhjYjZkYWE3MjVmOTlmZWU0ZjQ3MWI5OWU1ZWE4M2Iz"
  }, {
    "key": "dsjheader4",
    "val": "4fd14d6289c7135d20ea0dbbf696430e&T1dJMlpqZ3daamszTXpFMFlXTmpZbVZsTjJFMk1EVTRZekptTlRCbFl6VT18MTYzNTQwMTk5NDg2NTcyNjE1N3w5YTgzODY3YjI3YTk5ZDM5N2NkMzJmMjFkNGNmMTkwMjhhNzI2OThl"
  }, {
    "key": "dsjheader5",
    "val": "e65693338e104458aaae82fd4467e58a&T1RaalpUTTNOakprWWpVek5UQmtNekF6TVdKaFpHVmhObUprTkRkbE5EUT18MTYzNTQyNzkwMzYyOTM5OTY0NHw3OWViZTg5MjVmYWU3YWQwMzBjNDhjODBlYTA5NzU0ZjY5MjRjN2Uw"
  }],
  "sessions": [],
  "isLoaded": true
  }
  
