
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
* `driver.get_log('browser'), page_source, name; refresh()`
* `from selenium.webdriver.common.by import By; e=driver.find_elements(By.XPATH, P), e.send_keys('')`
* `driver.execute_cdp_cmd('Network.setUserAgentOverride', {"userAgent":"python", "platform":"Windows"}); driver.execute_script("return navigator.userAgent") `
* [Cookie: `driver.get_cookies(); delete_cookie(); add_cookie()`](https://www.selenium.dev/documentation/en/support_packages/working_with_cookies/)

### requests
* `import requests; r=requests.get("http://www.example.com"); r.content; r.text; r.status_code, r.headers['Content-Type']; r.request.headers`
* Handle response: `if response: print('Success!'); response.raise_for_status(); except requests.exceptions.HTTPError as err: `
* requests-html, requests-random-user-agent
* [Guide](https://realpython.com/python-requests/). 
  [Brief intro](https://realpython.com/python-packages/#requests-for-interacting-with-the-web)

### Reference
* [avoid getting blocked](https://www.codementor.io/@scrapingdog/10-tips-to-avoid-getting-blocked-while-scraping-websites-16papipe62)
* Get header/test http: https://httpbin.org/headers
