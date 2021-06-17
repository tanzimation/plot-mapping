import matplotlib.pyplot as plt
import time as t

times = []
mistakes = 0
print("This programme will help you type faster. Write 'Stupid' for 5 times as fast as you can")
input("press enter to continue")
while len(times) < 5:
    start = t.time()
    word = input("type the word:")
    end = t.time()
    time_elapsed = end - start
    times.append(time_elapsed)
    if word.lower() != "stupid":
        mistakes += 1
print("You made", str(mistakes), "mistake(s)")
print("Let's see your evolution ")
t.sleep(4)
x = [1, 2, 3, 4, 5]
y = times
plt.plot(x, y)
legend = ["1", "2", "3", "4", "5"]
plt.xticks(x, legend)
plt.xlabel("Your attempts")
plt.ylabel("Times in seconds")
plt.title("Your evolution")
plt.show()