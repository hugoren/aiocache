import logging

from .backends.memory import SimpleMemoryCache
from ._version import __version__


logger = logging.getLogger(__name__)
__cache_types = [SimpleMemoryCache]

try:
    import aioredis
except ImportError:
    logger.info("aioredis not installed, RedisCache unavailable")
else:
    from aiocache.backends.redis import RedisCache

    __cache_types.append(RedisCache)
    del aioredis

try:
    import aiomcache
except ImportError:
    logger.info("aiomcache not installed, Memcached unavailable")
else:
    from aiocache.backends.memcached import MemcachedCache

    __cache_types.append(MemcachedCache)
    del aiomcache


from .factory import caches, Cache  # noqa: E402
from .decorators import cached, cached_stampede, multi_cached  # noqa: E402


__all__ = (
    "caches",
    "Cache",
    "cached",
    "cached_stampede",
    "multi_cached",
    *__cache_types,
    "__version__",
)
