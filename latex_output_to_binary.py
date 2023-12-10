# this file is used to convert LaTeX output to bianry data
# LaTeX has trouble writing binary data to files directly
import sys

input_fn = sys.argv[1]
output_fn = sys.argv[2]

with open(input_fn) as in_file:
    input_data = in_file.read()
    numbers = map(int, filter(lambda x: len(x) > 0, input_data.split(chr(10))))
    with open(output_fn, 'wb') as out_file:
        for num in numbers:
            out_file.write(num.to_bytes(1))

