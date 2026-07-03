# 文件上传

  

    
    
    <!DOCTYPE html>
    <html>
      <head>
        <meta charset="utf-8">
        <title>菜鸟教程(runoob.com)</title>
      </head>
      <body>
    
        <h1>我的第一个标题</h1>
    
        <p>我的第一个段落。</p>
    
      </body>
    </html>

其中

**< body>**

**< /body>**

body标签中间的内容在网页可见

  * **标签**



尖括号括起来的叫标签，HTML 标签是包裹内容的标记，定义内容类型和格式

标签需要闭合<flash></flash>，HTML文件从开始标签开头结束标签结尾

**例：**

**< script> 标签：**用于定义客户端脚本，比如 JS，元素既可包含脚本语句，也可通过 src 属性指向外部脚本文件。

**< svg>标签：**用于定义矢量图形的标签，可绘制图形、图标等。

**< img>标签：**用于在页面中插入图像的标签，它是单标签不需要闭合，通过src属性指定图像的路径让浏览器显示照片。alt属性则是图片加载失败时显示的备用文本。
    
    
    <img src="image.jpg" alt="这是一张示例图片">

**< a>标签：**用于定义超链接，通过href属性指定链接目标。
    
    
    <a href="https://www.runoob.com"> Link </a>

![](https://cdn.nlark.com/yuque/0/2026/png/51646461/1772970097586-abdf3555-5fa2-4d11-b8fb-a2dff55fc844.png)

页面跳转

[https://www.runoob.com/html/html-links.html](<https://www.runoob.com/html/html-links.html>)关于链接标签的详细解释

**< 表单>：**表单用于收集用户的输入信息，表示文档中的一个区域，此区域包含交互控件，将用户收集到的信息发送到 Web 服务器。
    
    
    <form action="/" method="post">
        <!-- 文本输入框 -->
        <label for="name">用户名:</label>
        <input type="text" id="name" name="name" required>
      
    ........
      
        <input type="submit" value="提交">
    </form>

![](https://cdn.nlark.com/yuque/0/2026/png/51646461/1772969407616-c3bc86d1-4a04-487c-aff5-18e51cbdac80.png)

关于表单的具体内容：[https://www.runoob.com/html/html-forms.html](<https://www.runoob.com/html/html-forms.html>)
