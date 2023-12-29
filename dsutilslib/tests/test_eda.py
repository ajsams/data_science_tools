import os

from dsutils import eda


def test_detect_encoding():
    # Making sure to include non ascii characters in data
    # Otherwise "utf-8" will be detected as "ascii" by chardet
    data = ["Test, Data", "34, 25", "300192, 2039", "é, ñ"]
    test_filepath = "tests/test_data/test_encoding.csv"
    encoding_type = "utf-8"  # could expland this to test over multiple encodings

    # Ensure directory exists
    os.makedirs(os.path.dirname(test_filepath), exist_ok=True)

    # Write the test file
    with open(test_filepath, "w", encoding=encoding_type) as file:
        for line in data:
            file.write(line + "\n")

    assert eda.detect_encoding(test_filepath) == encoding_type
