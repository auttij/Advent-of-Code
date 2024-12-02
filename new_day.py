import sys, os, shutil, argparse
from aocd import get_data
from datetime import datetime
from pathlib import Path


def get_arg_parser():
    now = datetime.now()
    current_day = now.day
    current_year = now.year
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-year",
        type=int,
        default=current_year,
        choices=range(2015, current_year + 1),
        help="Year of selected aoc problem",
    )
    parser.add_argument(
        "-day",
        type=int,
        default=current_day,
        choices=range(1, 26),
        help="Day of selected aoc problem",
    )
    parser.add_argument(
        "--full-year",
        action=argparse.BooleanOptionalAction,
        help="Setup all the days in a year at once",
    )
    return parser


class newDayCreator:
    def __init__(self, year, day):
        self.year = year
        self.day = day

        template_dir = "template"
        self.template_file_name = os.listdir(template_dir)[0]
        self.template_path = f"{template_dir}/{self.template_file_name}"

    def create_year(self):
        for i in range(1, 26):
            success = self.create_day(self.year, i)
            if not success:
                print(f"couldn't download inputs for {self.year}-{i}")
                print("Stopping...")
                return 1

    def create_day(self, year=None, day=None):
        if year == None:
            year = self.year
        if day == None:
            day = self.day

        folder = f"{year}/{day}"

        if not os.path.exists(folder):
            print(f"Creating folder {folder}")
            Path(folder).mkdir(parents=True, exist_ok=True)

        target_filename = f"{folder}/{self.template_file_name}"
        if not os.path.exists(target_filename):
            print(f"Copying template file")
            shutil.copy(self.template_path, target_filename)

        return self.create_inputs(folder, year, day)

    def create_inputs(self, folder, year, day):
        self.write_input_file(f"{folder}/input1.txt", "")
        try:
            data = get_data(day=day, year=year)
            self.write_input_file(f"{folder}/input2.txt", data)
            return True
        except:
            return False

    def write_input_file(self, file_path, data):
        print("Writing input file:", file_path)
        if data:
            print("Peek at data:\n", data[:30], "\n")
        with open(file_path, "w") as f:
            f.write(data)


def main(args):
    parser = get_arg_parser()
    pargs = parser.parse_args(args)
    ndc = newDayCreator(pargs.year, pargs.day)
    if pargs.full_year:
        ndc.create_year()
    else:
        ndc.create_day()


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
