import subprocess as sp
def merge(merged_branch):
  sp.run('git fetch', shell=True)
  sp.run('git pull', shell =True)
  update_result = sp.run('git merge origin/master', shell=True, stdout=sp.PIPE)
  update_output = str(update_result.stdout)
  if "conflict" in update_output:
    print('')
    print('Se encontraron conflictos al actualizar con master')
    exit()
  else:
    print('')
    merge_result = sp.run('git merge '+merged_branch, shell=True, stdout=sp.PIPE)
    merge_output = str(merge_result.stdout)
    if "conflict" in merge_output:
      print('Se encontraron conflictos para realizar el merge')
      while True:
        prompt = str(input('Abortar el merge? (Y/n): '))
        if prompt == 'y' or prompt == 'Y':
          sp.run('git merge --abort')
          print('')
          print('Listo!')
        else:
          print('Resolver el conflicto y volver a intentar')
          exit()
    else:
      while True:
        prompt = str(input('No hubo conflictos. Pushear dev? (Y/n) '))
        if (prompt == 'y' or prompt == 'Y'):
          sp.run('git push', shell=True)
          print('')
          print('Listo!')
          exit()
        else:
          print('Ok! Saliendo...')
          exit()