
name = "glfw"

version = "3.2.1"

build_requires = [
]

requires = [        
]

variants = [
    ["platform-linux", "arch-x86_64", "os-Fedora-25"]
]

uuid = "glfw"

def commands():
    
    if building:        
        env.GLFW_INCLUDE_DIR = '{root}/include'
        env.LD_LIBRARY_PATH.append('{root}/lib')

        