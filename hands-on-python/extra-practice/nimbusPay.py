
def crash_report(filepath):
  failed_count = 0
  failed_amount = 0
  corrupted = 0

  try:
    with open(filepath, "r") as f:
      for line in f:

        try:
          line = line.strip()
          parts = line.split("|")
          parts = [p.strip() for p in parts]

          if len(parts) != 4:
            raise ValueError("Incomplete record")

          amount = float(parts[2])
          status = parts[3]

          if status == "FAILED":
            failed_amount += amount
            failed_count +=1
        except (ValueError, IndexError):
          corrupted += 1

  except FileNotFoundError:
   print("File not found")
   return None

  print("Corrupted Lines: ", corrupted)
  return f"Failed count: {failed_count}, Failed Amount: {failed_amount}"


print(crash_report("EXTRA PRACTRICES/transactions.log"))
