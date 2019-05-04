""" file-to-sh
by webmsgr """
import base64
import os
import sys


def filetosh(inputfile, outputfile, files):
    """ Convert one or more files places them in a sh file """
    with open(inputfile) as inp:
        indata = inp.read()
        inp.close()
    newlines = indata.split("\n")
    linenum = 0
    for line in indata.split("\n"):
        if line[0] == "^":
            filept = files[int(''.join([i for i in line if i not in "^()"]))-1]
            with open(filept, "rb") as inf:
                filedata = inf.read()
                inf.close()
            newline = """echo \"{}\"> tmp.b64\nbase64 -d tmp.b64 > {}\nrm tmp.b64""".format(
                base64.b64encode(filedata).decode(),
                os.path.basename(filept)
            )
            newlines[linenum] = newline
        linenum += 1
    newfile = "\n".join(newlines)
    with open(outputfile, "w") as output:
        output.write(newfile)
        output.close()
    return True


def main(argv):
    """ Main function """
    try:
        infile = argv[0]
        outfile = argv[1]
        files = argv[2:]
    except IndexError:
        print("Usage: filetosh.py <input sh> <output sh> <embed file 1> [embed file 2] ... [embed file x]")
        sys.exit()
    filetosh(infile, outfile, files)


if __name__ == "__main__":
    main(sys.argv[1:])
