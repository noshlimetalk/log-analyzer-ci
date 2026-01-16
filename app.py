def analyze_log(file):
    errors = 0
    warnings = 0

   with open(file, "r") as f:
        for line in f:
             if "ERROR" in line:
                 errors += 1
             if "WARNING" in line:
                 warnings += 1

  print(f"Errors: {errors}")
  print(f"Warnings: {warnings}")

if __name__ == "__main__":
    analyze_log("sample.log")
