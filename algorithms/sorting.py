import time
from utils.visualization import draw_plot

def bubble_sort(data, speed, plot_area):
    n = len(data)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if data[j] > data[j + 1]:
                data[j], data[j + 1] = data[j + 1], data[j]
            draw_plot(data, [j, j + 1], plot_area)
            time.sleep(speed)
    draw_plot(data, [], plot_area)

def selection_sort(data, speed, plot_area):
    n = len(data)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if data[j] < data[min_idx]:
                min_idx = j
            draw_plot(data, [i, j, min_idx], plot_area)
            time.sleep(speed)
        data[i], data[min_idx] = data[min_idx], data[i]
    draw_plot(data, [], plot_area)

def insertion_sort(data, speed, plot_area):
    n = len(data)
    for i in range(1, n):
        key = data[i]
        j = i - 1
        while j >= 0 and data[j] > key:
            data[j + 1] = data[j]
            draw_plot(data, [j, j + 1], plot_area)
            time.sleep(speed)
            j -= 1
        data[j + 1] = key
    draw_plot(data, [], plot_area)
