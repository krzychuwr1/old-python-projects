import subprocess


def do():
    """
    Compiles c++ and java sources.
    :return:none
    """
    try:
        subprocess.check_call(["javac", "java/IO1.java"])
        subprocess.check_call(["javac", "java/IO2.java"])
        subprocess.check_call(["javac", "java/CPU1.java"])
        subprocess.check_call(["javac", "java/CPU2.java"])
        subprocess.check_call(["g++", "-o", "c++/CPU1", "c++/CPU1.cpp"])
        subprocess.check_call(["g++", "-o", "c++/CPU2", "c++/CPU2.cpp"])
        subprocess.check_call(["g++", "-o", "c++/IO1", "c++/IO1.cpp"])
        subprocess.check_call(["g++", "-o", "c++/IO2", "c++/IO2.cpp"])
    except subprocess.CalledProcessError:
        print("An error has occured while compiling.")
        raise SystemExit
