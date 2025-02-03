import time
from utils.visualization import draw_plot

def reverse_array(data, speed, plot_area):
    n = len(data)
    for i in range(n // 2):
        data[i], data[n - i - 1] = data[n - i - 1], data[i]
        draw_plot(data, [i, n - i - 1], plot_area)
        time.sleep(speed)
    draw_plot(data, [], plot_area)

def find_max(data, plot_area):
    max_value = data[0]
    max_index = 0
    for i in range(len(data)):
        if data[i] > max_value:
            max_value = data[i]
            max_index = i
        draw_plot(data, [i, max_index], plot_area)
        time.sleep(0.5)
    return max_value, max_index

def calculate_sum(data, plot_area):
    total = 0
    for i in range(len(data)):
        total += data[i]
        draw_plot(data, [i], plot_area)
        time.sleep(0.5)
    return total
