import pip

if __name__ == "__main__":
    try:
        with open("requirements.txt", "r") as file:
            line = file.readline()
            while line:
                pip.main(['install', line])
                line = file.readline()
    except Exception as e:
        print("An error occured:\n{}".format(e))

    print("The installation was succesful\n")