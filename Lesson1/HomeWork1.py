# we have norway text in old style formatting
# re-write the same text as:
# #1 string with format() call
# #2 f-string
# use linter(https://github.com/wemake-services/wemake-python-styleguide)
# to check your new created python module for possible linter errors
# try to run code from pycharm/command line

norway_text = 'Automatisering akselererer %syeblikket da roboter vil ' \
              'erobre planeten v%sr. (%s)' % ('ø', 'å', 'Æ')

# 1 Using format() method:
norway_text2 = 'Automatisering akselererer {}yeblikket da roboter vil ' \
               'erobre planeten v{}r. ({})'.format('ø', 'å', 'Æ')
assert norway_text == norway_text2, 'Not equal'

# 2 Using f-string:
character1, character2, character3 = 'ø', 'å', 'Æ'
norway_text3 = f'Automatisering akselererer {character1}yeblikket ' \
               f'da roboter vil erobre planeten v{character2}r. ({character3})'
assert norway_text == norway_text3, 'Not equal'
