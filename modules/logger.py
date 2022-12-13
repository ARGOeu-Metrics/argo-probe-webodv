import logging
import logging.handlers


def get_logger(filename):
    logger = logging.getLogger("argo-probe-webodv")
    logger.setLevel(logging.INFO)

    logfile = logging.handlers.RotatingFileHandler(
        filename, maxBytes=512 * 1024, backupCount=2
    )
    logfile.setLevel(logging.INFO)
    logfile.setFormatter(logging.Formatter(
        "%(asctime)s - %(levelname)s - %(message)s", "%Y-%m-%d %H:%M:%S"
    ))
    logger.addHandler(logfile)

    return logger
