import os

from pydub import AudioSegment

def convert_to_wav(filepath, wav_dir='./data/interim/wav/'):
    if not os.path.exists(wav_dir):
        os.makedirs(wav_dir)
    file_basename, ext = os.path.basename(filepath).rsplit('.')
    audio = AudioSegment.from_file(filepath, ext)

    wav_filepath = os,path,join(wav_dir, file_basename + '.wav')
    audio.export(wav_filepath, format="wav")
    return wav_filepath

if __name__ == "__main__":
    convert_to_wav('./data/raw/mp3/aps-smp.mp3')