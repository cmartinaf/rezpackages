
name = "ptex"

version = "2.1.28"

build_requires = [
    'gcc-4.8.2+'    
]

requires = [        
]

variants = [
    ["platform-linux", "arch-x86_64", "os-Fedora-25"]
]

uuid = "ptex"

def commands():
    env.PATH.append("{root}/bin")
    
    if building:        
        env.PTEX_INCLUDE_DIR = '{root}/include'
        env.PTEX_LOCATION = '{root}'
        env.LD_LIBRARY_PATH.append('{root}/lib')

        