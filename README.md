# Extensions to csvkit

Some additions to the fabulous [csvkit][csvkit_gh]. At the moment just one tool: 

* `csvadd` to add a column to a csv file

## Requirements 

This tool needs `csvkit` installed. It is tested with csvkit v0.9.1.

## Installation

Put the script file `csvadd.py` somewhere in your path and make sure it is executable.

## Usage

The help message:

```
usage: csvadd.py [-h] [-d DELIMITER] [-t] [-q QUOTECHAR] [-u {0,1,2,3}] [-b] [-p ESCAPECHAR] [-z MAXFIELDSIZE]
                 [-e ENCODING] [-S] [-H] [-v] [-l] [--zero] [-n] [-i INSERTCOL] [-B] [-f FILLTYPE] [-c COLNAME]
                 [FILE]

Add a column to a CSV file.

positional arguments:
  FILE                  The CSV file to operate on. If omitted, will accept input on STDIN.

optional arguments:
  -h, --help            show this help message and exit
  -d DELIMITER, --delimiter DELIMITER
                        Delimiting character of the input CSV file.
  -t, --tabs            Specifies that the input CSV file is delimited with tabs. Overrides "-d".
  -q QUOTECHAR, --quotechar QUOTECHAR
                        Character used to quote strings in the input CSV file.
  -u {0,1,2,3}, --quoting {0,1,2,3}
                        Quoting style used in the input CSV file. 0 = Quote Minimal, 1 = Quote All, 2 = Quote Non-
                        numeric, 3 = Quote None.
  -b, --doublequote     Whether or not double quotes are doubled in the input CSV file.
  -p ESCAPECHAR, --escapechar ESCAPECHAR
                        Character used to escape the delimiter if --quoting 3 ("Quote None") is specified and to
                        escape the QUOTECHAR if --doublequote is not specified.
  -z MAXFIELDSIZE, --maxfieldsize MAXFIELDSIZE
                        Maximum length of a single field in the input CSV file.
  -e ENCODING, --encoding ENCODING
                        Specify the encoding the input CSV file.
  -S, --skipinitialspace
                        Ignore whitespace immediately following the delimiter.
  -H, --no-header-row   Specifies that the input CSV file has no header row. Will create default headers.
  -v, --verbose         Print detailed tracebacks when errors occur.
  -l, --linenumbers     Insert a column of line numbers at the front of the output. Useful when piping to grep or
                        as a simple primary key.
  --zero                When interpreting or displaying column numbers, use zero-based numbering instead of the
                        default 1-based numbering.
  -n, --names           Display column names and indices from the input CSV and exit.
  -i INSERTCOL, --insertcol INSERTCOL
                        Column index or name after which to add the new column (defaults to last column).
  -B, --before          Insert new column BEFORE the specified column instead of the default after the specified
                        column.
  -f FILLTYPE, --fill-type FILLTYPE
                        How to fill the new column: "empty", "linenumber" or string FILLTYPE (defaults to
                        "empty").
  -c COLNAME, --colname COLNAME
                        Header name of the new column.
```

[csvkit_gh]: https://github.com/wireservice/csvkit

<!--  LocalWords:  csvkit
 -->
