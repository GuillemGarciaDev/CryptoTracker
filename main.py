import toolbar as tl
import os


['bitcoin', 'ethereum', 'binancecoin', 'cardano', 'solana', 'ripple', 'polkadot', 'dogecoin', 'terra-luna']


if __name__ == "__main__":
    os.system("rm -r sources")
    os.system("mkdir sources")
    toolbar = tl.LaunchToolBar()
    toolbar.run()