import requests
import time
beemoviescript = open("beemoviescript.txt").read()
print(f"Script loaded : size {len(beemoviescript)} characters")


def split_string(text, blocksize):
    res = []
    block = text[:blocksize]
    #do..while
    while True:
        block = text[:blocksize]
        res.append(block)
        text = text[blocksize:]
        if(len(block) != blocksize):
            break
    return res

beeMovieBlocks = split_string(text=beemoviescript, blocksize=255)
#print(len(beeMovieBlocks))
#print(beeMovieBlocks[0])
for idx, scriptBlock in enumerate(beeMovieBlocks):
    r = requests.get(f"https://volatile.wtf/?key=BeeMovieScript{idx}&val={scriptBlock}")
    print(f"Done {idx}")
    if(r.headers['X-Rate-Limit-Reset']):
        print("Write limit reached")
        print(f"Sleeping for {r.headers['X-Rate-Limit-Reset']} seconds")
        time.sleep(int(r.headers['X-Rate-Limit-Reset']))