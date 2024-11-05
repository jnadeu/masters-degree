# brew_coffee.py
import time
import random
import redis as r
import uuid


LOCK_TIMEOUT = 5

# Create a Redis client
redis = r.Redis(host='localhost', port=6379, decode_responses=True)

def acquire_lock():
    lock_id = str(uuid.uuid4())  # Generate a unique lock ID
    # Attempt to acquire the lock with a timeout
    if redis.set("lock_key", lock_id, nx=True, ex=LOCK_TIMEOUT):
        return lock_id
    return None

def release_lock(lock_id):
    # Script to ensure that only the holder can release the lock
    script = """
    if redis.call('get', KEYS[1]) == ARGV[1] then
        return redis.call('del', KEYS[1])
    else
        return 0
    end
    """
    redis.eval(script, 1, "lock_key", lock_id)

def brew_coffee():
    # This function simulates a shared resource (coffee machine) that
    # can only be used by a single user (process) at the same time.
    # It takes 300ms to prepare a cup of coffee
    for i in range(3):
        print(".", end="", flush=True)
        time.sleep(0.1)
        print("Ready")


if __name__ == "__main__":
    while True:
        lock_id = acquire_lock()
        if lock_id:
            try:
                brew_coffee()
            finally:
                release_lock(lock_id)
        else:
            print("I also need my coffee!")
            time.sleep(0.2)
        time.sleep(0.03)
