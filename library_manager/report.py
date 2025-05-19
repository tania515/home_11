# library_manager/report.py

from .catalog import Library

def generate_report(library: Library):
    print('report')
    library.print_report()
    