import os, os.path as op
from typing import List


class Config:
    def __init__(self):
        # User, Password for https://wenshuapp.court.gov.cn
        self.username = "18810721592"
        self.password = "Abc#123456"

        # User-Agent for Headers
        self.ua_list = [
            'Mozilla/5.0 (iPhone; CPU OS 10_15_5 (Ergänzendes Update) like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.1.1 Mobile/14E304 Safari/605.1.15',
            'Mozilla/5.0 (Linux; Android 11; SAMSUNG-SM-T377A Build/NMF26X) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Mobile Safari/537.36',
        ]

        # General Config for Crawler
        self.use_cache = True
        self.do_split = True
        self.num_workers = 80

        # Common Files
        # directories
        self.driver_dir = "driver"
        self.cache_dir = "cache"
        self.data_dir = "data"
        self.split_dir = op.join(self.data_dir, "split")
        # driver file
        self.driver_path = op.join(self.driver_dir, "chromedriver.exe")
        # cache files
        self.headers_path = op.join(self.cache_dir, "headers.json")
        self.lock_path = op.join(self.cache_dir, "lock")
        # data files
        self.court_path = op.join(self.data_dir, "court.json")  # Stage 0
        self.query_length_path = op.join(self.data_dir, "query_length.json")  # Stage II
        self.doc_index_path = op.join(self.data_dir, "doc_index.json")  # Stage III
        self.proc_result_path = op.join(self.split_dir, "result_{}.json")  # Stage IV
        self.result_path = op.join(self.data_dir, "result.json")  # Stage IV

        # 文件检查和预创建（不检查driver文件夹）
        folders = [self.cache_dir, self.data_dir, self.split_dir]
        for folder in folders:
            if not op.exists(folder):
                os.makedirs(folder)
