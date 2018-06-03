#!/usr/local/bin/python3

import sys
import os
import logging
import logging.handlers
import json
import re


class Redirector:
    def __init__(self):
        self.base_dir = '/etc/squid_redirector'
        self.redirectors_file = os.path.join(self.base_dir, 'squid_redirector.json')
        self.redirectors = {}
        self.logger = self.get_logger()
        self.last_redirectors_modify = 0
        self.f = open('5.txt', 'w')
        self.start()

    def start(self):
        for line in sys.stdin:
            if self.last_redirectors_modify != os.stat(self.redirectors_file):
                self.update_redirectors()

            self.logger.info(line + '\n')
            self.f.write(line + '\n')
            self.f.flush()
            temp = line.split()
            if not temp:
                continue

            url = temp[0]
            redirect_url = self.get_redirect_by_url(url)
            if redirect_url == url:
                out = '%s\n' % url
            else:
                out = '302:http://%s\n' % redirect_url 
            
            sys.stdout.write(out)
            sys.stdout.flush()

        self.f.close()

    def get_redirect_by_url(self, url):
        for u in self.redirectors:
            if u in url:
                return self.redirectors[u]
        return url

    # MB NOT HAVE MEMORY!!!!!
    def update_redirectors(self):
        with open(self.redirectors_file, 'r') as f:
            data = f.read()
        self.redirectors = json.loads(data)

    def configurate_logging(self):
        self.check_log_file_exists()
        logging.basicConfig(filename=self.log_path,
            format='%(asctime)s %(levelname)s - %(message)s')

    def check_log_file_exists(self):
        if not os.path.exists(self.log_dir):
            os.makedirs(self.log_dir)

        if not os.path.exists(self.log_path):
            open(self.log_path, 'w').close()

    def get_logger(self):
        logger = logging.getLogger('myLogger')
        logger.setLevel(logging.INFO)

        handler = logging.handlers.SysLogHandler('/dev/log')
        formatter = logging.Formatter('%(asctime)s %(levelname)s - %(message)s')
        handler.formatter = formatter
        logger.addHandler(handler)

        return logger


if __name__ == '__main__':
    Redirector()