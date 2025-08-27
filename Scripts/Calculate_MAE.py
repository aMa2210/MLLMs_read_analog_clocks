import pandas as pd
from sklearn.metrics import mean_absolute_error
import os


def find_files(directory, extension):
    file_paths = []
    for file in os.listdir(directory):
        full_path = os.path.join(directory, file)
        if os.path.isfile(full_path) and file.endswith(extension):
            file_paths.append(full_path)
    return file_paths


directory = 'Results/distorted'
extension = '.xlsx'
filenames = find_files(directory, extension)

def time_to_seconds(time_obj):
    if time_obj == 'No result':
        return -1
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


for filename in filenames:
    df = pd.read_excel(filename)

    number = df['answer'].apply(time_to_seconds)
    extracted_answer = df['extracted_answer'].apply(time_to_seconds)

    valid_mask = (number != -1) & (extracted_answer != -1)
    number = number[valid_mask]
    extracted_answer = extracted_answer[valid_mask]

    # max error is 6 hour, if the difference is more than 6 hours, then substract it
    time_difference = 6 * 3600
    diff = extracted_answer - number
    abs_diff = abs(extracted_answer - number)
    extracted_answer[(abs_diff > time_difference) & (diff > 0)] = 2*time_difference-extracted_answer[(abs_diff > time_difference) & (diff > 0)]
    extracted_answer[(abs_diff > time_difference) & (diff <= 0)] = 2*time_difference+extracted_answer[(abs_diff > time_difference) & (diff <= 0)]
    # 计算MAE
    mae = mean_absolute_error(number, extracted_answer)
    print(f'{filename}## MAE: {mae}')
