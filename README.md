# requests-h2
[Requests](https://github.com/psf/requests) that supports HTTP/2

requests-h2是一个支持http2的http请求库，本项目基于requests与h2，除增加了额外参数外，与requests使用方法一致。

```python
>>> import requests-h2 as requests
>>> r = requests.get('https://www.google.com', http2=True)
>>> r.status_code
200
>>> r.version
'HTTP/2'
```

requests-h2 allows you to send HTTP/1.1 and HTTP/2 requests extremely easily.

requests-h2 is built on requests, make some extensions to support HTTP/2 request and add som other features.