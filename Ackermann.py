import sys

sys.setrecursionlimit(10000)

class Colors:
    ''' Doc '''
    
    END      = '\33[0m'
    BOLD     = '\33[1m'
    ITALIC   = '\33[3m'
    
    BLACK  = '\33[30m'
    RED    = '\33[31m'
    GREEN  = '\33[32m'
    YELLOW = '\33[33m'
    BLUE   = '\33[34m'
    VIOLET = '\33[35m'
    BEIGE  = '\33[36m'
    WHITE  = '\33[37m'

    def color_print(self, color_text, text):
        print('{}{}{}'.format(color_text, text, self.END))

class Ackermann(Colors):
    ''' Doc '''

    def __init__(self, top=None, init=True):
        self.top = top

        if init:
            self.color_print(self.BOLD, '\nWelcome, this is the Ackermann\'s algorithm')
            print('Please insert a number to generate the table with test values')
            self.menu()

    
    def menu(self):
        while True:
            try:
                print('\n----------------------------------')
                print('1: Print recursive table')
                print('2: Print specific value')
                print('0: Exit')
                print('----------------------------------\n')
                action = int(input('\nInsert a valid option: '))

                if action == 1:
                    self.print_table()
                elif action == 2:
                    self.print_specific_value()
                elif action == 0:
                    print('Bye, come back soon!')
                    break
                else:
                    print('was inserted a incorrect value, try again')
            except ValueError:
                print('Has occurred a problem, try again')
                self.menu()
    
    def print_table(self):
        self.top = int(input('From 1 to <value>:'))
        print('\n------------------')
        print('| m | n | A(m,n) |')
        print('------------------')

        for i in range(1, self.top + 1):
            for j in range(1, i + 1):
                print('| {} | {} |  {}  |'.format(i, j, self.ackermann(i, j)))
    
    def print_specific_value(self):
        m = int(input('Insert value to M: '))
        n = int(input('Insert value to N: '))

        print('\n A({}, {}) = {}'.format(
            m, n, self.ackermann(m, n)
        ))

    def ackermann(self, m, n):
        if m == 0:
            return n + 1
        elif n == 0:
            return self.ackermann(m - 1, 1)
        else: # m or n rather than zero
            return self.ackermann(m - 1, self.ackermann(m, n - 1))


Ackermann()
#print(Ackermann(init=False).ackermann(1,1))
