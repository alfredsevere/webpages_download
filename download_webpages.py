import requests
import threading

class DownloadThread(threading.Thread):
    def __init__(self, url):
        threading.Thread.__init__(self)
        self.url = url

    def run(self):
        response = requests.get(self.url)
        print(f"Downloaded {self.url}, length: {len(response.text)} chars")

def main(urls):
    threads = []

    for url in urls:
        thread = DownloadThread(url)
        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()

if __name__ == "__main__":
    urls = [
        "http://www.python.org",
        "http://www.google.com",
        "https://www.wikipedia.org",
        # Add more urls as needed
    ]

    main(urls)
