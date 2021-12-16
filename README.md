# yudzuki.py

LunaProject公式APIライブラリ / An API Wrapper for YudzukiAPI

***
Installation
====
安定版 / Stable:
```bash
#comming soon...
```

ベータ版 / Beta:
```bash
#Windows
$ py -3 -m pip install git+https://github.com/LunaProject-Discord/yuduzki.py
$ py -3 -m pip install git+ssh://git@github.com/LunaProject-Discord/yudzuki.py

#Linux
$ python3 -m pip install git+https://github.com/LunaProject-Discord/yuduzki.py
$ python3 -m pip install git+ssh://git@github.com/LunaProject-Discord/yudzuki.py
```

***
使用法 / Usage
====
```python
import yudzuki
import asyncio

client = yudzuki.YudzukiClient("YudzukiAPI Token Here")

async def coro(user_id:int):
    result = await client.get_user(user_id)
    print(result)

loop = asyncio.get_event_loop()
loop.run_until_complete(coro(546682137240403984))

-> Midorichan#3451
```

***
Requirements
====
* **Python 3.8**
* **aiohttp**
* **urllib**

***
サポート / Support
====
https://lunaproject.jp/support
