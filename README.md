# Remotion Audiogram Template

This template is for creating "audiograms". In other words, video clips from podcast episodes, or any other audio. It's a popular way of sharing audio snippets on social media.

[Example video](https://twitter.com/marcusstenbeck/status/1460641903326732300)

<p align="center">
  <img src="https://github.com/marcusstenbeck/remotion-template-audiogram/raw/main/Promo.png">
</p>

Start changing things like this:

- Adjust length of video in `src/Root.tsx`
- Replacing audio, cover and subtitles in the `public/` folder
- Tweak `src/Composition.tsx`
- **Make sure to add audio, cover, and subtitles** files in the `public/` folder
- `cover.png` should be a 300x300px image

## Commands

**Install Dependencies**

```console
yarn
```

**Start Preview**

```console
yarn dev
```

**Render video**

```console
yarn remotion render
```

**Upgrade Remotion**

```console
yarn remotion upgrade
```

**Transcript file generation**
First create a python venv
```console
sudo apt install python3-venv
python3 -m venv <path to venv>
```
Install the python dependencies
```console
pip3 install -r requirements.txt
```
Run the python script that does a word-level transcription using OpenAI's Whisper model

```console
python3 whispter-srt.py
```

## Docs

Get started with Remotion by reading the [fundamentals page](https://www.remotion.dev/docs/the-fundamentals).

## Where to get a transcript (SRT file)? [Recommendations from the Original Author]

There are a few places:

- Your podcasting host might provide them for you.
- Descript makes transcription really easy.
- There are tons of other, paid solutions, like [Otter.ai](https://otter.ai), [Scriptme.io](https://scriptme.io) and [ListenRobo.com](https://listenrobo.com).
- And open-source solutions available, like [Subs AI](https://github.com/abdeladim-s/subsai)

For the purposes of this repo, make sure to export subtitles that are segmented by word (rather than sentence).