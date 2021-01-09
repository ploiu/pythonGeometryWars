from core import get_current_level, difficulty_modifier
from event import LEVEL_START_EVENT, LEVEL_PROGRESS_EVENT, LEVEL_END_EVENT
from level import Level


def level_start(level_start_event):
    set_enemies = level_start_event.__dict__['enemies'] if 'enemies' in level_start_event.__dict__ else None
    level = Level()
    level.start()


def level_progress(level_progress_event):
    level = get_current_level()
    level.progress()


def level_end(level_end_event):
    Level.current_level += (1 * difficulty_modifier)


# export this list to register them all
handlers = {
    LEVEL_START_EVENT: [level_start],
    LEVEL_PROGRESS_EVENT: [level_progress],
    LEVEL_END_EVENT: [level_end]
}
