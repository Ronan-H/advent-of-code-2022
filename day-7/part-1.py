
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

    def sum_of_sizes_under_limit(self, limit):
        if self.size > 0:
            # skip files (only include directories)
            return 0

        # first, calculate the total size for this directory
        this_total = 0
        for child in self.children.values():
            this_total += child.total_size

        # then, recurse into the children to sum up their total sizes (not exceeding the limit)
        child_total = 0
        for child in self.children.values():
            child_total += child.sum_of_sizes_under_limit(limit)

        # keep the running total while still enforcing the limit
        return (this_total if this_total <= limit else 0) + child_total


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
print(root.sum_of_sizes_under_limit(100000))
