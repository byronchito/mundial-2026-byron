from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
import webbrowser


PORT = 8000
APP_DIR = Path(__file__).resolve().parent


class AppHandler(SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=str(APP_DIR), **kwargs)


if __name__ == "__main__":
    address = ("127.0.0.1", PORT)
    url = f"http://{address[0]}:{address[1]}/index.html"
    print(f"App lista en: {url}")
    print("Para cerrar, presiona Ctrl + C")
    webbrowser.open(url)
    ThreadingHTTPServer(address, AppHandler).serve_forever()
