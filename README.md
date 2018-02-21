# SumUp-Analytics-Test
SumUp Analytics Full-Stack Development Test - Thibaut Fenain (thibautfenain1@gmail.com)

# Python Quick Start Guide

This guide will walk you through deploying a Python / Flask application on [Deis Workflow][].

## Usage

```console
$ git clone https://github.com/thiblades/SumUp_Analytics_Test.git
$ cd SumUp_Analytics_Test
$ pip3 install -r requirements.txt
       Collecting Flask==0.12.0 (from -r requirements.txt (line 1))
  Downloading Flask-0.12-py2.py3-none-any.whl (82kB)
    100% |████████████████████████████████| 92kB 1.1MB/s 
Collecting Jinja2==2.8.1 (from -r requirements.txt (line 2))
  Downloading Jinja2-2.8.1-py2.py3-none-any.whl (264kB)
    100% |████████████████████████████████| 266kB 1.2MB/s 
Collecting click>=2.0 (from Flask==0.12.0->-r requirements.txt (line 1))
  Downloading click-6.7-py2.py3-none-any.whl (71kB)
    100% |████████████████████████████████| 71kB 1.3MB/s 
Collecting itsdangerous>=0.21 (from Flask==0.12.0->-r requirements.txt (line 1))
  Downloading itsdangerous-0.24.tar.gz (46kB)
    100% |████████████████████████████████| 51kB 1.4MB/s 
Collecting Werkzeug>=0.7 (from Flask==0.12.0->-r requirements.txt (line 1))
  Downloading Werkzeug-0.14.1-py2.py3-none-any.whl (322kB)
    100% |████████████████████████████████| 327kB 1.1MB/s 
Collecting MarkupSafe (from Jinja2==2.8.1->-r requirements.txt (line 2))
  Downloading MarkupSafe-1.0.tar.gz
Building wheels for collected packages: itsdangerous, MarkupSafe
  Running setup.py bdist_wheel for itsdangerous ... done
  Stored in directory: /home/thibaut/.cache/pip/wheels/fc/a8/66/24d655233c757e178d45dea2de22a04c6d92766abfb741129a
  Running setup.py bdist_wheel for MarkupSafe ... done
  Stored in directory: /home/thibaut/.cache/pip/wheels/88/a7/30/e39a54a87bcbe25308fa3ca64e8ddc75d9b3e5afa21ee32d57
Successfully built itsdangerous MarkupSafe
Installing collected packages: MarkupSafe, Jinja2, click, itsdangerous, Werkzeug, Flask
Successfully installed Flask-0.12 Jinja2-2.8.1 MarkupSafe-0.23 Werkzeug-0.14.1 click-6.7 itsdangerous-0.24
You are using pip version 8.1.1, however version 9.0.1 is available.
You should consider upgrading via the 'pip install --upgrade pip' command.

$python3 app.py
 * Running on http://localhost:7777/ (Press CTRL+C to quit)
127.0.0.1 - - [21/Feb/2018 11:27:22] "GET / HTTP/1.1" 200 -

```
