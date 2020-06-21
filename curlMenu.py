import os
import sys

def main():
  x = 0
  
  print('Welcome to the database manager!\nPlease select the function you wish to run: \n')
  while(x == 0):
    selection = raw_input('\nCreate document(Enter C),\nRead document(Enter R),\nUpdate document(Enter U),\nDelete document(Enter D),\nExit application(Enter E): ').strip().lower()
    if selection == 'c':
      amount = input('\n\nHow many indexes are in your document?:  ')
      y = amount
      names = []
      values = []
      while(amount > 0):
        print('\nIndex number %d:' % amount)
        name = raw_input('\nEnter the name of the index: ')
        value = raw_input('\nEnter the value of the index: ')
        names.append(name)
        values.append(value)
        amount -= 1   
        
      indexString = ''
      z = 0
      if y == 1:
        indexString += '\"' + names[0] + '\"' + ' : ' + '\"' + values[0] + '\"'
      else:
        while(y > 0):
          if y == 1:
            indexString += '\"' + names[z] + '\"' + ' : ' + '\"' + values[z] + '\"'
          else:
            indexString += '\"' + names[z] + '\"' + ' : ' + '\"' + values[z] + '\", '
          z += 1
          y -= 1
        
      curlString = 'curl -H \"Content-Type: application/json\" -X POST -d \'{' + indexString + '}\' http://localhost:8080/createStock'
      print curlString
      os.system(curlString)
      
      answer = raw_input('\n\nContinue operations? (y/n)').strip().lower()
      if answer == 'n':
        x = 1
        
        
    if selection == 'r':
      name = raw_input('\nEnter the ticker value of the document you wish to read: ')
      curlString = 'curl -X GET http://localhost:8080/getStock?ticker=\"' + name + '\"'
      print curlString
      os.system(curlString)
      
      answer = raw_input('\n\nContinue operations? (y/n)').strip().lower()
      if answer == 'n':
        x = 1
    
    if selection == 'u':
      name = raw_input('\nEnter the ticker value of the document you wish to change: ')
      sector = raw_input('\nEnter the new sector(replace any spaces in the name with %20): ')
      
      curlString = 'curl -X PATCH \"http://localhost:8080/updateStock?ticker=\"' + name + '\"&sector=\"' + sector + '\"\"'
      print curlString
      os.system(curlString)
      
      answer = raw_input('\n\nContinue operations? (y/n)').strip().lower()
      if answer == 'n':
        x = 1
    
    if selection == 'd':
      name = raw_input('Enter the ticker name of the document you wish to delete: ')
      curlString = 'curl -X DELETE http://localhost:8080/deleteStock?ticker=\"' + name + '\"'
      print curlString
      os.system(curlString)
      
      answer = raw_input('\n\nContinue operations? (y/n)').strip().lower()
      if answer == 'n':
        x = 1
    
    else:
      break
        
  
main()