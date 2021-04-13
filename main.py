import requests,json,urllib.request,random,sys,time
from rich import print
from rich.console import Console
from rich.text import Text
from rich.panel import Panel
from rich.padding import Padding
from rich.style import Style

def getJsonQuote():
    with open("quotes.json") as f:
        data = json.load(f)
        randomInt = random.randint(0,(len(data)-1))
        quoteBody = data[randomInt]["text"]
        quoteAuthor = data[randomInt]["author"]
    f.close()
    return quoteBody,quoteAuthor


def getAdafruitQuote():
    lis = []
    with urllib.request.urlopen("https://www.adafruit.com/api/quotes.php") as response:
        quote = response.read()
        quote = quote.decode("utf-8")
        quote = quote.replace('[{"text":"','')
        quote = quote.replace('author":"','')
        quote = quote.replace('"}]','')
        quote = quote.split('","')
        
        quoteBody = quote[0]
        quoteAuthor = quote[1]

        return quoteBody,quoteAuthor

def displayQuote():
    console = Console()
    console.clear()
    if random.randint(0,1) == 0:
        quoteBody, quoteAuthor = getAdafruitQuote()
    else:
        quoteBody, quoteAuthor = getJsonQuote() 
    text = Text('"'+quoteBody +'"\n\n\n- '+ quoteAuthor)
    text.stylize("bold")
    console.print(Panel.fit(Padding(text,(1,1,1,1),style="o")))

def addQuote():
    quoteBody = input("Quote: ")
    quoteAuthor = input("Quote Author: ")
    print("\n\n\n")
    print(quoteBody)
    print("\n\n\n-" + quoteAuthor)
    if input("\nIs this what you would like to add? ") != "y":
        sys.exit()
    with open('quotes.json') as json_file:
        data = json.load(json_file)
        temp = data
        quoteTemplate = {
            "author": str(quoteAuthor),
            "text": str(quoteBody)
            }
        temp.append(quoteTemplate)
    with open("quotes.json","w") as f:
        json.dump(data, f, indent=4)
    f.close()
    print("WRITTEN")
while True:
    
    displayQuote()
    time.sleep(10)

