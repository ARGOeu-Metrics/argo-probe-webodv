from distutils.core import setup

NAME = "argo-probe-webodv"


def get_ver():
    try:
        for line in open(NAME + '.spec'):
            if "Version:" in line:
                return line.split()[1]

    except IOError:
        raise SystemExit(1)


setup(
    name=NAME,
    version=get_ver(),
    author="SRCE",
    author_email="kzailac@srce.hr",
    description="ARGO probe that sends a POST request to webODV and checks "
                "that it is successful",
    url="https://github.com/ARGOeu-Metrics/argo-probe-webodv",
    package_dir={'argo_probe_webodv': 'modules'},
    packages=['argo_probe_webodv'],
    data_files=[('/usr/libexec/argo/probes/webodv', ['src/check_webodv.py'])]
)
