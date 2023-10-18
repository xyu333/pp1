tasks = int(input(print("Please provide the number of tasks: ")))
correct = int(input(print("Please provide the number of tasks completed correctly: ")))
if correct/tasks>=0.5: 
    print("Test passed")
else:
    print("Test failed")