import feedparser
import json
import hashlib
import os
from deepgram import Deepgram
import asyncio
import json
from tqdm import tqdm
from time import sleep

async def main():
    f = open('settings.json')
    settings = json.load(f)
    f.close()

    DEEPGRAM_API_KEY = settings['api_token']

    feed = feedparser.parse("https://api.sr.se/api/rss/pod/21650")

    progress = tqdm(feed['entries'])
    for entry in progress:
        soundfile_url = entry['links'][1]['href']
        title = entry['title']
        summary = entry['summary']
        hashed_link = hashlib.sha1(bytes(entry['link'], 'utf-8')).hexdigest()
        transcript_file = os.path.join("transcripts", f"{hashed_link}.json")

        if os.path.exists(transcript_file):
            progress.set_description(f"Transcript for {title} already exists, skipping.")
            continue

        progress.set_description(f"{title}")

        dg_client = Deepgram(DEEPGRAM_API_KEY)
        source = {'url': soundfile_url}
        options = {'punctuate': True, 'language': 'sv', 'model': 'general'}

        response = await dg_client.transcription.prerecorded(source, options)

        with open(transcript_file, 'w') as outfile:
            json.dump(response, outfile)

asyncio.run(main())
