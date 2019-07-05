def song_decoder(song):
    word = "WUB"
    newword = song.replace(word, " ")
    newword = newword.strip()
    newword = " ".join(newword.split())
    return newword

print(song_decoder("WUBWEWUBAREWUBWUBTHEWUBCHAMPIONSWUBMYWUBFRIENDWUB"))