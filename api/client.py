import asyncio
import aiohttp
from app_logging import logger


class APIClient:
    def __init__(self, base_urls, timeout=30):
        self.base_urls = base_urls
        self.current_base_url = base_urls[0]
        self.timeout = timeout

    def _build_url(self, url_template, **url_params):
        return self.current_base_url + url_template.format(**url_params)

    async def _request(self, method, url_template, **request_kwargs):
        url_params = {k: v for k, v in request_kwargs.items() if k not in ['json', 'data', 'headers', 'params']}
        url = self._build_url(url_template, **url_params)

        for base_url in self.base_urls:
            self.current_base_url = base_url
            try:
                async with aiohttp.ClientSession() as session:
                    async with session.request(method, url, **{k: v for k, v in request_kwargs.items() if k in ['json', 'data', 'headers', 'params']}) as response:
                        if 400 <= response.status < 500:
                            logger.error(f"Client error {response.status} for {url}")
                            return False
                        elif 500 <= response.status < 600:
                            logger.error(f"Server error {response.status} for {url}")
                            return None
                        response.raise_for_status()
                        return await response.json()
            except asyncio.TimeoutError:
                logger.error(f"Timeout error for {url}")
            except aiohttp.ClientResponseError as e:
                logger.error(f"Error {e.status} for {url}: {e.message}")
                if 400 <= e.status < 500:
                    return False
                elif 500 <= e.status < 600:
                    return None
            except aiohttp.ClientError as e:
                logger.error(f"Request error for {url}: {e}")
        logger.error(f"Failed to complete request after trying all base URLs")
        return None

    async def get(self, url_template, **kwargs):
        return await self._request('GET', url_template, **kwargs)

    async def post(self, url_template, data=None, json=None, **kwargs):
        return await self._request('POST', url_template, data=data, json=json, **kwargs)

    async def put(self, url_template, data=None, json=None, **kwargs):
        return await self._request('PUT', url_template, data=data, json=json, **kwargs)

    async def delete(self, url_template, **kwargs):
        return await self._request('DELETE', url_template, **kwargs)
