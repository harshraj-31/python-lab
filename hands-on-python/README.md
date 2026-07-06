# Hands-On Python

A collection of Python practice scripts covering core language concepts through
to GUI apps, database connectivity, and data analysis.

## Folder guide

| Folder | Contents |
|---|---|
| `arrays/` | Basic array/list algorithms (reverse, largest/second-largest, move zeroes) |
| `basics-to-medium/` | Fundamentals and logic-building exercises (lists, dicts, sets, map/filter/reduce) |
| `dsa-practice/` | Small OOP/DSA-style simulations (GPS, toll plaza, conveyor belt, smart printer, etc.) |
| `database-connectivity/` | MySQL connectivity examples using `mysql.connector` |
| `gui-tkinter/` | Tkinter GUI examples, from a basic window to a DB-backed GUI |
| `hackerrank/` | Solutions to HackerRank-style problems |
| `matplotlib/` | Data visualization examples (bar, pie, scatter, histogram charts) |
| `pandas/` | Data analysis examples (Series, DataFrame, filtering, aggregation) |
| `extra-practice/` | Misc. standalone practice scripts |

## Tech stack

- Python 3
- pandas
- matplotlib
- Tkinter
- MySQL (`mysql-connector-python`)

## Notes

- Scripts under `database-connectivity/` and `gui-tkinter/` that use `mysql.connector`
  expect a local MySQL server with matching credentials/schema — check each script's
  connection block before running.
- `pandas/` and `matplotlib/` scripts read from the accompanying data files
  (`.csv`, `.xlsx`, `.txt`) in the same folder.
