###### Documentation  #####################################################
# def blueram():
#     '''Documentation
# ololol
# azaza'''
#     print('Hello')
# print( blueram.__doc__)




###### Функции используют функции ##############################################
# Example 1
def blueram(name):
    print('Hello, ' + name + '!')  # или здесь можно поставить name()

def read_name():
    return ':::' + input('Input your name: ') + ':::'

blueram(read_name()) # или здесь можно поставить blueram( read_name )
