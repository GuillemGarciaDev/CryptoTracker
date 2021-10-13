import toolbar as tl
import os

if __name__ == "__main__":
    os.system("rm -r sources")
    os.system("mkdir sources")
    toolbar = tl.LaunchToolBar()
    toolbar.run()