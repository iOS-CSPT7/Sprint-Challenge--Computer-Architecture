import sys
print(sys.argv)
from cpu import *

def main(argv):
    """Main."""
    if len(argv) != 2:
        print(f"usage: {argv[0]} filename", file=sys.stderr)
        return 1
    cpu = CPU()
    cpu.load(argv[1])
    # cpu.load()
    cpu.run()
    return 0
if __name__ == "__main__":
    sys.exit(main(sys.argv))