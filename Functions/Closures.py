def html_tag(tag):
    def html_text(text):
        print("<"+tag+">"+text+"</"+tag+">")
    return html_text
f1 = html_tag("h1")
f1("Hello Sir")
f1("This is the list of items:")

f2 = html_tag("li")
f2("Pen")
f2("Pencil")
f2("Eraser")
f2("Sharpner")
