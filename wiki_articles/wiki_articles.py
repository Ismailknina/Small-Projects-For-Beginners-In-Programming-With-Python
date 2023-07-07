import tkinter 
import webbrowser
import requests
from bs4 import BeautifulSoup

def random_article():
    try:
        article_title = ""
        # target url
        url = 'https://en.wikipedia.org/wiki/Special:Random'
        # making requests instance
        reqs = requests.get(url)
        # using the BeautifulSoup module
        soup = BeautifulSoup(reqs.text, 'html.parser')
        article_title = soup.find(class_="firstHeading").text
        def opening():
            webbrowser.open(f"https://en.wikipedia.org/wiki/{article_title}")    
        def no_btn():
            root.destroy()

        root = tkinter.Tk()
        wiki_articles = tkinter.Label(root , text="WiKi Articles" , foreground="white" , font=("Bold", 40) , background=("purple"))
        wiki_articles.pack(padx = 25 , pady = 25 , fill = "x")
        article_title_label = tkinter.Label(root , text=f"The Article Title Is :\n{article_title}", foreground="black" , font=("Bold", 40) , background=("white"))
        article_title_label.pack(padx = 15 , pady = 5 )
        Interesting_label = tkinter.Label(root , text="Are you interested with this one", foreground="pink" , font=("Bold", 20) )
        Interesting_label.pack(padx = 15 , pady = 5 )
        yes_button = tkinter.Button(root , text="YES" , command=opening)
        yes_button.pack(padx = 10 , pady = 10)
        no_button = tkinter.Button(root , text="No" , command=no_btn)
        no_button.pack(padx = 10 , pady = 10)
        root.mainloop()
    except:
        pass

random_article()