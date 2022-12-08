import flatdict
import json

with open("input.txt", "r", encoding="utf-8") as puzzle_input:
    input = [line.strip() for line in puzzle_input.readlines()]


class FileStructure:
    def __init__(self):
        self.cwd: str = "root"
        self.file_system = {"root": dict()}
        self.dir_sizes = []

        self.setup_files()
        self.get_dir_sizes()

        self.free_space = 70_000_000 - sum(flatdict.FlatDict(self.file_system).itervalues())

    def resolve_command(self, command):
        match command:
            case ["cd", ".."]:
                self.cwd = self.cwd[:self.cwd.rfind("/")]
            case ["cd", "/"]:
                self.cwd = "root"
            case ["cd", sub_dir]:
                self.cwd += "/" + sub_dir
            case _:
                pass

    def add_file(self, name, file_size=0):
        sd = self.file_system
        for d in self.cwd.split("/"):
            sd = sd[d]
        if not file_size:
            sd[name] = dict()
        else:
            sd[name] = file_size

    def setup_files(self):
        for line in input:
            if line.startswith("$"):
                self.resolve_command(line.split()[1:])
            else:
                match line.split():
                    case ["dir", dir_name]:
                        self.add_file(dir_name)
                    case [file_size, file_name] if file_size.isnumeric():
                        self.add_file(file_name, int(file_size))

    def get_dir_sizes(self, current_dict=None):
        if current_dict is None:
            current_dict = self.file_system
        for key, value in current_dict.items():
            if type(value) == dict:
                self.dir_sizes.append((key, sum(flatdict.FlatDict(value).itervalues())))
                self.get_dir_sizes(value)


puzzle_structure = FileStructure()

print(json.dumps(puzzle_structure.file_system, indent=4))  # IF YOU WANT

print(sum([size for _, size in puzzle_structure.dir_sizes if size <= 100_000]))  # ANSWER PART ONE


print(min(
    [size for _, size in puzzle_structure.dir_sizes if puzzle_structure.free_space + size >= 30_000_000]
))  # ANSWER PART TWO
