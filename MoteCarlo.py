import matplotlib.pyplot as plt
import random

total = 1000
num_samples = 20

inside = 0
sampleX = []
sampleY = []

for i in range(total):
  x = random.uniform(-1, 1)
  y = random.uniform(-1, 1)
  if x*x+y*y <= 1:
    inside = inside +1
  #collect samples first and draw them later
  sampleX.append(x)
  sampleY.append(y)

print("Pi: " + str(inside/total*4))

# create colorful rectangle and circle
rect = plt.Rectangle((-1, -1), 2, 2, color='g')
circle = plt.Circle((0, 0), 1, color='r')

fig, ax = plt.subplots()

ax.add_patch(rect)
ax.add_patch(circle)

plt.plot(sampleX[:num_samples], sampleY[:num_samples], 'bo')
plt.xlim([-1, 1])
plt.ylim([-1, 1])
plt.show()