# The Abuse Project Audio Dataset (TAPAD)

<p align="center">
<b>World's largest profanity audio dataset<br><br>
Dataset consists of ‭<a href="#checkfiles">26,365</a> audio files<br>
  Click <a href="https://github.com/0x48piraj/tapad/wiki">here</a> for documentation<br><br>
See <a href="https://github.com/0x48piraj/theabuseproject">The Abuse Project</a></b>
</p>

**TAPAD (∿)** is an open dataset, meaning it will grow over time as more data is contributed. In order to enable reproducibility and accurate citation the dataset is versioned using git tags.

## Current Status & ID3

| Category           | Const           |
|--------------------|-----------------|
| Total files        | `26,365`        |
| Dataset updated    | `July 30, 2019` |
| Language classes   | `75`            |
| File Type          | MP3             |
| Mime Type          | audio/mpeg      |
| Mpeg Audio Version | 2               |
| Audio Layer        | 3               |
| Audio Bitrate      | 32 kbps         |
| Sample Rate        | 24000           |
| Channel Mode       | Single Channel  |
| Ms Stereo          | Off             |
| Intensity Stereo   | Off             |
| Codec Type         | audio           |
| Codec Time Base    | 1/24000         |
| Codec Tag          | 0x0000          |
| Sample Fmt         | fltp            |
| Sample Rate        | 24000           |
| Channels           | 1               |
| Channel Layout     | mono            |
| Bits Per Sample    | 0               |
| R Frame Rate       | 0/0             |
| Avg Frame Rate     | 0/0             |
| Time Base          | 1/14112000      |

Languages are required to be 2 letters, normally their 2 letter ISO code, **see: [ISO_639-1](https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes)**

## Scripts & Utilities

| Filename           | Location           | Description                                   | Type               |
|--------------------|--------------------|-----------------------------------------------|--------------------|
| `record.py`        | `acquire\custom`   | Records audio in WAV format (default: 3 sec)  | Helper script      |
| `wingen.py`        | `acquire\generate` | TTS conversion using `SAPI.SpVoice`           | Helper script      |
| `gTTSgen.py`       | `acquire\generate` | TTS conversion using **gTTS** & `abuse 0.1.1` | Helper script      |
| `gspectogram.py`   | `utils`            | Generates spectrogram of a wav file           | Utility tool       |

## Structure

```
.
├───af
├───ar
├───bn
├───bs
├───ca
├───cs
├───cy
├───da
├───de
├───el
├───en
│   ├───1 (340 wav files)
│   └───2
├───en-au
├───en-ca
├───en-gb
├───en-gh
├───en-ie
├───en-in
├───en-ng
├───en-nz
├───en-ph
├───en-tz
├───en-uk
├───en-us
├───en-za
├───eo
├───es
├───es-es
├───es-us
├───et
├───fi
├───fr
├───fr-ca
├───fr-fr
├───hi
├───hr
├───hu
├───hy
├───id
├───is
├───it
├───ja
├───jw
├───km
├───ko
├───la
├───lv
├───mk
├───ml
├───mr
├───my
├───ne
├───nl
├───no
├───pl
├───pt
├───pt-br
├───pt-pt
├───ro
├───ru
├───si
├───sk
├───sq
├───sr
├───su
├───sv
├───sw
├───ta
├───te
├───th
├───tl
├───tr
├───uk
├───vi
├───zh-cn
└───zh-tw
```
Most of these audio classes have 347 MP3 files of **~5.783 minutes** each. MP3 **had** a lot of patent issues but according to [Wikipedia](https://en.wikipedia.org/wiki/MP3), _"If the longest-running patent mentioned in the aforementioned references is taken as a measure, then the MP3 technology became patent-free in the United States on **16 April 2017** when U.S. Patent 6,009,399, held by and administered by Technicolor, expired"_.

#### Checking files <a name="checkfiles"></a>

```bash
find audio/ -type f | wc -l
```

## Made with TAPAD

Did you use or saw TAPAD in a paper, project or app? Add it here!

* [The Abuse Project](https://github.com/0x48piraj/theabuseproject)
* (...)

## Maintainers

The dataset is maintained by :

- Piyush Raj ([@0x48piraj](https://github.com/0x48piraj))
- Manav Kapil ([@manav1999](https://github.com/manav1999))

## LICENSE

<a rel="license" href="http://creativecommons.org/licenses/by-nc-sa/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by-nc-sa/4.0/88x31.png" /></a><br />This work is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by-nc-sa/4.0/">Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License</a>.

To view a copy of this license, visit **[NC-SA 4.0](LICENSE.md)** or send a letter to Creative Commons, PO Box 1866, Mountain View, CA 94042, USA.