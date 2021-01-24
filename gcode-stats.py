import math
import os
import sys
import timeit


def get_files(directory):
    return sorted(os.path.join(directory, f) for f in os.listdir(directory) if f.endswith('.gcode'))


def stats(file_path):
    tic = timeit.default_timer()
    with open(file_path, 'r') as fh:
        last = None
        total_x = 0
        total_y = 0
        total = 0

        for line_text in fh.readlines():
            parts = line_text.split()
            if parts:
                command = parts[0]
                if command in ('G0', 'G1'):
                    coord = dict()
                    for i in (range(1, len(parts))):
                        part = parts[i]
                        if part.startswith(('X', 'Y', 'Z')):
                            key = part[0:1]
                            val = part[1:]
                            coord[key] = float(val) if val else 0

                    x = coord.get('X')
                    y = coord.get('Y')
                    z = coord.get('Z')

                    if x and y:
                        if last is not None:
                            x2 = last[0]
                            y2 = last[1]
                            x_dist = abs(x2 - x)
                            y_dist = abs(y2 - y)
                            dist = math.hypot(x_dist, y_dist)
                            total_x += x_dist
                            total_y += y_dist
                            total += dist

                        last = [x, y]

        return {'total': total / 1000, 'x': total_x / 1000, 'y': total_y / 1000, 'elapsed': timeit.default_timer() - tic}


def format_stats(file_name, stats):
    return f'File: {file_name}' \
           f'\nTotal distance: {stats["total"]:,.3f} m' \
           f'\nX distance={stats["x"]:,.3f} m' \
           f'\nY distance={stats["y"]:,.3f} m' \
           f'\nElapsed={stats["elapsed"]:,.3f} sec\n'


if len(sys.argv) != 2:
    print (f'Missing argument for file or directory. \nUsage: {sys.argv[0]} <file/directory>')
    exit(1)

path = sys.argv[1]

if os.path.isdir(path):
    for file in get_files(path):
        print(format_stats(file, stats(file)))
elif os.path.isfile(path):
    print(format_stats(path, stats(path)))
else:
    print(f'No such file or directory: {path}')
    exit(1)
