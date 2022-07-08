from pygit2 import Repository
branch = Repository('.').head.shorthand
print(branch)