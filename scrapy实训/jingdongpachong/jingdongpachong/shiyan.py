base_url = "https://search.jd.com/Search?keyword=%E7%94%B7%E8%A3%85&wq=%E7%94%B7%E8%A3%85&page={}"
urls = []
for i in range(100):
    url = base_url.format(i*2+1)
    urls.append(url)


