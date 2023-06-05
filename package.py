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
    import os
    c.release_packages_path = os.environ["SSE_REZ_REPO_RELEASE_EXT"]

requires = [
]

private_build_requires = [
]

variants = [
    ["platform-linux", "arch-x86_64", "os-centos-7"]
]

build_system = "cmake"
uuid = "repository.glfw"

def pre_build_commands():
    command("source /opt/rh/devtoolset-6/enable")

def commands():
    env.GLFW_ROOT = "{root}"
    env.GLFW_LOCATION = "{root}"
    env.LD_LIBRARY_PATH.append("{root}/lib64")
