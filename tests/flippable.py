import sys

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Failing")
        exit(1)
    elif sys.argv[1] == "True":
        print("Succeeding")
        exit(0)
    else:
        print("Failing")
        exit(1)