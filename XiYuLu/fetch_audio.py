from bs4 import BeautifulSoup
import requests

def fetch_audio(html_content):
    # 解析HTML内容
    soup = BeautifulSoup(html_content, 'html.parser')

    # 查找所有<a>标签，并且这些标签具有data-src属性
    a_tags = soup.find_all('a', attrs={'data-src': True})

    # 提取每个<a>标签的data-src属性值
    data_src_values = [a['data-src'] for a in a_tags]

    # 输出结果

    print(len(data_src_values))
    for src in data_src_values:
        download_audio(src)
        # 根据src的值，下载音频文件
        

def download_audio(url):
    # 发送HTTP请求并获取响应
    response = requests.get(url)

    # 本地文件名
    local_filename = url.split('/')[-1]

    # 将响应内容写入本地文件
    with open(local_filename, 'wb') as f:
        f.write(response.content)

    return local_filename
    

def fetch_html(url):
    # 给定的网址
    # url = "https://example.com/path/to/file.py"

    # 本地文件名
    local_filename = "downloaded_file.py"

    # 发送HTTP请求并获取响应
    response = requests.get(url)
    html_text = response.text

    return html_text

url = "https://topics.gmw.cn/node_86148.htm"
html_content = fetch_html(url) 
audio_src = fetch_audio(html_content)
# print(audio_src)




