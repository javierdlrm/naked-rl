from .policies import Policy, older_first
from .simulator import run_simulation


class MonteCarloTodoList:
    def __init__(
        self,
        deadline,
        max_priority,
        max_task_duration,
        max_session_duration,
        max_complexity,
        importance_threshold,
    ):
        self.deadline = deadline
        self.max_priority = max_priority
        self.max_task_duration = max_task_duration
        self.max_session_duration = max_session_duration
        self.max_complexity = max_complexity
        self.importance_threshold = importance_threshold

        print(f"Monte Carlo To-Do List created")

    def run_simulations(self, num_simulations: int, policy: Policy) -> [dict]:
        progress = []
        for i in range(0, num_simulations):
            print(f"Running simulation {i + 1} ...", end=" ")
            session_progress = run_simulation(
                deadline,
                max_priority,
                max_task_duration,
                max_session_duration,
                max_complexity,
                importance_threshold,
                policy,
            )
            print("done")

            progress.append({"simulation": i, "progress": session_progress})
        return progress


if __name__ == "__main__":

    # list settings
    deadline = 20
    importance_threshold = 4
    max_priority = 5
    max_task_duration = 6
    max_session_duration = 4
    max_complexity = 3

    # create mc list
    mc = MonteCarloTodoList(
        deadline,
        max_priority,
        max_task_duration,
        max_session_duration,
        max_complexity,
        importance_threshold,
    )

    # run simulations
    progress = mc.run_simulations(num_simulations=20, policy=older_first)

    completed = sum(
        [1 for sp in progress if sum([p["completed"] for p in sp["progress"]]) == 100]
    )

    print(f"Done: All tasks completed in {completed} simulations")
