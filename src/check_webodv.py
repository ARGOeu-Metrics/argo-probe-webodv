#!/usr/bin/python3
import argparse
import sys

from argo_probe_webodv.exceptions import CriticalException, WarningException
from argo_probe_webodv.response import Analyse
from argo_probe_webodv.logger import get_logger


def main():
    parser = argparse.ArgumentParser("WebODV custom probe")
    parser.add_argument(
        "-u", "--url", dest="url", type=str, required=True,
        help="API endpoint URL"
    )
    parser.add_argument(
        "-s", "--secret", dest="secret", type=str, required=True,
        help="secret"
    )
    parser.add_argument(
        "-t", "--timeout", dest="timeout", type=int, required=True,
        help="timeout"
    )
    parser.add_argument(
        "-l", "--logfile", dest="logfile", type=str,
        default="/var/log/nagios/argo-probe-webodv.log",
        help="location of log file"
    )
    args = parser.parse_args()

    logger = get_logger(filename=args.logfile)

    data = {
        "webodv_monitor_secret": args.secret,
        "treeview_num_end_nodes": 3,
        "OutVar": {
            "0": 1,
            "1": 2,
            "2": 3
        },
        "OutVarEx": 4,
        "OutVarState": {
           "checked": {
               "0": "var_0",
               "1": "var_1",
               "2": "var_2",
               "3": "var_3"
           }
        },
        "use_or_logic": "T",
        "coords": {
            "0": 22.92,
            "1": 29.53,
            "2": 81.01,
            "3": 78.79
        },
        "pointsize": 0.5,
        "date1": "01/01/1850",
        "date2": "12/31/2024",
        "treeview_mode": 0,
        "file_format": "txt",
        "datasetname": "SeaDataNet>Arctic_Ocean>SDC_ARC_DATA_TS_V1",
        "branch": "default"
    }

    # these are the default status_code and printed message if everything is ok
    nagios_code = 0
    msg = "OK - Export successful"

    try:
        # we log start of probe execution and the return message in the logfile
        logger.info(f"Probe invoked as {' '.join(sys.argv)}")
        analyse = Analyse(url=args.url, data=data, timeout=args.timeout)
        # if something is wrong, this part of code raises either
        # WarningException or CriticalException, and the probes exits with
        # the according status_code
        analyse.analyse()
        logger.info(msg)

    except CriticalException as e:
        msg = "CRITICAL - {}".format(str(e))
        nagios_code = 2
        logger.error(msg)

    except WarningException as e:
        msg = "WARNING - {}".format(str(e))
        nagios_code = 1
        logger.warning(msg)

    except Exception as e:
        # if there's been an unhandled exception, this would cause probe to
        # exit with status_code 3 (UNKNOWN)
        msg = "UNKNOWN - {}".format(str(e))
        nagios_code = 3
        logger.error(msg)

    print(msg)
    if nagios_code == 0:
        logger.info(f"Probe exiting with code {nagios_code}...")

    else:
        logger.error(f"Probe exiting with code {nagios_code}...")

    sys.exit(nagios_code)


if __name__ == "__main__":
    main()
