import openai
import datetime

client = openai.OpenAI()

fine_tuning_jobs = client.fine_tuning.jobs.list(limit=5)

print("Listing fine-tuning jobs:")
i = 0
for job in fine_tuning_jobs:
    if i >= 5:
        break
    human_readable_time = datetime.datetime.utcfromtimestamp(job.created_at).strftime('%Y-%m-%d %H:%M:%S')
    print(f"Job ID: {job.id}")
    print(f"Status: {job.status}")
    print(f"Model: {job.fine_tuned_model if job.fine_tuned_model else 'Not Available'}")
    print(f"Created At: {human_readable_time}")
    print(f"Hyperparameters: {job.hyperparameters}")
    print("-" * 40)  # Separator for readability
    i += 1
