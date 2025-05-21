import matplotlib.pyplot as plt


x = [1, 2, 3, 4, 5]
y = [3, 4, 3, 4, 5]
y1 = [5, 13, 2.4, 8, 21]


plt.plot(x, y, label='Line A', color='blue', marker='o', linestyle='--', linewidth=2)


plt.plot(x, y1, label='Line B', color='green', marker='s', linestyle='-', linewidth=3)

plt.title("Customized Line Graph")
plt.xlabel("X values")
plt.ylabel("Y values")
plt.grid(True)        
plt.legend()          


plt.show()