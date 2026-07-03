# SSRF——CTF题目

### 1、请求方式

![](https://cdn.nlark.com/yuque/0/2026/png/51646461/1779699002339-a6ee6b48-d354-4299-92b8-c7e8800bb06f.png)

![](https://cdn.nlark.com/yuque/0/2026/png/51646461/1779699015203-8c5d70c0-f6f6-4056-ad25-be16371298ec.png?x-oss-process=image%2Fcrop%2Cx_0%2Cy_763%2Cw_1319%2Ch_512)

加载进来后改用POST方式访问

![](https://cdn.nlark.com/yuque/0/2026/png/51646461/1779699048915-73399573-20a1-47ee-b3ec-60de30dfbd37.png)

要求使用PUT请求 就用BP抓包在请求头位置一顿改就可以了 最后改成NSSCTF得到Flag

### 2、HTTP请求协议

![](https://cdn.nlark.com/yuque/0/2026/png/51646461/1779699637866-3027c487-244a-49bb-b072-acda17de11a5.png)

![](https://cdn.nlark.com/yuque/0/2026/png/51646461/1779699670076-7e576d28-6359-4b91-81b4-89d2a0c166ac.png)

抓包 改

![](https://cdn.nlark.com/yuque/0/2026/png/51646461/1779699775267-a048a0fe-50ac-4738-9664-b656961f9bd7.png)

竟然爆400了 何意味

![](https://cdn.nlark.com/yuque/0/2026/png/51646461/1779699820667-9333df7e-729f-4914-95e8-a638d1c156cb.png)

要改成2.0 好吧

### 3、HTTP请求头

![](https://cdn.nlark.com/yuque/0/2026/png/51646461/1779699954248-7319a056-199e-45d6-ab2e-4d4f2975553f.png)

![](https://cdn.nlark.com/yuque/0/2026/png/51646461/1779700081845-04aabb10-c813-4f14-98a2-269ba62573de.png)

按要求添加

![](https://cdn.nlark.com/yuque/0/2026/png/51646461/1779700146162-4737a609-ca62-4282-8cff-2f7539ee8b01.png)

![](https://cdn.nlark.com/yuque/0/2026/png/51646461/1779700166743-4aa63a44-87ad-44f6-a9b3-38a723c47a57.png)

好像环境寄了 不做了 下一题

### 3、Cookie伪造

![](https://cdn.nlark.com/yuque/0/2026/png/51646461/1779700387620-f9c8347f-39db-4967-858e-57102f87926f.png)

将Cookie的值改为admin即可看到flag
