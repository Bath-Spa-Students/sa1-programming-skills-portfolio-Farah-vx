#dictionary
dictionary = {'name': 'farah',
              'age': '18',
              'nation' : 'srilanka'}

print(dictionary)

#finding the type
dictionary = {'name': 'farah',
              'age': '18',
              'nation' : 'srilanka'}

print(dictionary,type(dictionary))

#checking if the student is in the dictionary 
dictionary = {'name': 'farah',
              'age': '18',
              'nation' : 'srilanka'}

print(dictionary.get('student'))
      
#giving a value to student
dictionary = {'name': 'farah',
              'age': '18',
              'nation' : 'srilanka'}
print(dictionary.get('student','joshua'))

#testing .items
dictionary = {'name': 'farah',
              'age': '18',
              'nation' : 'srilanka'}
print(dictionary.items())

#checking keys
dictionary = {'name': 'farah',
              'age' : '18',
              'nation' : 'srilanka'}
print(dictionary.keys())

#deleting a key
dictionary = {'name': 'farah',
              'age': '18',
              'nation' : 'srilanka'}

del dictionary ['age']
print (dictionary.items())

#pop method
dictionary = {'name': 'farah',
              'age': '18',
              'nation' : 'srilanka'}

print (dictionary.pop('name'))
print(dictionary.values())
print(dictionary.keys())

#pop items
dictionary = {'name': 'farah',
              'age': '18',
              'nation' : 'srilanka'}

print(dictionary.popitem())
print(dictionary.keys())
print(dictionary.values())

#loop
dictionary = {'name': 'farah',
              'age': '18',
              'nation' : 'srilanka'}

for key,value in dictionary.items():
    print(f'key: {key},value: {value}')
