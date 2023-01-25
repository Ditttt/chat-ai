import aiohttp
import asyncio
import sys


class ChatGpt:
    @staticmethod
    async def chat_gpt(inp):
        async with aiohttp.ClientSession() as session:
            api_key = "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"
            payload = {
                "model": "text-davinci-003",
                "prompt": inp,
                "temperature": 0.5,
                "max_tokens": 2048,
                "presence_penalty": 0,
                "frequency_penalty": 0,
                "best_of": 1,
            }
            headers = {
                "Authorization": f"Bearer {api_key}"
            }
            async with session.post(
                "https://api.openai.com/v1/completions", json=payload, headers=headers
            ) as resp:
                if resp.status != 200:
                    teks = f'\033[1m\033[31mError: API request failed with status code || {resp.status}\033[0m\033[0m'
                    return teks
                else:
                    response = await resp.json()
                    return f'\033[92m{response["choices"][0]["text"][2:]}\033[0m'