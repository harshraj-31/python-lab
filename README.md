# Python Programs

A personal collection of Python programs — coursework assignments and hands-on
practice projects — organized by topic.

## Structure

```
python-programs/
├── dsa-course-assignments/   # Class-test & practical-set assignments
│   ├── class-tests-and-practice/
│   └──  gui-db-mini-projects/
│   
└── hands-on-python/          # Self-directed practice, by topic
    ├── arrays/
    ├── basics-to-medium/
    ├── dsa-practice/
    ├── database-connectivity/
    ├── gui-tkinter/
    ├── hackerrank/
    ├── matplotlib/
    ├── pandas/
    └── extra-practice/
```

See the `README.md` inside each top-level folder for a breakdown of what's in it.

## Requirements

Most scripts only need Python 3's standard library. A few folders have extra
dependencies:

```bash
pip install pandas matplotlib mysql-connector-python openpyxl
```

- `hands-on-python/pandas/` and `matplotlib/` → `pandas`, `matplotlib`, `openpyxl` (for `.xlsx` files)
- `hands-on-python/database-connectivity/`, `hands-on-python/gui-tkinter/`
  (DB-backed scripts), and `dsa-course-assignments/gui-db-mini-projects/`
  → `mysql-connector-python` + a running local MySQL server
- Tkinter ships with most standard Python installs; on Linux you may need
  `sudo apt install python3-tk`

## Notes

- File and folder names have been normalized (consistent casing, no spaces)
  for cleaner imports and GitHub browsing.
- Line endings are normalized to LF and files are UTF-8.
- Generated/runtime artifacts (a saved chart image, a log file produced by
  running a script) were left out since they're outputs, not source — they'll
  be recreated when you run the corresponding script.
