import sys

solved_cube = [           1, 1,
                          1, 1,
                2, 2,
                2, 2,
                          3, 3,
                          3, 3,
                                    4, 4,
                                    4, 4,
                                              5, 5,
                                              5, 5,
                          6, 6,
                          6, 6]

starting_cube = [         1, 1,
                          1, 1,
                2, 2,
                2, 2,
                          3, 3,
                          3, 3,
                                    4, 4,
                                    4, 4,
                                              5, 5,
                                              5, 5,
                          6, 6,
                          6, 6]

def cube_print(cube_to_print):
    print('    ' + cube_to_print[0] + ' ' + cube_to_print[1])
    print('    ' + cube_to_print[2] + ' ' + cube_to_print[3])
    print(cube_to_print[4] + ' ' + cube_to_print[5] + ' ' + cube_to_print[8] + ' ' + cube_to_print[9] + ' ' + cube_to_print[12] + ' ' + cube_to_print[13] + ' ' + cube_to_print[16] + ' ' + cube_to_print[17])
    print(cube_to_print[6] + ' ' + cube_to_print[7] + ' ' + cube_to_print[10] + ' ' + cube_to_print[11] + ' ' + cube_to_print[14] + ' ' + cube_to_print[15] + ' ' + cube_to_print[18] + ' ' + cube_to_print[19])
    print('    ' + cube_to_print[20] + ' ' + cube_to_print[21])
    print('    ' + cube_to_print[22] + ' ' + cube_to_print[23])
    print()

def is_solved(cube):
    if (cube[0] == cube[1]) and (cube[2] == cube[3]) and (cube[0] == cube[2]):
        if (cube[4] == cube[5]) and (cube[6] == cube[7]) and (cube[4] == cube[6]):
            if (cube[8] == cube[9]) and (cube[10] == cube[11]) and (cube[8] == cube[10]):
                return True
    return False

def add_to_set(cube, cube_queue_set):
    cube_copy = cube[:]
    for i in range(0, 4):
        cube_copy = Ri(L(cube_copy))
        for j in range(0, 4):
            cube_copy = D(Ui(cube_copy))
            cube_queue_set.add(int(''.join(map(str, cube_copy))))

    cube_copy = F(Bi(cube_copy))
    for i in range(0, 4):
        cube_copy = Ri(L(cube_copy))
        for j in range(0, 4):
            cube_copy = D(Ui(cube_copy))
            cube_queue_set.add(int(''.join(map(str, cube_copy))))

    cube_copy = F(F(Bi(Bi(cube_copy))))
    for i in range(0, 4):
        cube_copy = Ri(L(cube_copy))
        for j in range(0, 4):
            cube_copy = D(Ui(cube_copy))
            cube_queue_set.add(int(''.join(map(str, cube_copy))))


def find_orientation(cube, cube_keys):
    k = 0
    cube_copy = cube[:]
    for i in range(0, 4):
        cube_copy = Ri(L(cube_copy))
        for j in range(0, 4):
            cube_copy = D(Ui(cube_copy))
            if int(''.join(map(str, cube_copy))) in cube_keys:
                return k, i, j, cube_copy

    cube_copy = F(Bi(cube_copy))
    k += 1
    for j in range(0, 4):
        cube_copy = D(Ui(cube_copy))
        if int(''.join(map(str, cube_copy))) in cube_keys:
            return k, 3, j, cube_copy

    cube_copy = F(F(Bi(Bi(cube_copy))))
    k += 2
    for j in range(0, 4):
        cube_copy = D(Ui(cube_copy))
        if int(''.join(map(str, cube_copy))) in cube_keys:
            return k, 3, j, cube_copy

def convert_to_moves(list_of_numbers):
    move_names = ['U', 'Ui', 'F', 'Fi', 'R', 'Ri', 'U2', 'F2', 'R2']
    return [move_names[x] for x in list_of_numbers]

def U(cube):
    cube_copy = cube[:]
    (cube_copy[0], cube_copy[1], cube_copy[2], cube_copy[3], cube_copy[4], cube_copy[5], cube_copy[8], cube_copy[9], cube_copy[12], cube_copy[13], cube_copy[16], cube_copy[17]) = (cube_copy[2], cube_copy[0], cube_copy[3], cube_copy[1], cube_copy[8], cube_copy[9], cube_copy[12], cube_copy[13], cube_copy[16], cube_copy[17], cube_copy[4], cube_copy[5])
    return cube_copy

def Ui(cube):
    cube_copy = cube[:]
    (cube_copy[0], cube_copy[1], cube_copy[2], cube_copy[3], cube_copy[4], cube_copy[5], cube_copy[8], cube_copy[9], cube_copy[12], cube_copy[13], cube_copy[16], cube_copy[17]) = (cube_copy[1], cube_copy[3], cube_copy[0], cube_copy[2], cube_copy[16], cube_copy[17], cube_copy[4], cube_copy[5], cube_copy[8], cube_copy[9], cube_copy[12], cube_copy[13])
    return cube_copy

def F(cube):
    cube_copy = cube[:]
    (cube_copy[2], cube_copy[3], cube_copy[5], cube_copy[7], cube_copy[8], cube_copy[9], cube_copy[10], cube_copy[11], cube_copy[12], cube_copy[14], cube_copy[20], cube_copy[21]) = (cube_copy[7], cube_copy[5], cube_copy[20], cube_copy[21], cube_copy[10], cube_copy[8], cube_copy[11], cube_copy[9], cube_copy[2], cube_copy[3], cube_copy[14], cube_copy[12])
    return cube_copy

def Fi(cube):
    cube_copy = cube[:]
    (cube_copy[2], cube_copy[3], cube_copy[5], cube_copy[7], cube_copy[8], cube_copy[9], cube_copy[10], cube_copy[11], cube_copy[12], cube_copy[14], cube_copy[20], cube_copy[21]) = (cube_copy[12], cube_copy[14], cube_copy[3], cube_copy[2], cube_copy[9], cube_copy[11], cube_copy[8], cube_copy[10], cube_copy[21], cube_copy[20], cube_copy[5], cube_copy[7])
    return cube_copy

def D(cube):
    cube_copy = cube[:]
    (cube_copy[6], cube_copy[7], cube_copy[10], cube_copy[11], cube_copy[14], cube_copy[15], cube_copy[18], cube_copy[19], cube_copy[20], cube_copy[21], cube_copy[22], cube_copy[23]) = (cube_copy[18], cube_copy[19], cube_copy[6], cube_copy[7], cube_copy[10], cube_copy[11], cube_copy[14], cube_copy[15], cube_copy[22], cube_copy[20], cube_copy[23], cube_copy[21])
    return cube_copy

def Di(cube):
    cube_copy = cube[:]
    (cube_copy[6], cube_copy[7], cube_copy[10], cube_copy[11], cube_copy[14], cube_copy[15], cube_copy[18], cube_copy[19], cube_copy[20], cube_copy[21], cube_copy[22], cube_copy[23]) = (cube_copy[10], cube_copy[11], cube_copy[14], cube_copy[15], cube_copy[18], cube_copy[19], cube_copy[6], cube_copy[7], cube_copy[21], cube_copy[23], cube_copy[20], cube_copy[22])
    return cube_copy

def B(cube):
    cube_copy = cube[:]
    (cube_copy[0], cube_copy[1], cube_copy[4], cube_copy[6], cube_copy[13], cube_copy[15], cube_copy[16], cube_copy[17], cube_copy[18], cube_copy[19], cube_copy[22], cube_copy[23]) = (cube_copy[13], cube_copy[15], cube_copy[1], cube_copy[0], cube_copy[23], cube_copy[22], cube_copy[18], cube_copy[16], cube_copy[19], cube_copy[17], cube_copy[4], cube_copy[6])
    return cube_copy

def Bi(cube):
    cube_copy = cube[:]
    (cube_copy[0], cube_copy[1], cube_copy[4], cube_copy[6], cube_copy[13], cube_copy[15], cube_copy[16], cube_copy[17], cube_copy[18], cube_copy[19], cube_copy[22], cube_copy[23]) = (cube_copy[6], cube_copy[4], cube_copy[22], cube_copy[23], cube_copy[0], cube_copy[1], cube_copy[17], cube_copy[19], cube_copy[16], cube_copy[18], cube_copy[15], cube_copy[13])
    return cube_copy

def R(cube):
    cube_copy = cube[:]
    (cube_copy[1], cube_copy[3], cube_copy[9], cube_copy[11], cube_copy[12], cube_copy[13], cube_copy[14], cube_copy[15], cube_copy[16], cube_copy[18], cube_copy[21], cube_copy[23]) = (cube_copy[9], cube_copy[11], cube_copy[21], cube_copy[23], cube_copy[14], cube_copy[12], cube_copy[15], cube_copy[13], cube_copy[3], cube_copy[1], cube_copy[18], cube_copy[16])
    return cube_copy

def Ri(cube):
    cube_copy = cube[:]
    (cube_copy[1], cube_copy[3], cube_copy[9], cube_copy[11], cube_copy[12], cube_copy[13], cube_copy[14], cube_copy[15], cube_copy[16], cube_copy[18], cube_copy[21], cube_copy[23]) = (cube_copy[18], cube_copy[16], cube_copy[1], cube_copy[3], cube_copy[13], cube_copy[15], cube_copy[12], cube_copy[14], cube_copy[23], cube_copy[21], cube_copy[9], cube_copy[11])
    return cube_copy

def L(cube):
    cube_copy = cube[:]
    (cube_copy[0], cube_copy[2], cube_copy[4], cube_copy[5], cube_copy[6], cube_copy[7], cube_copy[8], cube_copy[10], cube_copy[17], cube_copy[19], cube_copy[20], cube_copy[22]) = (cube_copy[19], cube_copy[17], cube_copy[6], cube_copy[4], cube_copy[7], cube_copy[5], cube_copy[0], cube_copy[2], cube_copy[22], cube_copy[20], cube_copy[8], cube_copy[10])
    return cube_copy

def Li(cube):
    cube_copy = cube[:]
    (cube_copy[0], cube_copy[2], cube_copy[4], cube_copy[5], cube_copy[6], cube_copy[7], cube_copy[8], cube_copy[10], cube_copy[17], cube_copy[19], cube_copy[20], cube_copy[22]) = (cube_copy[8], cube_copy[10], cube_copy[5], cube_copy[7], cube_copy[4], cube_copy[6], cube_copy[20], cube_copy[22], cube_copy[2], cube_copy[0], cube_copy[19], cube_copy[17])
    return cube_copy

def F2(cube):
    cube_copy = cube[:]
    cube_copy = F(F(cube_copy))
    return cube_copy

def U2(cube):
    cube_copy = cube[:]
    cube_copy = U(U(cube_copy))
    return cube_copy

def R2(cube):
    cube_copy = cube[:]
    cube_copy = R(R(cube_copy))
    return cube_copy

def L2(cube):
    cube_copy = cube[:]
    cube_copy = L(L(cube_copy))
    return cube_copy

def D2(cube):
    cube_copy = cube[:]
    cube_copy = D(D(cube_copy))
    return cube_copy

def B2(cube):
    cube_copy = cube[:]
    cube_copy = B(B(cube_copy))
    return cube_copy

def bfs():
    cube_queue = [starting_cube]
    cube_queue_set = set()
    cube_queue_set.add(int(''.join(map(str, starting_cube))))
    visited_nodes = set()
    path = {}
    path[int(''.join(map(str, starting_cube)))] = (None, None)

    cube_queue_inv = [solved_cube]
    cube_queue_set_inv = set()
    cube_queue_set_inv.add(int(''.join(map(str, solved_cube))))
    visited_nodes_inv = set()
    path_inv = {}
    path_inv[int(''.join(map(str, solved_cube)))] = (None, None)

    while(1):
        if len(cube_queue) != 0:
            parent_cube = cube_queue.pop(0)
            i = 0

            if int(''.join(map(str, parent_cube))) in visited_nodes_inv:
                found(parent_cube, path, path_inv, 0)
            for child in [U(parent_cube), Ui(parent_cube), F(parent_cube), Fi(parent_cube), R(parent_cube), Ri(parent_cube), U(U(parent_cube)), F(F(parent_cube)), R(R(parent_cube))]:
                child_string = int(''.join(map(str, child)))
                if child_string in visited_nodes:
                    continue
                if child_string not in cube_queue_set:
                    path[child_string] = (parent_cube, i)
                    cube_queue.append(child)
                    add_to_set(child, cube_queue_set)
                i += 1
            add_to_set(parent_cube, visited_nodes)

        if len(cube_queue_inv) != 0:
            parent_cube_inv = cube_queue_inv.pop(0)
            i = 0

            if int(''.join(map(str, parent_cube_inv))) in visited_nodes:
                found(parent_cube_inv, path, path_inv, 1)
            for child in [U(parent_cube_inv), Ui(parent_cube_inv), F(parent_cube_inv), Fi(parent_cube_inv), R(parent_cube_inv), Ri(parent_cube_inv), U(U(parent_cube_inv)), F(F(parent_cube_inv)), R(R(parent_cube_inv))]:
                child_string = int(''.join(map(str, child)))
                if child_string in visited_nodes_inv:
                    continue
                if child_string not in cube_queue_set_inv:
                    path_inv[child_string] = (parent_cube_inv, i)
                    cube_queue_inv.append(child)
                    add_to_set(child, cube_queue_set_inv)
                i += 1
            add_to_set(parent_cube_inv, visited_nodes_inv)

def found(cube, path, path_inv, inv):
    action_list = list()
    action_list_inv = list()

    if inv == 0:
        k, i, j, cube_inv = find_orientation(cube, path_inv)
    else:
        cube_inv = cube[:]
        k, i, j, cube = find_orientation(cube, path)
        k, i, j, cube_inv = find_orientation(cube, path_inv)

    while cube is not None:
        row = path[int(''.join(map(str, cube)))]
        if len(row) == 2:
            cube = row[0]
            action = row[1]
            if action is not None:
                action_list.append(action)
        else:
            break

    action_list = convert_to_moves(action_list[::-1])
    action_list.append(['', 'Z', '', 'Zi'][k])
    action_list.append(['Xi', 'X2', 'X', ''][i])
    action_list.append(['Yi', 'Y2', 'Y', ''][j])

    while cube_inv is not None:
        row = path_inv[int(''.join(map(str, cube_inv)))]
        if len(row) == 2:
            cube_inv = row[0]
            action = row[1]
            if action is not None:
                if action < 6:
                    if (action % 2 == 0):
                        action += 1
                    else:
                        action -= 1
                action_list_inv.append(action)
        else:
            break

    action_list.extend(convert_to_moves(action_list_inv))
    print(' '.join([x for x in action_list if x != '']))

    exit(0)

starting_cube = [x for x in sys.argv[1]]
starting_cube = map(int, starting_cube)

bfs()
