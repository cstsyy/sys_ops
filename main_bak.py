# menu 1
ops_map = {
    'u': 'user',
    'f': 'filesystem',
    'n': 'network',
    's': 'services',
    'q': 'quit'
}

print ops_map

choice = True
while choice != "q":
    choice = raw_input('''
        user(u)
        filesystem(f)
        network(n)
        services(s)
        quit(q)
        '''
                       )

    print ops_map[choice]

# menu 2
ops_map = {
    'u': 'user',
    'f': 'filesystem',
    'n': 'network',
    's': 'services'
}


def ops_choice():
    return ops_map[raw_input('''
    Choose a operation:

    user(u)
    filesystem(f)
    network(n)
    services(s)

    Enter choice: ''').strip().lower()[0]]


print ops_choice()