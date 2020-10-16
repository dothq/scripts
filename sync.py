import os
import sys
import glob

def info(message):
    sys.stdout.write('\x1b[1;34mINFO\x1b[0m ' + message + "\n")

def tip(message):
    sys.stdout.write('\x1b[1;33mTIP\x1b[0m ' + message + "\n")

def run_fast_scandir(dir, ext):
    subfolders, files = [], []

    for f in os.scandir(dir):
        if f.is_dir():
            subfolders.append(f.path)
        if f.is_file():
            files.append(f.path)


    for dir in list(subfolders):
        sf, f = run_fast_scandir(dir, ext)
        subfolders.extend(sf)
        files.extend(f)
    return subfolders, files

def main():    
    dot_dir = os.getcwd() + "/dot";
    ff_dir = os.getcwd() + "/firefox";

    info("Syncing your files in " + dot_dir + "...")

    subfolders, files = run_fast_scandir(dot_dir, [""])

    for file in files:
        fle = file.partition(dot_dir)[2]

        if fle.startswith(".git"): break
        if fle.startswith(".hg"): break

        dot_file = "/dot" + fle
        ff_file = "/firefox" + fle
        print("\33[94m" + dot_file + "\33[0m  \33[90m⟶\33[0m    " + "\33[33m" + (ff_file) + "\33[0m")

        rs_from = dot_dir + fle
        rs_to = ff_dir + fle

        # os.system(f"rsync --recursive --dry-run --human-readable --relative --update --progress {rs_from} {rs_to}")
        os.system(f"ln -sf {rs_from} {rs_to}")

    print("\33[0m")
    print("Done.")

if __name__ == "__main__":
    main()