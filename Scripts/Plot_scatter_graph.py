import pandas as pd
import matplotlib.pyplot as plt
from sklearn.metrics import mean_absolute_error
import os

def find_files(directory, extension):
    file_paths = []
    for file in os.listdir(directory):
        full_path = os.path.join(directory, file)
        if os.path.isfile(full_path) and file.endswith(extension):
            file_paths.append(full_path)
    return file_paths

model_names = ['GPT4o','Gemma3-12b','Llama3.2-11B','Qwen2.5-7B']
model_names_in_filenames = ['gpt4o','gemma-3-12b-it','Llama-3.2-11B-Vision-Instruct','Qwen2.5-VL-7B-Instruct']
filenames = [f'Results/standard/Test_{modelname}_Results.xlsx' for modelname in model_names_in_filenames]

colors = ['blue', 'green', 'orange', 'purple']
markers = ['o', 's', '^', 'x']

def time_to_seconds(time_obj):
    if not isinstance(time_obj, str):
        time_str = time_obj.strftime('%H:%M:%S') if len(str(time_obj).split(':')) == 3 else time_obj.strftime('%H:%M:%S')[
                                                                                        :-3]
    else:
        time_str = time_obj
    if len(time_str.split(":")) == 3:
        hours, minutes, seconds = map(int, time_str.split(':'))
    else:
        hours, minutes = map(int, time_str.split(':'))
        seconds = 0

    return hours * 3600 + minutes * 60 + seconds



plt.figure(figsize=(8, 8))
fontsize=18
for filename, model_name, color, marker in zip(filenames, model_names, colors, markers):
    df = pd.read_excel(filename)
    df = pd.read_excel(filename)

    number = df['answer'].apply(time_to_seconds)
    extracted_answer = df['extracted_answer'].apply(time_to_seconds)

    # max error is 6 hour, if the difference is more than 6 hours, then substract it
    time_difference = 6 * 3600
    diff = extracted_answer - number
    abs_diff = abs(extracted_answer - number)
    extracted_answer[(abs_diff > time_difference) & (diff > 0)] = 2*time_difference-extracted_answer[(abs_diff > time_difference) & (diff > 0)]
    extracted_answer[(abs_diff > time_difference) & (diff <= 0)] = 2*time_difference+extracted_answer[(abs_diff > time_difference) & (diff <= 0)]

    mae = mean_absolute_error(number, extracted_answer)
    print(f'MAE: {mae}')
    c = number - extracted_answer
    plt.scatter(number, extracted_answer, color=color, marker=marker, label=f'{model_name}', s=20)


plt.plot([3600, 46800], [3600, 46800], color='red', linestyle='--', label='Perfect Match (y=x)')
# plt.plot([0, 59], [0, 0], color='red', linestyle='--')

offset = 0.025
plt.legend(fontsize=fontsize, frameon=False, loc='upper left', bbox_to_anchor=(0-offset, 1+offset))

# plt.title(f'Scatter plot for {filename.replace(".xlsx","")}')
plt.xlabel('Ground Truth',fontsize=fontsize)
# plt.ylabel('Error')
plt.ylabel('Prediction', fontsize=fontsize)
plt.xticks(fontsize=fontsize)
plt.yticks(fontsize=fontsize)


plt.ylim(-5000, 69500)

plt.savefig(f'Figures/scatter.pdf', bbox_inches='tight', pad_inches=0.1)
plt.close()