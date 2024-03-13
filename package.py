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
]

build_system = "cmake"
uuid = "repository.glfw"

def pre_build_commands():
    info = {}
    with open("/etc/os-release", 'r') as f:
        for line in f.readlines():
            if line.startswith('#'):
                continue
            line_info = line.replace('\n', '').split('=')
            if len(line_info) != 2:
                continue
            info[line_info[0]] = line_info[1].replace('"', '')
    linux_distro = info.get("NAME", "centos")
    print("Using Linux distro: " + linux_distro)

    if linux_distro.lower().startswith("centos"):
        command("source /opt/rh/devtoolset-6/enable")
    elif linux_distro.lower().startswith("rocky"):
        pass

def commands():
    env.GLFW_ROOT = "{root}"
    env.GLFW_LOCATION = "{root}"
    env.LD_LIBRARY_PATH.append("{root}/lib64")
