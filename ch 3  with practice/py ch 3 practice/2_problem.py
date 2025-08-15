letter = ''' 
Dear <|Name|>,
you are selected!
<|Date|>
'''

print(letter.replace("<|Name|>","Drisha").replace("<|Date|>","20 April  2026"))
#name or date comma me likhane ka and replace chaining karte hai