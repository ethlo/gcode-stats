# gcode-stats
Simple calculator for print-head movement statistics for a gcode model.

## Usage
Sample output for gcode file generated for Emma Maersk model: https://www.thingiverse.com/thing:3142367
```shell
$ python gcode-stats.py emma_petg.gcode 
Total distance: 2,156.701 m
X distance=1,489.576 m
Y distance=1,017.886 m
Elapsed=1.269 sec
```

And in 150% size:
```shell
$ python gcode-stats.py /home/morten/Downloads/emma_150_petg.gcode 
Total distance: 4,426.098 m
X distance=3,034.928 m
Y distance=3,040.363 m
Elapsed=2.195 sec
```
