
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
* `driver.get_log('browser'), page_source, name; refresh(); capabilities`
* `from selenium.webdriver.common.by import By; e=driver.find_elements(By.XPATH, P), e.send_keys('')`
* `driver.execute_cdp_cmd('Network.setUserAgentOverride', {"userAgent":"python", "platform":"Windows"}); driver.execute_script("return navigator.userAgent") `
* [Cookie: `driver.get_cookies(); delete_cookie(); add_cookie()`](https://www.selenium.dev/documentation/en/support_packages/working_with_cookies/)
* `from selenium.webdriver.common.action_chains import ActionChains; action = ActionChains(driver); action.move_to_element(element).click().perform()`
* [Action Chains](https://www.geeksforgeeks.org/action-chains-in-selenium-python/)
* Disable security check: `chrome.exe --user-data-dir="C:\Users\user1\chomedev" --disable-web-security --disable-site-isolation-trials`
* 

### requests
* `import requests; r=requests.get("https://httpbin.org/get"); r.content; r.text; r.status_code, r.headers['Content-Type']; r.request.headers`
* Handle response: `if response: print('Success!'); response.raise_for_status(); except requests.exceptions.HTTPError as err: `
* requests-html, requests-random-user-agent
* [Guide](https://realpython.com/python-requests/). 
  [Brief intro](https://realpython.com/python-packages/#requests-for-interacting-with-the-web)
* `requests.utils.get_encoding_from_headers(headers)`

### Javascript
* `console.dir(obj); methods only: console.dir(obj.__proto__); console.log(obj); Object.getOwnPropertyNames(obj) `
* [DevTools](https://indepth.dev/useful-techniques-for-debugging-code-using-chrome-devtools)
  * monitor/unmonitor; copy(var) - clipboard; 
  * ctrl+shift+p - run cmd: capture
* scroll: document.body.scrollHeight; arguments[0].scrollIntoView();
* [css selector](https://www.w3schools.com/css/css_selectors.asp)

### Diagnose
* Resolve circular referrence
```Javascript
const getCircularReplacer = () => {
  const seen = new WeakSet();
  return (key, value) => {
    if (typeof value === "object" && value !== null) {
      if (seen.has(value)) {
        return;
      }
      seen.add(value);
    }
    return value;
  };
};
```

* Print all vars
```Javascript
{
    const standardGlobals = new Set(["window", "self", "document", "name", "location", "customElements", "history", "locationbar", "menubar", "personalbar", "scrollbars", "statusbar", "toolbar", "status", "closed", "frames", "length", "top", "opener", "parent", "frameElement", "navigator", "origin", "external", "screen", "innerWidth", "innerHeight", "scrollX", "pageXOffset", "scrollY", "pageYOffset", "visualViewport", "screenX", "screenY", "outerWidth", "outerHeight", "devicePixelRatio", "clientInformation", "screenLeft", "screenTop", "defaultStatus", "defaultstatus", "styleMedia", "onsearch", "isSecureContext", "performance", "onappinstalled", "onbeforeinstallprompt", "crypto", "indexedDB", "webkitStorageInfo", "sessionStorage", "localStorage", "onabort", "onblur", "oncancel", "oncanplay", "oncanplaythrough", "onchange", "onclick", "onclose", "oncontextmenu", "oncuechange", "ondblclick", "ondrag", "ondragend", "ondragenter", "ondragleave", "ondragover", "ondragstart", "ondrop", "ondurationchange", "onemptied", "onended", "onerror", "onfocus", "onformdata", "oninput", "oninvalid", "onkeydown", "onkeypress", "onkeyup", "onload", "onloadeddata", "onloadedmetadata", "onloadstart", "onmousedown", "onmouseenter", "onmouseleave", "onmousemove", "onmouseout", "onmouseover", "onmouseup", "onmousewheel", "onpause", "onplay", "onplaying", "onprogress", "onratechange", "onreset", "onresize", "onscroll", "onseeked", "onseeking", "onselect", "onstalled", "onsubmit", "onsuspend", "ontimeupdate", "ontoggle", "onvolumechange", "onwaiting", "onwebkitanimationend", "onwebkitanimationiteration", "onwebkitanimationstart", "onwebkittransitionend", "onwheel", "onauxclick", "ongotpointercapture", "onlostpointercapture", "onpointerdown", "onpointermove", "onpointerup", "onpointercancel", "onpointerover", "onpointerout", "onpointerenter", "onpointerleave", "onselectstart", "onselectionchange", "onanimationend", "onanimationiteration", "onanimationstart", "ontransitionrun", "ontransitionstart", "ontransitionend", "ontransitioncancel", "onafterprint", "onbeforeprint", "onbeforeunload", "onhashchange", "onlanguagechange", "onmessage", "onmessageerror", "onoffline", "ononline", "onpagehide", "onpageshow", "onpopstate", "onrejectionhandled", "onstorage", "onunhandledrejection", "onunload", "alert", "atob", "blur", "btoa", "cancelAnimationFrame", "cancelIdleCallback", "captureEvents", "clearInterval", "clearTimeout", "close", "confirm", "createImageBitmap", "fetch", "find", "focus", "getComputedStyle", "getSelection", "matchMedia", "moveBy", "moveTo", "open", "postMessage", "print", "prompt", "queueMicrotask", "releaseEvents", "requestAnimationFrame", "requestIdleCallback", "resizeBy", "resizeTo", "scroll", "scrollBy", "scrollTo", "setInterval", "setTimeout", "stop", "webkitCancelAnimationFrame", "webkitRequestAnimationFrame", "chrome", "caches", "ondevicemotion", "ondeviceorientation", "ondeviceorientationabsolute", "originAgentCluster", "cookieStore", "showDirectoryPicker", "showOpenFilePicker", "showSaveFilePicker", "speechSynthesis", "onpointerrawupdate", "trustedTypes", "crossOriginIsolated", "openDatabase", "webkitRequestFileSystem", "webkitResolveLocalFileSystemURL"]);

    for (const key of Object.keys(window)) {
        if (!standardGlobals.has(key)) {
            console.log(key+" = "+JSON.stringify(window[key], getCircularReplacer()))
        }
    }
}
```


### Reference
* [An overview of HTTP](https://developer.mozilla.org/en-US/docs/Web/HTTP/Overview)
* [FastAPI to Build Python Web APIs](https://realpython.com/fastapi-python-web-apis/)
* [Async IO in Python](https://realpython.com/async-io-python/)
* [Getting Started With Async Features](https://realpython.com/python-async-features/)
* [The Guide To Ethical Scraping Of Dynamic Websites](https://www.smashingmagazine.com/2021/03/ethical-scraping-dynamic-websites-nodejs-puppeteer/)
* [avoid getting blocked](https://www.codementor.io/@scrapingdog/10-tips-to-avoid-getting-blocked-while-scraping-websites-16papipe62)
* Get header/test http: https://httpbin.org/headers
