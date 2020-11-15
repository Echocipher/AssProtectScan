import argparse
import sys
from IPy import IP
import time
import socket
from multiprocessing.dummy import Pool as ThreadPool
from lib.config import *
from lib.exploit import *
import asyncio
from concurrent.futures import ThreadPoolExecutor

class AssProtectScan(object):
    def __init__(self, target, thread,service):
        self.target = target
        self.thread = thread
        self.service = service
        self.ips    = []
        self.ports  = []
        self.time   = time.time()
        self.get_ip()
        self.get_port(self.service)
        self.check = check()
    
    def get_ip(self):
        #获取待扫描地址段
        iplist = IP(self.target)
        for ip in list(iplist):
            self.ips.append(str(ip))

    def get_port(self,service):
        if service == "all":
            self.ports = list(p for p in services.values())
        else:
            self.ports = []
            inputserver = service.split(",")
            for service in inputserver:
                if service in services.keys():
                    self.ports.append(services[service])
                else:
                    print ("{}[-] Not support to check  {} !{}".format(R,service,W))
                    sys.exit(1)
    
    def scan(self, ip, port):
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(0.3)
            if s.connect_ex((ip, port)) == 0:
                print ("{}[*] Find {}:{} open, brute force..{}".format(B, ip, port, W))
                self.handle(ip, port)
        except Exception as e:
            print(e)
        except KeyboardInterrupt:
            print ('\n{}[-] 用户终止扫描...{}'.format(R, W))
            sys.exit(1)
        finally:
            s.close()

    def handle(self, ip, port):
        for v,k in services.items():
            if k == str(port):
                if v == 'mysql':
                    self.check.mysql(ip)
                elif v == 'mssql':
                    self.check.mssql(ip)
                elif v == 'oracle':
                    self.check.oracle(ip)
                elif v == 'postgresql':
                    self.check.postgresql(ip)
                elif v == 'redis':
                    self.check.redis(ip)
                elif v == 'mongodb':
                    self.check.mongodb(ip)
                elif v == 'memcached':
                    self.check.memcached(ip)
                elif v == 'ssh':
                    self.check.sshbrute(ip)
                elif v == 'ftp':
                    self.check.ftpbrute(ip)
                elif v == 'rsync':
                    self.check.rsyncscan(ip)
                elif v == 'php_fpm':
                    self.check.php_fpmscan(ip)
                elif v =='smb':
                    self.check.smbbrute(ip)
                elif v == 'zookeeper':
                    self.check.zookeeper(ip)
                elif v == 'docker':
                    self.check.docker(ip)
                else:
                    self.check.elasticsearch(ip)

    def run(self):
        loop = asyncio.get_event_loop()
        executor = ThreadPoolExecutor(self.thread)
        tasks = []
        for ip in self.ips:
            print ('{}[*] Checking... {} {}'.format(S, ip, W))
            for port in self.ports:
                task = loop.run_in_executor(executor, self.scan, ip, int(port))
                tasks.append(task)
        try:
            loop.run_until_complete(asyncio.wait(tasks))
        except Exception as e:
            pass
        except KeyboardInterrupt:
            pool.terminate()
            print ('\n{}[-] 用户终止扫描...{}'.format(R, W))
        finally:
            print ('-'*55)
            print ('{}[+] 扫描完成耗时 {} 秒.{}'.format(O, time.time()-self.time, W) )


def banner():
    banner = '''

   __    ___  ___    ___   ___    __    _  _ 
  /__\  / __)/ __)  / __) / __)  /__\  ( \( )
 /(__)\ \__ \\__ \  \__ \( (__  /(__)\  )  ( 
(__)(__)(___/(___/  (___/ \___)(__)(__)(_)\_)

        Refactoring weakscan to python3

       Author: Apri1y | Rock | Echocipher
       
                远离久坐，保护屁股
    '''
    print (B + banner + W)
    print('-'*55)

def main():
    banner()
    parser = argparse.ArgumentParser(description='Example: python {} 192.168.1.0/24'.format(sys.argv[0]))
    parser.add_argument('target', help=u'192.168.1.0/24')
    parser.add_argument('-s', type=str, default="all", dest='service',
                        help=u'all,php_fpm,mongodb,zookeeper,ssh,mysql,mssql,ftp,rsync,postgresql,redis,elasticsearch,oracle,memcached,smb,doker|默认 all,扫描多个用,隔开。例如:"ftp,mssql"')
    parser.add_argument('-t', type=int, default=70, dest='thread', help=u'线程数(默认50)')
    args   = parser.parse_args()
    myscan = AssProtectScan(args.target, args.thread,args.service)
    myscan.run()
if __name__ == '__main__':
    main()