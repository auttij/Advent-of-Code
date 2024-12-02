import sys, os, shutil
import urllib.request
from aocd import get_data


class newDayCreator:
    def __init__(self, day, force=False):
        self.day = day
        self.year = 2024
        self.force = force

    def create(self):
        print("Starting new day folder generation")
        if self.force:
            self.empty_dir()
        self.copy_template()
        self.create_inputs()

    def write_input_file(self, filename, data):
        file_path = f"{self.day/filename}"
        print(f"printing {len(data)} lines of data to {file_path}")
        with open(file_path, "w") as f:
            for line in data:
                f.write(line)

    def empty_dir(self):
        print(f"Emptying and deleting directory {self.day}")
        if self.force:
            folder = f"{self.day}"
            for filename in os.listdir(folder):
                file_path = os.path.join(folder, filename)
                try:
                    if os.path.isfile(file_path) or os.path.islink(file_path):
                        os.unlink(file_path)
                    elif os.path.isdir(file_path):
                        shutil.rmtree(file_path)
                except Exception as e:
                    print("Failed to delete %s. Reason: %s" % (file_path, e))
            os.rmdir(folder)

    def copy_template(self):
        if not os.path.exists(self.day):
            print(f"Creating folder /{self.day}")
            os.mkdir(self.day)
        print(f"Copying /template/day.py to {self.day}/day.py")
        shutil.copy("template/day.py", f"{self.day}/day.py")

    def create_inputs(self):
        with open(f"{self.day}/input1.txt", "w") as f:
            pass
        with open(f"{self.day}/input2.txt", "w") as f:
            data = get_data(day=int(self.day), year=self.year)
            f.write(data)


if __name__ == "__main__":
    if not len(sys.argv) > 1:
        print("Argument for day required")
    else:
        day = sys.argv[1]
        force = False
        if "--force" in sys.argv or "-f" in sys.argv:
            force = True
        if not os.path.exists(day) or force:
            ndc = newDayCreator(day, force)
            ndc.create()
        else:
            print(f"Path for day {day} already exists")
