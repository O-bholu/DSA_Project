import streamlit as st
import numpy as np
from algorithms.sorting import bubble_sort, selection_sort, insertion_sort
from algorithms.searching import linear_search, binary_search
from utils.visualization import draw_plot
from algorithms.tree import insert_node, delete_node, inorder_traversal


def find_element(arr, target):
    return target in arr


def reverse_array(arr):
    return arr[::-1]


def sum_of_array(arr):
    return sum(arr)


def max_min_array(arr):
    return max(arr), min(arr)


st.title("DSA Visualizer")
st.sidebar.header("Configuration")

# Sidebar for selecting the operation
operation = st.sidebar.selectbox("Select Operation", [
    "Sorting Algorithms",
    "Searching Algorithms",
    "Array Operations",
    "Tree Operations"
])

array_size = st.sidebar.slider("Array Size", 10, 100, 20)
speed = st.sidebar.slider("Speed (Seconds per Step)", 0.01, 1.0, 0.1)

if st.sidebar.button("Generate New Array"):
    data = list(np.random.randint(10, 100, size=array_size))
    st.session_state["data"] = data

if "data" not in st.session_state:
    st.session_state["data"] = list(np.random.randint(10, 100, size=array_size))

data = st.session_state["data"]

# Show the array
st.write("Generated Array:", data)
plot_area = st.empty()

# Operation selection
if operation == "Sorting Algorithms":
    algorithm = st.sidebar.selectbox("Select Sorting Algorithm", [
        "Bubble Sort", "Selection Sort", "Insertion Sort"
    ])
    if st.button("Start Sorting"):
        if algorithm == "Bubble Sort":
            bubble_sort(data, speed, plot_area)
        elif algorithm == "Selection Sort":
            selection_sort(data, speed, plot_area)
        elif algorithm == "Insertion Sort":
            insertion_sort(data, speed, plot_area)

elif operation == "Searching Algorithms":
    target = st.sidebar.number_input("Enter value to search", min_value=0)
    algorithm = st.sidebar.selectbox("Select Searching Algorithm", [
        "Linear Search", "Binary Search"
    ])
    if st.button("Start Searching"):
        if algorithm == "Linear Search":
            result = linear_search(data, target, plot_area)
            st.write(f"Result: {'Found' if result != -1 else 'Not Found'}")
        elif algorithm == "Binary Search":
            result = binary_search(data, target, plot_area)
            st.write(f"Result: {'Found' if result != -1 else 'Not Found'}")

elif operation == "Array Operations":
    array_action = st.sidebar.selectbox("Select Array Operation", [
        "Find Element", "Reverse Array", "Sum of Array", "Max & Min of Array"
    ])

    if array_action == "Find Element":
        target = st.sidebar.number_input("Enter value to find", min_value=0)
        if st.button("Find Element"):
            found = find_element(data, target)
            st.write(f"Element {'Found' if found else 'Not Found'} in the array.")

    elif array_action == "Reverse Array":
        if st.button("Reverse Array"):
            data = reverse_array(data)
            st.session_state["data"] = data
            st.write("Reversed Array:", data)
            draw_plot(data, [], plot_area)

    elif array_action == "Sum of Array":
        if st.button("Calculate Sum"):
            total = sum_of_array(data)
            st.write(f"Sum of Array: {total}")

    elif array_action == "Max & Min of Array":
        if st.button("Find Max & Min"):
            maximum, minimum = max_min_array(data)
            st.write(f"Max Value: {maximum}, Min Value: {minimum}")

elif operation == "Tree Operations":
    tree_action = st.sidebar.selectbox("Select Tree Operation", [
        "Insert Node", "Delete Node", "Inorder Traversal"
    ])

    if "tree" not in st.session_state:
        st.session_state["tree"] = None

    if tree_action == "Insert Node":
        node_value = st.sidebar.number_input("Enter value to insert", min_value=0)
        if st.button("Insert Node"):
            st.session_state["tree"] = insert_node(st.session_state["tree"], node_value)
            st.write(f"Inserted Node: {node_value}")

    elif tree_action == "Delete Node":
        node_value = st.sidebar.number_input("Enter value to delete", min_value=0)
        if st.button("Delete Node"):
            st.session_state["tree"] = delete_node(st.session_state["tree"], node_value)
            st.write(f"Deleted Node: {node_value}")

    elif tree_action == "Inorder Traversal":
        if st.button("Show Inorder Traversal"):
            traversal_result = inorder_traversal(st.session_state["tree"])
            st.write("Inorder Traversal:", traversal_result)

draw_plot(data, [], plot_area)
