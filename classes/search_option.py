class SearchOption:
    def __init__(self, option):
        self.option = option

    def get_search_o(self, i):
        for so in self.option:
            print(str(i) + '. ' + so)
            i += 1

    '''
    def ex_search(self, i):
        running = True
        index = 1
        ex_index = 1
        ex_index != i

        while running:
            if ex_index < 4:
                print(str(index) + '. ' + self.option[ex_index])
                index += 1
                ex_index += 1
            else:
                running = False
    '''
