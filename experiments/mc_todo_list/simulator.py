from .generator import Generator
from .types import Session, List, Progress
from .analyser import tally_session
from .policies import Policy


def run_session(session: Session, lists: [List], policy: Policy) -> Session:

    session.progress = []

    while session.duration > 0:

        # apply policy
        task, list_ = policy(lists)

        if task is None:
            break

        progress = None
        if task.duration <= session.duration:  # complete task
            session.duration -= task.duration
            progress = Progress(task.name, task.duration, True)
            task.done = True
            list_.done = all([t.done for t in list_.tasks])
        else:  # consume session
            task.duration -= session.duration
            progress = Progress(task.name, session.duration, False)
            task.duration = False
            session.duration = 0

        session.progress.append(progress)


def run_simulation(
    deadline: int,
    max_priority: int,
    max_task_duration: int,
    max_session_duration: int,
    max_complexity: int,
    importance_threshold: int,
    policy: Policy,
):
    # create generator
    generator = Generator(
        max_priority, max_task_duration, max_session_duration, max_complexity
    )

    # generate tasks
    tasks = generator.tasks(num_tasks=16, deadline=deadline)

    # generate lists
    lists = generator.lists(tasks=[tasks[0:5], tasks[6:15]])

    # generate sessions
    sessions = generator.sessions(deadline)

    # run simulation
    progress = []
    for session in sessions:

        # run session
        run_session(session, lists, policy)

        # analyse session
        compl, compl_im, compl_it = tally_session(session, tasks, importance_threshold)

        # store
        progress.append(
            {
                "completed": compl,
                "completed_important": compl_im,
                "completed_in_time": compl_it,
            }
        )

    return progress
