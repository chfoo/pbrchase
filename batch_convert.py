import glob
import subprocess
import os.path


def main():
    for filename in glob.glob('sounds/*/*.wav'):
        output_filename = os.path.splitext(filename)[0] + '.ogg'
        subprocess.check_call(['sox', filename, output_filename])

        output_filename = os.path.splitext(filename)[0] + '.mp3'
        subprocess.check_call(['sox', filename, output_filename])


if __name__ == '__main__':
    main()
