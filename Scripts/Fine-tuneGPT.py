from openai import OpenAI
client = OpenAI()


file = client.files.create(
  file=open("Fine-tuneData/standard_300.jsonl", "rb"),
  purpose="fine-tune"
)

fine_tune_job = client.fine_tuning.jobs.create(
    training_file=file.id,
    model="gpt-4.1-2025-04-14",
    suffix='Tairan_standard_300',
  )

job_id = fine_tune_job.id
status = fine_tune_job.status

print(f'Fine-tuning model with jobID: {job_id}.')
print(f"Training Response: {fine_tune_job}")
print(f"Training Status: {status}")
