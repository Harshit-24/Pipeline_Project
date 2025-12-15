from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from typing import Dict, List

app = FastAPI()

# ✅ CORS CONFIG (IMPORTANT)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # allow frontend
    allow_credentials=True,
    allow_methods=["*"],  # allow POST, OPTIONS, etc.
    allow_headers=["*"],
)


@app.get("/")
def read_root():
    return {"Ping": "Pong"}


@app.post("/pipelines/parse")
def parse_pipeline(payload: Dict):
    nodes: List[Dict] = payload.get("nodes", [])
    edges: List[Dict] = payload.get("edges", [])

    num_nodes = len(nodes)
    num_edges = len(edges)

    # Build graph
    graph = {node["id"]: [] for node in nodes}
    for edge in edges:
        graph[edge["source"]].append(edge["target"])

    visited = set()
    stack = set()

    def has_cycle(node):
        visited.add(node)
        stack.add(node)
        for neighbor in graph.get(node, []):
            if neighbor not in visited:
                if has_cycle(neighbor):
                    return True
            elif neighbor in stack:
                return True
        stack.remove(node)
        return False

    is_dag = True
    for node in graph:
        if node not in visited:
            if has_cycle(node):
                is_dag = False
                break

    return {
        "num_nodes": num_nodes,
        "num_edges": num_edges,
        "is_dag": is_dag,
    }
