#https://www.codewars.com/kata/551dc350bf4e526099000ae5/train/python
def song_decoder(song):
    return " ".join([word for word in song.split("WUB") if word != ""])
    
