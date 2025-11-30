import sys, shutil, argparse
from aocd import get_data
from datetime import datetime
from pathlib import Path


def get_arg_parser():
    today = datetime.now()

    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-year",
        type=int,
        default=today.year,
        choices=range(2015, today.year + 1),
        help="Year of selected AoC problem",
    )
    parser.add_argument(
        "-day",
        type=int,
        default=today.day,
        choices=range(1, 26),
        help="Day of selected AoC problem",
    )
    parser.add_argument(
        "--full-year",
        action=argparse.BooleanOptionalAction,
        help="Generate folders for all 25 days at once",
    )
    return parser


class NewDayCreator:
    def __init__(self, year: int, day: int, template_dir: str = "template"):
        self.year = year
        self.day = day
        self.template_dir = Path(template_dir)

        if not self.template_dir.exists():
            raise FileNotFoundError(f"Template directory '{template_dir}' not found.")

    def create_year(self):
        print(f"Creating all days for {self.year}")
        day_count = 26 if (self.year < 2025) else 13

        for day in range(1, day_count):
            print(f"\n=== Day {day} ===")
            ok = self.create_day(self.year, day)
            if not ok:
                print(f"⚠️  Failed to download input for {self.year}-{day}, stopping.")
                return False
        return True

    def create_day(self, year=None, day=None):
        year = year or self.year
        day = day or self.day

        day_folder = (
            Path(year / day) if isinstance(year, Path) else Path(f"{year}/{day}")
        )
        day_folder.mkdir(parents=True, exist_ok=True)

        print(f"📁 Creating folder: {day_folder}")

        # Copy template directory recursively
        self.copy_template(day_folder)

        # Create input files
        return self.create_inputs(day_folder, year, day)

    def copy_template(self, target_folder: Path):
        print("📄 Copying template files...")
        for item in self.template_dir.iterdir():

            target = target_folder / item.name

            # Copy directories
            if item.is_dir():
                shutil.copytree(item, target, dirs_exist_ok=True)
            else:
                # Copy individual files
                shutil.copy2(item, target)

    def create_inputs(self, folder: Path, year: int, day: int):
        # empty input1
        input1 = folder / "input1.txt"
        print(f"📝 Creating empty {input1}")
        input1.write_text("")

        # real input2 from AoC
        input2 = folder / "input2.txt"
        print(f"🌐 Downloading input for {year}-{day}...")

        try:
            data = get_data(year=year, day=day)
            input2.write_text(data)
            print("   ✔ Download OK")
            return True
        except Exception as e:
            print("   ✗ Download failed:", e)
            return False


def main(args):
    parser = get_arg_parser()
    p = parser.parse_args(args)

    creator = NewDayCreator(p.year, p.day)

    if p.full_year:
        creator.create_year()
    else:
        creator.create_day()


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
