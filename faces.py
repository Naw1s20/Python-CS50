import emoji
def main():
    
    
    text=input()
    converted = convert(text)
    print(converted)


def convert(phrase):
        emoted = emoji.emojize(phrase, language="alias")
        
        return emoted
    
main()