import time

from core.logger import get_logger
from tqdm import tqdm

logger = get_logger()


class Timer:
    def __init__(self, work_time: int, rest_time: int = 0, cycles: int = 1):
        self.work_time = work_time
        self.rest_time = rest_time
        self.cycles = cycles

    def start(self):
        logger.info(
            f"Timer started | Work: {self.work_time} min, Rest: {self.rest_time} min, Cycles: {self.cycles}"
        )
        for cycle in range(1, self.cycles + 1):
            self.run_cycle(cycle)
        logger.info("Timer finished. Well done!")

    def run_cycle(self, cycle: int):
        print(f"\nCycle {cycle}/{self.cycles}")
        logger.info(f"Starting cycle {cycle}/{self.cycles}")

        self.run_phase(self.work_time, "Work time")

        if self.rest_time > 0:
            self.run_phase(self.rest_time, "Rest time")

    def run_phase(self, minutes: int, phase: str):
        total_seconds = minutes * 60
        print(f"{phase} started for {minutes} minutes")

        with tqdm(
            total=total_seconds,
            bar_format="{l_bar}{bar} | {n_fmt}/{total_fmt} [Time left: {remaining}]",
        ) as progress_bar:
            for remaining in range(total_seconds, 0, -1):
                mins, secs = divmod(remaining, 60)
                progress_bar.set_description(f"{phase}: {mins:02}:{secs:02}")
                time.sleep(1)
                progress_bar.update(1)

        print(f"\n{phase} ended.")
        logger.info(f"{phase} completed")
