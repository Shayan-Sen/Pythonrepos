import matplotlib.pyplot as plt
goal_types=["penalty","field goal","free kick"]
no_goals=[20,34,8]
cols=['red','green','blue']

plt.pie(no_goals,colors=cols,labels=goal_types,
        autopct="%.2f%%",explode=(0.0, 0.0, 0.2),
        shadow=True)
plt.show()

