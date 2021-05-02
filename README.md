# yudzuki.py

An API Wrapper for YudzukiAPI

***

Installation
====
Stable:
```bash
#comming soon...
```

Beta:
```bash
#Windows
py -3 -m pip install git+https://github.com/LunaProject-Discord/yuduzki.py

#Linux
python3 -m pip install git+https://github.com/LunaProject-Discord/yuduzki.py
```

***
Usage:
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

Support
====
https://lunaproject.jp/support
