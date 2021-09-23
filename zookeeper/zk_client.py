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

class ZookeeperClient(object):
    BASE_PATH = "/cloud_service"
    BASE_COMMON_PATH = "/cloud_service/common"
    HOST_SCRIBE_PATH = BASE_COMMON_PATH + '/scribe'

def __init__(self,zk_Host):
        self.zk_Host = resolve_host(zk_Host)

    def get(self,path,with_stat=False):
        with ZKConnection(self.zk_Host) as zk:
            if zk.exists(path):
                value, stat = zk.get(path)
                logging.info('zk:get %s ,%s ', path, value)
                if with_stat:
                    return value,stat
                else:
                    return value
            else:
                logging.error("zk:get %s get none", path)
                return None
    def set(self,path,value):
        with ZKConnection(self.zk_Host,read_only=False) as zk:
            logging.info('zk:set %s, %s',path,value)
            if zk.exists(path):
                zk.set(self,path,value)
            else:
                zk.create(self,path,value=value,makepath=True)

    def get_subscribed_host(self):
        return self.get(self.HOST_SCRIBE_PATH)

if __name__ == "__main__":
    z = ZookeeperClient('localhost:2181')
