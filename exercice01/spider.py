import os
import re
import requests
from urllib.parse import urlparse, urljoin
import argparse

class Page:
    def __init__(self, url, depth=5, path='./data'):
        self.url = url
        self.depth = depth
        self.path = path
        self.visited_urls = set()

    def download_images(self):
        self._recursive_download(self.url, self.depth)

    def _recursive_download(self, url, depth):
        if depth <= 0:
            return

        if url in self.visited_urls:
            return

        self.visited_urls.add(url)

        try:
            response = requests.get(url)
            if response.status_code == 200:
                img_urls = re.findall(r'<img[^>]*src=["\']([^"\']+)["\']', response.text)
                for img_url in img_urls:
                    img_url = urljoin(url, img_url)
                    img_ext = os.path.splitext(img_url)[1].lower()
                    if img_ext in ('.jpg', '.jpeg', '.png', '.gif', '.bmp'):
                        img_name = os.path.basename(urlparse(img_url).path)
                        img_path = os.path.join(self.path, img_name)
                        os.makedirs(os.path.dirname(img_path), exist_ok=True)
                        with open(img_path, 'wb') as f:
                            f.write(requests.get(img_url).content)
                for link in re.findall(r'<a\s+(?:[^>]*?\s+)?href=["\']([^"\']+)["\']', response.text):
                    next_url = urljoin(url, link)
                    self._recursive_download(next_url, depth - 1)
        except Exception as e:
            print(f"Error downloading images from {url}: {e}")

def main():
    parser = argparse.ArgumentParser(description="Download images recursively from a URL")
    parser.add_argument("-r", action="store_true", help="Recursively download images")
    parser.add_argument("-l", type=int, help="Maximum depth level of recursive download")
    parser.add_argument("-p", "--path", help="Path where downloaded files will be saved (default is ./data/)")
    parser.add_argument("url", help="URL of the page to download images from")
    args = parser.parse_args()

    if args.path:
        path = args.path
    else:
        path = './data'

    if args.l:
        depth = args.l
    else:
        depth = 5

    if args.r:
        page = Page(args.url, depth=depth, path=path)
    else:
        page = Page(args.url, depth=1, path=path)
    page.download_images()

if __name__ == "__main__":
    main()
