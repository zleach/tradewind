import os, sys

# Ensure the package's directory is on the Python module search path so that
# sibling modules (e.g. ``names``) can be imported as top-level modules when
# the package is loaded via ``from app import ...``.
_pkg_dir = os.path.dirname(__file__)
if _pkg_dir not in sys.path:
    sys.path.insert(0, _pkg_dir)
