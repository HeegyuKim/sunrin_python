
import song

class Album:
	
	title = ''
	artist = ''
	created = ''
	description = ''
	num_songs = 0
	songs = []

	def __init__(self, title, artist, created, description, songs):
		self.title = title
		self.artist = artist
		self.created = created
		self.description = description
		self.num_songs = len(songs)
		self.song = list(songs)


s1 = song.Song()
s1.title = '안아줘'
s1.singer = '정준일'
s1.composer = '정준일'
s1.lyrics = '그냥 날 안아줘~~'

s2 = song.Song()
s2.title = '벛꽃엔딩'
s2.singer = '장범준'
s2.composer = 'lyrics'
s2.lyrics = '봄바람 휘날리며 우리 걸어요x100000'

a = Album('라이브', '정준일', '2015/07/01', '정준일의 음악 앨범',
	#['너에게', 'Overture(Live)', 'in Love', 'Greet', 'Christmas merry, merry']
	[s1, s2]
	)
