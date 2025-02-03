import matplotlib.pyplot as plt

def draw_plot(data, highlights, plot_area):
    plt.clf()
    colors = ['blue' if x not in highlights else 'red' for x in range(len(data))]
    plt.bar(range(len(data)), data, color=colors)
    plt.xlabel("Index")
    plt.ylabel("Value")
    plt.title("Visualization")

    for i, value in enumerate(data):
        plt.text(i, value + 1, str(value), ha='center', va='bottom', fontsize=8)

    plot_area.pyplot(plt)