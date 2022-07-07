from urllib.request import urlopen
from urllib.request import Request
from urllib.parse import urlencode    #转码


def get_html(url):
    header = {
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.96 Safari/537.36"
    }
    request = Request(url,headers=header)
    response = urlopen(request)
    # print(response.read().decode())
    return response.read()


def save_html(filename,html_bytes):
    with open(filename,"wb")as f:
        f.write(html_bytes)
    print(filename + "保存成功")


def main():
    content = input("请输入要爬取的页面:")
    num = input("请输入要下载多少页:")
    base_url = "https://tieba.baidu.com/f?ie=utf-8&{}"
    for pn in range(int(num)):
        args = {
            "pn":pn*50,
            "kw":content
        }
        filename = "第"+str(pn+1)+"页.html"
        save = "正在保存第" + str(pn + 1) + "页.html"
        args = urlencode(args)
        print("正在下载"+filename)
        html_bytes = get_html(base_url.format(args))
        save_html(filename,html_bytes)



if __name__ == '__main__':
    main()