# Monte Carlo To-Do List

Use of Monte Carlo method to analyze the optimal policy to decide which tasks should be done first.

## Concepts

- **Task**: Something that should be done.
- **List**: Group of tasks
- **Progress**: Amount of effort dedicated to a specific task.
- **Session**: One iteration of work, composed of one or more progress. (e.g days, weeks...)


## Policies

- **Older first**: Olders tasks are attended first (i.e FIFO)
- **Recent first**: Recent tasks are attended first (i.e LIFO)
- **Closer deadline first**: Tasks with sooner deadline are attended first.
- **Further deadline first**: Tasks with later deadline are attended first.
- **Priority first**: Tasks with higher priority are attended first.
- **Redundant first**: Tasks with lower priority are attended first.
- **Complex first**: Tasks with higher complexity are attended first.
- **Easy first**: Tasks with lower complexity are attended first.
- **Time-consuming first**: Tasks with higher duration are attended first.
- **Brief first**: Tasks with lower duration are attended first.
- **Easy important first**: Tasks with lower complexity and higher priority are attended first.
- **Easy closer deadline first**: Tasks with lower complexity and closer deadline are attended first.
- **Brief important first**: Tasks with lower duration and higher priority are attended first.

## Roles

- **Generator**: Element in charge of generate a random bunch of tasks grouped in lists based on a specific setting (i.e maximum priority, maximum duration...)
- **Simulator**: Element in charge of running a single simulation.
- **Runner**: Element in charge of running multiple simulations and aggregating the results.
- **Analyser**: Element in charge of extracting insights from the results of the simulations.

## TODO:

- Visualization of progress
- More complex policies