from diskcache import Cache
import config

cache = Cache(config.CACHE_DIR)

def add_to_set(set_name, value):
    """Add a value to a cached set."""
    s = cache.get(set_name, default=set())
    if value not in s:
        s.add(value)
        cache.set(set_name, s)

def pop_from_set(set_name):
    """Retrieve and remove a value from the cached set."""
    s = cache.get(set_name, default=set())
    if not s:
        return None
    value = s.pop()
    cache.set(set_name, s)
    return value

def set_contains(set_name, value):
    """Check if a value exists in the cached set."""
    return value in cache.get(set_name, default=set())

def set_cardinality(set_name):
    """Return the size of the cached set."""
    return len(cache.get(set_name, default=set()))

print("✅ Cache system initialized!")
