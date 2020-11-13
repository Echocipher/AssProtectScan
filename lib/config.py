#coding:utf-8
#扫描的服务类型及默认对口
services = {'ftp':'21',
            'ssh':'22',
            'smb':'445',
            'rsync': '873',
            'zookeeper': '2181',
            'docker': '2375',
            'php_fpm':'9000',
            'mssql':'1433',
            'oracle':'1521',
            'mysql':'3306',
            'postgresql':'5432',
            'redis':'6379',
            'elasticsearch':'9200',
            'memcached':'11211',
            'mongodb':'27017',
            'hadoop':'50070'}
       

passwd = ['123456' ,'qwe123!@#', 'admin', 'root', 'password', '123123', '123', '1', '', '{user}','{user}{user}','{user}1','{user}123','{user}2020','{user}2019','{user}!','oracle','P@ssw0rd!!','qwa123','12345678','test','123qwe!@#','123456789','123321','1314520','666666','woaini','fuckyou','000000','1234567890','8888888','qwerty','1qaz2wsx','abc123','abc123456','1q2w3e4r','123qwe','159357','p@ssw0rd','p@55w0rd','password!', 'p@ssw0rd!','password1','r00t','system','111111','admin','654321','321','1234567','12345678','88888888','pass','passwd','sinoxms123','!QA@WS','passw0rd','0p;/.lo(','Huawei12#$','Changeme123','Changeme_123','suhui12!','changeme','Passw0rdpLjk3a','poly123']

#colour
W = '\033[0m'
G = '\033[1;32m'
O = '\033[1;33m'
R = '\033[1;31m'
B = '\033[1;34m'
S = '\033[90m'

#oracle默认用户及密码
oracle_user = ['sys','system','sysman','scott','aqadm','Dbsnmp','system']
oracle_pass_default = ['','manager','oem_temp','tiger','aqadm','dbsnmp','oracle']

#ftp常见用户
ftp_user = ['ftp', 'ftproot', 'www','root', 'admin', 'user', 'test', 'web',
            'administrator', 'oracle', 'server', 'data',  'access','sys_base','admintrade']

#ssh 常见用户
ssh_user = ['ubuntu','root', 'weblogic', 'oracle', 'db2admin']

