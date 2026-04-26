# %% [markdown]
# # Python Core — Tuples
#
# ## Section 1 — Complete Lesson
#
# A tuple is an ordered and immutable collection of values.
#
# Tuples are used when data should NOT change.
#
# Common use cases:
#
# - coordinates (x, y)
# - RGB colors
# - database rows
# - model outputs (fixed structure)
# - function returns
# - configuration constants
#
# Main properties:
#
# - ordered
# - immutable
# - index-based
# - iterable
# - allows duplicates
#
# Core syntax:
#
# data = (10, 20, 30)
# single = (10,)       # important!
#
# data[0]
# data[-1]
# data[1:3]
#
# len(data)
# min(data)
# max(data)
# sum(data)
#
# 10 in data
#
# for x in data:
#     print(x)
#
# Unpacking:
#
# x, y = (10, 20)
#
# Extended unpacking:
#
# a, *b = (1, 2, 3, 4)
#
# Convert:
#
# tuple_list = list(data)
# new_tuple = tuple(tuple_list)
#
# Count:
#
# data.count(10)
#
# Index:
#
# data.index(20)
#
# Nested tuple:
#
# dataset = ((25, 50000), (30, 70000))
#
# dataset[0][1]
#
# Important notes:
#
# - Tuples are immutable → safer than lists
# - Faster than lists in many cases
# - Good for fixed structure data
# - Often used in ML as (features, label)
# - Can be used as dictionary keys (lists cannot)
#


# %% [markdown]
# ## Exercise 1 — Sensor Coordinate System
#
# You have 2D sensor coordinates.
#
# Tasks:
#
# - create a tuple (x, y)
# - print x and y separately
# - calculate distance from origin
#
# Goal:
#
# Practice tuple access + real math usage.

# %%
point = (3, 4)

# write your code here


# %% [markdown]
# ## Exercise 2 — Model Output Structure
#
# Model returns:
#
# (prediction, confidence)
#
# Tasks:
#
# - unpack values
# - print both
# - check if confidence > 0.8
#
# Goal:
#
# Practice unpacking (very important in ML).

# %%
model_output = (1, 0.87)

# write your code here


# %% [markdown]
# ## Exercise 3 — Dataset Row Processing
#
# Each row is:
#
# (age, income, purchased)
#
# Tasks:
#
# - unpack values
# - print each
# - convert purchased to bool
#
# Goal:
#
# Practice tuple as dataset row.

# %%
row = (35, 72000, 1)

# write your code here


# %% [markdown]
# ## Exercise 4 — Multiple Return Values Simulation
#
# Simulate a function returning multiple values:
#
# (mean, min, max)
#
# Tasks:
#
# - unpack values
# - print report
#
# Goal:
#
# Understand why tuples are used in functions.

# %%
stats = (22.5, 20.1, 25.3)

# write your code here


# %% [markdown]
# ## Exercise 5 — Tuple Immutability Test
#
# Try to change a value in a tuple.
#
# Then:
#
# - convert to list
# - modify value
# - convert back to tuple
#
# Goal:
#
# Understand immutability deeply.

# %%
data = (10, 20, 30)

# write your code here


# %% [markdown]
# ## Exercise 6 — Feature & Label Split (ML)
#
# Dataset row:
#
# (features, label)
#
# Tasks:
#
# - unpack features and label
# - print features
# - print label
#
# Goal:
#
# Core ML data pattern.

# %%
sample = ((25, 72000, 680), 1)

# write your code here


# %% [markdown]
# ## Exercise 7 — Batch Dataset Processing
#
# You have dataset:
#
# tuple of rows
#
# Tasks:
#
# - loop over dataset
# - extract all ages
# - extract all labels
# - calculate average age
#
# Goal:
#
# Tuple + loop + ML dataset logic.

# %%
dataset = (
    (25, 50000, 1),
    (32, 64000, 0),
    (47, 120000, 1),
    (22, 35000, 0)
)

# write your code here


# %% [markdown]
# ## Exercise 8 — Using Tuple as Dictionary Key
#
# Create dictionary:
#
# key = (x, y)
# value = label
#
# Tasks:
#
# - create at least 3 entries
# - access one value
# - print dictionary
#
# Goal:
#
# Advanced concept (tuple hashable).

# %%
points = {
    (1, 2): "A",
    (3, 4): "B"
}

# write your code here


# %% [markdown]
# ## Exercise 9 — Nested Tuple Metrics (ML)
#
# Structure:
#
# (
#   (accuracy, precision, recall),
#   (train_time, inference_time)
# )
#
# Tasks:
#
# - unpack everything
# - calculate average score
# - print report
#
# Goal:
#
# Deep tuple unpacking.

# %%
metrics = ((0.91, 0.89, 0.88), (45.2, 0.12))

# write your code here


# %% [markdown]
# ## Exercise 10 — Final Project: Immutable ML Pipeline Config
#
# You have a tuple config:
#
# (
#   model_name,
#   (learning_rate, epochs),
#   (train_size, test_size)
# )
#
# Tasks:
#
# - unpack all values
# - print config
# - simulate updating learning_rate (using conversion)
# - rebuild tuple
# - print updated config
#
# Goal:
#
# Combine immutability + ML config + restructuring.

# %%
config = ("NeuralNet", (0.01, 20), (0.8, 0.2))

# write your code here