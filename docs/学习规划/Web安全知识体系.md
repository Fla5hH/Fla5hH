# DS改版

### Web漏洞种类

##### a. SQL注入

      * 联合查询注入
      * 报错注入（extractvalue、updatexml、floor）
      * 布尔盲注
      * 时间盲注
      * 堆叠注入
      * 宽字节注入
      * 二次注入
      * HTTP头注入（User-Agent、Referer、Cookie、X-Forwarded-For）
      * ORDER BY注入



##### b. XSS

      * 反射型XSS
      * 存储型XSS
      * DOM型XSS
      * 盲XSS
      * 常用利用点：script、img、svg、iframe、onerror、onload、javascript:



##### c. XXE

      * 有回显XXE
      * 无回显XXE（Blind XXE）
      * 基于错误的XXE
      * 利用场景：读文件、SSRF、端口探测、DoS



##### d. CSRF

      * GET型CSRF
      * POST型CSRF（form、JSON）
      * Flash CSRF
      * 防御绕过：Token可预测、Token未绑定、空Token



##### e. SSRF

      * 常见协议：http、https、gopher、dict、file、ftp
      * 攻击目标：内网探测、云元数据、Redis/Memcached/MongoDB未授权、Struts2漏洞
      * 绕过方式：localhost变形、短地址、302跳转、DNS rebinding、CRLF



##### f. 文件上传

      * 客户端绕过：JS校验禁用、改扩展名后抓包
      * 服务端绕过：MIME类型、文件头、扩展名（大小写、双写、点/空格/::$DATA）、条件竞争
      * 解析漏洞：IIS解析漏洞、Apache多后缀解析、Nginx配置不当
      * 图片马结合文件包含
      * 编辑器上传漏洞（UEditor、FCKeditor等）



##### g. 文件包含

      * 本地文件包含（LFI）
      * 远程文件包含（RFI）
      * PHP伪协议：php://input、php://filter、file://、data://、phar://、expect://
      * 日志文件包含、Session文件包含、临时文件包含



#### 1\. Python与Java关键语法种类

##### a. Python

      * requests库（GET/POST、Cookie/Session处理、文件上传、代理、超时）
      * urllib/urllib2基础
      * http.client
      * 多线程（threading/queue）、异步（asyncio/aiohttp）
      * 字符串处理、编码解码、正则
      * 时间与随机数



##### b. Java

      * 基础语法（类、对象、继承、多态）
      * 反射（Class.forName、getMethod、invoke）
      * 动态代理
      * 类加载器（URLClassLoader、defineClass）
      * Runtime.exec执行命令
      * JNDI基础（lookup、Reference）
      * 序列化与反序列化（ObjectInputStream）



#### 2\. 网络协议关键种类

    * HTTP/HTTPS：请求行/头/体、响应状态码、方法、Content-Type、Cookie与Session、CORS、缓存机制
    * DNS：A/AAAA/CNAME/MX/NS/TXT记录、递归与迭代查询、DNS隧道（iodine、dnscat2）
    * SMB：端口139/445、SMBv1漏洞（MS17-010）、psexec、smbexec、空会话（IPC$）
    * LDAP：查询语法、LDAP注入、LDAPS、JNDI-LDAP利用
    * 其他：SSH、FTP、RDP、Kerberos、NTLM认证流程



#### 3\. 中间件/组件漏洞种类

##### a. Shiro

      * Shiro-550（RememberMe AES-CBC固定密钥反序列化）
      * Shiro-721（RememberMe AES-GCM Padding Oracle攻击）



##### b. Fastjson

      * 出网利用链（JdbcRowSetImpl + JNDI/LDAP/RMI）
      * 不出网利用链（BasicDataSource + BCEL、ClassPathXmlApplicationContext、TemplatesImpl）
      * 其他利用链：Commons-io写文件、JNDI高版本绕过



##### c. Log4j2

      * JNDI注入（log4j2 2.0-2.14.1）
      * 支持的协议：ldap、rmi、dns、iiop、http
      * 常见WAF绕过变形：![](https://cdn.nlark.com/yuque/__latex/6856341a4b8853875de8c050582ced58.svg){::-j}、![](https://cdn.nlark.com/yuque/__latex/29e95e06f8676d46f7ca1bf316a1b539.svg)等



##### d. Struts2

      * S2-001（OGNL注入）
      * S2-005（OGNL注入）
      * S2-007（Integer验证）
      * S2-008（devMode）
      * S2-009/012（参数名注入）
      * S2-013/S2-014（标签属性）
      * S2-015（通配符）
      * S2-016（action:前缀）
      * S2-019（动态方法调用）
      * S2-032/S2-033/S2-037（REST插件）
      * S2-045/S2-046（Content-Type/Content-Disposition）
      * S2-048（struts2-struts1-plugin）
      * S2-052（REST插件XStream反序列化）
      * S2-053/S2-057（namespace）
      * S2-059/061（标签属性OGNL）
      * S2-062（类似059）



##### e. 常见未授权访问

      * Redis（写Webshell、SSH公钥、计划任务、主从复制RCE）
      * MongoDB（未授权访问、注入）
      * Memcached
      * Elasticsearch（CVE-2014-3120等RCE）
      * ZooKeeper
      * Docker API（2375端口，创建容器挂载宿主机目录）
      * Jenkins（script console、未授权访问构建）
      * CouchDB
      * Jupyter Notebook
      * ActiveMQ
      * RabbitMQ
      * Kubernetes ApiServer



#### 4\. Webshell与内存马种类

##### a. Webshell

      * 一句话木马（PHP: eval/assert, ASP: Eval/Execute, JSP: Runtime.exec）
      * 小马/大马（文件管理、命令执行、数据库管理、端口扫描）
      * 加密/混淆Webshell（自定义加密、openssl、类冰蝎/哥斯拉流量加密）



##### b. 内存马

      * Servlet型内存马（动态注册Servlet）
      * Filter型内存马（动态注册Filter，优先级高）
      * Listener型内存马（利用ServletRequestListener/HttpSessionListener）
      * Valve型内存马（Tomcat Valve管道）
      * Agent型内存马（Javaagent修改字节码，跨应用、无文件落地）
      * Websocket型内存马
      * 框架特定内存马（Spring Interceptor/Controller）



#### 5\. 内网渗透种类

##### a. 信息收集

      * 网络发现：IP段扫描、存活探测、端口服务识别
      * 域信息：域控定位、域用户/组/计算机列表、域信任关系
      * 凭证收集：浏览器密码、数据库配置、RDP保存密码、注册表
      * 密码抓取：mimikatz（wdigest、kerberos、msv）、procdump+lsass、SAM文件



##### b. 横向移动

      * IPC$ + at/schtasks
      * PsExec
      * WMI（wmic /node）
      * WinRM
      * DCOM（MMC20.Application、ShellWindows等）
      * SMBexec
      * 哈希传递（Pass-the-Hash）
      * 票据传递（Pass-the-Ticket）



##### c. 提权

      * Windows：系统溢出（ms17-010、cve-2021-1732等）、bypassUAC、令牌窃取、服务提权、AlwaysInstallElevated
      * Linux：SUID提权、sudo提权、内核溢出、cron任务、Docker组



##### d. 隧道/代理

      * 正向/反向代理：FRP、NPS、EarthWorm（ew）、reGeorg、Neo-reGeorg、chisel
      * 端口转发：SSH本地/远程/动态转发、netsh、socat、iptables
      * DNS/ICMP隧道：iodine、dnscat2、icmpsh



##### e. 域渗透

      * Kerberoasting（查询SPN、离线破解服务账户密码）
      * AS-REP Roasting
      * DCSync（利用DRSUAPI抓取域哈希）
      * 黄金票据（Golden Ticket）
      * 白银票据（Silver Ticket）
      * 委派攻击（非约束委派、约束委派、基于资源的约束委派）
      * 跨域攻击（域信任、林信任、SIDHistory）
      * NTLM中继攻击（SMB/HTTP/LDAP中继）



##### f. 权限维持

      * Windows：隐藏账户、计划任务、启动项、WMI事件订阅、DLL劫持、服务、SSP
      * 域：黄金票据、Skeleton Key、AdminSDHolder
      * Linux：SSH公钥、crontab、shell配置文件、LD_PRELOAD后门



##### g. 防御绕过

      * 杀软对抗：免杀、白利用、内存加载
      * 日志清理：wevtutil、auditpol禁用、手工清除
      * 防火墙/策略绕过：端口复用、协议伪装


