先打开下面的链接进入京东待评价商品页面
https://club.jd.com/myJdcomments/myJdcomments.action?sort=0

用Chrome等相同内核浏览器打开上面的链接后按F12键，选择console，复制粘贴以下代码，content 里的内容自由替换，先运行脚本1，再运行脚本2
脚本1
京东自动评价脚本1：一键批量评价-不能晒单，追加图片
var content = '老板好，老板娘也好，最重要的是质量很好，包装严实，材质很好，质量也不错，到货也很快物流满分，包装快递满分，配送员态度满分，好评、好评、好评，重要的话说三遍，不是为了凑字数，确实没有凑字数，字数够了吧？'; 
function a(){
var close=document.getElementsByClassName('btn-9 fail-close');
if(close.length>0){close[0].click()}
var assess=document.getElementsByClassName('btn-9')[0];
if(assess!=null){for(var i=0;i<2;i++){
assess.click();
var area=document.getElementsByClassName('area area01')[0];
area.value=content;area.setAttribute('id','id'+0);
$('#id'+0).blur();
var star=document.getElementsByClassName('star5')[0];star.click()}
var submit=document.getElementsByClassName('btn-5 mr10 setcomment')[0];
submit.click();
setTimeout('a()',5000)}};
a();

脚本2
京东自动评价脚本2：支持一键批量晒单/追加图片
var time; 
function a() { 
var close = document.getElementsByClassName('btn-9'); 
if (close.length > 0) { 
close[0].click() 
var imgs = document.getElementsByName('imgs1')[0]; 
if (imgs != null) { 
imgs.value = "//img30.360buyimg.com/shaidan/jfs/t1/212837/21/5696/32102/61a08a72E9ec497cc/4cb1af0c3c0d2b33.jpg,//img30.360buyimg.com/shaidan/jfs/t1/206321/25/16622/11531/61a08a8bE2a26267f/85dfac1da21b591d.jpg,//img30.360buyimg.com/shaidan/jfs/t1/145921/20/22724/15387/61a08a9bEc7baa1f9/8e692d782ac64026.jpg"; 
var submit = document.getElementsByClassName('btn-5 mr10 setcomment')[0]; 
submit.click(); 
time = setTimeout('a()', 5000) 
} 
} else { 
clearTimeout(time); 
} 
}; 
a();

程序每5秒就会执行一次，直到把所有待评价的订单都评价完，评价后就可以收到赠送的京豆奖励了，每单大概是10-40京豆奖励