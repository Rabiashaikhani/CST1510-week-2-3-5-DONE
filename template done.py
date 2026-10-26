"""
RECORD CHECK  -  my version
===========================

Name  : Rabia Shaikhani
Lane  :  AI 
Date  :22-10-2026

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""

# ====================================================================== CLASS

#    Excellent : also add over_limit_count as a class-level running total -
#                see the note below.

# your class goes here
class Record:
    def __init__(self, label, value, limit):
        """Store the label, value and limit."""
        self.label = label
        self.value = value
        self.limit = limit

    def status(self):
        """Return the status based on the percentage."""
        percent = (self.value / self.limit) * 100

        if percent >= 100:
            return "OVER LIMIT"
        elif percent >= 90:
            return "WARNING"
        else:
            return "OK"


# ==================================================================== RECORDS
# 2. Create your records.
#
#  
#    Typical   : same, but now print each one's .status() as well.
#    Excellent : instead, write load_records(path) that reads label,value,limit
#                lines from a file and returns a list of Record objects. Make
#                your own data file, one record per line.


records = [
    Record("R-001", 45.0, 100.0),
    Record("R-002", 95.0, 100.0),
    Record("R-003", 120.0, 100.0)
]


# ==================================================================== OUTPUT
# 3. Print a report for each record.
#
#    Threshold : label, value, limit, inside a border.
#    Typical   : add the result of .status().
#    Excellent : also keep a running count of how many came back OVER LIMIT
#                across every record, and print that once, after the loop.
#                (Simplest: a plain variable outside the loop, same pattern
#                as Week 4. If you want it to live ON the object instead,
#                that is a stretch worth trying - but a variable is enough.)

for record in records:
    print()
    print("=" * 34)
    print(f"  RECORD CHECK  -  {record.label}")
    print("=" * 34)

    # your report lines go here

    print("=" * 34)
    print("Label:", record.label)
    print("Value:", record.value)
    print("Limit:", record.limit)
    print("Status:", record.status())


# ==========================================================================
# 4. Before you finish:
#
#    [x] Run it and check every record's numbers by hand
#    [x] Check every method only reads/changes its OWN object (self) -
#        nothing reaches outside itself
#    [x] Check every method and __init__ has a one-line docstring
