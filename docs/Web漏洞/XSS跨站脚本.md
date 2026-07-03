# XSS

### 1、什么是SSRF？

SSRF(Server-Side Request Forgery:服务器端请求伪造)

由于服务端提供了从其他服务器应用获取数据的功能，但又没有对目标地址做严格过滤与限制

导致攻击者可以传入任意的地址（URL）来让后端服务器对其发起请求，并返回对该目标地址请求的数据  
数据流：攻击者---->服务器---->目标地址  
根据后台使用的函数的不同，对应的影响和利用方法又有不一样
    
    
    PHP中下面函数的使用不当会导致SSRF:
    file_get_contents()
    fsockopen()
    curl_exec()

如果一定要通过后台服务器远程去对用户指定("或者预埋在前端的请求")的地址进行资源请求,**则请做好目标地址的过滤** 。

### 2、SSRF的基本利用形式

#### ①. 内网资产探测与端口扫描

这是最基础的利用方式：通过不断变化请求的 IP 和端口，根据返回内容、响应时间或错误信息的差异，来判断内网存活主机及开放服务。

#### ②.窃取云环境元数据

在云环境中，实例元数据服务通常通过固定的内部地址（链路本地地址）提供，包含凭据、配置等信息。这是 SSRF 最具价值的利用场景之一。

#### ③. 攻击内部未授权服务（协议利用）

很多内部服务（Redis、Memcached、MySQL、FastCGI 等）监听在 `127.0.0.1` 上且无密码，利用 SSRF 配合特定协议可向其发送攻击载荷。

**Gopher 协议** ：能构造任意 TCP 数据包，是攻击 Redis 的经典手段。例如：

可在 Redis 中写入计划任务或 SSH 公钥，进而反弹 Shell。

**Dict 协议** ：`dict://127.0.0.1:11211/stat` 可探测 Memcached 信息，也可执行某些命令。

**HTTP 包装** ：部分应用允许 CRLF 注入，将 HTTP 请求走私到内网服务。

#### ④. 读取本地文件（File 协议）

如果 SSRF 支持 `file://` 协议，可直接读取服务器本地文件系统。

  * `file:///etc/passwd`



以下是常用的攻击手段

  * gopher 协议攻击 Redis 写 Webshell，使用gopher协议时需要双重URL编码
  * dict / gopher 攻击 FastCGI 执行任意命令
  * 结合 file:// 读取敏感文件 + 其他信息泄露漏洞



  


[靶场](<https://www.yuque.com/mrflashbang/fygz7r/gco97z8s039lsmf4>)

和

[CTF](<https://www.yuque.com/mrflashbang/fygz7r/xx88vziv13omxoy0>)
