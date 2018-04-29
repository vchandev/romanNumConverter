def convert(num):

  romanNum = ''
  quotient = 0
  remainder = num

  romanDict = {int(1000): str('M'),
                500: 'D',
                100: 'C',
                 50: 'L',
                 10: 'X',
                  9: 'IX',
                  8: 'VIII',
                  7: 'VII',
                  6: 'VI',
                  5: 'V',
                  4: 'IV',
                  3: 'III',
                  2: 'II',
                  1: 'I'
          }
          
  for key, value in romanDict.items():
    i = 1
    
    quotient = int(remainder/key)
    
    if quotient == 0:
      continue
  
    if quotient >= 1:
      
      while i <= quotient:
        romanNum += value
        i += 1
        
    remainder = int(remainder%key)
  
  return romanNum
    
def main():
  
  result = ''
  
  n = input("Enter a number(1-4999): ")
  n = int(n)
  
  if n < 1 or n > 4999:
    print('Invalid Number')
  else:
    result = convert(n)
    print('Roman Numeral: ', result)

main()