import json

async def json_or_text(response):
    text = await response.text(encoding='utf-8')
    
    try:
        if response.headers['Content-Type'] == 'application/json':
            return json.loads(await response.json())
    except KeyError:
        pass

    return text

def staff_value(value):
    if value == 1:
        return "staff"
    elif value == 2:
        return "admin"
    elif value == 3:
        return "subowner"
    elif value == 4:
        return "owner"
    else:
        return "default"
