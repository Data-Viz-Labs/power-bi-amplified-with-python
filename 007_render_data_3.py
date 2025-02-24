import matplotlib.pyplot as plt

plt.figure(figsize=(10,10))
ax = plt.gca()

dataset.plot(kind='line',x='Fname',y='Children',ax=ax)
dataset.plot(kind='line',x='Fname',y='Pets', color='red', ax=ax)

plt.show()
