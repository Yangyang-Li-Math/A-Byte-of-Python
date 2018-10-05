import os
import time

source = ['./__pycache__']

target_dir = './backup'

target = target_dir + os.sep + time.strftime('%Y%m%d%H%M%S') + '.zip'

if not os.path.exists(target_dir):
    os.mkdir(target_dir)

zip_command = 'zip -r {0} {1}'.format(target, ' '.join(source))

print('Zip command')
print(zip_command)
if os.system(zip_command) == 0:
    print('Successful backup to', target)
else:
    print('Backup FAILED')