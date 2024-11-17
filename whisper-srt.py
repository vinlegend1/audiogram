import whisper

# Load the Whisper model
model = whisper.load_model("small")  # Or "small", "medium", "large" for more accuracy

# Transcribe the audio
result = model.transcribe("public/audio.mp3", word_timestamps=True)

# Write to .srt with word-level timing
with open("public/subtitles.srt", "w", encoding="utf-8") as file:
    index = 1
    for segment in result["segments"]:
        for word in segment["words"]:
            start_time = word["start"]
            end_time = word["end"]
            word_text = word["word"]

            # Format start and end times
            start_srt = f"{int(start_time//3600):02}:{int((start_time%3600)//60):02}:{int(start_time%60):02},{int((start_time%1)*1000):03}"
            end_srt = f"{int(end_time//3600):02}:{int((end_time%3600)//60):02}:{int(end_time%60):02},{int((end_time%1)*1000):03}"

            # Write entry
            file.write(f"{index}\n{start_srt} --> {end_srt}\n{word_text}\n\n")
            index += 1

