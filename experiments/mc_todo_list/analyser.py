from .types import Task, Session


def tally_session(
    session: Session, tasks: [Task], importance_threshold: int
) -> (float, float, float):

    completed, completed_important, completed_in_time = 0, 0, 0
    num_tasks = len(tasks)

    for progress in session.progress:
        if progress.done:
            completed += 1
            task = next((t for t in tasks if t.name is progress.task_name))
            if task.priority >= importance_threshold:
                completed_important += 1
            if task.deadline <= session.id:
                completed_in_time += 1

    return (
        completed / num_tasks,
        completed_important / num_tasks,
        completed_in_time / num_tasks,
    )
