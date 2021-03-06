import argparse
import logging
import sys

from lib.event_manager import Atman
from lib.globals import LOGGER_TAG


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Alien')
    parser.add_argument("--verbose", "-v", action="store_true")
    parser.add_argument("--show_logs", "-s", action="store_false")
    parser.add_argument("--log_file", "-lf", default=None, help="Set path to save log output")
    args = parser.parse_args()

    logger = logging.getLogger(LOGGER_TAG)

    if args.log_file:
        log_file_handler = logging.FileHandler(args.log_file)
        formatter = logging.Formatter('[%(asctime)s] [%(levelname)s] [%(threadName)s] %(message)s')
        log_file_handler.setFormatter(formatter)
        logger.addHandler(log_file_handler)

    if args.show_logs:
        stdout_handler = logging.StreamHandler(sys.stdout)
        formatter = logging.Formatter('[%(levelname)s] [%(threadName)s] %(message)s')
        stdout_handler.setFormatter(formatter)
        logger.addHandler(stdout_handler)

    if args.verbose:
        logger.setLevel(level=logging.DEBUG)
    else:
        logger.setLevel(level=logging.INFO)

    trigger_events = Atman()
    trigger_events.start()
    trigger_events.join()
