import sys


def format_lirik(lirik):
    lines = []
    for line in lirik.split("\n"):
        line = line.capitalize()
        lines.append(line)
    return "\n".join(lines)

print('\n'*2)
print(format_lirik(sys.argv[1]))