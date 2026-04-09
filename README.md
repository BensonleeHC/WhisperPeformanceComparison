Repo for record only. 04/10 2026
---
Computer: i7-11700K(no OC) + 3060ti + 32G(2400MHz)

Model : OpenAI-Whisper (https://github.com/openai/whisper)

Sub-Model : Turbo

Audio : Sample.mp3

Decoder : librosa / soundfile for reduce size after pack to executable.

Material : 3 minutes video download from Youtube

Time:
---
"Turbo" result : CPU 5m / 3060ti 21s . 93% reduce

"Tiny" result : CPU 13s / 3060ti 10s . odd.......

Accurcy:
---
No noticable error with Turbo model

Accuracy reduce when change model to tiny, about 10% accurcy decrease.

switch "librosa" to build-in "soundfile" decoder with "tiny", drop accurcy to non-sense sentence.


Pyinstaller size:
---
with only --onefile parameter, almost reach 200M on "tiny" model

can analyze size using --onedir, torch_cpu.dll almost 100M (kinda make sense since OpenAI-Whisper runs on tensorflow)

advance reduce size with UPX, final size about 25M. (acceptable)

can refer .spec file for excluding non-neccessary module and include most important whisper/assets for AI model.

cost about 5% more time with executable than python file.
