name = "alembic"

version = "1.6.1"

authors = [
    ""
]

description = \
    """
    """

requires = [
    "pyilmbase-2",
    "boost-1.55"
]

build_requires = [
    "gcc-4.8.2+",
    "openexr-2.2",
    "ilmbase-2.2",
    "boost-1.55",
    "pyilmbase-2",
    "python-2.7",
    "hdf5-1.8.9+"
]

variants = [
    ["platform-linux", "arch-x86_64", "os-Fedora-25"]
]

tools = [
]

uuid = "alembic"

def commands():
    env.PATH.append("{root}/bin")
    env.LD_LIBRARY_PATH.append("{root}/lib")
    env.PYTHONPATH.append('{root}/lib/python2.7/site-packages')

    if building:
        env.PKG_CONFIG_PATH.append("{root}/lib/pkgconfig")
        env.ALEMBIC_INCLUDE_DIR = "{root}/include"