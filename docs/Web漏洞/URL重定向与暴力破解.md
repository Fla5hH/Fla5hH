# 暴力破解

不安全的url跳转问题可能发生在一切执行了url地址跳转的地方。  
如果后端采用了前端传进来的(可能是用户传参,或者之前预埋在前端页面的url地址)参数作为了跳转的目的地,而又没有做判断的话就可能发生"跳错对象"的问题。  
通常是前端将传递 `$_GET['url']`后台, 后台没有对其作任何安全判断就赋值给了变量`$url`, 然后通过`header`函数进行跳转
    
    
    $html="";
    if(isset($_GET['url']) && $_GET['url'] != null){
      
      $url = $_GET['url'];
      
      if($url == 'i'){
        $html.="<p>好的,希望你能坚持做你自己!</p>";
      }else {
        header("location:{$url}");
      }
    }
    

  * 点击发现第三句话会跳转回概述界面



![](https://cdn.nlark.com/yuque/0/2025/png/51646461/1761239841431-a7d86af5-f281-4af7-bfff-79fe7ed59882.png)

  * 在BP抓包 然后将URL改成别的网站 即可达到重定向的效果



![](https://cdn.nlark.com/yuque/0/2025/png/51646461/1761239941737-01493a01-1ee9-40b7-abc9-0fc222fb8f2d.png)

![](https://cdn.nlark.com/yuque/0/2025/png/51646461/1761240627147-2e45df76-187b-4be4-949a-af26cdc40cdf.png)

  * 历史记录里可以看到代表有网站重定向的302代码



![](https://cdn.nlark.com/yuque/0/2025/png/51646461/1761240107531-fe2286eb-b1f6-4f5a-a014-2a92f3e68ee8.png)

  * 在重放器里跟随重定向



![](https://cdn.nlark.com/yuque/0/2025/png/51646461/1761240410937-a1b6a34e-0da2-44e6-b2f6-e11974786cc8.png)

  * 成功来到b站



![](https://cdn.nlark.com/yuque/0/2025/png/51646461/1761240432593-0260d85c-d163-47dc-9dcb-700f4c7e4b56.png)
