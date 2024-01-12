from requests.exceptions import InvalidSchema
from requests.sessions import Session as _Session

from adapters import HTTPAdapter, HTTP2Adapter


class Session(_Session):

    def __init__(self, http2=False, proxies=None,
                 pool_connections=100, pool_maxsize=100, max_retries=0):
        super().__init__()
        self.proxies = dict(proxies or {})
        self.mount(
            "https://",
            HTTPAdapter(
                pool_connections=pool_connections,
                pool_maxsize=pool_maxsize,
                max_retries=max_retries
            )
        )
        self.mount(
            "http://",
            HTTPAdapter(
                pool_connections=pool_connections,
                pool_maxsize=pool_maxsize,
                max_retries=max_retries
            )
        )

        self.http2 = http2
        self.pool_connections = pool_connections
        self.pool_maxsize = pool_maxsize
        self._http2adapter = None

    @property
    def http2adapter(self):
        if self._http2adapter is None:
            self._http2adapter = HTTP2Adapter(
                pool_connections=self.pool_connections,
                pool_maxsize=self.pool_maxsize
            )
        return self._http2adapter

    def get_adapter(self, url):
        """
        Returns the appropriate connection adapter for the given URL.

        :rtype: requests.adapters.BaseAdapter
        """
        if self.http2:
            return self.http2adapter
        for (prefix, adapter) in self.adapters.items():
            if url.lower().startswith(prefix.lower()):
                return adapter

        # Nothing matches :-/
        raise InvalidSchema(f"No connection adapters were found for {url!r}")

    def send(self, request, **kwargs):
        if self.http2:
            kwargs.setdefault("trust_env", self.trust_env)
        return super().send(request, **kwargs)

    def close(self):
        """Closes all adapters and as such the session"""
        for v in self.adapters.values():
            v.close()
        if self._http2adapter is not None:
            self._http2adapter.close()


if __name__ == "__main__":
    with Session(http2=True) as sess:
        print(sess.get('https://www.baidu.com').version)
