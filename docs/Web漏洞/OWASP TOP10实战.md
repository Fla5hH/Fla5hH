# OWASP TOP10

**1、验证码绕过（on client 客户端）**

  * 通过乱输验证码发现只是页面提醒，bp并未抓到包，得以判断验证码是由前端生成的，并未传回服务器验证



![](https://cdn.nlark.com/yuque/0/2025/png/51646461/1761292184194-90b59929-8724-4b65-a1d7-5402c8ebe0e0.png)

![](https://cdn.nlark.com/yuque/0/2025/png/51646461/1761292219239-3682d09c-25f4-45de-a9e4-6715bae409e2.png)

  * 抓包，放到爆破模块删去验证码变量，直接爆破账密即可，得到admin/123456



![](https://cdn.nlark.com/yuque/0/2025/png/51646461/1761292472203-dc1a183b-6220-4f6b-b8be-5b85c30c2f44.png)

  


  


**2、验证码绕过（on server 服务器端）**

![](https://cdn.nlark.com/yuque/0/2025/png/51646461/1761292562473-4d89286f-efaa-4451-bb69-bda7deade3df.png)

![](https://cdn.nlark.com/yuque/0/2025/png/51646461/1761292706767-36498567-87f7-45e8-9cc0-cae579f70791.png)

  * 输入错误验证码后明显看到页面重新加载后再提示，抓包也明显发现有单独的验证码包，此处验证码应为服务器端校验，但有的服务器不会实时刷新验证码，抓到登录包后直接发送到爆破模块爆破账密
  * ![](https://cdn.nlark.com/yuque/0/2025/png/51646461/1761292858685-4f200940-1984-4533-b706-560c57c4bb12.png)



  


**3、Token防爆破**

![](https://cdn.nlark.com/yuque/0/2025/png/51646461/1761293064005-5a81e20c-e235-4ca3-830a-c45cef0fd023.png)

  * 登陆框抓包发现token验证，选择Pitchfork音叉类型爆破



![](https://cdn.nlark.com/yuque/0/2025/png/51646461/1761293189108-f3f05a74-8d2b-4882-8df7-f08b026a5315.png)

  * 因为token每次下发一个，所以线程数选择一个



![](https://cdn.nlark.com/yuque/0/2025/png/51646461/1761293371222-fb31ca8f-a16e-400d-b6fd-718de6fe1f12.png)

  * 模式选择递归提取



![](https://cdn.nlark.com/yuque/0/2025/png/51646461/1761293432328-1a47719f-f614-4a90-92bb-59a4460fc176.png)

  * 在响应包中找到token的值，复制



![](https://cdn.nlark.com/yuque/0/2025/png/51646461/1761293660036-7c60fc59-9652-4523-a324-adc6bb8e7e63.png)

  * 将复制的token值放进payload设置里开始爆破，分别设置1，2payload集



![](https://cdn.nlark.com/yuque/0/2025/png/51646461/1761293735061-6cf0273c-231d-4150-bce4-7e9740788847.png)
