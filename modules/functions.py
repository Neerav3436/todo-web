
FIRST_CONSTANT = 'first constant'
SECOND_CONSTANT = 'second constant'


def get_todos(filepath='files/sample.txt'): # default overriden by arg if provided
    
    '''
    This code is used to get todos
    basically read files
    '''
    todos = []
    with open(filepath) as file_local:
            todos = file_local.readlines()
    return todos


def write_todos(todos_arg, filepath = 'files/sample.txt'): # non default param moves first and defult in trailing
    
    '''
    This code is used to write todos
    basically write files
    '''
    with open(filepath,"w") as file_local:
            file_local.writelines(todos_arg)



print("inside functions....", __name__) 
'''
prints __main__ when executed via functions
prints modules.functions when called from section14.py as it imports modules.functions to reach this main
'''

if __name__=='__main__':
      print("called from functions.py")
else:
      print("called via imports from section14.py")