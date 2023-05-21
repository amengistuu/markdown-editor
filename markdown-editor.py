formats = ('plain', 'bold', 'italic', 'header', 'link', 'inline-code',
           'ordered-list', 'unordered-list', 'new-line')

commands = ('!help', '!done')


formatted_text = ''''''


def helper():
    print('Available formatters: ', ' '.join(formats))
    print('Special commands: ', ' '.join(commands))


def header():
    while True:
        try:
            level = int(input('Level: '))
            assert 1 <= level <= 6
            text = input('Text: ')
        except (ValueError, AssertionError):
            print('The level should be within the range of 1 to 6')
            continue
        else:
            break

    return '#' * level + ' ' + text + new_line()


def plain():
    text = input('Text: ')
    return text


def link():
    while True:
        try:
            label = input('Label: ')
            url = input('URL: ')
        except ValueError:
            pass
        else:
            break

    return f'[{label}]({url})'


def inline_code():
    text = input('Text: ')
    return f'`{text}`'


def bold():
    text = input('Text: ')
    return f'**{text}**'


def italic():
    text = input('Text: ')
    return f'*{text}*'


def new_line():
    return '\n'

def ordered_list():
    while True:
        try:
            rows = int(input('Number of rows: '))
            assert rows > 0
            collector = []
            for num in range(rows):
                text = input(f'Row #{num + 1}: ')
                collector.append(text)
        except(ValueError, AssertionError):
            print('The number of rows should be greater than zero')
            continue
        else:
            break
    our_list = ""
    counter = 1
    for item in collector:
        our_list += f'{counter}. {str(item) + new_line()}'
        counter += 1
    return our_list

def unordered_list():
    while True:
        try:
            rows = int(input('Number of rows: '))
            assert rows > 0
            collector = []
            for num in range(rows):
                text = input(f'Row #{num + 1}: ')
                collector.append(text)
        except(ValueError, AssertionError):
            print('The number of rows should be greater than zero')
            continue
        else:
            break
    our_list = ""
    for item in collector:
        our_list += f'* {str(item) + new_line()}'
    return our_list

def formatter(format_type, text):
    text += format_funcs.get(format_type)()
    return text

format_funcs = dict(
        {
            'header': header,
            'plain': plain,
            'link': link,
            'inline-code': inline_code,
            'bold': bold,
            'italic': italic,
            'new-line': new_line,
            'ordered-list': ordered_list,
            'unordered-list': unordered_list
        }
    )


while True:
    cmd = input('Choose a formatter: ')
    if cmd == '!help':
        helper()
    elif cmd == '!done':
        break
    elif cmd in formats:
        formatted_text = formatter(cmd, formatted_text)
        print(formatted_text)
    else:
        print('Unknown formatting type or command')