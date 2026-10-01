import urllib.request
import urllib.parse
import json
import time
import os

os.makedirs('images', exist_ok=True)

# List of exact Wikimedia Commons file titles for real Madeira photos
FILES = {
    "slide02_hero.jpg": "File:View from Miradouro do Pico do Arieiro - Madeira 05.jpg",
    "slide08_funchal.jpg": "File:Funchal (Madeira, Portugal), Porto do Funchal -- 2025 -- 1291.jpg",
    "slide09_quinta.jpg": "File:Quinta Jardins do Lago, Funchal, Madeira - 2013-05-26 - DSC02716.jpg",
    "slide10_espetada.jpg": "File:Zum Grill umgebautes Fass mit Espetada-Spießen.jpg",
    "slide11_saolourenco.jpg": "File:Ponta de São Lourenço, Madeira, Portugal, 2019-05-28, DD 31.jpg",
    "slide12_prainha.jpg": "File:Prainha Beach (42402305755).jpg",
    "slide13_machico.jpg": "File:Madeira - Machico - view across the bay on a stormy day (33192095770).jpg",
    "slide14_pr1.jpg": "File:Górski szlak pieszy PR1 z Pico Arreiro do Pico Ruivo - Vereda do Areeiro - Madeira, Portugalia, sierpień 2022.jpg",
    "slide16_quintafurao.jpg": "File:Porto Santo in distance, from Miradouro da Quinta do Furão (in Santana).jpg",
    "slide17_caldeirao.jpg": "File:LCV - Levada channel and forest path on Levada do Caldeirão Verde, Madeira, 2012.jpg",
    "slide18_santana.jpg": "File:Santana (Madeira, Portugal), Casas Típicas de Santana -- 2025 -- 1378.jpg",
    "slide19_saovicente.jpg": "File:Costa de San Vicente, Madeira, Portugal, 2019-05-30, DD 66.jpg",
    "slide20_fanal.jpg": "File:Foggy Fanal forest in Seixal, Porto Moniz, Madeira, 2023 May.jpg",
    "slide21_portomoniz.jpg": "File:Piscinas volcánicas naturales, Porto Moniz, Madeira, Portugal, 2019-05-30, DD 70.jpg",
    "slide22_seixal.jpg": "File:View of Seixal, Madeira, from mountain road.jpg",
    "slide23_25fontes.jpg": "File:Madeira-Rabacal-Levada das 25 Fontes (PR6)-bridge-02ASD.jpg",
    "slide24_cabogirao.jpg": "File:View from Miradouro do Cabo Girão 02.jpg",
    "slide25_funchal_sea.jpg": "File:Funchal (Madeira, Portugal), Porto do Funchal -- 2025 -- 1308.jpg",
    "slide26_monte.jpg": "File:Funchal Carros do Monte 2016 3.jpg",
    "slide27_dining.jpg": "File:Espada with Banana Madeira.jpg",
    "slide28_airport.jpg": "File:Madeira Airport Runway Crop.jpg"
}

headers = {'User-Agent': 'MadeiraExpeditionDeck/2.0 (research and educational presentation)'}

for filename, wiki_title in FILES.items():
    dest_path = os.path.join('images', filename)
    if os.path.exists(dest_path) and os.path.getsize(dest_path) > 30000:
        print(f"Skipping {filename} (already exists, {os.path.getsize(dest_path):,} bytes)")
        continue

    print(f"Fetching URL for {filename} ({wiki_title})...")
    api_url = f"https://commons.wikimedia.org/w/api.php?action=query&titles={urllib.parse.quote(wiki_title)}&prop=imageinfo&iiprop=url|thumburl&iiurlwidth=1280&format=json"
    req = urllib.request.Request(api_url, headers=headers)
    
    try:
        with urllib.request.urlopen(req) as resp:
            data = json.loads(resp.read().decode())
            pages = data.get('query', {}).get('pages', {})
            img_url = None
            for pid, pdata in pages.items():
                ii = pdata.get('imageinfo', [{}])[0]
                img_url = ii.get('thumburl') or ii.get('url')
                break
                
        if not img_url:
            print(f"  FAILED to find image URL for {wiki_title}")
            continue
            
        print(f"  Downloading from: {img_url[:70]}...")
        img_req = urllib.request.Request(img_url, headers=headers)
        with urllib.request.urlopen(img_req) as resp, open(dest_path, 'wb') as out_f:
            out_f.write(resp.read())
            
        sz = os.path.getsize(dest_path)
        print(f"  ✓ Saved {filename} ({sz:,} bytes)")
    except Exception as e:
        print(f"  ERROR for {filename}: {e}")
        
    time.sleep(1.2)  # Respectful pause to avoid Wikimedia rate limits

print("\n--- Download summary ---")
all_ok = True
for filename in FILES:
    p = os.path.join('images', filename)
    if os.path.exists(p) and os.path.getsize(p) > 30000:
        print(f"  {filename}: {os.path.getsize(p):,} bytes")
    else:
        print(f"  {filename}: MISSING or small")
        all_ok = False

if all_ok:
    print("\nAll 21 authentic Madeira images successfully downloaded and verified!")
