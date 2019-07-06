import os

def generate(dir, depth, file): 
    for path in os.listdir(dir): 
        if depth == 1 and path == 'README.md':
            continue
        if path.startswith('.'):
            continue
        fullPath = os.path.join(dir, path) 
        print(fullPath)
        if os.path.isdir(fullPath): 
            for i in range(0, depth):
                file.write('#')
            file.write(' ' + path + '\n')
            generate(fullPath, depth + 1, file) 
        else:
            file.write('- [' + path + '](' + fullPath + ')' + '\n')

dir = './'
with open('README.md', 'w') as README:
    generate(dir, 1, README)