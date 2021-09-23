#encoding : utf-8
import os
import ConfigParser
import argparse

parser = argparse.ArgumentParser(description='start cloud service')
configuration = ConfigParser.configParser()

def add_argument(*args,**kwargs):
    parser.add_argument(*args,**kwargs)

def read_config(global_symbol_table):
    parser.add_argument('-b', '--bind', dest='bind', help='bind ip address.')
    parser.add_argument('-p', '--port', dest='port', help='listen port.')
    parser.add_argument('-c', '--config', dest='config', default='config', help='specify the location of the config file.')
    parser.add_argument('-d', '--debug', dest='debug', default=False, action='store_true', help='debug option.')
    parser.add_argument('-z', '--zookeeper', dest='zookeeper', default='', help='Zookeeper host. Override config file. Do not use zookeeper when `ignore`')

    args = parser.parse_args()

    if os.path.exists(args.config):
        configuration.read(args.config)
        if args.bind:
            configuration.set('main','bind',value=args.bind)
        if args.port:
            configuration.set('main', 'port', value=args.port)
        if args.zookeeper:
            configuration.set('zookeeper', 'host', value=args.zookeeper)
    else:
        parser.print_help()

    debug = args.debug

    if configuration.has_option('main', 'debug') and configuration.getboolean('main', 'debug'):
        debug = True
    env = configuration.get('main', 'env')

    #from cloudservice.zookeeper import ZookeeperClient
    #zk = ZookeeperClient(configuration.get('zookeeper', 'host'))

    #global_symbol_table['DEBUG'] = debug
    #global_symbol_table['ENV'] = env
    #global_symbol_table['zk'] = zk
    #global_symbol_table['args'] = args


