import sys
import argparse
from git_gpt import commit, status

def main():
  args = sys.argv[1:]
  parser = argparse.ArgumentParser(description='Run git commands with the assistance of OpenAI GPT-3.', prog='git-gpt')
  parser.add_argument('command', help='a git command e.g. commit')
  parser.add_argument('--dry-run', action='store_true', help='prints the output of the command instead of running it')
  options = parser.parse_args(args)
  command = options.command
  try:
    if command == 'commit':
      commit(options)
    elif command == 'status':
      status(options)
    else:
      raise Exception(f"unrecognized command: '{command}'")
  except Exception as e:
    print(e, file=sys.stderr)
    sys.exit(1)

if __name__ == '__main__':
  main()
