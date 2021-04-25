import json

async def json_or_text(response):
    text = await response.text(encoding='utf-8')
    
    try:
        if response.headers['content-type'] == 'application/json':
            return json.loads(text)
    except KeyError:
        pass

    return text