# HTML基础

**搜索引擎：Google，shadon，fofa，鹰图，搜狗（可以搜微信公众号）**

#Google搜索语法

site:bbc.edu.cn

site:bbc.edu.cn 登录 

学院 身份证

site:bbc.edu.cn intext:管理后台|登录|用户名|密码|验证码|系统|账号|手册 初始密码

site:bbc.edu.cn inurl:doc_id=1（可能出现注入）

site:edu.cn inurl:admin|login|admin_login|login_admin|system|boss|master|mange|manger

# 找文件上传的漏洞

site:edu.cn inurl:file

site:edu.cn inurl:load

# 找注入点页面

site:edu.cn inurl:php?id=

# 找重要文件

site:edu.cn inurl:robots.txt

site:edu.cn inurl:txt

site:edu.cn filetype:mdbsite:edu.cn filetype:ini

site:edu.cn filetype:phpsite:edu.cn filetype:asp

# fofa语法

domain=""（子域名）

ip="x.x.x.x/24"（c段/隐藏资产）

ip="x.x.x.x/20"（c段/隐藏资产）

# 扫c段，需要先确定真实ip，检查是否有cdn

# 1.nalookup来查看

nslookup www.baidu.com

# 2.超级ping，网站：ping.chinaz.com（查看得到ip是否相同，不同则有cdn）

**工商数据收集**

主要收集企业股权架构补充：子公司的持股51%及以上都算该主公司资产

爱企查

企查查

小蓝本（小程序）

天眼查（app->找产品信息）

点点

具体实战：

第一步：得到一个网址后，到www.aizhan.com ,进行whois查询，得到其他的后缀域名，看是否与主站有关联。（ip反查，查找域名）

其他工具：

微步情报社区：[https://x.threatbook.com/Whois](<https://x.threatbook.com/Whois>)：[https://ipwhois.cnnic.net.cn/icp](<https://ipwhois.cnnic.net.cn/icp>)

备案查询：[https://beian.miit.gov.cn/#/Integrated/recordQuery](<https://beian.miit.gov.cn/#/Integrated/recordQuery>)

第二步：收集网站子域名，可以利用工具微步社区；或者ip反查，查找一些子域名
