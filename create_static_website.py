import requests
import time
import uvicorn
import threading
import contextlib
import itertools

from webapp import app, languages


def convert_webapp_to_html_files():
    url_list = ["", "imprint", "publications", "privacy"]
    url_base = "http://127.0.0.1:5001"

    for item in itertools.product(languages, url_list):
        locale, url = item
        r = requests.get(url_base + "/" + locale + "/" + url)

        if url == "":
            fname = "index"
        else:
            fname = url

        with open(f"{fname}_{locale}.html", "w") as fp:
            html_text = r.text

            # replace href to other endpoints with html files
            for href in url_list[1:]:
                html_text = html_text.replace(
                    f'href="{url_base}/{locale}/{href}"', f'href="{href}_{locale}.html"'
                )
                html_text = html_text.replace(
                    f'href="/{locale}"', f'href="index_{locale}.html"'
                )

            # fix href to css, js, and images files in the static folder
            html_text = html_text.replace("../static", "static")
            html_text = html_text.replace(url_base + "/static", "static")

            fp.write(html_text)


class Server(uvicorn.Server):
    def install_signal_handlers(self):
        # overload this method which otherwise only work in main thread
        pass

    @contextlib.contextmanager
    def run_in_thread(self):
        thread = threading.Thread(target=self.run)
        thread.start()
        try:
            while not self.started:
                time.sleep(1e-3)
            yield
        finally:
            self.should_exit = True
            thread.join()


config = uvicorn.Config(
    app, host="127.0.0.1", port=5001, log_level="info", loop="asyncio"
)
server = Server(config=config)


with server.run_in_thread():
    convert_webapp_to_html_files()
