import time
from utils.visualization import draw_plot

def linear_search(data, target, plot_area):
    for i in range(len(data)):
        draw_plot(data, [i], plot_area)
        time.sleep(0.5)
        if data[i] == target:
            return i
    return -1

def binary_search(data, target, plot_area):
    left, right = 0, len(data) - 1
    while left <= right:
        mid = (left + right) // 2
        draw_plot(data, [mid], plot_area)
        time.sleep(0.5)
        if data[mid] == target:
            return mid
        elif data[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1
