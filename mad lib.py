import random
from madlibStories import Beach, Zoo

if __name__ == "__main__":
    m = random.choice([Beach,Zoo])
    m.madlib()