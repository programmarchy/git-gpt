import os
import subprocess
import sys
import openai

try:
  output = subprocess.check_output(["git", "diff", "--staged"])
except Exception as e:
  print(e, file=sys.stderr)
  sys.exit(1)

diff = output.decode()

prompt = 'Write a git commit message for the following diff.'
prompt = prompt + '\n\n' + diff

res = openai.Completion.create(
  engine="text-davinci-003",
  prompt=prompt,
  temperature=0.7,
  max_tokens=250,
  top_p=1,
  frequency_penalty=0.3,
  presence_penalty=0.3
)

if not res.choices:
  sys.stderr.write("GPT could not generate a commit message.")
  sys.exit(1)

commit_message = res.choices[0].text.strip()

subprocess.run(["git", "commit", "-m", commit_message])
