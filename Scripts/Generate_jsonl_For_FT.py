import pandas as pd
import json
import os
import base64
import re

def encode_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode('utf-8')


input_file = 'Dataset_for_experiment/thin_hands/Train'
output_file = f'Fine-tuneData/thin_hands_300.jsonl'
all_files = os.listdir(input_file)

prompt = '''What time is shown on the clock in the given image?'''


with open(output_file, 'w') as outfile:
    for png_name in all_files:
        image_path = os.path.join(input_file, png_name)
        correct_answer = png_name.replace('.png','').replace('_',':')
        print(correct_answer)
        base64_image = encode_image(image_path)
        json_line = {
            "messages": [
                {
                    "role": "user",
                    "content": [
                        {"type": "text", "text": prompt},
                        {
                            "type": "image_url",
                            "image_url": {
                                "url": f"data:image/png;base64,{base64_image}"
                            }
                        }
                    ]
                },
                {"role": "assistant", "content": f'The time shown on the clock is **{correct_answer}**.'}
            ]
        }
        outfile.write(json.dumps(json_line) + '\n')
