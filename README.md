# Partial Report Change Detection Task (PERL - Oxford)

## Version 1.0 (11/02/2023)

Task made by Michael Colwell (michael.colwell@psych.ox.ac.uk), with suggestions and improvements by Prof Catherine Harmer (catherine.harmer@psych.ox.ac.uk).

<p align="center">
<img src="https://media1.giphy.com/media/v1.Y2lkPTc5MGI3NjExZWM0MTI0YjE0MmYwNWNiM2I0YTA1ZmRlMjk5MjlhMGM5NTBkNTg1ZiZlcD12MV9pbnRlcm5hbF9naWZzX2dpZklkJmN0PWc/juXBiZHQOUFpK2tEah/giphy.gif" width="400" height="340" />
</p>

## License
This task and pre-processing scripts are open-source and free for all to use, including students and researchers. You do not need 
additional permission from the author (M Colwell). However, we ask that if you publish data using this task that you cite 
the materials/original publications. Please also consult the author if you plan on making substantial alterations to the task shell.

Materials publication: TBC

Clinical study record: https://clinicaltrials.gov/ct2/show/NCT05849675

Research publication: TBC (PEACE Study - publication TBC)

Testing & Debugging by: PERL Lab Oxford

## Purpose of the task
This is an adaption of a classic task of visuo-spatial working memory, also known as a partial report change detection task. This task 
was created specifically to probe both location in space and colour (in a colour-blind friendly manner). Colours in the task
use a palette known as 'Color Universal Design (CUD)' created by Masataka Okabe and Kei Ito to allow colour discriminations across all
colour-blind populations. 

Color Universal Design (CUD) - How to make figures and presentations that are friendly to Colorblind people. Masataka Okabe and Kei Ito.
http://jfly.iam.u-tokyo.ac.jp/color/

This task is intended to be used in healthy individuals to probe visuo-spatial working memory across a parametric distribution. Thus, it would
provide an adequete measurement to investigate the cognitive effects of a psychopharmacologically active agent. The task is currently in use
in the PEACE study in Oxford (An fMRI investigation of the effects of selective histamine-3 receptor antagonism on cognitive and emotional processing in healthy individuals).

## Task specifications

The initial stimulus presentation lasts 300ms, followed by a short pseudo-random ISI (0.7-1.1s), then the set will reappear on the screen with
the colour of one stimulus having changed. Participants then must click on the changed square using the mouse, followed by another pseudo-random 
ISI (0.7-1.1s). Following the ISI, a colour wheel of eight colours will be presented; using the mouse participants must identify the original colour of the
changed (target) stimulus.

There are four main blocks throughout the experiment, with each block having a set number of stimuli per trial. The first block consists of three stimuli, the second
four, the third five and the final six. Participants undertake a tutorial/practice trial before taking part in the main task.

Stimuli will only appear onscreen in a 1:1 square, so that only central vision is required throughout. All stimuli are at least '0.1x0.1' units apart from each other,
with a pseudo-random location on an even grid pattern (0,0.1,0.2,0.3). No stimuli appear more than 0.3 units away from center-screen. No more than two stimuli appear
in each quadrant of the X,Y axes at any stage. Every stimulus in a set will always have a unique colour. Some stimulus colour changes have high contrast (e.g. yellow -> black),
while others are more subtle (e.g. blue -> sky blue). 

## Instructions

1. Download Psychopy (version v2021.2.3 and above) - https://www.psychopy.org/download.html
2. Once installed, unzip the contents of this folder to a location on your computer
3. Open the 'Colour Change Detection Task - Oxford PERL' folder and double click on 'Colour Change Detection Task Oxford PERL'.psyexp
5. Click 'run' experiment and enter sessional details (e.g., participant ID).
6. Press run and follow onscreen instructions
7. Once the experiment has ended, you will find your test data in the 'data' folder.

## Individual setup

Depending on your monitor, you will want to change the monitor settings in 'psychopy'. The default monitor is optimised for a small laptop monitor. 
Ideally, you want to change the monitor specifications (e.g. screen width) so that the grey centred box is only occupying 50% of vertical pixels. The purpose of this
is that a smaller box means all stimuli appear in central, not peripheral, vision.
