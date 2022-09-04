from dataclasses import dataclass


@dataclass
class Task:
    name: str
    priority: int
    duration: int
    complexity: int
    deadline: int
    done: bool = False


@dataclass
class List:
    name: str
    tasks: [Task]
    deadline: int
    done: bool = False


@dataclass
class Progress:
    task_name: str
    duration: int
    done: bool = False


@dataclass
class Session:
    id: int
    name: str
    duration: int
    progress: [Progress]
