import re
import json
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM


model_name = "google/flan-t5-small"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSeq2SeqLM.from_pretrained(model_name)


def sanitize_json(output):
    """
    Fix common formatting issues in the LLM-generated JSON output.
    """
    try:
        output = output.replace("'", '"')   # Replace single quotes with double quotes for valid JSON

        if not output.startswith("["):
            output = "[" + output
        if not output.endswith("]"):
            output = output + "]"  # we ensure output is wrapped in square brackets

        output = re.sub(r"[^\[\]{}:,\"'a-zA-Z0-9_\s]", "", output)     # Remove invalid characters outside JSON syntax

        # Validate and parse JSON
        return output
    except Exception as e:
        print(f"Error sanitizing JSON: {e}")
        return output


def extract_valid_json(output):
    """
    Extracts and validates JSON from the LLM's output.
    """
    try:
        sanitized_output = sanitize_json(output)
        return json.loads(sanitized_output)
    except json.JSONDecodeError as e:
        print(f"Error parsing JSON: {e}")
    return None


def generate_transformations(user_input):
    """
    Use Flan-T5 to generate structured JSON transformations based on user input.
    """
    try:
        prompt = f"""
        Gnerate valid JSON transformations for a Pandas DataFrame.
        The transformations must strictly follow the JSON format and perform actions on the DataFrame.

        Example input:
        Filter rows where salary > 75000, select columns ['name', 'salary'], and sort by 'salary' descending.

        Example output:
        [
            {{"action": "filter_by_predicate", "column": "salary", "condition": "> 75000"}},
            {{"action": "select_columns", "columns": ["name", "salary"]}},
            {{"action": "sort_by_column", "column": "salary", "ascending": false}}
        ]

        Your task:
        Input: {user_input}
        Output (strict JSON only):
        """

        inputs = tokenizer(prompt, return_tensors="pt", truncation=True, max_length=512)
        outputs = model.generate(
            inputs.input_ids,
            attention_mask=inputs.attention_mask,
            max_new_tokens=100,
            num_return_sequences=1,
            pad_token_id=tokenizer.eos_token_id
        )
        generated_text = tokenizer.decode(outputs[0], skip_special_tokens=True)
        print("Raw LLM Output:")
        print(generated_text)

        sanitized_output = sanitize_json(generated_text)
        print("Sanitized Output:")
        print(sanitized_output)
        return extract_valid_json(sanitized_output)
    except Exception as e:
        print(f"Error generating transformations: {e}")
        return []
