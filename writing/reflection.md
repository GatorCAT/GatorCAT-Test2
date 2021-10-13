# Data Analysis

TODO: PLEASE DELETE ALL OF THE TODO MARKERS AND THE ASSOCIATED PROMPTS

## Add Your Name Here

## Program Input and Output

### What is the output from running the following commands?

TODO: Use a fenced code block to provide the output for this command.

`poetry run dataanalysis --data-file input/data.txt`

### What are the first five lines of the contents of the file that is input into the `datasummarizer`?

TODO: Use a fenced code block to provide the contents of the file.

### What is the output from running the test suite with the command `poetry run task test`?

TODO: Use a fenced code block to provide the output from running the test suite.

## Source Code

### Describe in detail how your provided source code works

#### What is a function that analyzes a data set by computing the standard deviation? How does it work?

TODO: Use a fenced code block to provide the requested source code
TODO: Write at least one paragraph to explain the requested source code

#### What is the purpose of the following function in the context of the `display` module?

TODO: Write at least one paragraph to explain the provided source code

```
def transform_string_to_number_list(data_text: str) -> List[float]:
    """Transform a string of (date, float) values to a list of floats."""
    data_number_list = []
    for line in data_text.splitlines():
        ordered_pair = line.split(",")
        data_number_list.append(float(ordered_pair[1]))
    return data_number_list
```

#### What is the purpose of the following function in the context of the `summarize` module?

TODO: Write at least one paragraph to explain the provided source code

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

## Professional Development

### What are some examples of computer science skills that were important 30 years ago but are less important to learn now? Why are they less important now?

TODO: Provide a one-paragraph response to this question, using source code or commands for reference as needed

### What are some examples of computer science skills that were important 30 years ago but are just as important to learn now? Why are they as important now as in the past?

TODO: Provide a one-paragraph response to this question, using source code or commands for reference as needed
