<div align="center">
<img src="../.github/icons/surprise_famil.png" width="120">
<br>
<h1>Surprise Famil</h1>
</div>

## About

**Surprise Famil** is a card game produced by Manda-Joshua Associations in collaboration with content creator [FamilOficial](https://www.youtube.com/channel/UCnQr4y7llL-A5Uxc3ZuBz9g).
This game was released the July 21st, 2025.

> _Collect cards, sell, buy and discover all characters!_

This game is available for Android in the [Play Store](https://play.google.com/store/apps/details?id=com.famil.mandajoshua) and [Itch.io](https://mandajoshua.itch.io/lasflipantessorpresasfamiliares).
Further info about the gameplay mechanics can be found in this [MadzalMedia article](https://madzalmediaincorporated.fandom.com/es/wiki/Surprise_Famil).

## Xploit

In **Surprise Famil**, there is a built-in feature for security backups, it generates a QR code with encoded LZ1 payload for your progress, alternatively, it can be saved as a **.sfm** file.

It is known that apps from MadzalMedia lack of a proper backend server, using [Catbox](https://catbox.moe) as a CDN and fully relying on the `localStorage` API for local progress saving.

Since there is no server or client side check for improper or impossible saves, it allows players to create modified savefiles without any restrictions (besides the risk of [getting banned](https://github.com/Mlc01dev/MZ-Xploits/tree/main?tab=readme-ov-file#disclaimer) if promoted the practice).

> _Yes, I got banned after open sourcing this._ ~ PwLDev

## Container

The **.sfm** container, similar to other MadZalMedia apps is essentially just a JSON container file which contains minimized save data.
The data itself is composed by two fundamental parts, the **outer payload** and **inner payload**, both JSON and one contains each other.

The key, type and reverse engineered descriptions are shown for each part in the following tables.

### Outer Payload

Format: **JSON**

|   Key   |  Type  | Description                   |
| :-----: | :----: | :---------------------------- |
|    v    |  int   | Scheme version (1)            |
|    t    | string | Base64 encoded inner payload  |
| created |  int   | Unix timestamp in ms (unused) |

### Inner Payload

Format: **JSON**, Base64 encoded in the outer payload.

|       Key       |  Type  | Description                            |
| :-------------: | :----: | :------------------------------------- |
|   familcoins    |  int   | Amount of in-game coins                |
| cajasAcumuladas |  int   | Amount of accumulated boxes            |
| ultimaCajaCheck |  int   | Last box check timestamp in ms         |
|   inventario    | object | Inventory object, keys can be nullable |

### Inventory

This is a key-value object, where the value is the amount of cards of that character.

Format: **JSON object**

<details>
<summary>Known Cards</summary>

Famil, Incognita, ElvisTeck, CBJ, West Macedonia, Cryselyn, Mm manda, U. Lat, Chileno, Sini, Natt, TheGabriel, FamilAlien, El canadista, Niko La bolita, Cono Geography, CountryTina, Andreo, Mr. Mercurio, Mexican0tan, Natt incognita, Cris, Frann, Kairon, Juan, Bebe dino, Mr. Nico, Camaroncito, Mal dibujado, Sammy, NET, Advystiles, BoliviaCB, Famil Maid, Mr. CountryVenezuela, FamilHumano, NattHumana, JOB, MegaFamilSurprise, CountryVelada, FamilAstronauta, Famil GoodBoy, FamilBriel, 3rr0r_404, Senegal, FamilBrawl

</details>

## Tool

The `create_sfm.py` Python 3 CLI tool allows to create and modify **.sfm** savefiles and then output them as JSON (in .sfm container), LZ1 strings or QR Code.

First make sure you are inside the `surprise_famil` directory.

```sh
cd surprise_famil
```

This tool requires Python 3 along with some required dependencies, you can install them using the following command.

```sh
pip3 install -r requirements.txt
```

After installing the dependencies, run this command to get help onto how to use the tool.

```sh
python3 create_sfm.py -h
```

## Credits

- Documentation and tool written by [PwLDev](https://github.com/PwLDev)
- Reverse engineered with help of [Mlcdev01](https://github.com/Mlc01dev)
