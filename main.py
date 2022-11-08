import sys
import json
import clipboard

SAVED_DATA = "clipboard.json"


def saveData(filepath, data):
    with open(filepath, "w") as f:
        json.dump(data, f)

def loadData(filepath):
    try:
        with open(filepath, "r") as f:
            data = json.load(f)
            return data
    except:
        return {}

# to check for arguments

if len(sys.argv) == 2:
    command = sys.argv[1]
    data = loadData(SAVED_DATA)

    if command == 'save':
        key = input('Enter a key: ')
        data[key] = clipboard.paste()
        # data[key] = 'default'
        saveData(SAVED_DATA, data)
        print('data saved !')
    elif command == 'load':
        key = input('Enter a key: ')
        if key in data:
            clipboard.copy(data[key])
            # print(data[key])
            print('data copied to clipboard')
        else:
            print('key does not exist, please check what you typed')
    elif command == 'list':
        print(data)
    elif command == 'delete':
        key = input('Enter a key: ')
        if key in data:
            data.pop(key)
            saveData(SAVED_DATA, data)
            print(data.copy())
            print('%s has been deleted' % (key))
        else:
            print('%s does not exist, please check what you typed' % (key))
    else:
        print('unknown command')
        print('command should either be save, load or list')
else:
    print('please pass in one command')
    print('command should either be save, load or list')