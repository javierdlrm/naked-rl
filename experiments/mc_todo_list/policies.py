from typing import Protocol
from .types import Task, List


class Policy(Protocol):
    def __call__(self, lists: [List]) -> Task:
        ...


def older_first(lists: [List]) -> (Task, List):
    tasks = [t for l in lists for t in l.tasks if not t.done]
    if len(tasks) == 0:
        return None, None
    task = tasks[0]
    list_ = next((l for l in lists if task in l.tasks))
    return task, list_


def recent_first(lists: [List]) -> (Task, List):
    tasks = [t for l in lists for t in l.tasks if not t.done]
    if len(tasks) == 0:
        return None, None
    task = tasks[-1]
    list_ = next((l for l in lists if task in l.tasks))
    return task, list_


def closer_deadline_first(lists: [List]) -> (Task, List):
    tasks = [t for l in lists for t in l.tasks if not t.done]
    return sorted(tasks, key=lambda t: t.deadline)


def further_deadline_first(lists: [List]) -> (Task, List):
    tasks = [t for l in lists for t in l.tasks if not t.done]
    return sorted(tasks, key=lambda t: t.deadline, reverse=True)


def priority_first(lists: [List]) -> (Task, List):
    tasks = [t for l in lists for t in l.tasks if not t.done]
    return sorted(tasks, key=lambda t: t.priority, reverse=True)


def redundant_first(lists: [List]) -> (Task, List):
    tasks = [t for l in lists for t in l.tasks if not t.done]
    return sorted(tasks, key=lambda t: t.priority)


def complex_first(lists: [List]) -> (Task, List):
    tasks = [t for l in lists for t in l.tasks if not t.done]
    return sorted(tasks, key=lambda t: t.complexity, reverse=True)


def easy_first(lists: [List]) -> (Task, List):
    tasks = [t for l in lists for t in l.tasks if not t.done]
    return sorted(tasks, key=lambda t: t.complexity)


def timeconsuming_first(lists: [List]) -> (Task, List):
    tasks = [t for l in lists for t in l.tasks if not t.done]
    return sorted(tasks, key=lambda t: t.duration, reverse=True)


def brief_first(lists: [List]) -> (Task, List):
    tasks = [t for l in lists for t in l.tasks if not t.done]
    return sorted(tasks, key=lambda t: t.duration)


def easy_important_first(lists: [List]) -> (Task, List):
    tasks = [t for l in lists for t in l.tasks if not t.done]
    return sorted(tasks, key=lambda t: t.complexity / t.priority)


def easy_closed_deadline_first(lists: [List]) -> (Task, List):
    tasks = [t for l in lists for t in l.tasks if not t.done]
    return sorted(tasks, key=lambda t: t.complexity / t.deadline)
