from http.server import BaseHTTPRequestHandler
from datetime import datetime
from urllib import parse
import platform


class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        paths = self.path
        url_components = parse.urlsplit(paths)
        query = parse.parse_qsl(url_components.query)
        dic = dict(query)
        name = dic.get("name")

        if name:
            message = "Hello, {}".format(name)
        else:
            message = "Hello, Stranger!"

        message += f"\nGreetings from Python version {platform.python_version()}"
        message += f"\nCurrent time: {datetime.now()}"
        message += f"\n{self.path[:-1]}"

        self.send_response(200)
        self.send_header("Content-Type", "text/plain")
        self.end_headers()
        self.wfile.write(message.encode())

        return
