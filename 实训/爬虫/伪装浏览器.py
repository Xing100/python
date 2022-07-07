from fake_useragent import UserAgent
headers = {"UserAgent":UserAgent().random}
print(headers)