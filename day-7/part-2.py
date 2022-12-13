
class ElfFile:
    def __init__(self, name, size):
        self.name = name
        self.size = size
        self.total_size = size
        self.children = dict()

    def add_child(self, elf_file):
        self.children[elf_file.name] = elf_file

    def add_children_to_total_size(self):
        for child in self.children.values():
            child.add_children_to_total_size()
            self.total_size += child.total_size

    def get_min_size_over_value(self, value):
        if self.size == 0 and self.total_size >= value:
            diff = self.total_size - value
            values = [diff] + [c.get_min_size_over_value(value) for c in self.children.values()]
            return min(values)
        else:
            return 999999999999999


root = ElfFile('root', 0)
pwd = [root]

with open('./input') as file:
    for line in file:
        line = line.rstrip()
        top = pwd[-1]

        if line.startswith('$ ls'):
            # these can safely be ignored
            continue

        if line.startswith('$ cd'):
            d = line.split(' ')[2]
            if d == '..':
                pwd.pop()
            elif d == '/':
                pwd = [root]
            else:
                pwd.append(top.children[d])
        else:
            # must be a file/dir listing
            parts = line.split(' ')
            file_size = 0 if parts[0] == 'dir' else int(parts[0])
            file_name = parts[1]
            top.add_child(ElfFile(file_name, file_size))


root.add_children_to_total_size()
used = root.total_size

disk_size = 70000000
free_needed = 30000000
available = disk_size - used
min_to_delete = free_needed - available

min_deletable = root.get_min_size_over_value(min_to_delete)
answer = min_deletable + min_to_delete
print(answer)
