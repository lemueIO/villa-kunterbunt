import os
import sys
from mutagen.mp3 import MP3
from mutagen.id3 import ID3, APIC, TIT2, TPE1, TALB, error

def embed_metadata(mp3_path, img_path, title, artist, album):
    print(f"Processing {mp3_path}...")
    try:
        audio = MP3(mp3_path, ID3=ID3)
        
        # Add ID3 tag if it doesn't exist
        try:
            audio.add_tags()
        except error:
            pass
            
        audio.tags.add(TIT2(encoding=3, text=title))
        audio.tags.add(TPE1(encoding=3, text=artist))
        audio.tags.add(TALB(encoding=3, text=album))
        
        with open(img_path, 'rb') as img_file:
            audio.tags.add(
                APIC(
                    encoding=3, # 3 is for utf-8
                    mime='image/png', # or image/jpeg
                    type=3, # 3 is for the cover(front) image
                    desc=u'Cover',
                    data=img_file.read()
                )
            )
        audio.save()
        print(f"Successfully updated {mp3_path}")
    except Exception as e:
        print(f"Error updating {mp3_path}: {e}")

if __name__ == "__main__":
    base_dir = "/home/elliot/git_repos/villa-kunterbunt/core/data"
    
    # 1. Main
    embed_metadata(
        os.path.join(base_dir, "main/audio/die_villa_kunterbunt_das_hoerbuch.mp3"),
        os.path.join(base_dir, "main/images/thumbs/die_villa_kunterbunt_abook_cover_front_thumb.png"),
        "Das Hörbuch",
        "Villa Kunterbunt",
        "Das Hörbuch"
    )
    
    # 2. Cowork
    embed_metadata(
        os.path.join(base_dir, "cowork/audio/die_villa_kunterbunt_anthologie_das_hoerbuch.mp3"),
        os.path.join(base_dir, "cowork/images/thumbs/die_villa_kunterbunt_anthologie_audiobook_cover_front_thumb.png"),
        "Das Hörbuch",
        "Villa Kunterbunt",
        "Die Anthologie & Apokryphen"
    )
    
    # 3. Meta E01
    embed_metadata(
        os.path.join(base_dir, "meta/audio/das_villa_kunterbunt_kompendium_die_erweiterte_studienanalyse.mp3"),
        os.path.join(base_dir, "meta/images/thumbs/das_villa_kunterbunt_kompendium_audiobook_cover_front_thumb.png"),
        "E01: Das Kompendium",
        "Villa Kunterbunt",
        "Das Kompendium"
    )
    
    # 4. Meta E02
    embed_metadata(
        os.path.join(base_dir, "meta/audio/villa_kunterbunt_korrespondenz_epos.mp3"),
        os.path.join(base_dir, "meta/images/thumbs/das_villa_kunterbunt_kompendium_audiobook_cover_front_thumb.png"),
        "E02: Das Epos",
        "Villa Kunterbunt",
        "Das Kompendium"
    )
