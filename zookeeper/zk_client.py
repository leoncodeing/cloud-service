# coding: utf-8
import logging
import kazoo.client
from ..httpserver import resolve_host


logger = logging.getLogger(name="kazoo")
logger.setLevel(logging.CRITICAL)


class ZKConnection(object):
    def __init__(self, zk_host, read_only=True):
        self.zk = kazoo.client.KazooClient(hosts=zk_host, read_only=read_only)

    def __enter__(self):
        self.zk.start()
        return self.zk

    def __exit__(self, type, value, traceback):
        if self.zk:
            self.zk.stop()
