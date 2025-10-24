<div align="center">
<img src="../.github/icons/madsulu_go.png" width="120">
<br>
<h1>MadSulu Go</h1>
</div>

## About

**MadSulu Go** is a niche video streaming app targeting Latin America developed by JoshuaPRO5 and Mm Manda, distributed by MadZalMedia Incorporated.
Most of its content is countryball-related, however, you can also find distinct web series inside the content catalogue.
The app formerly known as MadZal Flux and MSP (Más Series y Pelis).

This app is available in [Play Store](https://play.google.com/store/apps/details?id=flux.mandajoshua) and [Itch.io](https://mandajoshua.itch.io/madsulugo) exclusively for Android devices. Further information about the app can be found in this [MadzalMedia article](https://madzalmediaincorporated.fandom.com/es/wiki/MadSulu_GO).

## Xploits

**MadSulu Go** used to be split into two separate apps: MadZal Flux and MSP (Más Series y Pelis), later these apps would combine into a single one and migrated to an HTML5 interface.

Me (PwLDev) and Mlcdev01 have been finding multiple vulnerabilities since they left the native code.
As of now, there are several known Xploits, most of them are still active.

**Known Xploits:**

- [Web24](https://youtube.com/shorts/sW432kAt7dk) [PATCHED]
- [Bad Notification](xploits/bad_notification.md)
- [MGH 1.0](xploits/MGH_1.0.md)
- MGH 2.0

Further information about each Xploit can be found in their respective documentation.

## Container

The **.msg** container, similar to other MadZalMedia apps is essentially a JSON container file which contains minimized account sharing data.
It is composed by two fundamental parts, the **outer payload** and **inner payload**, both are JSON formatted and one contains each other.

Key, type and reverse engineered descriptions are shown for each component in the following tables.

### Outer Payload

Format: **JSON**

| Key |  Type  | Description                  |
| :-: | :----: | :--------------------------- |
|  v  |  int   | Scheme version (1)           |
|  t  | string | Base64 encoded inner payload |

### Inner Payload

Format: **JSON**, Base64 encoded in the outer payload.

|          Key           | Type  | Description                       |
| :--------------------: | :---: | :-------------------------------- |
| madsulu_recientes_idx0 | array | Array of recently watched content |
|    madsulu_profiles    | array | Array of existing profile objects |

### Profile

Format: **JSON**
| Key | Type | Description |
| :-: | :----: | :--------------------------- |
| name | string | Profile name |
| kids | boolean | Wether the profile is for kids |
| avatar | string | Static avatar image URL |

### Content

Format: **JSON**
| Key | Type | Description |
| :-: | :----: | :--------------------------- |
| ref | string | Internal content ID (?) |
| nombre | string | Content title |
| img | string | Static image URL |
| ts | int | Last watched timestamp in ms (optional) |

## Tool

There is a work-in-progress Python 3 tool `create_msg.py` to create loadable backups for **MadSulu Go**.

## Credits

- Documentation and tool written by [PwLDev](https://github.com/PwLDev)
- Reverse engineered with help of [Mlcdev01](https://github.com/Mlc01dev)
