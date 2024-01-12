import io


class BytesSlicer:

    def __init__(self, chunk_size=None):
        self._buffer = io.BytesIO()
        self._chunk_size = chunk_size

    def slice(self, content):
        if self._chunk_size is None:
            # get all
            return [content] if content else []

        self._buffer.write(content)
        if self._buffer.tell() >= self._chunk_size:
            value = self._buffer.getvalue()
            # slice
            chunks = [value[i: i+self._chunk_size]
                      for i in range(0, len(value), self._chunk_size)]
            if len(chunks[-1]) == self._chunk_size:
                # every chunk can be sliced to chunk size
                self._buffer.seek(0)
                self._buffer.truncate()
                return chunks
            else:
                # use flush to get the last chunk
                self._buffer.seek(0)
                self._buffer.write(chunks[-1])
                self._buffer.truncate()
                return chunks[:-1]
        else:
            return []

    def flush(self):
        value = self._buffer.getvalue()
        self._buffer.seek(0)
        self._buffer.truncate()
        return [value] if value else []
