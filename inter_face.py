import json
import requests
import asyncio

async def req():
    name = await requests.form.get('name')
    value = await requests.form.get('value')

    return (name,value)


