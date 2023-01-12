import logging
import logging.handlers


def get_logger(filename):
    # creating logger with name argo-probe-webodv
    logger = logging.getLogger("argo-probe-webodv")
    logger.setLevel(logging.INFO)

    # this will create logfile 'filename' which is going to be rotated; the file
    # will be rotated when it reaches size of 512 MB and 2 older copies will be
    # saved - the older ones are deleted
    logfile = logging.handlers.RotatingFileHandler(
        filename, maxBytes=512 * 1024, backupCount=2
    )
    logfile.setLevel(logging.INFO)
    logfile.setFormatter(logging.Formatter(
        "%(asctime)s - %(levelname)s - %(message)s", "%Y-%m-%d %H:%M:%S"
    ))
    logger.addHandler(logfile)

    return logger
