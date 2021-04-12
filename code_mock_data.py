#
center = [[1,2],[3,5],[4,6],[7,7],[13,17],[19,20],[20,23],[25,25],[30,24],[30,20]]

# generate 2d classification dataset
n = len(center) 

X, y = make_blobs(n_samples=1000, centers=center, n_features=2)
# scatter plot, dots colored by class value
df = DataFrame(dict(x=X[:,0], y=X[:,1], label=y))
x = np.arange(n)
ys = [i+x+(i*x)**2 for i in range(n)]
colors = cm.rainbow(np.linspace(0, 1, len(ys)))
fig, ax = pyplot.subplots()
grouped = df.groupby('label')
for key, group in grouped:
    group.plot(ax=ax, kind='scatter', x='x', y='y', label=key, color=colors[key])
pyplot.show()


plt.plot(X[:,0], X[:,1], '.')
