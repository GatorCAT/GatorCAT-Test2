# Data Analysis

## Wesley Long

## Program Input and Output

### What is the output from running the following commands?

```bash
📦 The data file contains 50 data values in it!

🚀 Let's do some sophisticated data analysis!

🧮 Here are the results of the data analysis:

        The computed mean is 87.80
        The computed median is 88.05

        The computed variance is 3.69
        The computed standard deviation is 1.92

💡 What does this tell you about the population of this city?
```

`poetry run dataanalysis --data-file input/data.txt`

### What are the first five lines of the contents of the file that is input into the `datasummarizer`?

```
1970-01-01,81.342
1971-01-01,83.300
1972-01-01,84.700
1973-01-01,85.500
1974-01-01,86.100
```

### What is the output from running the test suite with the command `poetry run task test`?

```bash
=============================================== test session starts ================================================
platform win32 -- Python 3.9.2, pytest-5.4.3, py-1.10.0, pluggy-0.13.1
rootdir: C:\Users\wesle\Documents\CompSci\cs102FA2021\Labs\computer-science-102-fall-2021-ee-data-analysis-WesleyL30\dataanalysis
collected 13 items

tests\test_summarize.py ...........
tests\test_transform.py ..

================================================ 13 passed in 0.07s ================================================
```

## Source Code

### Describe in detail how your provided source code works

#### What is a function that analyzes a data set by computing the standard deviation? How does it work?

```python
def compute_standard_deviation(numbers: List[float]) -> float:
    """Compute the standard deviation of a list of numbers."""
    # call the function to calculate the variance
    variance = compute_variance(numbers)
    # calculate the standard deviation as the square root of the variance
    std = variance ** 0.5
    # return the calculated standard devision of the list of numbers
    return std
```
This function allows us to analyze the given dataset by computing the standard deviation for us quickly.  The function reads in a list of floating point values, and computes the variance of these values through the use of the `compute_variance()` function that was declared prior to this function.  From there, the variance of the list of numbers is returned to this function, allowing us to swiftly compute the last step.  Which is taking the square root of the variance that was calculated.

#### What is the purpose of the following function in the context of the `transform` module?

```
def transform_string_to_number_list(data_text: str) -> List[float]:
    """Transform a string of (date, float) values to a list of floats."""
    data_number_list = []
    for line in data_text.splitlines():
        ordered_pair = line.split(",")
        data_number_list.append(float(ordered_pair[1]))
    return data_number_list
```

This function is meant to read in a string of values, which we assume was inputted from an exterior file.  An empty list is declared to hold the values we wish to use.  We read through the string "line by line" using the built-in `splitlines()` function, and we then split the line again using the `split()` function to save the current line as an n-tuple.  Which allows us to skim through multiple values of the current line based on the delimiter that was used, in this case it was a comma as the input file expected is in a csv format.  From there the n-tuple that was created is searched through to retrieve the values that we want, and save them to the list that was declared prior.  In this case we know where the value we want will be, so we declare the index of the tuple where it is located.

#### What is the purpose of the following function in the context of the `summarize` module?

```
def compute_difference(numbers: List[float]) -> List[float]:
    """Compute difference for each value from the calculated mean."""
    # compute the mean
    mean = compute_mean(numbers)
    # compute the differences from the mean
    differences = []
    for number in numbers:
        differences.append(number - mean)
    return differences
```

This function is used to compute the difference between a given value, and the mean of the entire set.  For example if the mean ended up being the number 7, and one of our numbers was 9, then our given number would have a difference of 2.  While the number 5 would have a difference of -2, due to it being smaller than the mean.  We first calculate the mean using the `compute_mean()` function declared prior.  Then we declare an empty list for our output, and iterate through the list that was given as input.  From there we take the number found within our list, and subtract the calculated mean from it, giving us our difference.  That value is then appended to the list that we declared.  After the for loop is finished running, the list of all of the calculated values is returned.

## Professional Development

### What are some examples of computer science skills that were important 30 years ago but are less important to learn now? Why are they less important now?

Some skills that were important 30 years ago were the use of older languages like Fortran or Cobol.  These languages have become nearly obsolete due to their competitors stepping up their game, and becoming more "mainstream"  While these aren't bad skills to learn in themselves, it would be more worth our time to learn more recent languages and frameworks.  Even though the need for Cobol programmers has risen recently due to very very old code becoming an issue.

### What are some examples of computer science skills that were important 30 years ago but are just as important to learn now? Why are they as important now as in the past?

Writing industry standard, or just standard, code was important 30 years ago, and is still important today.  There will always be best practices to use to ensure swift and efficient development.  While these standards and methods may not be exactly the same today, the concept of creating standardized code and using safe practices still lives on today, and is extremely important.  Another skill that is just as important today, is bug fixing.  This skill entails, finding where the bug is, understanding what the code does, understanding why it isn't working correctly, and then figuring out how to fix it are all very important to the field of computer science.  Without it we would never be able to fix our code or have anything functional.
