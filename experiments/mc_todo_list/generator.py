import random as rd
from .types import Task, List, Session


class Generator:
    def __init__(
        self,
        max_priority: int,
        max_task_duration: int,
        max_session_duration: int,
        max_complexity: int,
    ):

        self.max_priority = max_priority
        self.max_task_duration = max_task_duration
        self.max_session_duration = max_session_duration
        self.max_complexity = max_complexity

    def tasks(self, num_tasks: int, deadline: int):
        return [self._get_task(i, deadline) for i in range(0, num_tasks)]

    def _get_task(self, id: int, deadline: int):
        return Task(
            name=f"Task {id}",
            priority=rd.randint(1, self.max_priority),
            duration=rd.randint(1, self.max_task_duration),
            complexity=rd.randint(1, self.max_complexity),
            deadline=rd.randint(deadline * 0.75, deadline),
            done=False,
        )

    def lists(self, tasks: [[Task]]):
        return [self._get_list(i, tsks) for i, tsks in enumerate(tasks)]

    def _get_list(self, id: int, tasks: [Task]):
        return List(
            name=f"List {id}",
            tasks=tasks,
            deadline=max([t.deadline for t in tasks]),
            done=False,
        )

    def sessions(self, deadline: int):
        return [self._get_session(i) for i in range(0, deadline)]

    def _get_session(self, i: int):
        return Session(
            id=i,
            name=f"Session {i}",
            duration=rd.randint(
                self.max_session_duration * 0.75, self.max_session_duration
            ),
            progress=None,
        )
