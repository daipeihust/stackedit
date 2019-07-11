#!/usr/local/bin/python3
import os

def generate(dir, depth, file): 
    for path in os.listdir(dir): 
        if depth == 1 and path == 'README.md':
            continue
        if path.startswith('.'):
            continue
        fullPath = os.path.join(dir, path) 
        if os.path.isdir(fullPath): 
            for i in range(0, depth):
                file.write('#')
            title = ' ' + path + '\n'
            print(title)
            file.write(title)
            generate(fullPath, depth + 1, file) 
        else:
            if not path.endswith('.md'):
                continue
            content = '- [' + path + '](' + fullPath + ')' + '\n'
            print(content)
            file.write(content)

dir = './'
with open('README.md', 'w') as README:
    generate(dir, 1, README)
    README.write('<br><br>\n > Note: 不要在仓库根目录直接增加文件，新增的文件放在对应的目录下面，每次新增文件后在命令行执行：python3 directory.py')
print('done!')