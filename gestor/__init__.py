import sys

if sys.version_info < (3, 12):  # runs before any module that uses 3.12 syntax, for both `-m gestor` and `-m gestor.mcp`
    sys.exit("gestor needs Python 3.12 or newer; this is " + sys.version.split()[0])
