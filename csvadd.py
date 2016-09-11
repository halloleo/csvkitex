#!/usr/bin/env python
"""
csvinsert is based on csvcut from csvkit
"""

import itertools

from csvkit import CSVKitReader, CSVKitWriter
from csvkit.cli import CSVKitUtility, parse_column_identifiers, match_column_identifier
from csvkit.headers import make_default_headers
from csvkit.exceptions import ColumnIdentifierError

class CSVInsert(CSVKitUtility):
    description = 'Add a column to a CSV file.'

    def add_arguments(self):
        self.argparser.add_argument('-n', '--names', dest='names_only', action='store_true',
            help='Display column names and indices from the input CSV and exit.')
        self.argparser.add_argument('-i', '--insertcol', dest='insertcol',
            help='Column index or name after which to add the new column (defaults to last column).')
        self.argparser.add_argument('-B', '--before', dest='before', action='store_true',
            help='Insert new column BEFORE the specified column instead of the default after the specified column.')
        self.argparser.add_argument('-f', '--fill-type', dest='filltype', default='empty',
            help='How to fill the new column: "empty", "linenumber" or string FILLTYPE (defaults to "empty").')
        self.argparser.add_argument('-c', '--colname', dest='colname', default='new_column',
            help='Header name of the new column.')

    def main(self):
        if self.args.names_only:
            self.print_column_names()
            return

        rows = CSVKitReader(self.input_file, **self.reader_kwargs)

        if self.args.no_header_row:
            row = next(rows)

            column_names = make_default_headers(len(row))

            # Put the row back on top
            rows = itertools.chain([row], rows)
        else:
            column_names = next(rows)

        # find where new colum goes
        id = len(column_names)-1
        if self.args.insertcol:
            id = match_column_identifier(column_names, self.args.insertcol, self.args.zero_based)
            if self.args.before:
                id -= 1

        # create the ranges
        left_cols = range(0, id+1)
        right_cols= range(id+1, len(column_names))

        # write header
        output = CSVKitWriter(self.output_file, **self.writer_kwargs)
        out_row = [column_names[c] for c in left_cols] + [self.args.colname] + [column_names[c] for c in right_cols]
        output.writerow(out_row)

        # write data
        for (ln,row) in  enumerate(rows, start=1):
            new_cell = self.args.filltype
            if self.args.filltype in ['empty']:
                new_cell = ""
            if self.args.filltype in ['line_number', 'linenumber']:
                new_cell = ln
            out_row = [row[c] for c in left_cols] + [new_cell] + [row[c] for c in right_cols]
            output.writerow(out_row)

def launch_new_instance():
    utility = CSVInsert()
    utility.main()

if __name__ == "__main__":
    launch_new_instance()

