# AI-Powered DataFrame Manipulation

The script allows for Pandas DataFrames manipulation using natural language commands. It combines predefined programming logic with the capabilities of a lightweight language model, Flan-T5, to interpret user input and generate structured operations dynamically. The process is designed to handle transformations step-by-step, ensuring flexibility and ease of use.

## Model Overview

The model used was Flan-T5, optimized for task-specific instructions and excels at generating structured outputs like JSON. Once the model generates JSON commands, these are validated and executed on the DataFrame to ensure the desired transformations are applied.

## How It Works

The process begins with the user providing a natural language description of the transformation they want to apply. For example, a user might input: "Filter rows where salary > 75000 and add a column 'bonus' as salary \* 0.1." The model processes this input and generates a sequence of JSON commands that represent the required transformations. The system applies these transformations step-by-step to the DataFrame, and the final result, along with intermediate states, is displayed for debugging and verification.

The tool simplifies DataFrame manipulations by splitting the process into smaller, logical steps:

1. **Filter by Predicate:** This step narrows down rows in the DataFrame based on a condition. For example, filtering rows where `salary > 75000` removes all rows that don’t meet this criterion. It’s like a sieve that ensures only relevant data passes through.

2. **Select Columns:** After filtering, users can specify the columns they want to focus on, such as `['name', 'salary', 'bonus']`. This step reduces noise in the data, but it can fail if a required column, like `bonus`, hasn’t been created yet.

3. **Add Column:** This transformation is essential for deriving new information. For instance, calculating `bonus = salary * 0.1` creates a new column in the DataFrame with computed values. If this step is missing or executed out of order, subsequent operations may fail.

4. **Aggregate:** Aggregation groups the data by a key (like `department`) and summarizes it. For example, grouping by `department` and summing the `salary` produces a concise table showing the total salary for each department. However, aggregation removes unrelated columns unless explicitly included, which requires careful handling.

## Challenges and Solutions

A significant challenge was ensuring the Flan-T5 model produces valid and actionable JSON commands. Sometimes, the model generates malformed outputs, which are addressed through sanitization and validation steps. Additionally, dependencies between transformations, such as creating a column before selecting it, were managed by reordering operations dynamically. Aggregation posed another challenge since it discards unrelated columns by design, but this behavior was documented and explained to users.

By dividing complex transformations into smaller tasks, the tool simplifies handling multi-step operations, reducing the likelihood of errors and making debugging easier.


## Example

Let’s consider a typical workflow. A user might request: "Filter rows where salary > 75000, add a new column 'bonus' as salary * 0.1, and select ['name', 'bonus']." The tool processes this input and applies the transformations sequentially. It first filters the rows, then adds the `bonus` column, and finally selects the required columns. If all transformations are successful, the result might look like this:

|   name   |   bonus   |
|----------|-----------|
|   Eve    |   8000.0  |
|  Grace   |   9000.0  |

