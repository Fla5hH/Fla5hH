#!/usr/bin/env python3
"""
语雀知识库 → GitHub 仓库 自动组织脚本
将已转换的 Markdown 文件按分类整理到对应目录
"""

import os
import shutil
import re
import requests

# === 配置 ===
SRC_DIR = r'C:\Users\18304\Documents\Codex\2026-07-03\new-chat\work\yuque_markdown'
TARGET_DIR = r'C:\Users\18304\Documents\Codex\2026-07-03\new-chat\work\organized_repo'
IMG_DIR = os.path.join(TARGET_DIR, 'docs', 'images')

# === 文件分类规则（文件名 → 目标路径） ===
FILE_MAP = {
    # Web漏洞
    'SQL注入.md': 'docs/Web漏洞/SQL注入.md',
    'SQL注入—常规绕过.md': 'docs/Web漏洞/SQL注入—常规绕过.md',
    'XSS跨站脚本.md': 'docs/Web漏洞/XSS跨站脚本.md',
    'XSS.md': 'docs/Web漏洞/XSS(OWASP).md',
    'CSRF跨站请求伪造.md': 'docs/Web漏洞/CSRF跨站请求伪造.md',
    'SSRF漏洞.md': 'docs/Web漏洞/SSRF漏洞.md',
    'SSRF.md': 'docs/Web漏洞/SSRF(OWASP).md',
    'DNS重绑定—常与SSRF同用.md': 'docs/Web漏洞/DNS重绑定—常与SSRF同用.md',
    'URL重定向.md': 'docs/Web漏洞/URL重定向.md',
    '暴力破解.md': 'docs/Web漏洞/暴力破解.md',
    '文件上传.md': 'docs/Web漏洞/文件上传.md',
    
    # CTF
    'FZNCTF—Web.md': 'docs/CTF/FZNCTF—Web.md',
    'CTFShow—Web入门.md': 'docs/CTF/CTFShow—Web入门.md',
    '0xGame—Web（week1）.md': 'docs/CTF/0xGame—Web（week1）.md',
    'CTF Show—Web应用安全与防护.md': 'docs/CTF/CTF Show—Web应用安全与防护.md',
    'SSRF——CTF题目.md': 'docs/CTF/SSRF——CTF题目.md',
    
    # OWASP
    'OWASP TOP10.md': 'docs/OWASP/OWASP TOP10.md',
    
    # 内网渗透
    '内网.md': 'docs/内网渗透/内网基础架构——域和组.md',
    
    # 安全知识点
    'Spring框架常见漏洞.md': 'docs/知识点/Spring框架常见漏洞.md',
    'JS逆向.md': 'docs/知识点/JS逆向.md',
    '什么是JWT.md': 'docs/知识点/JWT安全.md',
    'AES算法的五种工作模式.md': 'docs/知识点/AES算法的五种工作模式.md',
    'WEB前后端交互逻辑.md': 'docs/知识点/WEB前后端交互逻辑.md',
    '信息收集语法.md': 'docs/知识点/信息收集语法.md',
    'HTML基础.md': 'docs/知识点/HTML基础.md',
    '_知识点_.md': 'docs/知识点/知识点索引.md',
    
    # 漏洞挖掘
    '【漏洞】广西大学论文授权提交系统存在水平越权.md': 'docs/漏洞挖掘/广西大学论文授权系统水平越权.md',
    '_挖到的洞_.md': 'docs/漏洞挖掘/挖洞笔记.md',
    '《漏洞挖掘》.md': 'docs/漏洞挖掘/SQL注入挖掘记录.md',
    
    # 其他
    '学习路线图.md': 'docs/其他/学习路线图.md',
    'DS改版.md': 'docs/其他/DS改版.md',
    '无标题文档.md': 'docs/其他/无标题文档.md',
    '靶场.md': 'docs/其他/靶场概览.md',
}

def download_images():
    """下载 Markdown 中引用的语雀图片到本地"""
    os.makedirs(IMG_DIR, exist_ok=True)
    downloaded = set()
    
    for root, _, files in os.walk(TARGET_DIR):
        for fname in files:
            if not fname.endswith('.md'):
                continue
            path = os.path.join(root, fname)
            with open(path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            urls = re.findall(r'!\[.*?\]\((https?://[^)]+)\)', content)
            for url in urls:
                if 'nlark.com' not in url:
                    continue
                
                img_name = re.sub(r'[?&].*', '', url.split('/')[-1])
                if not img_name:
                    img_name = str(hash(url)) + '.png'
                
                local_path = os.path.join(IMG_DIR, img_name)
                if img_name not in downloaded and not os.path.exists(local_path):
                    try:
                        r = requests.get(url, timeout=10, headers={
                            'User-Agent': 'Mozilla/5.0'
                        })
                        with open(local_path, 'wb') as img_f:
                            img_f.write(r.content)
                        downloaded.add(img_name)
                        print(f'  [IMG] Downloaded: {img_name}')
                    except Exception as e:
                        print(f'  [IMG] Failed: {url[:50]}... {e}')
                
                # Replace URL with local path
                new_url = f'../images/{img_name}'
                content = content.replace(url, new_url)
            
            with open(path, 'w', encoding='utf-8') as f:
                f.write(content)

def main():
    os.makedirs(TARGET_DIR, exist_ok=True)
    
    print(f'Organizing files from: {SRC_DIR}')
    print(f'Target directory: {TARGET_DIR}')
    print()
    
    for src_name, rel_path in FILE_MAP.items():
        src_path = os.path.join(SRC_DIR, src_name)
        if not os.path.exists(src_path):
            print(f'  [SKIP] Not found: {src_name}')
            continue
        
        target_path = os.path.join(TARGET_DIR, rel_path)
        os.makedirs(os.path.dirname(target_path), exist_ok=True)
        shutil.copy2(src_path, target_path)
        print(f'  [OK] {src_name} → {rel_path}')
    
    print(f'\n✅ Organized {len(FILE_MAP)} files to {TARGET_DIR}')
    print()
    
    # Download images
    print('Downloading images from cdn.nlark.com...')
    download_images()
    print(f'\n✅ Images saved to {IMG_DIR}')
    
    print()
    print('Next steps:')
    print(f'  1. cd {TARGET_DIR}')
    print('  2. git init && git add . && git commit -m "init"')
    print('  3. git remote add origin https://github.com/Fla5hH/my-security-knowledge.git')
    print('  4. git push -u origin main')

if __name__ == '__main__':
    main()
