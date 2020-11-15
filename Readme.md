# AssProtectScan



`AssProtectScan`是将`WeakScan`利用`Python3`重构的版本，其中改写了部分流程以及检测方法，增加了部分字典参数，最终扫描成功结果会保存到`AssProtectScan.py`所在目录的`result.txt`中。

## 支持漏洞

目前支持对以下漏洞进行检测

- `mysql`弱口令爆破 
- `redis`弱口令爆破
- `ssh`弱口令爆破
- `ftp`弱口令爆破
- `postgresql`弱口令爆破
- `oracle`弱口令爆破
- `mssql`弱口令爆破
- `smb`弱口令爆破
- `redis`未授权访问
- `mongodb`未授权访问
- `Memcached`未授权访问
- `elasticsearch`未授权访问
- `ftp`未授权访问
- `rsync`未授权访问
- `zookeeper`未授权访问
- `docker`未授权访问
- `php_fpm`未授权访问

## 环境配置

`AssProtectScan`基于[Python 3.6.0](https://www.python.org/downloads/release/python-360/)开发和测试，安装Python环境可以参考[Python 3 安装指南](https://pythonguidecn.readthedocs.io/zh/latest/starting/installation.html#python-3)。运行以下命令检查`Python`和`pip3`版本：

```
python -V
pip3 -V
```

如果你看到类似以下的输出便说明Python环境没有问题：

```
Python 3.6.0
pip 19.2.2 from C:\Users\shmilylty\AppData\Roaming\Python\Python36\site-packages\pip (python 3.6)
```

开始使用

```
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
python3 get-pip.py
git clone https://github.com/Echocipher/AssProtectScan.git
cd AssProtectScan
pip3 install -r requirements.txt
python3 AssProtectScan.py -h
```

## 使用说明

用法如下

```
python3 AssProtectScan.py [-h] [-s SERVICE] [-t THREAD] target
```

具体参数值代表含义如下表所示

| 参数值 | 功能         |
| ------ | ------------ |
| -h     | 查看帮助信息 |
| -s     | 设置服务信息 |
| -t     | 设置线程数目 |
| target | 设置目标信息 |

### 实例说明

#### 获取帮助信息

```
python3 AssProtectScan.py -h
```

或者可以使用`--help`参数

```
python3 AssProtectScan.py --help
```

#### 检测的服务类型

目前`-s`参数共支持以下参数，分别对应相应类型的漏洞检测

```
all
php_fpm
mongodb
zookeeper
ssh
mysql
mssql
ftp
rsync
postgresql
redis
elasticsearch
oracle
memcached
smb
doker
```

默认 `all`，扫描多个用`,`隔开。例如：`"ftp,mssql"`

##### 检测所有服务类型

```
python3 AssProtectScan.py 192.168.0.1/24
```

##### 检测`ssh`以及`mysql`

```
python3 AssProtectScan.py -s "ssh,mysql" 192.168.0.1/24
```

#### 脚本线程数

线程数`-t`默认为`50`

```
python3 AssProtectScan.py -t 100 192.168.0.1/24
```

#### 目标

`target`是我们要配置的目标，支持单个`IP`及网段配置

##### 检测单个IP

```
python3 AssProtectScan.py 192.168.0.1
```

##### 检测整个C段

```
python3 AssProtectScan.py 192.168.0.1/24
```

