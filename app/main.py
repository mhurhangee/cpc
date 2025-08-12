from neo4j import GraphDatabase
import os

from utils.env_loader import load_project_env

load_project_env()

print("NEO4J_PASSWORD:", os.getenv("NEO4J_PASSWORD"))

uri=os.getenv("NEO4J_URI","bolt://localhost:7687")
user="neo4j"
pw=os.getenv("NEO4J_PASSWORD")
with GraphDatabase.driver(uri,auth=(user,pw)).session() as s:
 print(s.run("RETURN 1 AS ok").single()["ok"])
