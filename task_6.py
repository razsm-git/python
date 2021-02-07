with open('text_6.txt', 'r', encoding='utf-8') as lesson:
    my_dict = {}
    while True:
        hour_lek = 0
        hour_pr = 0
        hour_lab = 0
        var = lesson.readline()
        if var == '':
            break
        else:
            try:
                lek = var.index('лек')
                hour_lek = int(var[lek - 3: lek - 1])
            except ValueError:
                err = 1
            try:
                pr = var.index('пр')
                hour_pr = int(var[pr - 3: pr - 1])
            except ValueError:
                err = 1
            try:
                lab = var.index('лаб')
                hour_lab = int(var[lab - 3: lab - 1])
            except ValueError:
                err = 1
            try:
                name_ind = var.index(':')
                name = var[0: name_ind]
            except ValueError:
                err = 1
            # my_dict[name] = int(hour_pr)
            my_dict[name] = hour_lek + hour_pr + hour_lab
    print(my_dict)
