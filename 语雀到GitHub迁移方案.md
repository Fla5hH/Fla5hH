# 语雀知识库 → GitHub 主页 迁移方案

> 📍 目标：将语雀（默认知识库）的全部 32 篇文档以 Markdown 格式迁移至 GitHub Profile  
> 🔗 GitHub: [github.com/Fla5hH](https://github.com/Fla5hH)

---

## 一、整体架构方案

### 仓库结构设计

有两种方案可选：

#### 方案 A：单仓库 + Wiki 风格（推荐）

```
Fla5hH/
├── README.md              ← GitHub Profile 主页
├── docs/                   ← 语雀文档全量迁移
│   ├── Web漏洞/
│   │   ├── SQL注入.md
│   │   ├── SQL注入—常规绕过.md
│   │   ├── XSS跨站脚本.md
│   │   ├── CSRF跨站请求伪造.md
│   │   ├── SSRF漏洞.md
│   │   ├── 文件上传.md
│   │   ├── URL重定向.md
│   │   └── 暴力破解.md
│   ├── 靶场训练/
│   │   ├── Pikachu/
│   │   │   ├── CSRF(OWASP版).md
│   │   │   ├── SSRF(OWASP版).md
│   │   │   └── XSS(OWASP版).md
│   │   └── OWASP TOP10/
│   │       └── ...
│   ├── CTF/
│   │   ├── FZNCTF—Web.md
│   │   ├── CTFShow—Web入门.md
│   │   ├── 0xGame—Web.md
│   │   └── CTF Show—Web应用安全与防护.md
│   ├── 安全知识点/
│   │   ├── Spring框架常见漏洞.md
│   │   ├── JS逆向.md
│   │   ├── JWT安全.md
│   │   ├── AES算法五种工作模式.md
│   │   ├── 信息收集语法.md
│   │   └── WEB前后端交互逻辑.md
│   ├── 内网渗透/
│   │   └── 内网基础架构—域和组.md
│   └── 漏洞挖掘/
│       └── 广西大学论文授权系统水平越权.md
```

#### 方案 B：多仓库（各方向独立仓库）

| 仓库名 | 内容 |
|--------|------|
| `Fla5hH` | Profile README + 导航 |
| `Web-Security-Notes` | Web 漏洞学习笔记全部 |
| `CTF-Writeup` | CTF 解题记录 |
| `Vuln-Labs` | Pikachu/靶场通关记录 |
| `Vulnerability-Discovery` | 真实漏洞挖掘报告 |
| `Penetration-Testing-Notes` | 内网渗透/知识点 |

---

## 二、文档图片处理

语雀文档中有大量图片（来自 cdn.nlark.com），需要做以下处理：

### 方案 1：保留引用 + 本地缓存（推荐）

```
docs/
└── images/               ← 存放所有图片
    ├── sql-injection/
    ├── xss/
    └── ...
```

写一个脚本批量下载图片：

```python
import os, re, requests
from urllib.parse import urlparse

def download_images(md_dir, img_dir):
    os.makedirs(img_dir, exist_ok=True)
    for root, _, files in os.walk(md_dir):
        for fname in files:
            if not fname.endswith('.md'): continue
            path = os.path.join(root, fname)
            with open(path, 'r', encoding='utf-8') as f:
                content = f.read()
            urls = re.findall(r'!\[.*?\]\((https://cdn\.nlark\.com[^)]+)\)', content)
            for url in urls:
                parsed = urlparse(url)
                fname_img = os.path.basename(parsed.path)
                local_path = os.path.join(img_dir, fname_img)
                if not os.path.exists(local_path):
                    r = requests.get(url)
                    with open(local_path, 'wb') as img_f:
                        img_f.write(r.content)
                content = content.replace(url, f'./images/{fname_img}')
            with open(path, 'w', encoding='utf-8') as f:
                f.write(content)
```

### 方案 2：直接用语雀 CDN 链接（最简单）

直接保留 `cdn.nlark.com` 链接，不需额外操作。缺点是如果语雀图床政策变化可能会失效。

---

## 三、README.md 如何集成文档导航

在 Profile README 中加入"知识库"版块，直接引用 docs/ 目录：

```markdown
## 📚 我的安全知识库

我系统整理了 Web 安全学习笔记，放在这个仓库里：

### 🎯 Web 漏洞
- [SQL注入](docs/Web漏洞/SQL注入.md)
- [XSS跨站脚本](docs/Web漏洞/XSS跨站脚本.md)
- [CSRF跨站请求伪造](docs/Web漏洞/CSRF跨站请求伪造.md)
- [SSRF漏洞](docs/Web漏洞/SSRF漏洞.md)
- [文件上传](docs/Web漏洞/文件上传.md)

### ⚔️ CTF Writeup
- [FZNCTF—Web](docs/CTF/FZNCTF—Web.md)
- [CTFShow—Web入门](docs/CTF/CTFShow—Web入门.md)
- [0xGame—Web](docs/CTF/0xGame—Web.md)

### 🏴 漏洞挖掘
- [广西大学论文授权系统水平越权漏洞](docs/漏洞挖掘/广西大学论文授权系统水平越权.md)

### 🔬 知识点
- [Spring框架常见漏洞](docs/知识点/Spring框架常见漏洞.md)
- [JWT安全](docs/知识点/JWT安全.md)
- [JS逆向](docs/知识点/JS逆向.md)

### 🌐 内网渗透
- [内网基础架构—域和组](docs/内网渗透/内网基础架构—域和组.md)
```

---

## 四、已转换好的 Markdown 文档

所有 32 篇文档已经 **从 .lakebook 提取并转换为 Markdown 格式**，位于：

```
C:\Users\18304\Documents\Codex\2026-07-03\new-chat\work\yuque_markdown\
```

### 操作步骤

```bash
# 1. 创建 GitHub 仓库
git init my-security-knowledge
cd my-security-knowledge

# 2. 复制已转换的 Markdown 文件到对应目录（按分类整理）
# （需要手动按上面目录结构分类存放）

# 3. 如果你用的是方案B，直接分别创建每个仓库
#   - 每个仓库独立的 README.md
#   - 仓库间通过 Profile README 互相引用

# 4. 推送
git add .
git commit -m "init: 语雀知识库迁移至 GitHub"
git remote add origin https://github.com/Fla5hH/<repo-name>.git
git push -u origin main
```

---

## 五、需要注意的问题

1. **语雀图片防盗链**：`cdn.nlark.com` 可能在某些场景下限制外链访问，建议批量下载到本地
2. **文档内交叉引用**：原文档中有 `[详见](https://www.yuque.com/...)` 的链接，迁移后需要替换为仓库内相对路径
3. **中文文件名**：Git 对中文文件名支持良好，但某些工具链可能有问题，可考虑用拼音或英文命名
4. **README 格式化**：建议在 README 中添加目录树（用 `tree` 命令生成）方便导航
5. **License**：建议加一个 LICENSE 文件（如 MIT），声明文档许可
