import sys
class Trie:

	def __init__(self, c):

		self.childrenMap = {}
		self.isCompleteWord = False
		self.numWords = 0
		self.char = c
		if c == '*':
			self.isRootNode = True
		else:
			self.isRootNode = False


	def addWord(self, word):

		if len(word) == 0:
			self.isCompleteWord = True
			self.numWords += 1
			return

		if word[0] not in self.childrenMap:
			self.childrenMap[word[0]] = Trie(word[0])

		cnode = self.childrenMap[word[0]]
		self.numWords += 1

		cnode.addWord(word[1:])

	def findNumWords(self, prefix):

		if len(prefix) == 0:
			# Prefix is matched , return 
			return self.numWords

		if prefix[0] not in self.childrenMap:
			return 0

		cnode = self.childrenMap[prefix[0]]

		return cnode.findNumWords(prefix[1:])

n = int(raw_input().strip())
root = Trie('*')
isFirstFind = True
for a0 in xrange(n):
    op, contact = raw_input().strip().split(' ')
    
    if op == 'add':
        root.addWord(contact)
    elif op == 'find':
        if not isFirstFind:
            sys.stdout.write('\n')
        sys.stdout.write(str(root.findNumWords(contact)))
        isFirstFind = False