# requests-h2
[Requests](https://github.com/psf/requests) that supports HTTP/1.1 and HTTP/2.

It may help people who want requests-style coding to send HTTP2 requests and don't want to upgrade their OpenSSL version, and
it allows you to send HTTP/1.1 and HTTP/2 requests extremely easily.


requests-h2是一个支持http2的http请求库，本项目基于requests与httpcore，除增加了额外参数外，与requests使用方法一致。

You use it just like requests:
```python
>>> import requests-h2 as requests
>>> r = requests.get('https://www.google.com', http2=True)
>>> r.status_code
200
>>> r.version
'HTTP/2'
```

## Requirements
Python 3.7+


## Dependencies
- requests
- httpcore
- urllib3<2


## Motivation
We are used to using `requests` to send HTTP requests, but it doesn't support HTTP2 util 2023 and maybe util now.
Although there are some libraries which have already supported HTTP2,but it's hard for me to change dependencies,so i created 
this project
to meet my demands.
And the `urllib3` which `requests` relies on is doing their effort to support HTTP2,but they need `OpenSSL` > 1.11,and anyone
who don't want to upgrade it still can use this library.
