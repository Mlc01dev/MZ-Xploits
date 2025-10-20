import argparse
import base64
import json
import sys

from lzstring import LZString
from pyqrcode import QRCode
from time import time
from typing import cast, Dict

KNOWN_CARDS = [
  "Famil",          "Incognita",            "ElvisTeck",
  "CBJ",            "West Macedonia",       "Cryselyn",
  "Mm manda",       "U. Lat",               "Chileno",
  "Sini",           "Natt",                 "TheGabriel",
  "FamilAlien",     "El canadista",         "Niko La bolita",
  "Cono Geography", "CountryTina",          "Andreo",
  "Mr. Mercurio",   "Mexican0tan",          "Natt incognita",
  "Cris",           "Frann",                "Kairon",
  "Juan",           "Bebe dino",            "Mr. Nico",
  "Camaroncito",    "Mal dibujado",         "Sammy",
  "NET",            "Advystiles",           "BoliviaCB",
  "Famil Maid",     "Mr. CountryVenezuela", "FamilHumano",
  "NattHumana",     "JOB",                  "MegaFamilSurprise",
  "CountryVelada",  "FamilAstronauta",      "Famil GoodBoy",
  "FamilBriel",     "3rr0r_404",            "Senegal",
  "FamilBrawl"
]


def decode_lz(input: str) -> Dict:
    payload = input.removeprefix("LZ1:").strip()
    decoded = LZString.decompressFromBase64(payload)

    return json.loads(decoded)

def encode_lz(input: Dict) -> str:
    payload = json.dumps(input).strip()
    encoded = LZString.compressToBase64(payload)

    return "LZ1:" + encoded

def create_outer(
    input: Dict,
    version: int = 1,
    created: int = None,
) -> Dict:
    if created is None:
        created = round(time() * 1000)

    payload = json.dumps(input)
    payload_bytes = payload.encode("utf-8")

    encoded_bytes = base64.b64encode(payload_bytes)
    encoded_string = encoded_bytes.decode("ascii") # base64 encoded json

    outer = dict()
    outer["v"] = version
    outer["t"] = encoded_string
    outer["created"] = created # field unused
    return outer

def create_inner(
    source: Dict = None,
    coins: int = None,
    boxes: int = None,
    last_check: int = None,
    inventory: str = None
) -> Dict:
    if source is not None:
        if source.get("t"):
            source_bytes = base64.b64decode(source.get("t"))
            source_string = source_bytes.decode("utf-8")
            source = json.loads(source_string)

    if coins is None:
        if source.get("familcoins"):
            coins = source.get("familcoins")
        else:
            coins = 0

    if boxes is None:
        if source.get("cajasAcumuladas"):
            boxes = source.get("cajasAcumuladas")
        else:
            boxes = 0

    if last_check is None:
        if source.get("ultimaCajaCheck"):
            last_check = source.get("ultimaCajaCheck")
        else:
            last_check = 0

    if inventory is not None:
        if inventory.lower() == "all":
            inv = dict()
            for card in KNOWN_CARDS:
                inv[card] = 1
        else:
            try:
                inv = json.loads(inventory)
            except ValueError:
                # fallback to empty inventory
                inv = dict()
    else:
        if source.get("inventario") is not None:
            inv = source.get("inventario")
        else:
            inv = dict()

    inner = dict()
    inner["familcoins"] = coins
    inner["cajasAcumuladas"] = boxes
    inner["ultimaCajaCheck"] = last_check
    inner["inventario"] = inv
    return inner
    
def main():
    parser = argparse.ArgumentParser(
        prog="create_sfm",
        description="Create and modify Surprise Famil .sfm payloads.",
        add_help=True,
        usage="%(prog)s [options]"
    )
    modes = ["lz1", "json", "sfm", "qrcode"]

    parser.add_argument("-i", "--input", help="input payload to modify, either LZ1 string or JSON", type=str)
    parser.add_argument("-m", "--mode", help="payload output mode", choices=modes, default="json")
    parser.add_argument("-t", "--timestamp", help="payload created date in milliseconds (field unused)", type=int)
    parser.add_argument("-o", "--output", help="output file", type=str)

    parser.add_argument("--boxes", help="accumulated amount of boxes", type=int)
    parser.add_argument("--coins", help="amount of coins", type=int)
    parser.add_argument("--last-check", help="last box checked timestamp in milliseconds", type=int)
    parser.add_argument("--inventory", help="inventory JSON contents (or all)", type=str)

    if len(sys.argv) < 2:
        parser.print_help()
        sys.exit(0)

    args = parser.parse_args()
    source: Dict = None

    if args.input:
        if args.input.startswith("LZ1:"):
            print("Decoding LZ1 input...")
            source = decode_lz(args.input)
        else:
            try:
                source = json.loads(args.input)
            except ValueError:
                print("Failed to parse JSON or LZ1 payload source input.")
                sys.exit(1)

    print("Creating inner payload...")
    inner = create_inner(source, args.coins, args.boxes, args.last_check, args.inventory)

    print("Creating outer payload...")
    outer = create_outer(inner, 1, args.timestamp)
 
    if args.mode == "lz1":
        lz = encode_lz(outer)

        if args.output is not None:
            with open(args.output, "w+t") as file:
                file.write(lz)
                file.close()
                print(f"LZ1 string written to {args.output}")
        else:
            print("\n\nSFM payload:\n" + lz + "\n\n")
    elif args.mode == "json" or args.mode == "sfm":
        # treat sfm as json alias
        data = json.dumps(outer)

        if args.output is not None:
            with open(args.output, "w+t") as file:
                file.write(data)
                file.close()
                print(f"SFM payload written to {args.output}")
        else:
            print("\n\nSFM Payload:\n" + data + "\n\n")
    elif args.mode == "qrcode":
        lz = encode_lz(outer)
        qr = QRCode(lz, "M")

        if args.output is not None:
            qr.png(args.output, 5)
            print(f"QR code payload written to {args.output}")
        else:
            print(qr.terminal())
    else:
        print("Invalid mode selected.")
        sys.exit(1)

    print("== MZ-Xploits by PwLDev and Mlcdev01 ==")
    sys.exit(0)

if __name__ == "__main__":
    main()