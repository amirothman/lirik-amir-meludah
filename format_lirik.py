import sys


def format_lirik(lirik_path):
    with open(lirik_path, "r") as f:
        lirik = f.read()
    lines = []
    for line in lirik.split("\n"):
        line = line.capitalize()
        lines.append(line)
    return "\n".join(lines)

print('\n'*2)
print(format_lirik(sys.argv[1]))