# file-to-sh
Converts file(s) into a bash shell script that extracts the file(s)
# Requirements
* python 3


# Usage

`python3 filetosh.py <input> <output> <embeded file 1> [embeded file 2] ... [embeded file x]`

# Example input file

```
echo before
^(0)
echo after
```

