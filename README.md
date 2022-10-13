# argo-probe-webodv

The probe inspects webODV API by sending a POST request, and then checking that the response is as excpected.

## Synopsis

The probe takes three mandatory arguments: API endpoint URL, secret for login, and timeout in seconds (time after which the probe execution will be terminated). 

```
/usr/libexec/argo/probe/check_webodv.py -h
usage: WebODV custom probe [-h] -u URL -s SECRET -t TIMEOUT

optional arguments:
  -h, --help            show this help message and exit
  -u URL, --url URL     API endpoint URL
  -s SECRET, --secret SECRET
                        secret
  -t TIMEOUT, --timeout TIMEOUT
                        timeout
```

Example execution of the probe:

```
/usr/libexec/argo/probe/check_webodv.py -u http://localhost/webodv/api/monitor -s some-secret -t 30
OK - Export successful
```
