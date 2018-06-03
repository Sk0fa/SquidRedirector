#!/usr/bin/python3
import sys
import os
import logging
import logging.handlers
import json
import re


class Redirector:
    def __init__(self):
        sys.excepthook = self.except_hook
        self.base_dir = '/etc/squid-redirect'
        self.redirects_file = os.path.join(self.base_dir, 'squid_redirector.json')
        self.redirects = {}
        self.logger = self.get_logger()
        self.last_redirects_modify = 0
        self.domain_re = re.compile(r'https?://([a-zA-Z0-9\.-]+)(?:/.*?)?')

    def start(self):
        for line in sys.stdin:
            if self.last_redirects_modify != os.stat(self.redirects_file):
                self.update_redirects()
                self.last_redirects_modify = os.stat(self.redirects_file)

            request_info = line.split()
            if not request_info:
                continue
            self.handle_request(request_info[0])          

    def handle_request(self, url):
        redirect_url = self.get_redirect_by_url(url)
        if redirect_url == url:
            out = '%s\n' % url
            self.logger.info('%s is not redirect\n' % url)
        else:
            out = '302:http://%s\n' % redirect_url 
            self.logger.info('%s redirect to %s\n' % (url, redirect_url))
            
        sys.stdout.write(out)
        sys.stdout.flush()

    def get_redirect_by_url(self, url):
        match = self.domain_re.search(url)

        for u in self.redirects:
            if match and u in match.group(1):
                return self.redirects[u]

        return url

    def update_redirects(self):
        with open(self.redirects_file, 'r') as f:
            data = f.read()

        self.redirects = json.loads(data)

    def get_logger(self):
        logger = logging.getLogger('squidRedirectLogger')
        logger.setLevel(logging.INFO)

        handler = logging.handlers.SysLogHandler('/dev/log')
        formatter = logging.Formatter('Squid-Redirector: %(levelname)s - %(message)s')
        handler.formatter = formatter
        logger.addHandler(handler)

        return logger

    def except_hook(self, exctype, value, traceback):
        if exctype == KeyboardInterrupt:
            sys.__excepthook__(exctype, value, traceback)
            return

        self.logger.error("Error: ", exc_info=(exctype, value, traceback))
        sys.exit(1)


if __name__ == '__main__':
    Redirector().start()