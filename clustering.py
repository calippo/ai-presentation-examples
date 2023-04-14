import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from matplotlib.patches import Circle

# Define the dataset
shoes = [
    {'type': 'Sneakers', 'price': 100, 'comfort': 7},
    {'type': 'Slippers', 'price': 20, 'comfort': 9},
    {'type': 'Dress Shoes', 'price': 150, 'comfort': 5},
    {'type': 'Sneakers', 'price': 95, 'comfort': 8},
    {'type': 'Slippers', 'price': 22, 'comfort': 10},
    {'type': 'Dress Shoes', 'price': 140, 'comfort': 4},
    {'type': 'Sneakers', 'price': 110, 'comfort': 6},
    {'type': 'Slippers', 'price': 25, 'comfort': 9},
    {'type': 'Dress Shoes', 'price': 155, 'comfort': 3},
]

# Extract the features
X = [[shoe['price'], shoe['comfort']] for shoe in shoes]

# Define the number of clusters
k = 3

# Perform k-means clustering
kmeans = KMeans(n_clusters=k)
kmeans.fit(X)
y_kmeans = kmeans.predict(X)

# Define the colors and markers for each cluster
colors = ['r', 'g', 'b']
markers = ['o', 's', '^']

# Create figure with XKCD style
with plt.xkcd():
    fig, ax = plt.subplots()

    # Plot the data points with different colors and markers for each cluster
    for i in range(k):
        ax.scatter(
            [X[j][0] for j in range(len(X)) if y_kmeans[j] == i],
            [X[j][1] for j in range(len(X)) if y_kmeans[j] == i],
            label=f'{shoes[i]["type"]}',
            c=colors[i],
            marker=markers[i],
            alpha=0.8,
            edgecolor='black'
        )

        # Add circle around the cluster
        circle = Circle(
            (kmeans.cluster_centers_[i][0], kmeans.cluster_centers_[i][1]),
            kmeans.inertia_ / 2 / k,
            color=colors[i],
            linewidth=2,
            alpha=0.3,
            linestyle='--'
        )
        ax.add_artist(circle)

    # Set x and y axis labels and title
    ax.set_xlabel('Price ($)')
    ax.set_ylabel('Comfort (1-10)')
    ax.set_title('Shoes Clustering')

    # Add legend
    handles, labels = ax.get_legend_handles_labels()
    unique_labels = list(set(labels))
    handles = [handles[labels.index(l)] for l in unique_labels]
    ax.legend(handles, unique_labels)

    # Show the plot
    plt.show()