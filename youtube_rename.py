file=open('youtube.txt','w')
try:
    file.write('youtube channel')
finally:
    file.close()

with open('youtube.txt','w') as file:
    file.write('youtube channel')