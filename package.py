name = "glfw"

version = "3.4.0"

authors = [
    "Camilla Lowy"
]

description = \
    """
    GLFW is an Open Source, multi-platform library for OpenGL, OpenGL ES and
    Vulkan application development.
    """

with scope("config") as c:
    # Determine location to release: internal (int) vs external (ext)

    # NOTE: Modify this variable to reflect the current package situation
    release_as = "ext"

    # The `c` variable here is actually rezconfig.py
    # `release_packages_path` is a variable defined inside rezconfig.py

    import os
    if release_as == "int":
        c.release_packages_path = os.environ["SSE_REZ_REPO_RELEASE_INT"]
    elif release_as == "ext":
        c.release_packages_path = os.environ["SSE_REZ_REPO_RELEASE_EXT"]

requires = [
]

private_build_requires = [
    "cmake",
    "gcc",
]

variants = [
    ["platform-linux", "arch-x86_64", "os-centos-7"]
]

build_system = "cmake"

uuid = "repository.glfw"

def commands():
    env.GLFW_ROOT = "{root}"
    env.GLFW_LOCATION = "{root}"
    env.LD_LIBRARY_PATH.append("{root}/lib64")
