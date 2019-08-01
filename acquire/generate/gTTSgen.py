from gtts import gTTS
import abuse

counter = 0
ab = abuse.ListAllAbuses()
for abuse in ab:
    m=gTTS(text=abuse, lang="en", slow=False)
    m.save("{}.mp3".format(abuse))
    counter+=1
print("Number of files created : {}".format(str(counter)))