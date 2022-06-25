import random

def getWords(filename):
  f = open(filename, "r")
  list = []
  for line in f:
    words = line.split()
    for word in words:
      list.append(word)
  return tuple(list)

nouns = getWords('nouns.txt')
verbs = getWords('verbs.txt')
articles = getWords('articles.txt')
prepositions = getWords('prepositions.txt')

def sentence():
  return nounPhrase() + " " + verbPhrase()

def nounPhrase():
  return random.choice(articles) + " " + random.choice(nouns)

def verbPhrase():
    return random.choice(verbs) + " " + nounPhrase() + " " + prepositionalPhrase()

def prepositionalPhrase():
  return random.choice(prepositions) + " " + nounPhrase()
  
def main():
  number = int(input("Enter the number of sentences: "))
  for count in range(number):
    print(sentence())