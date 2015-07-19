import glob
import subprocess
import os.path


def main():
    for filename in glob.glob('*.wav'):
        output_filename = os.path.splitext(filename)[0] + '.ogg'
        subprocess.check_call(['sox', filename, output_filename])


if __name__ == '__main__':
    main()
