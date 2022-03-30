# Ex 1
import re 

r_final = ""
file = open("ex1.txt", "r")
for line in file:
    r = re.sub(r'(\\title)','#',line)
    r1 = re.sub(r'\\section',"##",r)
    r2 = re.sub(r'\\subsection',"###",r1)
    r3 = re.sub(r'\\\\begin{.*}', "",r2)
    r4 = re.sub(r'\\item'," - ",r3)
    r5 = re.sub(r'\\end{.*}$', "", r4)
    #r6 = re.sub(r'(\n+)',"",r5)
    print(r5)
    r_final += r5
output = open("output_1.txt", "w+")
output.write(r_final)
output.close()

file.close()
