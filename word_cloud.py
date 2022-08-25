import glob
from tqdm import tqdm
import json
from collections import Counter

all_words = Counter()

stop_words = ['det', 'som', 'och', 'är', 'att', 'på', 'en', 'i', 'jag', 'var', 'man', 'så', 'men', 'inte', 'de', 'den', 'har', 'med', 'för', 'vi', 'här', 'om', 'till', 'av', 'kan', 'du', 'också', 'ett', 'då', 'lite', 'där', 'hade', 'ska', 'mycket', 'finns', 'ju', 'när', 'väldigt','sig', 'sen', 'kommer', 'vad', 'från', 'eller', 'skulle', 'vara', 'nu', 'alla', 'tror', 'kanske', 'bara', 'in', 'upp', 'någon', 'många', 'nej','vill', 'får', 'gjorde', 'hur', 'blev', 'blir', 'väl', 'mig', 'ut', 'fick', 'mer', 'säga', 'göra', 'vet', 'gör', 'precis', 'ganska', 'något', 'andra', 'fanns', 'säger', 'heter', 'ser', 'någonting', 'bra', 'måste', 'sin', 'just', 'alltså', 'går', 'olika', 'utan', 'under', 'även', 'hela', 'själv', 'kom', 'ni', 'efter', 'över', 'varit',  'helt', 'samma', 'min', 'sätt', 'kunde', 'allt', 'gick', 'sa', 'några', 'ingen', 'detta', 'få', 'stor', 'ta', 'tar', 'se', 'alltid', 'stora', 'faktiskt', 'del', 'nog']

progress = tqdm(glob.glob('transcripts/*.json'))
for transcript_file in progress:
    with open(transcript_file) as transcript_json:
        data = json.load(transcript_json)
        words = [x['word'] for x in data['results']['channels'][0]['alternatives'][0]['words'] if x['word'] not in stop_words]
        all_words.update(words)
#        print(all_words.most_common(20))
print([a[0] for a in all_words.most_common(20)])
