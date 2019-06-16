import os
import re
import shutil

def main():
    if not os.path.exists("sounds"):
        os.mkdir("sounds")

    for dirname in os.listdir("PLAYER_JIKKYO"):
        result = re.match(r"GRP_.*_([a-z][a-z])", dirname)

        if result:
            language = result.group(1)
        else:
            language = "en"

        for wavname in os.listdir(os.path.join("PLAYER_JIKKYO", dirname)):
            if language != "en":
                dest_name = wavname[3:]
            else:
                dest_name = wavname

            path = os.path.join("PLAYER_JIKKYO", dirname, wavname)
            dest = os.path.join("sounds", language, dest_name)

            if not os.path.exists(os.path.join("sounds", language)):
                os.mkdir(os.path.join("sounds", language))

            shutil.copyfile(path, dest)

            print(f"{path} -> {dest}")


if __name__ == "__main__":
    main()
