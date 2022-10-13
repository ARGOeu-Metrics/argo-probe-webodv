import argparse
import sys

from argo_probe_webodv.exceptions import CriticalException, WarningException
from argo_probe_webodv.response import Analyse


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
    args = parser.parse_args()

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

    nagios_code = 0

    try:
        analyse = Analyse(url=args.url, data=data)
        analyse.analyse()
        print("OK - Export successful")

    except CriticalException as e:
        print("CRITICAL - {}".format(str(e)))
        nagios_code = 2

    except WarningException as e:
        print("WARNING - {}".format(str(e)))
        nagios_code = 1

    except Exception as e:
        print("UNKNOWN - {}".format(str(e)))
        nagios_code = 3

    sys.exit(nagios_code)


if __name__ == "__main__":
    main()
