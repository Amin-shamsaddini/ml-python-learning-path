# %% [markdown]
# # Python Core — Strings
#
# ## Section 1 — Complete Lesson
#
# A string is text data in Python.
#
# Strings are used for:
#
# - names
# - emails
# - passwords
# - file paths
# - labels
# - prompts
# - API messages
# - logs
# - text preprocessing in ML/NLP
#
# Main properties:
#
# - ordered
# - immutable
# - index-based
# - iterable
# - supports slicing
#
# Core syntax:
#
# ```python
# text = "Python"
# text = 'Python'
# multiline = """Hello
# World"""
#
# text[0]
# text[-1]
# text[1:4]
# text[::-1]
#
# len(text)
#
# "Py" in text
# "Java" not in text
#
# text.lower()
# text.upper()
# text.title()
# text.capitalize()
# text.strip()
# text.lstrip()
# text.rstrip()
# text.replace("old", "new")
#
# text.startswith("Py")
# text.endswith("on")
#
# text.split()
# text.split(",")
# "-".join(words)
#
# text.find("word")
# text.count("a")
#
# text.isalpha()
# text.isdigit()
# text.isalnum()
# text.isspace()
#
# name = "Ali"
# age = 25
# message = f"My name is {name} and I am {age}"
#
# value = 0.93456
# print(f"Accuracy: {value * 100:.2f}%")
# ```
#
# Important notes:
#
# - Strings are immutable: methods return new strings
# - Use `.strip()` when cleaning user input
# - Use `.lower()` for consistent comparison
# - Use `split()` to turn text into parts
# - Use `join()` to build clean text
# - In ML/NLP, strings are the base of text preprocessing


# %% [markdown]
# ## Exercise 1 — Clean User Input
#
# You receive a username with extra spaces and mixed case.
#
# Tasks:
#
# - remove extra spaces
# - convert username to lowercase
# - check username length
# - print a clean report
#
# Goal:
#
# Practice `.strip()`, `.lower()`, and `len()`.

# %%
username = "   AI_Student_2026   "

# write your code here


# %% [markdown]
# ## Exercise 2 — Email Normalization
#
# You receive an email from a form.
#
# Tasks:
#
# - remove extra spaces
# - convert email to lowercase
# - check if email contains `"@"`
# - check if email ends with `".com"`
# - print a validation report
#
# Goal:
#
# Practice string cleaning and basic validation.

# %%
email = "   Student.Example@GMAIL.COM   "

# write your code here


# %% [markdown]
# ## Exercise 3 — File Extension Checker
#
# You have a file path.
#
# Tasks:
#
# - check if the file is a CSV file
# - check if the file is a JSON file
# - extract the file name from the path
# - print a clean report
#
# Goal:
#
# Practice `.endswith()` and `.split()`.

# %%
file_path = "data/raw/customer_churn.csv"

# write your code here


# %% [markdown]
# ## Exercise 4 — Text Label Cleaning for ML
#
# You have a messy class label.
#
# Tasks:
#
# - remove extra spaces
# - convert to lowercase
# - replace spaces with underscores
# - print the cleaned label
#
# Example:
#
# `"  High Risk Customer  "` -> `"high_risk_customer"`
#
# Goal:
#
# Practice text preprocessing for ML labels.

# %%
label = "  High Risk Customer  "

# write your code here


# %% [markdown]
# ## Exercise 5 — Tokenize a Sentence
#
# You have a sentence.
#
# Tasks:
#
# - convert sentence to lowercase
# - remove leading/trailing spaces
# - split sentence into words
# - count number of words
# - print all results
#
# Goal:
#
# Practice basic NLP preprocessing.

# %%
sentence = "   Python is great for Machine Learning and AI   "

# write your code here


# %% [markdown]
# ## Exercise 6 — Prompt Quality Check
#
# You are building an AI app.
#
# A user sends a prompt.
#
# Tasks:
#
# - remove extra spaces
# - count prompt length
# - count number of words
# - check if prompt is too short
# - prompt is too short if it has fewer than 5 words
# - print a prompt report
#
# Goal:
#
# Practice string preprocessing for AI applications.

# %%
prompt = "  explain machine learning simply  "

# write your code here


# %% [markdown]
# ## Exercise 7 — Log Message Parser
#
# You have a log message.
#
# Format:
#
# ```text
# LEVEL|DATE|SERVICE|MESSAGE
# ```
#
# Tasks:
#
# - split the log message by `"|"`
# - extract level
# - extract date
# - extract service
# - extract message
# - print a clean log report
#
# Goal:
#
# Practice parsing structured text.

# %%
log_message = "ERROR|2026-04-26|training-service|Model training failed"

# write your code here


# %% [markdown]
# ## Exercise 8 — Simple Text Feature Extraction
#
# You have customer feedback text.
#
# Tasks:
#
# - convert text to lowercase
# - count total characters
# - count total words
# - count how many times `"bad"` appears
# - count how many times `"good"` appears
# - create a simple sentiment signal:
#
# ```python
# good_count - bad_count
# ```
#
# - print a feature report
#
# Goal:
#
# Practice simple NLP-style feature extraction.

# %%
feedback = "The product is good but the delivery was bad. Overall good support."

# write your code here


# %% [markdown]
# ## Exercise 9 — Build Clean Report String
#
# You have model metrics.
#
# Tasks:
#
# - create a clean multi-line report using f-string
# - accuracy, precision, recall must be shown as percentages
# - each percentage must have 2 decimal places
# - print the final report
#
# Goal:
#
# Practice professional string formatting.

# %%
model_name = "Random Forest"
accuracy = 0.9345
precision = 0.9123
recall = 0.8876

# write your code here


# %% [markdown]
# ## Exercise 10 — Final Project: Text Preprocessing Pipeline
#
# You have raw text for a simple NLP pipeline.
#
# Tasks:
#
# - remove leading/trailing spaces
# - convert to lowercase
# - replace `"."` with empty string
# - replace `","` with empty string
# - split text into words
# - remove empty words if any
# - count total words
# - count unique words
# - rebuild cleaned text using `" ".join(...)`
# - print a professional preprocessing report
#
# Goal:
#
# Combine cleaning, tokenization, counting, and text reconstruction.

# %%
raw_text = "   Machine Learning, AI, and Python. Python is powerful for AI.   "

# write your code here