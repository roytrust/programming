
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
* driver. get_log('browser'), page_source, name
* `driver.execute_cdp_cmd('Network.setUserAgentOverride', {"userAgent":"python", "platform":"Windows"}); driver.execute_script("return navigator.userAgent") `

### requests
* `import requests; response = requests.get("http://www.example.com"); response.text, response.status_code`
* Handle response: `if response: print('Success!'); response.raise_for_status(); except requests.exceptions.HTTPError as err: `
* [Guide](https://realpython.com/python-requests/). 
  [Brief intro](https://realpython.com/python-packages/#requests-for-interacting-with-the-web)

### Reference
* [avoid getting blocked](https://www.codementor.io/@scrapingdog/10-tips-to-avoid-getting-blocked-while-scraping-websites-16papipe62)

