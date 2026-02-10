import os
from mutagen.mp3 import MP3

def check_duration(file_path):
    if not os.path.exists(file_path):
        print(f"File not found: {file_path}")
        return
    
    try:
        audio = MP3(file_path)
        duration = audio.info.length
        bitrate = audio.info.bitrate
        minutes = int(duration // 60)
        seconds = int(duration % 60)
        print(f"File: {os.path.basename(file_path)}")
        print(f"Duration: {duration:.2f} seconds ({minutes}:{seconds:02d})")
        print(f"Bitrate: {bitrate / 1000:.2f} kbps")
        
        # Check for TLEN in ID3
        if audio.tags:
            tlen = audio.tags.get("TLEN")
            if tlen:
                print(f"ID3 TLEN: {tlen.text[0]} ms")
            else:
                print("ID3 TLEN: Not found")
        
        print("-" * 20)
    except Exception as e:
        print(f"Error processing {file_path}: {e}")

if __name__ == "__main__":
    base_dir = "core/data"
    files = [
        "cowork/audio/die_villa_kunterbunt_anthologie_das_hoerbuch.mp3",
        "main/audio/die_villa_kunterbunt_das_hoerbuch.mp3",
        "meta/audio/eon_trustpilot_enthuellung_podcast.mp3",
        "meta/audio/eon_trustpilot_enthuellungsbericht_zur_bewertungsplattform.mp3"
    ]
    
    for f in files:
        check_duration(os.path.join(base_dir, f))
