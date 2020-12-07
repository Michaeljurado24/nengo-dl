"""
We use semantic versioning (see http://semver.org/).
and conform to PEP440 (see https://www.python.org/dev/peps/pep-0440/).
'.devN' will be added to the version unless the code base represents
a release version. Release versions are git tagged with the version.

We avoid the use of f-strings so that this can be imported in Python < 3.6,
since it is required by setup.py.
"""

import warnings

name = "nengo-dl"
version_info = (3, 4, 1)  # (major, minor, patch)
dev = 0  # set to None for releases

version = "{v}{dev}".format(
    v=".".join(str(v) for v in version_info),
    dev=(".dev%d" % dev) if dev is not None else "",
)

# check nengo version
try:
    import nengo.version
except ImportError:
    # nengo not installed, can't check version
    pass
else:
    minimum_nengo_version = (3, 0, 0)

    # for release versions of nengo-dl, this should be the latest released
    # nengo version. for dev versions of nengo-dl, this should be the current
    # nengo dev version.
    latest_nengo_version = (3, 2, 0)

    if nengo.version.version_info < minimum_nengo_version:  # pragma: no cover
        raise ValueError(
            (
                "NengoDL does not support Nengo version {nengo_version}. "
                "Upgrade with 'pip install --upgrade --no-deps nengo'."
            ).format(nengo_version=nengo.version.version)
        )
    elif nengo.version.version_info > latest_nengo_version:  # pragma: no cover
        warnstr = (
            "This version of NengoDL has not been tested with your Nengo version "
            "({nengo_version}). The latest fully supported version is {latest_version}."
        ).format(
            nengo_version=nengo.version.version,
            latest_version=".".join(str(x) for x in latest_nengo_version),
        )
        warnings.warn(warnstr)
