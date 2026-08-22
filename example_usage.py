from client import RealtimeVoiceTranslationMultilingualDubbingClient

def main():
    client = RealtimeVoiceTranslationMultilingualDubbingClient()
    res = client.stream_translate_voice('pcm_stream_live', 'en', ['es', 'ja', 'de'])
    print('Source: ' + res['source_lang'] + ' | Avg Latency: ' + str(res['average_latency_ms']) + 'ms | Voice Preserved: ' + str(res['voice_identity_preserved']))
    print('Dubbed Streams:')
    for d in res['realtime_dubbed_streams']:
        print('  [' + d['lang'].upper() + '] ' + d['translated_text'] + ' (' + str(d['latency_ms']) + 'ms, ' + str(round(d['voice_clone_similarity']*100, 1)) + '% similarity)')

if __name__ == '__main__':
    main()
