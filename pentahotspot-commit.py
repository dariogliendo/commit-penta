#! python3
import subprocess as sp
import methods
import sys

branch_name = sp.getoutput('git rev-parse --abbrev-ref HEAD')
if (branch_name == 'dev2023'):
  print('No commitees en dev!!')
  exit()

if (len(sys.argv) > 1) & (len(sys.argv[1]) > 0):
  commit_message = sys.argv[1]
else:
  commit_message = input('Ingresar el mensaje de commit: ')
full_commit_message = '['+branch_name+'] '+commit_message

sp.run('git add .')
commit_result = sp.run('git commit -a -m \"'+full_commit_message+'\"', stdout=sp.PIPE, shell=True)
commit_output = str(commit_result.stdout)

if "nothing to commit" in commit_output:
  print('No hay nada para commitear')
  exit()
else:
  print('')
  sp.run('git push --set-upstream origin '+branch_name, shell=True)
  print('')

while True:
    prompt = input('Mergear a dev? (Y/n):')
    if prompt == 'y' or prompt == 'Y':
      sp.run('git checkout dev2023', shell=True)
      methods.merge(branch_name)
    else:
      print('Saliendo sin merge a dev...')
      exit()