# Node-Based Pipeline Builder

This project is a node-based pipeline builder that allows users to visually create, connect, and analyze workflows using a drag-and-drop interface. It is inspired by modern no-code / low-code tools and focuses on flexibility, scalability, and clear architecture.

---

## 🚀 What This Project Does

- Allows users to create pipelines by dragging nodes onto a canvas
- Supports multiple node types such as Input, Text, LLM, and Output
- Enables connections between nodes to form a directed graph
- Sends the pipeline structure to a backend for analysis
- Validates whether the pipeline is a Directed Acyclic Graph (DAG)

---

## 🧩 Key Features

### 1. Reusable Node Abstraction

- All nodes are built on top of a shared base abstraction
- Reduces duplicated code and makes it easy to add new node types
- Ensures consistent structure and behavior across nodes

### 2. Dynamic Text Node

- Automatically resizes as the user types
- Supports dynamic variables like {{input}} which dynamically generate input handles

### 3. Visual Pipeline Builder

- Drag-and-drop interface using React Flow
- Smooth connections between nodes
- Clear visualization of data flow

### 4. Backend Integration & DAG Validation

- Frontend sends nodes and edges to a FastAPI backend
- Backend calculates:
- Number of nodes
- Number of edges
- Whether the pipeline forms a DAG
- Uses graph traversal logic to detect cycles
- Results are shown to the user instantly via alerts

---

## 🛠 Tech Stack

### Frontend

- React
- React Flow
- Zustand (state management)

### Backend

- Python
- FastAPI
- Uvicorn

---

## ▶️ How to Run the Project

### Frontend

```bash
cd frontend
npm install
npm start

```
