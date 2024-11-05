import redis
from redis.cluster import ClusterNode

# Connect to the Redis cluster
node = [ClusterNode('localhost', 7001)]
rc = redis.RedisCluster(startup_nodes=node, decode_responses=True)

# Add grades for each student in lab1, lab2, and lab3
rc.zadd("lab1", {"Alice": 7, "Bob": 7, "Charlie": 6})
rc.zadd("lab2", {"Alice": 8, "Bob": 7, "Charlie": 7})
rc.zadd("lab3", {"Alice": 9, "Bob": 8, "Charlie": 6})

# Calculate final grades manually since weights are not directly supported in zunionstore
# and also we need all keys must map to the same key slot using zunionstore
for student in ["Alice", "Bob", "Charlie"]:
    lab1_grade = rc.zscore("lab1", student) * 0.2
    lab2_grade = rc.zscore("lab2", student) * 0.2
    lab3_grade = rc.zscore("lab3", student) * 0.6
    final_grade = lab1_grade + lab2_grade + lab3_grade
    
    # Add to the final grades sorted set
    rc.zadd("final_grades", {student: final_grade})
    rc.zunionstore()

# Retrieve and print the final grades
final_grades = rc.zrange("final_grades", 0, -1, withscores=True)
print("Final Grades:")
for student, grade in final_grades:
    print(f"{student}: {grade:.2f}")