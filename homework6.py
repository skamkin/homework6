class_book = {'Antonov':5 ,'Volodin':10}
print(class_book)
print(class_book['Volodin'])
print(class_book.get('Kamkin'))
class_book.update({'Mishin: 15 ,'
                   'Ushakov': 27})
print(class_book)
a = (class_book.pop('Volodin'))
print(a)
print(class_book)
set_ = {1,2,3,4,'String',2,3,'String',(5,6)}
print(set_)
list_ = set(set_)
print(list_.add((15,16)))
print(list_.remove('String'))
print(list_)