from pocketsphinx import LiveSpeech

speech = LiveSpeech(
    Verbose=False,
    sampling_rate=16000,
    buffer_size=4096,
    no_search=False,
    full_utt=False,
    hmm='model',
    lm='model.lm.bin',
    dic='model.dic')

for phrase in speech:
    print(phrase)