from youtube_transcript_api import YouTubeTranscriptApi

def get_transcript(vid):
	res = YouTubeTranscriptApi.get_transcript(vid, languages=["pt-PT"])
	tlist = []
	
	for i in res:
		tlist.append((i['text']))

	with open('file.md', 'w+') as f:

		# write elements of list
		for items in tlist:
			f.write('%s\n' %items)

		print("File written successfully")

vid = "xQ156y4TtJs"
get_transcript(vid)
