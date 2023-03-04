from importlib.metadata import PackageNotFoundError, version

try:
    __version__ = version("what-i-hear")
except PackageNotFoundError:
    # package is not installed
    pass
