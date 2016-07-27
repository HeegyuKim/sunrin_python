
class Song:

	title = ""
	singer = ""
	composer = ""
	lyrics = ""

	def __str__(self):
		return "title=%s, singer=%s, composer=%s, lyrics=%s" % \
				(self.title, self.singer, self.composer, self.lyrics)

s = Song()
s.title = '벛꽃엔딩'
s.singer = '장범준'
s.composer = 'lyrics'
s.lyrics = '봄바람 휘날리며 우리 걸어요x100000'

print(s)