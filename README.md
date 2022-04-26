# How-to-delete-a-specific-text-in-a-file-python-

How to delete a specific line in a file? (python)

  with open("new.txt", "r") as f:
        lines = f.readlines()
      f.close()
  with open("new.txt", "w") as f:
        for line in lines:
          if line.strip("\n") != "your text":
            f.write(line)
