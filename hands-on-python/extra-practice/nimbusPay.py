# ===========================================================
#              TRANSACTION / CRASH REPORT
# ===========================================================
# This program reads a transaction log file and:
#
# 1. Counts the number of FAILED transactions.
# 2. Calculates the total amount of FAILED transactions.
# 3. Counts corrupted or incomplete records.
# 4. Handles the case where the file does not exist.
# ===========================================================


def crash_report(filepath):

    # Variables used to store our results.
    failed_count = 0
    failed_amount = 0
    corrupted = 0


    # -------------------------------------------------------
    # OPEN AND READ THE FILE
    # -------------------------------------------------------
    # try is used because the file may not exist.

    try:

        with open(filepath, "r") as f:

            # Read the file one line at a time.
            for line in f:

                # ---------------------------------------------------
                # PROCESS EACH LINE
                # ---------------------------------------------------
                # Each individual record can contain invalid data,
                # so we use another try block for each line.

                try:

                    # Remove spaces and the newline character.
                    line = line.strip()

                    # Split the record using "|" as the separator.
                    parts = line.split("|")

                    # Remove extra spaces around each field.
                    parts = [p.strip() for p in parts]


                    # ------------------------------------------------
                    # CHECK WHETHER THE RECORD IS COMPLETE
                    # ------------------------------------------------
                    # A valid record must contain exactly 4 parts.

                    if len(parts) != 4:
                        raise ValueError("Incomplete record")


                    # ------------------------------------------------
                    # GET AMOUNT AND STATUS
                    # ------------------------------------------------

                    # Convert the amount from string to float.
                    amount = float(parts[2])

                    # Get the transaction status.
                    status = parts[3]


                    # ------------------------------------------------
                    # PROCESS FAILED TRANSACTION
                    # ------------------------------------------------
                    # If the transaction status is FAILED,
                    # add its amount to the total and increase
                    # the failed transaction count.

                    if status == "FAILED":
                        failed_amount += amount
                        failed_count += 1


                # ----------------------------------------------------
                # HANDLE INVALID RECORDS
                # ----------------------------------------------------
                # ValueError can occur when:
                # - Amount cannot be converted to float.
                # - We manually raise ValueError for incomplete data.
                #
                # IndexError can occur if we try to access
                # a list position that doesn't exist.

                except (ValueError, IndexError):

                    corrupted += 1


    # ---------------------------------------------------------------
    # HANDLE MISSING FILE
    # ---------------------------------------------------------------
    # If the specified file does not exist,
    # FileNotFoundError will occur.

    except FileNotFoundError:

        print("File not found")
        return None


    # ---------------------------------------------------------------
    # DISPLAY RESULTS
    # ---------------------------------------------------------------

    print("Corrupted Lines:", corrupted)

    return f"Failed count: {failed_count}, Failed Amount: {failed_amount}"


# ===========================================================
#                    CALL THE FUNCTION
# ===========================================================

print(crash_report("EXTRA PRACTRICES/transactions.log"))


# ===========================================================
#                    EXAM SUMMARY
# ===========================================================
# ✔ try
#    Used to test code that may produce an exception.
#
# ✔ except
#    Handles the exception instead of stopping the program.
#
# ✔ with open()
#    Opens a file and automatically closes it afterward.
#
# ✔ FileNotFoundError
#    Occurs when the specified file does not exist.
#
# ✔ ValueError
#    Occurs when a value has an invalid type or format.
#
#    Example:
#    float("hello")
#
# ✔ IndexError
#    Occurs when trying to access an index
#    that does not exist.
#
# ✔ raise ValueError()
#    Manually creates a ValueError when
#    a record does not meet our requirements.
#
# ✔ strip()
#    Removes extra spaces and newline characters.
#
# ✔ split("|")
#    Breaks a string into parts using "|" as separator.
#
# ✔ float()
#    Converts a value from string to decimal number.
#
# ✔ f-string
#    Used to easily combine variables with text.
#
# Important concept:
# The outer try-except handles FILE errors,
# while the inner try-except handles RECORD errors.
# ===========================================================
