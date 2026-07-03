# SSRF漏洞

#### 1、反射型XSS（get）（post只是传参的位置不同payload相同 不单开写了）

![](https://cdn.nlark.com/yuque/0/2026/png/51646461/1778490482176-354e9359-f8c5-4ce4-bb3c-283b3563957d.png)

发现输入框只能输入20个字符，到前端给他改成100

![](https://cdn.nlark.com/yuque/0/2026/png/51646461/1778490777163-40eaada0-ca70-4e02-94e3-7d4658fed35c.png)

把最经典的<script>注入进去即可

![](https://cdn.nlark.com/yuque/0/2026/png/51646461/1778490922961-3f2be006-e6b5-4799-8906-007e6d7f19e5.png?x-oss-process=image%2Fcrop%2Cx_0%2Cy_30%2Cw_940%2Ch_229)

#### 2、存储型XSS

![](https://cdn.nlark.com/yuque/0/2026/png/51646461/1778491246373-c7c472c6-8f10-476b-8fd9-7ec53eb12c7e.png)

在留言板存储的恶意代码会导致重新进入界面依旧弹窗，因为代码已经被存储起来

![](https://cdn.nlark.com/yuque/0/2026/png/51646461/1778491299900-e33ca6fe-d799-4a18-9074-3631465b6415.png)

  


#### 3、DOM型XSS（XSS-X原理一样 不再写了）
    
    
    <script>
    function domxss(){
    var str = document.getElementById("text").value;
    document.getElementById("dom").innerHTML = "<a href='"+str+"'>what do you see?</a>";
    }
    //试试：'><img src="#" onmouseover="alert('xss')">
    //试试：' onclick="alert('xss')">,闭合掉就行
    </script>

var str = document.getElementById("text").value;

通过调用DOM接口，获取页面中含text的元素，即输入框中的内容赋值给str

document.getElementById("dom").innerHTML

`.innerHTML`：将该元素的内部 HTML 内容设置为等号右边的字符串

"<a href='"+str+"'>what do you see?</a>"

动态生成一个超链接，其中 `href` 属性的值**直接来自用户的输入**`**str**`

**漏洞的点就在于href没有过滤输入**
    
    
    "<a href='"+'><img src="#" onmouseover="alert('xss')">+"'>what do you see?</a>"

将Payload1替换成str 发现<a>标签被闭合，新的img标签src='#'是一个无效资源

触发onmouseover导致弹窗
    
    
    "<a href='"+' onclick="alert('xss')">+"'>what do you see?</a>"

Payload2原理相同先单引号闭合href，然后用空格分割开，加入一个onclick属性

这样点击链接就会触发alert

  


#### 4、XSS之盲打

![](https://cdn.nlark.com/yuque/0/2026/png/51646461/1778578008279-971e88f3-acb8-4029-bc42-ee5aea68d11b.png)

先试一下常规Payload 发现没有反应

![](https://cdn.nlark.com/yuque/0/2026/png/51646461/1778578072479-d4f7d172-2ff9-4076-83e3-bbef9e141b00.png)

通过提示发现客户端页面无法弹窗

![](https://cdn.nlark.com/yuque/0/2026/png/51646461/1778578137820-e979d9f8-fa8b-43a2-889a-966fb5119fd6.png)

登录进后台页面发现成功弹窗

  


#### 5、XSS之过滤

![](https://cdn.nlark.com/yuque/0/2026/png/51646461/1778578405366-582243e6-1178-4d6d-b8e4-c28dea7c7af1.png)

输入别的在下面都显示，但是这个Payload就会被过滤掉

所以猜测<script>标签被过滤了，换一个别的Payload
    
    
    <img src=1 onerror=alert("xss");>

![](https://cdn.nlark.com/yuque/0/2026/png/51646461/1778578481329-0f0e30cf-78ca-46fa-bbf5-d11e6f784fd4.png)

成功弹窗

  


#### 6、XSS之htmlspecialchars()

![](https://cdn.nlark.com/yuque/0/2026/png/51646461/1778588672941-2667d830-43a1-4d58-8faf-b3131fa86c67.png)

测试常规Payload，发现回显的是一个链接，猜测是<a>标签里的href

按F12寻找源代码

![](https://cdn.nlark.com/yuque/0/2026/png/51646461/1778588745216-45247ed1-756e-4da1-bcda-0f8749395b13.png)

<a href=""> </a>

所以采用闭合<a>标签的Payload

![](https://cdn.nlark.com/yuque/0/2026/png/51646461/1778771002885-5dbf68c0-c1f7-4c0a-b145-4a1295d08821.png)

alert里面用单引号和双引号是有区别的

![](https://cdn.nlark.com/yuque/0/2026/png/51646461/1778771056738-4d5f0d63-ad63-4caf-b467-0e9bceaebb47.png)

![](https://cdn.nlark.com/yuque/0/2026/png/51646461/1778771198995-8b2395ee-50eb-4283-befb-f088b4e53d36.png)

因为htmlspecialchars函数默认不对单引号做处理（不编码）
    
    
    $message=htmlspecialchars($_GET['message']);
    
    $html1.="<p class='notice'>你的输入已经被记录:</p>";
    
    //输入的内容被处理后输出到了input标签的value属性里面,试试:' onclick='alert(111)'
    
    $html2.="<a href='{$message}'>{$message}</a>";

使用单引号会导致浏览器在解析时错误闭合

浏览器解析步骤：

  1. 第一个 `'` 闭合了 `href` 属性值（此时 `href=''`）。
  2. 接着解析到 `onclick=`，视为一个新属性。
  3. 新属性 `onclick` 的值由下一个单引号界定：`onclick='alert(`
  4. 然后遇到 alert里面第一个`'`，这个单引号会提前结束 `onclick` 属性值
  5. 导致属性值变为 `alert(`，剩下的 `xss')` 成为无效文本。


    
    
    <a href='' onclick='alert('      ---后面的变成无效文本 xss')'>...</a>

但使用双引号时，双引号会被编码成&quot， 所以在浏览器解析时不会被提前闭合
    
    
    <a href='' onclick=    'alert(&quot;xss&quot;)'    >...</a>

alert会是一段完整的代码被解析出来，这样就可以弹窗了

或者可以换成alert(111)，纯数字就不用考虑引号解析的问题了

#### 7、XSS之href输出

![](https://cdn.nlark.com/yuque/0/2026/png/51646461/1778774281055-fb430a4a-5f8b-4106-b4b5-66cd23d4ae4a.png)

按提示输入后下方出现链接

![](https://cdn.nlark.com/yuque/0/2026/png/51646461/1778774355868-90352f14-ee42-4fc9-a1db-8a3e670fedd0.png)

![](https://cdn.nlark.com/yuque/0/2026/png/51646461/1778774396902-cbcc9e65-8a93-4c1c-a53b-f4856860a6fd.png)

查看前端代码发现还他妈是<a>标签

测试后发现左右尖括号和单双引号全被编码了

采用伪协议Payload
    
    
    javascript:alert(1)

原理如下：

通常浏览器在地址栏或超链接的 `href` 中遇到一个 URL 时，会执行以下步骤：

  1. 解析 URL 协议（如 `http:`、`https:`、`file:`、`javascript:` 等）。
  2. 根据协议执行相应的动作：


    * `http:` → 发送 HTTP 请求，加载页面。
    * `mailto:` → 打开邮件客户端。
    * `javascript:` → **不发起网络请求，而是将协议后面的内容当作 JS 代码在当前页面执行** 。



因此，当浏览器遇到 `<a href="javascript:alert(1)">...</a>` 时：

  * 浏览器提取 `javascript:` 后面的字符串 `alert(1)`。
  * 在当前页面的全局作用域中执行这段 JavaScript 代码。
  * 弹窗 `1`。


    
    
    if(isset($_GET['submit'])){
      if(empty($_GET['message'])){
        $html.="<p class='notice'>叫你输入个url,你咋不听?</p>";
      }
      if($_GET['message'] == 'www.baidu.com'){
        $html.="<p class='notice'>我靠,我真想不到你是这样的一个人</p>";
      }else {
        //输出在a标签的href属性里面,可以使用javascript协议来执行js
        //防御:只允许http,https,其次在进行htmlspecialchars处理
        
        $message=htmlspecialchars($_GET['message'],ENT_QUOTES);
        $html.="<a href='{$message}'> 阁下自己输入的url还请自己点一下吧</a>";
        
      }
    }

#### 8、XSS之JS输出

前端代码是这样的

![](https://cdn.nlark.com/yuque/0/2026/png/51646461/1778775811039-30ebd645-55e5-482c-8dd7-915084730df1.png)

发现是<script>标签闭合有问题 原本的标签与Payload标签错误的闭合到一块了
    
    
    </script><script>alert('Flash')</script>

直接手动给前面的闭合成功弹窗
