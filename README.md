# simpleCrawlerDrowzee
![Drowzee](https://github.com/mycode01/linkimages/blob/master/giggle/Drowzee.png)

월급도둑질하면서 만든 특정 사이트 크롤링 & 디스코드 웹훅 

## Installation
required     
* [Python 3.7+](https://www.python.org/downloads/) 

Use [PIP](https://pypi.org/) to build dependencies.

```bash
pip3 install virtualenv
virtualenv venv
source venv/bin/activate
pip install -r requirements.txt
deactivate
```

## Before Test
Before run, you need environment variables.

See the discord channel, get the environ variables, 
open `activate`file on `venv/bin/`, and 
put in that environ strings below `export PATH`.(it's around 54)
```bash
export PATH
export WEBHOOKURL="..."
export SOURCEURL="..."
``` 
save and restart venv.

## Build and test
```bash
(venv) python ./appMain.py
```
