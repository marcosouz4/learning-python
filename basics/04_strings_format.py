name = "Clayton"
degree = "Bachelor"
job = "Software Engineer"
experience = 10

print(name + " " + degree + " " + job + " " + str(experience))

# Format
print("{} {} {} {}".format(name, degree, job, experience))

# Format with index
print("{0} {2} {1} {3}".format(name, job, degree, experience))
