

import gzip
from webassets.filter import Filter
import io


__all__ = ('GZip',)


class GZip(Filter):
    """Applies gzip compression to the content given.

    This can be used if you are unable to let the webserver do the
    compression  on the fly, or just want to do precaching for additional
    performance.

    Note that you will still need to configure your webserver to send
    the files out marked as gzipped.
    """

    name = 'gzip'

    def output(self, _in, out, **kw):
        # HACK! FUGLY
        out = io.BytesIO(out.read().encode())
        _in = io.BytesIO(_in.read().encode())
        zfile = gzip.GzipFile(mode='w', compresslevel=6, fileobj=out)
        try:
            zfile.write(_in.read())
        finally:
            zfile.close()
