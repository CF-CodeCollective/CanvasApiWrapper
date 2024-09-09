file = open(r"c:\Users\Peter\VSCode\repos\CanvasEnroller\canvas_api\objects\enrollment.py", "r")

text = file.read()
text = text.replace("//", "#")

t = ""
for line in text.splitlines():
    if '"' in line:
        line = line.replace('"', '')
        index = line.index(':')
        line = line[:index]
        line += " = None"
    t += line + "\n"

text = t

print(text)

file.close()

file = open(r"c:\Users\Peter\VSCode\repos\CanvasEnroller\canvas_api\objects\enrollment.py", "w")

file.write(text)

file.close()