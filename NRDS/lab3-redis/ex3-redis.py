import redis
from redis.cluster import ClusterNode

nodes = [ClusterNode('localhost', 7005), 
        ClusterNode('localhost', 7001),
        ClusterNode('localhost', 7002),
        ClusterNode('localhost', 7003)]

# Create a Redis cluster connection
rc = redis.RedisCluster(startup_nodes=nodes, decode_responses=True)

# Set 1000 keys in Redis
for i in range(1, 1001):
    rc.set(f"key{i}", f"value{i}")

print("Keys have been set!")

# You can now use redis-cli to connect to each shard and check DBSIZE
# Example of how to execute DBSIZE on each individual node using redis-cli:
# $ redis-cli -p 7000 DBSIZE
# $ redis-cli -p 7001 DBSIZE
# And so on for other nodes...

