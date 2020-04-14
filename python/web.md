
### Proxy setup
* env variable: 
os.environ['HTTPS_PROXY'] = ''

* urllib
```python
import urllib.request

proxy_support = urllib.request.ProxyHandler({'http' : 'http://user:pass@server:port', 
                                             'https': 'https://...'})
opener = urllib.request.build_opener(proxy_support)
urllib.request.install_opener(opener)
```

### selenium
* [selenium dev](https://www.selenium.dev/)
* [ChromeDriver](https://chromedriver.chromium.org/)
* [selenium with python](https://selenium-python.readthedocs.io/)
* 
