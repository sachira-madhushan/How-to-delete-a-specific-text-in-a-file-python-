with open("new.txt", "r") as f:
	lines = f.readlines()
f.close()

with open("new.txt", "w") as f:
	for line in lines:
		if line.strip("\n") != "text that you want to delete":
f.write(line)