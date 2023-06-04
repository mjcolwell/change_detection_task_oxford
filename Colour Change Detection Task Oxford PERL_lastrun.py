#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2021.2.3),
    on June 04, 2023, at 16:42
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

from __future__ import absolute_import, division

from psychopy import locale_setup
from psychopy import prefs
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os  # handy system and path functions
import sys  # to get file system encoding

from psychopy.hardware import keyboard

win = visual.Window(viewScale=[100,100])


# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
psychopyVersion = '2021.2.3'
expName = 'Colour Change Detection Task Oxford PERL'  # from the Builder filename that created this script
expInfo = {'participant': '', 'Study_name': '', 'PREPOST': ''}
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='C:\\Users\\micha\\Desktop\\Colour_Change_Detection_Task_Oxford\\Colour Change Detection Task Oxford PERL_lastrun.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run after the window creation

# Setup the Window
win = visual.Window(
    size=[2560, 1440], fullscr=False, screen=0, 
    winType='pyglet', allowGUI=True, allowStencil=False,
    monitor='testMonitor', color=[-0.4667, -0.4667, -0.4510], colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='cm')
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# Setup eyetracking
ioDevice = ioConfig = ioSession = ioServer = eyetracker = None

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard()

# Initialize components for Routine "Startup_code"
Startup_codeClock = core.Clock()
##Defining colours to call throughout experiment##
##Colours are based on the Colour Universal Design
##by asataka Okabe and Kei Ito, allowing the task
##to be accessible to individuals with colourblindness.


CUDSkyblue = [-0.3255, 0.4118, 0.8275]
CUDbluegreen = [-1.0000, 0.2392, -0.0980]
CUDyellow = [0.8824, 0.7882, -0.4824]
CUDredpurple = [0.6000, -0.0510, 0.3098]
CUDblack = [-1.0000, -1.0000, -1.0000]
CUDindigo = [-0.4118, -1.0000, 0.0196]
CUDwhite = [1,1,1]
CUDvermilion = [0.6706, -0.2627, -1.0000]

#CUDblue = [-1.0000, -0.1059, 0.3961]
#CUDorange = [0.8039, 0.2471,-1.0000]

##Set mouse off initially
win.setMouseVisible(False)

#Create a ticker that adds up block progress
BlockNo = 1
###Define 8 colour wedges for choice wheel, divided by 45 degree segments

wedgeWhite = visual.Pie(win, fillColor = CUDwhite,start = 0,end = 41, size=(0.65,0.65),interpolate=True,lineWidth=3, name = 'wedgeWhite')

wedgeYellow = visual.Pie(win, fillColor = CUDyellow,start = 45,end = 86, size=(0.65,0.65),interpolate=True,lineWidth=3, name = 'wedgeYellow')

wedgeVermilion = visual.Pie(win, fillColor = CUDvermilion,start = 90,end = 131, size=(0.65,0.65),interpolate=True, lineWidth=3, name = 'wedgeVermilion')

wedgeRedPurple = visual.Pie(win, fillColor = CUDredpurple,start = 135,end = 176, size=(0.65,0.65),interpolate=True, lineWidth=3, name = 'wedgeRedPurple')

wedgeBlack = visual.Pie(win,fillColor = CUDblack,start = 180,end = 221, size=(0.65,0.65),interpolate=True, lineWidth=3, name = 'wedgeBlack')

wedgeIndigo = visual.Pie(win, fillColor = CUDindigo ,start = 225,end = 266, size=(0.65,0.65),interpolate=True, lineWidth=3, name = 'wedgeIndigo')

wedgeSkyBlue = visual.Pie(win, fillColor = CUDSkyblue,start = 270,end = 311, size=(0.65,0.65),interpolate=True, lineWidth=3, name = 'wedgeSkyBlue')

wedgeBlueGreen = visual.Pie(win, fillColor = CUDbluegreen,start = 315,end = 356, size=(0.65,0.65),interpolate=True, lineWidth=3, name = 'wedgeBlueGreen')

###Overlay black circle

GreyCircle = visual.Circle(win, colorSpace='rgb255', fillColor = 'grey', size=(0.3,0.3))

GreyCircle2 = visual.Circle(win, colorSpace='rgb255', fillColor = 'grey', size=(0.3,0.3))

####Draw Guide Squares

GuideYellow = visual.Rect(win, fillColor = CUDyellow, size=(0.1,0.1))

GuideWhite = visual.Rect(win, fillColor = CUDwhite, size=(0.1,0.1))

GuideVermilion = visual.Rect(win, fillColor = CUDvermilion, size=(0.1,0.1))

GuideRedPurple = visual.Rect(win, fillColor = CUDredpurple, size=(0.1,0.1))

GuideBlack = visual.Rect(win, fillColor = CUDblack, size=(0.1,0.1))

GuideIndigo = visual.Rect(win, fillColor = CUDindigo, size=(0.1,0.1))

GuideSkyBlue = visual.Rect(win, fillColor = CUDSkyblue, size=(0.1,0.1))

GuideBlueGreen = visual.Rect(win, fillColor = CUDbluegreen, size=(0.1,0.1))

grayBox = visual.rect.Rect(win, width=0.8, height=0.8, units='', lineWidth=0, lineColor=None, lineColorSpace=None, fillColor='grey', fillColorSpace=None, pos=(0, 0))

# Initialize components for Routine "Startup_screen"
Startup_screenClock = core.Clock()
NumberOBlocks_4 = visual.TextStim(win=win, name='NumberOBlocks_4',
    text='',
    font='Open Sans',
    pos=(0.00, 0.01), height=0.04, wrapWidth=0.75, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
ContinueButtonText_2 = visual.TextStim(win=win, name='ContinueButtonText_2',
    text='Click here to continue',
    font='Open Sans',
    pos=(0, -0.3), height=0.03, wrapWidth=0.75, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
ContinueButton_2 = visual.Rect(
    win=win, name='ContinueButton_2',
    width=(0.37, 0.09)[0], height=(0.37, 0.09)[1],
    ori=0.0, pos=(0, -0.3),
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor=None,
    opacity=None, depth=-2.0, interpolate=True)
mouse_4 = event.Mouse(win=win)
x, y = [None, None]
mouse_4.mouseClock = core.Clock()

# Initialize components for Routine "Instructions_Begin"
Instructions_BeginClock = core.Clock()
NumberOBlocks_5 = visual.TextStim(win=win, name='NumberOBlocks_5',
    text='',
    font='Open Sans',
    pos=(0.00, 0.01), height=0.04, wrapWidth=0.75, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
ContinueButtonText_3 = visual.TextStim(win=win, name='ContinueButtonText_3',
    text='Click here to continue',
    font='Open Sans',
    pos=(0, -0.3), height=0.03, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
ContinueButton_3 = visual.Rect(
    win=win, name='ContinueButton_3',
    width=(0.37, 0.09)[0], height=(0.37, 0.09)[1],
    ori=0.0, pos=(0, -0.3),
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor=None,
    opacity=None, depth=-2.0, interpolate=True)
mouse_5 = event.Mouse(win=win)
x, y = [None, None]
mouse_5.mouseClock = core.Clock()

# Initialize components for Routine "Instructions_Begin_2"
Instructions_Begin_2Clock = core.Clock()
NumberOBlocks_6 = visual.TextStim(win=win, name='NumberOBlocks_6',
    text='',
    font='Open Sans',
    pos=(0.00, 0.01), height=0.04, wrapWidth=0.75, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
ContinueButtonText_4 = visual.TextStim(win=win, name='ContinueButtonText_4',
    text='Click to start the tutorial',
    font='Open Sans',
    pos=(0, -0.3), height=0.03, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
ContinueButton_4 = visual.Rect(
    win=win, name='ContinueButton_4',
    width=(0.37, 0.09)[0], height=(0.37, 0.09)[1],
    ori=0.0, pos=(0, -0.3),
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor=None,
    opacity=None, depth=-2.0, interpolate=True)
mouse_6 = event.Mouse(win=win)
x, y = [None, None]
mouse_6.mouseClock = core.Clock()

# Initialize components for Routine "ISI_tutorial"
ISI_tutorialClock = core.Clock()
ISI1_cross_2 = visual.TextStim(win=win, name='ISI1_cross_2',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "Stimulus_disp_tutorial"
Stimulus_disp_tutorialClock = core.Clock()
Fixation_Point_3 = visual.TextStim(win=win, name='Fixation_Point_3',
    text='·',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
Target_3 = visual.Rect(
    win=win, name='Target_3',
    width=(0.125, 0.125)[0], height=(0.125, 0.125)[1],
    ori=0.0, pos=[0,0],
    lineWidth=1.0,     colorSpace='rgb',  lineColor=None, fillColor='white',
    opacity=None, depth=-1.0, interpolate=True)
Flan1_3 = visual.Rect(
    win=win, name='Flan1_3',
    width=(0.125, 0.125)[0], height=(0.125, 0.125)[1],
    ori=0.0, pos=[0,0],
    lineWidth=1.0,     colorSpace='rgb',  lineColor=None, fillColor='white',
    opacity=None, depth=-2.0, interpolate=True)
Flan2_3 = visual.Rect(
    win=win, name='Flan2_3',
    width=(0.125, 0.125)[0], height=(0.125, 0.125)[1],
    ori=0.0, pos=[0,0],
    lineWidth=1.0,     colorSpace='rgb',  lineColor=None, fillColor='white',
    opacity=None, depth=-3.0, interpolate=True)
Flan3_3 = visual.Rect(
    win=win, name='Flan3_3',
    width=(0.125, 0.125)[0], height=(0.125, 0.125)[1],
    ori=0.0, pos=[0,0],
    lineWidth=1.0,     colorSpace='rgb',  lineColor=None, fillColor=None,
    opacity=None, depth=-4.0, interpolate=True)
Flan4_3 = visual.Rect(
    win=win, name='Flan4_3',
    width=(0.125, 0.125)[0], height=(0.125, 0.125)[1],
    ori=0.0, pos=[0,0],
    lineWidth=1.0,     colorSpace='rgb',  lineColor=None, fillColor=None,
    opacity=None, depth=-5.0, interpolate=True)
Flan5_3 = visual.Rect(
    win=win, name='Flan5_3',
    width=(0.125, 0.125)[0], height=(0.125, 0.125)[1],
    ori=0.0, pos=[0,0],
    lineWidth=1.0,     colorSpace='rgb',  lineColor=None, fillColor=None,
    opacity=None, depth=-6.0, interpolate=True)

# Initialize components for Routine "ISI_tutorial"
ISI_tutorialClock = core.Clock()
ISI1_cross_2 = visual.TextStim(win=win, name='ISI1_cross_2',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "Loc_choice_tut"
Loc_choice_tutClock = core.Clock()
mouse_8 = event.Mouse(win=win)
x, y = [None, None]
mouse_8.mouseClock = core.Clock()
Fixation_Point_5 = visual.TextStim(win=win, name='Fixation_Point_5',
    text='·',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
Target_5 = visual.Rect(
    win=win, name='Target_5',
    width=(0.125, 0.125)[0], height=(0.125, 0.125)[1],
    ori=0.0, pos=[0,0],
    lineWidth=3.5,     colorSpace='rgb',  lineColor=None, fillColor='white',
    opacity=None, depth=-3.0, interpolate=True)
Flan1_5 = visual.Rect(
    win=win, name='Flan1_5',
    width=(0.125, 0.125)[0], height=(0.125, 0.125)[1],
    ori=0.0, pos=[0,0],
    lineWidth=3.5,     colorSpace='rgb',  lineColor=None, fillColor='white',
    opacity=None, depth=-4.0, interpolate=True)
Flan2_5 = visual.Rect(
    win=win, name='Flan2_5',
    width=(0.125, 0.125)[0], height=(0.125, 0.125)[1],
    ori=0.0, pos=[0,0],
    lineWidth=3.5,     colorSpace='rgb',  lineColor=None, fillColor='white',
    opacity=None, depth=-5.0, interpolate=True)
Flan3_5 = visual.Rect(
    win=win, name='Flan3_5',
    width=(0.125, 0.125)[0], height=(0.125, 0.125)[1],
    ori=0.0, pos=[0,0],
    lineWidth=3.5,     colorSpace='rgb',  lineColor=None, fillColor=None,
    opacity=None, depth=-6.0, interpolate=True)
Flan4_5 = visual.Rect(
    win=win, name='Flan4_5',
    width=(0.125, 0.125)[0], height=(0.125, 0.125)[1],
    ori=0.0, pos=[0,0],
    lineWidth=3.5,     colorSpace='rgb',  lineColor=None, fillColor=None,
    opacity=None, depth=-7.0, interpolate=True)
Flan5_5 = visual.Rect(
    win=win, name='Flan5_5',
    width=(0.125, 0.125)[0], height=(0.125, 0.125)[1],
    ori=0.0, pos=[0,0],
    lineWidth=3.5,     colorSpace='rgb',  lineColor=None, fillColor=None,
    opacity=None, depth=-8.0, interpolate=True)
ArrowHead = visual.ShapeStim(
    win=win, name='ArrowHead',
    size=(0.05, 0.05), vertices='triangle',
    ori=270.0, pos=(0.19, 0.1),
    lineWidth=1.0,     colorSpace='rgb',  lineColor=None, fillColor='green',
    opacity=None, depth=-9.0, interpolate=True)
ArrowBar = visual.Rect(
    win=win, name='ArrowBar',
    width=(0.07, 0.008)[0], height=(0.07, 0.008)[1],
    ori=0.0, pos=(0.24, 0.1),
    lineWidth=2.0,     colorSpace='rgb',  lineColor=None, fillColor='green',
    opacity=None, depth=-10.0, interpolate=True)
InstruText2 = visual.TextStim(win=win, name='InstruText2',
    text='Select the square which changed colour.',
    font='Open Sans',
    pos=(0, 0.3), height=0.03, wrapWidth=0.75, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-11.0);

# Initialize components for Routine "ISI_tutorial"
ISI_tutorialClock = core.Clock()
ISI1_cross_2 = visual.TextStim(win=win, name='ISI1_cross_2',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "Choice_tutorial"
Choice_tutorialClock = core.Clock()
mouse_9 = event.Mouse(win=win)
x, y = [None, None]
mouse_9.mouseClock = core.Clock()
ArrowHead2 = visual.ShapeStim(
    win=win, name='ArrowHead2',
    size=(0.05, 0.05), vertices='triangle',
    ori=90.0, pos=(0.165, -0.33),
    lineWidth=1.0,     colorSpace='rgb',  lineColor=None, fillColor='green',
    opacity=None, depth=-2.0, interpolate=True)
ArrowBar2 = visual.Rect(
    win=win, name='ArrowBar2',
    width=(0.07, 0.01)[0], height=(0.07, 0.01)[1],
    ori=53.0, pos=(0.1831, -0.365),
    lineWidth=1.0,     colorSpace='rgb',  lineColor=None, fillColor='green',
    opacity=None, depth=-3.0, interpolate=True)
InstruText = visual.TextStim(win=win, name='InstruText',
    text='Select the original colour of the square.',
    font='Open Sans',
    pos=(0, 0.35), height=0.03, wrapWidth=0.65, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-4.0);

# Initialize components for Routine "Clear_sc_tut"
Clear_sc_tutClock = core.Clock()

# Initialize components for Routine "break_2"
break_2Clock = core.Clock()
text_2 = visual.TextStim(win=win, name='text_2',
    text="Well done! Let's try another.",
    font='Open Sans',
    pos=(0, 0), height=0.04, wrapWidth=0.65, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "ISI_tutorial_2"
ISI_tutorial_2Clock = core.Clock()
ISI1_cross_3 = visual.TextStim(win=win, name='ISI1_cross_3',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "Stimulus_disp_tutorial_2"
Stimulus_disp_tutorial_2Clock = core.Clock()
Fixation_Point_6 = visual.TextStim(win=win, name='Fixation_Point_6',
    text='·',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
Target_6 = visual.Rect(
    win=win, name='Target_6',
    width=(0.125, 0.125)[0], height=(0.125, 0.125)[1],
    ori=0.0, pos=[0,0],
    lineWidth=1.0,     colorSpace='rgb',  lineColor=None, fillColor='white',
    opacity=None, depth=-1.0, interpolate=True)
Flan1_6 = visual.Rect(
    win=win, name='Flan1_6',
    width=(0.125, 0.125)[0], height=(0.125, 0.125)[1],
    ori=0.0, pos=[0,0],
    lineWidth=1.0,     colorSpace='rgb',  lineColor=None, fillColor='white',
    opacity=None, depth=-2.0, interpolate=True)
Flan2_6 = visual.Rect(
    win=win, name='Flan2_6',
    width=(0.125, 0.125)[0], height=(0.125, 0.125)[1],
    ori=0.0, pos=[0,0],
    lineWidth=1.0,     colorSpace='rgb',  lineColor=None, fillColor='white',
    opacity=None, depth=-3.0, interpolate=True)
Flan3_6 = visual.Rect(
    win=win, name='Flan3_6',
    width=(0.125, 0.125)[0], height=(0.125, 0.125)[1],
    ori=0.0, pos=[0,0],
    lineWidth=1.0,     colorSpace='rgb',  lineColor=None, fillColor=None,
    opacity=None, depth=-4.0, interpolate=True)
Flan4_6 = visual.Rect(
    win=win, name='Flan4_6',
    width=(0.125, 0.125)[0], height=(0.125, 0.125)[1],
    ori=0.0, pos=[0,0],
    lineWidth=1.0,     colorSpace='rgb',  lineColor=None, fillColor=None,
    opacity=None, depth=-5.0, interpolate=True)
Flan5_6 = visual.Rect(
    win=win, name='Flan5_6',
    width=(0.125, 0.125)[0], height=(0.125, 0.125)[1],
    ori=0.0, pos=[0,0],
    lineWidth=1.0,     colorSpace='rgb',  lineColor=None, fillColor=None,
    opacity=None, depth=-6.0, interpolate=True)

# Initialize components for Routine "ISI_tutorial_2"
ISI_tutorial_2Clock = core.Clock()
ISI1_cross_3 = visual.TextStim(win=win, name='ISI1_cross_3',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "Loc_choice_tut_2"
Loc_choice_tut_2Clock = core.Clock()
mouse_11 = event.Mouse(win=win)
x, y = [None, None]
mouse_11.mouseClock = core.Clock()
Fixation_Point_7 = visual.TextStim(win=win, name='Fixation_Point_7',
    text='·',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
Target_7 = visual.Rect(
    win=win, name='Target_7',
    width=(0.125, 0.125)[0], height=(0.125, 0.125)[1],
    ori=0.0, pos=[0,0],
    lineWidth=3.5,     colorSpace='rgb',  lineColor=None, fillColor='white',
    opacity=None, depth=-3.0, interpolate=True)
Flan1_7 = visual.Rect(
    win=win, name='Flan1_7',
    width=(0.125, 0.125)[0], height=(0.125, 0.125)[1],
    ori=0.0, pos=[0,0],
    lineWidth=3.5,     colorSpace='rgb',  lineColor=None, fillColor='white',
    opacity=None, depth=-4.0, interpolate=True)
Flan2_7 = visual.Rect(
    win=win, name='Flan2_7',
    width=(0.125, 0.125)[0], height=(0.125, 0.125)[1],
    ori=0.0, pos=[0,0],
    lineWidth=3.5,     colorSpace='rgb',  lineColor=None, fillColor='white',
    opacity=None, depth=-5.0, interpolate=True)
Flan3_7 = visual.Rect(
    win=win, name='Flan3_7',
    width=(0.125, 0.125)[0], height=(0.125, 0.125)[1],
    ori=0.0, pos=[0,0],
    lineWidth=3.5,     colorSpace='rgb',  lineColor=None, fillColor=None,
    opacity=None, depth=-6.0, interpolate=True)
Flan4_7 = visual.Rect(
    win=win, name='Flan4_7',
    width=(0.125, 0.125)[0], height=(0.125, 0.125)[1],
    ori=0.0, pos=[0,0],
    lineWidth=3.5,     colorSpace='rgb',  lineColor=None, fillColor=None,
    opacity=None, depth=-7.0, interpolate=True)
Flan5_7 = visual.Rect(
    win=win, name='Flan5_7',
    width=(0.125, 0.125)[0], height=(0.125, 0.125)[1],
    ori=0.0, pos=[0,0],
    lineWidth=3.5,     colorSpace='rgb',  lineColor=None, fillColor=None,
    opacity=None, depth=-8.0, interpolate=True)
InstruText2_2 = visual.TextStim(win=win, name='InstruText2_2',
    text='Select the square which changed colour.',
    font='Open Sans',
    pos=(0, 0.3), height=0.03, wrapWidth=0.75, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-9.0);

# Initialize components for Routine "ISI_tutorial_2"
ISI_tutorial_2Clock = core.Clock()
ISI1_cross_3 = visual.TextStim(win=win, name='ISI1_cross_3',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "Choice_tutorial_2"
Choice_tutorial_2Clock = core.Clock()
mouse_12 = event.Mouse(win=win)
x, y = [None, None]
mouse_12.mouseClock = core.Clock()
InstruText_2 = visual.TextStim(win=win, name='InstruText_2',
    text='Select the original colour of the square.',
    font='Open Sans',
    pos=(0, 0.35), height=0.03, wrapWidth=0.65, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);

# Initialize components for Routine "Clear_sc_tut"
Clear_sc_tutClock = core.Clock()

# Initialize components for Routine "Tutorial_end"
Tutorial_endClock = core.Clock()
NumberOBlocks_7 = visual.TextStim(win=win, name='NumberOBlocks_7',
    text='',
    font='Open Sans',
    pos=(0.00, 0.01), height=0.04, wrapWidth=0.85, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
ContinueButtonText_5 = visual.TextStim(win=win, name='ContinueButtonText_5',
    text='Click to begin the task',
    font='Open Sans',
    pos=(0, -0.3), height=0.03, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
ContinueButton_5 = visual.Rect(
    win=win, name='ContinueButton_5',
    width=(0.37, 0.09)[0], height=(0.37, 0.09)[1],
    ori=0.0, pos=(0, -0.3),
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor=None,
    opacity=None, depth=-2.0, interpolate=True)
mouse_10 = event.Mouse(win=win)
x, y = [None, None]
mouse_10.mouseClock = core.Clock()

# Initialize components for Routine "break_3"
break_3Clock = core.Clock()
text_3 = visual.TextStim(win=win, name='text_3',
    text=None,
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "MainInstructions"
MainInstructionsClock = core.Clock()
NumberOBlocks_2 = visual.TextStim(win=win, name='NumberOBlocks_2',
    text='',
    font='Open Sans',
    pos=(0.001, 0.24449), height=0.06, wrapWidth=0.75, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
InstructionsMainText = visual.TextStim(win=win, name='InstructionsMainText',
    text='',
    font='Open Sans',
    pos=(0, -0.0), height=0.04, wrapWidth=0.75, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
NumberOBlocks = visual.TextStim(win=win, name='NumberOBlocks',
    text='',
    font='Open Sans',
    pos=(0.00, 0.25), height=0.06, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-3.0);
ContinueButtonText = visual.TextStim(win=win, name='ContinueButtonText',
    text='Click here to begin',
    font='Open Sans',
    pos=(0, -0.3), height=0.03, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-4.0);
ContinueButton = visual.Rect(
    win=win, name='ContinueButton',
    width=(0.37, 0.09)[0], height=(0.37, 0.09)[1],
    ori=0.0, pos=(0, -0.3),
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor=None,
    opacity=None, depth=-5.0, interpolate=True)
mouse_3 = event.Mouse(win=win)
x, y = [None, None]
mouse_3.mouseClock = core.Clock()

# Initialize components for Routine "Time_gap"
Time_gapClock = core.Clock()
Focus = visual.TextStim(win=win, name='Focus',
    text='·',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "ISI"
ISIClock = core.Clock()
ISI1_cross = visual.TextStim(win=win, name='ISI1_cross',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "Stimulus_display"
Stimulus_displayClock = core.Clock()
Fixation_Point = visual.TextStim(win=win, name='Fixation_Point',
    text='·',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
Target = visual.Rect(
    win=win, name='Target',
    width=(0.15, 0.15)[0], height=(0.15, 0.15)[1],
    ori=0.0, pos=[0,0],
    lineWidth=2.0,     colorSpace='rgb',  lineColor=None, fillColor='white',
    opacity=None, depth=-1.0, interpolate=True)
Flan1 = visual.Rect(
    win=win, name='Flan1',
    width=(0.15, 0.15)[0], height=(0.15, 0.15)[1],
    ori=0.0, pos=[0,0],
    lineWidth=2.0,     colorSpace='rgb',  lineColor=None, fillColor='white',
    opacity=None, depth=-2.0, interpolate=True)
Flan2 = visual.Rect(
    win=win, name='Flan2',
    width=(0.15, 0.15)[0], height=(0.15, 0.15)[1],
    ori=0.0, pos=[0,0],
    lineWidth=2.0,     colorSpace='rgb',  lineColor=None, fillColor='white',
    opacity=None, depth=-3.0, interpolate=True)
Flan3 = visual.Rect(
    win=win, name='Flan3',
    width=(0.15, 0.15)[0], height=(0.15, 0.15)[1],
    ori=0.0, pos=[0,0],
    lineWidth=2.0,     colorSpace='rgb',  lineColor=None, fillColor='white',
    opacity=None, depth=-4.0, interpolate=True)
Flan4 = visual.Rect(
    win=win, name='Flan4',
    width=(0.15, 0.15)[0], height=(0.15, 0.15)[1],
    ori=0.0, pos=[0,0],
    lineWidth=2.0,     colorSpace='rgb',  lineColor=None, fillColor='white',
    opacity=None, depth=-5.0, interpolate=True)
Flan5 = visual.Rect(
    win=win, name='Flan5',
    width=(0.15, 0.15)[0], height=(0.15, 0.15)[1],
    ori=0.0, pos=[0,0],
    lineWidth=2.0,     colorSpace='rgb',  lineColor=None, fillColor='white',
    opacity=None, depth=-6.0, interpolate=True)

# Initialize components for Routine "ISI2"
ISI2Clock = core.Clock()
ISI2_cross = visual.TextStim(win=win, name='ISI2_cross',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "Location_choice"
Location_choiceClock = core.Clock()
mouse = event.Mouse(win=win)
x, y = [None, None]
mouse.mouseClock = core.Clock()
Fixation_Point_2 = visual.TextStim(win=win, name='Fixation_Point_2',
    text='·',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
Target_2 = visual.Rect(
    win=win, name='Target_2',
    width=(0.15, 0.15)[0], height=(0.15, 0.15)[1],
    ori=0.0, pos=[0,0],
    lineWidth=2.0,     colorSpace='rgb',  lineColor=None, fillColor='white',
    opacity=None, depth=-3.0, interpolate=True)
Flan1_2 = visual.Rect(
    win=win, name='Flan1_2',
    width=(0.15, 0.15)[0], height=(0.15, 0.15)[1],
    ori=0.0, pos=[0,0],
    lineWidth=2.0,     colorSpace='rgb',  lineColor=None, fillColor='white',
    opacity=None, depth=-4.0, interpolate=True)
Flan2_2 = visual.Rect(
    win=win, name='Flan2_2',
    width=(0.15, 0.15)[0], height=(0.15, 0.15)[1],
    ori=0.0, pos=[0,0],
    lineWidth=2.0,     colorSpace='rgb',  lineColor=None, fillColor='white',
    opacity=None, depth=-5.0, interpolate=True)
Flan3_2 = visual.Rect(
    win=win, name='Flan3_2',
    width=(0.15, 0.15)[0], height=(0.15, 0.15)[1],
    ori=0.0, pos=[0,0],
    lineWidth=2.0,     colorSpace='rgb',  lineColor=None, fillColor='white',
    opacity=None, depth=-6.0, interpolate=True)
Flan4_2 = visual.Rect(
    win=win, name='Flan4_2',
    width=(0.15, 0.15)[0], height=(0.15, 0.15)[1],
    ori=0.0, pos=[0,0],
    lineWidth=2.0,     colorSpace='rgb',  lineColor=None, fillColor='white',
    opacity=None, depth=-7.0, interpolate=True)
Flan5_2 = visual.Rect(
    win=win, name='Flan5_2',
    width=(0.15, 0.15)[0], height=(0.15, 0.15)[1],
    ori=0.0, pos=[0,0],
    lineWidth=2.0,     colorSpace='rgb',  lineColor=None, fillColor='white',
    opacity=None, depth=-8.0, interpolate=True)

# Initialize components for Routine "ISI3"
ISI3Clock = core.Clock()
ISI3_cross = visual.TextStim(win=win, name='ISI3_cross',
    text=' ',
    font='Open Sans',
    pos=(0, 0), height=0.075, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "Colour_choice"
Colour_choiceClock = core.Clock()
mouse_2 = event.Mouse(win=win)
x, y = [None, None]
mouse_2.mouseClock = core.Clock()

# Initialize components for Routine "Clear_Screen"
Clear_ScreenClock = core.Clock()

# Initialize components for Routine "BlockAdder"
BlockAdderClock = core.Clock()
text = visual.TextStim(win=win, name='text',
    text=' ',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);

# Initialize components for Routine "EndScreen"
EndScreenClock = core.Clock()
EndScreenText = visual.TextStim(win=win, name='EndScreenText',
    text="You have now completed the experiment. Thank you.\n\nPlease inform the researcher.\n\nPress 'qt' to close this window.",
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=0.65, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "Startup_code"-------
continueRoutine = True
# update component parameters for each repeat
win.setMouseVisible(False)
mouse.setPos(newPos=(0,0))
grayBox.setAutoDraw(True)
# keep track of which components have finished
Startup_codeComponents = []
for thisComponent in Startup_codeComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
Startup_codeClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "Startup_code"-------
while continueRoutine:
    # get current time
    t = Startup_codeClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=Startup_codeClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Startup_codeComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Startup_code"-------
for thisComponent in Startup_codeComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "Startup_code" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "Startup_screen"-------
continueRoutine = True
# update component parameters for each repeat
NumberOBlocks_4.setText("This is the 'Colour Change Detection Task'. Welcome!\n\n\nInstructions for this task will appear on the next screen.")
win.setMouseVisible(True)
# setup some python lists for storing info about the mouse_4
mouse_4.clicked_name = []
gotValidClick = False  # until a click is received
# keep track of which components have finished
Startup_screenComponents = [NumberOBlocks_4, ContinueButtonText_2, ContinueButton_2, mouse_4]
for thisComponent in Startup_screenComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
Startup_screenClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "Startup_screen"-------
while continueRoutine:
    # get current time
    t = Startup_screenClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=Startup_screenClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *NumberOBlocks_4* updates
    if NumberOBlocks_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        NumberOBlocks_4.frameNStart = frameN  # exact frame index
        NumberOBlocks_4.tStart = t  # local t and not account for scr refresh
        NumberOBlocks_4.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(NumberOBlocks_4, 'tStartRefresh')  # time at next scr refresh
        NumberOBlocks_4.setAutoDraw(True)
    
    # *ContinueButtonText_2* updates
    if ContinueButtonText_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        ContinueButtonText_2.frameNStart = frameN  # exact frame index
        ContinueButtonText_2.tStart = t  # local t and not account for scr refresh
        ContinueButtonText_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(ContinueButtonText_2, 'tStartRefresh')  # time at next scr refresh
        ContinueButtonText_2.setAutoDraw(True)
    if ContinueButtonText_2.status == STARTED:  # only update if drawing
        ContinueButtonText_2.setColor('white', colorSpace='rgb', log=False)
    
    # *ContinueButton_2* updates
    if ContinueButton_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        ContinueButton_2.frameNStart = frameN  # exact frame index
        ContinueButton_2.tStart = t  # local t and not account for scr refresh
        ContinueButton_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(ContinueButton_2, 'tStartRefresh')  # time at next scr refresh
        ContinueButton_2.setAutoDraw(True)
    if ContinueButton_2.status == STARTED:  # only update if drawing
        ContinueButton_2.setLineColor('white', log=False)
    if ContinueButton_2.contains(mouse):
        ContinueButton_2.lineColor = 'yellow'
        ContinueButtonText_2.color = 'yellow'
    else:
        ContinueButton_2.lineColor = 'white'
        ContinueButtonText_2.color = 'white'
    # *mouse_4* updates
    if mouse_4.status == NOT_STARTED and t >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        mouse_4.frameNStart = frameN  # exact frame index
        mouse_4.tStart = t  # local t and not account for scr refresh
        mouse_4.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(mouse_4, 'tStartRefresh')  # time at next scr refresh
        mouse_4.status = STARTED
        mouse_4.mouseClock.reset()
        prevButtonState = mouse_4.getPressed()  # if button is down already this ISN'T a new click
    if mouse_4.status == STARTED:  # only update if started and not finished!
        buttons = mouse_4.getPressed()
        if buttons != prevButtonState:  # button state changed?
            prevButtonState = buttons
            if sum(buttons) > 0:  # state changed to a new click
                # check if the mouse was inside our 'clickable' objects
                gotValidClick = False
                try:
                    iter(ContinueButton)
                    clickableList = ContinueButton
                except:
                    clickableList = [ContinueButton]
                for obj in clickableList:
                    if obj.contains(mouse_4):
                        gotValidClick = True
                        mouse_4.clicked_name.append(obj.name)
                if gotValidClick:  # abort routine on response
                    continueRoutine = False
    keys = event.getKeys()
    if 'q' in keys and 't' in keys:
            core.quit()
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Startup_screenComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Startup_screen"-------
for thisComponent in Startup_screenComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('NumberOBlocks_4.started', NumberOBlocks_4.tStartRefresh)
thisExp.addData('NumberOBlocks_4.stopped', NumberOBlocks_4.tStopRefresh)
thisExp.addData('ContinueButtonText_2.started', ContinueButtonText_2.tStartRefresh)
thisExp.addData('ContinueButtonText_2.stopped', ContinueButtonText_2.tStopRefresh)
thisExp.addData('ContinueButton_2.started', ContinueButton_2.tStartRefresh)
thisExp.addData('ContinueButton_2.stopped', ContinueButton_2.tStopRefresh)
# store data for thisExp (ExperimentHandler)
x, y = mouse_4.getPos()
buttons = mouse_4.getPressed()
if sum(buttons):
    # check if the mouse was inside our 'clickable' objects
    gotValidClick = False
    try:
        iter(ContinueButton)
        clickableList = ContinueButton
    except:
        clickableList = [ContinueButton]
    for obj in clickableList:
        if obj.contains(mouse_4):
            gotValidClick = True
            mouse_4.clicked_name.append(obj.name)
thisExp.addData('mouse_4.x', x)
thisExp.addData('mouse_4.y', y)
thisExp.addData('mouse_4.leftButton', buttons[0])
thisExp.addData('mouse_4.midButton', buttons[1])
thisExp.addData('mouse_4.rightButton', buttons[2])
if len(mouse_4.clicked_name):
    thisExp.addData('mouse_4.clicked_name', mouse_4.clicked_name[0])
thisExp.addData('mouse_4.started', mouse_4.tStart)
thisExp.addData('mouse_4.stopped', mouse_4.tStop)
thisExp.nextEntry()
# the Routine "Startup_screen" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "Instructions_Begin"-------
continueRoutine = True
# update component parameters for each repeat
NumberOBlocks_5.setText('In this task, you must detect changes which appear onscreen.\n\nA set of squares will appear for a short period. After, the squares will reappear with one square having a new colour.\n\nPlease remember the original colour of the square.')
win.setMouseVisible(True)
# setup some python lists for storing info about the mouse_5
mouse_5.clicked_name = []
gotValidClick = False  # until a click is received
# keep track of which components have finished
Instructions_BeginComponents = [NumberOBlocks_5, ContinueButtonText_3, ContinueButton_3, mouse_5]
for thisComponent in Instructions_BeginComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
Instructions_BeginClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "Instructions_Begin"-------
while continueRoutine:
    # get current time
    t = Instructions_BeginClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=Instructions_BeginClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *NumberOBlocks_5* updates
    if NumberOBlocks_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        NumberOBlocks_5.frameNStart = frameN  # exact frame index
        NumberOBlocks_5.tStart = t  # local t and not account for scr refresh
        NumberOBlocks_5.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(NumberOBlocks_5, 'tStartRefresh')  # time at next scr refresh
        NumberOBlocks_5.setAutoDraw(True)
    
    # *ContinueButtonText_3* updates
    if ContinueButtonText_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        ContinueButtonText_3.frameNStart = frameN  # exact frame index
        ContinueButtonText_3.tStart = t  # local t and not account for scr refresh
        ContinueButtonText_3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(ContinueButtonText_3, 'tStartRefresh')  # time at next scr refresh
        ContinueButtonText_3.setAutoDraw(True)
    if ContinueButtonText_3.status == STARTED:  # only update if drawing
        ContinueButtonText_3.setColor('white', colorSpace='rgb', log=False)
    
    # *ContinueButton_3* updates
    if ContinueButton_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        ContinueButton_3.frameNStart = frameN  # exact frame index
        ContinueButton_3.tStart = t  # local t and not account for scr refresh
        ContinueButton_3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(ContinueButton_3, 'tStartRefresh')  # time at next scr refresh
        ContinueButton_3.setAutoDraw(True)
    if ContinueButton_3.status == STARTED:  # only update if drawing
        ContinueButton_3.setLineColor('white', log=False)
    if ContinueButton_3.contains(mouse):
        ContinueButton_3.lineColor = 'yellow'
        ContinueButtonText_3.color = 'yellow'
    else:
        ContinueButton_3.lineColor = 'white'
        ContinueButtonText_3.color = 'white'
    # *mouse_5* updates
    if mouse_5.status == NOT_STARTED and t >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        mouse_5.frameNStart = frameN  # exact frame index
        mouse_5.tStart = t  # local t and not account for scr refresh
        mouse_5.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(mouse_5, 'tStartRefresh')  # time at next scr refresh
        mouse_5.status = STARTED
        mouse_5.mouseClock.reset()
        prevButtonState = mouse_5.getPressed()  # if button is down already this ISN'T a new click
    if mouse_5.status == STARTED:  # only update if started and not finished!
        buttons = mouse_5.getPressed()
        if buttons != prevButtonState:  # button state changed?
            prevButtonState = buttons
            if sum(buttons) > 0:  # state changed to a new click
                # check if the mouse was inside our 'clickable' objects
                gotValidClick = False
                try:
                    iter(ContinueButton)
                    clickableList = ContinueButton
                except:
                    clickableList = [ContinueButton]
                for obj in clickableList:
                    if obj.contains(mouse_5):
                        gotValidClick = True
                        mouse_5.clicked_name.append(obj.name)
                if gotValidClick:  # abort routine on response
                    continueRoutine = False
    keys = event.getKeys()
    if 'q' in keys and 't' in keys:
            core.quit()
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Instructions_BeginComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Instructions_Begin"-------
for thisComponent in Instructions_BeginComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('NumberOBlocks_5.started', NumberOBlocks_5.tStartRefresh)
thisExp.addData('NumberOBlocks_5.stopped', NumberOBlocks_5.tStopRefresh)
thisExp.addData('ContinueButtonText_3.started', ContinueButtonText_3.tStartRefresh)
thisExp.addData('ContinueButtonText_3.stopped', ContinueButtonText_3.tStopRefresh)
thisExp.addData('ContinueButton_3.started', ContinueButton_3.tStartRefresh)
thisExp.addData('ContinueButton_3.stopped', ContinueButton_3.tStopRefresh)
# store data for thisExp (ExperimentHandler)
x, y = mouse_5.getPos()
buttons = mouse_5.getPressed()
if sum(buttons):
    # check if the mouse was inside our 'clickable' objects
    gotValidClick = False
    try:
        iter(ContinueButton)
        clickableList = ContinueButton
    except:
        clickableList = [ContinueButton]
    for obj in clickableList:
        if obj.contains(mouse_5):
            gotValidClick = True
            mouse_5.clicked_name.append(obj.name)
thisExp.addData('mouse_5.x', x)
thisExp.addData('mouse_5.y', y)
thisExp.addData('mouse_5.leftButton', buttons[0])
thisExp.addData('mouse_5.midButton', buttons[1])
thisExp.addData('mouse_5.rightButton', buttons[2])
if len(mouse_5.clicked_name):
    thisExp.addData('mouse_5.clicked_name', mouse_5.clicked_name[0])
thisExp.addData('mouse_5.started', mouse_5.tStart)
thisExp.addData('mouse_5.stopped', mouse_5.tStop)
thisExp.nextEntry()
# the Routine "Instructions_Begin" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "Instructions_Begin_2"-------
continueRoutine = True
# update component parameters for each repeat
NumberOBlocks_6.setText('Once the squares reappear, click on the square which changed.\n\nThen, identify the original colour of the square using the colour wheel.\n\nYou are being timed.\n\nYou will now complete a quick tutorial.\n\n')
win.setMouseVisible(True)
# setup some python lists for storing info about the mouse_6
mouse_6.clicked_name = []
gotValidClick = False  # until a click is received
# keep track of which components have finished
Instructions_Begin_2Components = [NumberOBlocks_6, ContinueButtonText_4, ContinueButton_4, mouse_6]
for thisComponent in Instructions_Begin_2Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
Instructions_Begin_2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "Instructions_Begin_2"-------
while continueRoutine:
    # get current time
    t = Instructions_Begin_2Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=Instructions_Begin_2Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *NumberOBlocks_6* updates
    if NumberOBlocks_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        NumberOBlocks_6.frameNStart = frameN  # exact frame index
        NumberOBlocks_6.tStart = t  # local t and not account for scr refresh
        NumberOBlocks_6.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(NumberOBlocks_6, 'tStartRefresh')  # time at next scr refresh
        NumberOBlocks_6.setAutoDraw(True)
    
    # *ContinueButtonText_4* updates
    if ContinueButtonText_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        ContinueButtonText_4.frameNStart = frameN  # exact frame index
        ContinueButtonText_4.tStart = t  # local t and not account for scr refresh
        ContinueButtonText_4.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(ContinueButtonText_4, 'tStartRefresh')  # time at next scr refresh
        ContinueButtonText_4.setAutoDraw(True)
    if ContinueButtonText_4.status == STARTED:  # only update if drawing
        ContinueButtonText_4.setColor('white', colorSpace='rgb', log=False)
    
    # *ContinueButton_4* updates
    if ContinueButton_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        ContinueButton_4.frameNStart = frameN  # exact frame index
        ContinueButton_4.tStart = t  # local t and not account for scr refresh
        ContinueButton_4.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(ContinueButton_4, 'tStartRefresh')  # time at next scr refresh
        ContinueButton_4.setAutoDraw(True)
    if ContinueButton_4.status == STARTED:  # only update if drawing
        ContinueButton_4.setLineColor('white', log=False)
    if ContinueButton_4.contains(mouse):
        ContinueButton_4.lineColor = 'yellow'
        ContinueButtonText_4.color = 'yellow'
    else:
        ContinueButton_4.lineColor = 'white'
        ContinueButtonText_4.color = 'white'
    # *mouse_6* updates
    if mouse_6.status == NOT_STARTED and t >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        mouse_6.frameNStart = frameN  # exact frame index
        mouse_6.tStart = t  # local t and not account for scr refresh
        mouse_6.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(mouse_6, 'tStartRefresh')  # time at next scr refresh
        mouse_6.status = STARTED
        mouse_6.mouseClock.reset()
        prevButtonState = mouse_6.getPressed()  # if button is down already this ISN'T a new click
    if mouse_6.status == STARTED:  # only update if started and not finished!
        buttons = mouse_6.getPressed()
        if buttons != prevButtonState:  # button state changed?
            prevButtonState = buttons
            if sum(buttons) > 0:  # state changed to a new click
                # check if the mouse was inside our 'clickable' objects
                gotValidClick = False
                try:
                    iter(ContinueButton)
                    clickableList = ContinueButton
                except:
                    clickableList = [ContinueButton]
                for obj in clickableList:
                    if obj.contains(mouse_6):
                        gotValidClick = True
                        mouse_6.clicked_name.append(obj.name)
                if gotValidClick:  # abort routine on response
                    continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Instructions_Begin_2Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Instructions_Begin_2"-------
for thisComponent in Instructions_Begin_2Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('NumberOBlocks_6.started', NumberOBlocks_6.tStartRefresh)
thisExp.addData('NumberOBlocks_6.stopped', NumberOBlocks_6.tStopRefresh)
thisExp.addData('ContinueButtonText_4.started', ContinueButtonText_4.tStartRefresh)
thisExp.addData('ContinueButtonText_4.stopped', ContinueButtonText_4.tStopRefresh)
thisExp.addData('ContinueButton_4.started', ContinueButton_4.tStartRefresh)
thisExp.addData('ContinueButton_4.stopped', ContinueButton_4.tStopRefresh)
# store data for thisExp (ExperimentHandler)
x, y = mouse_6.getPos()
buttons = mouse_6.getPressed()
if sum(buttons):
    # check if the mouse was inside our 'clickable' objects
    gotValidClick = False
    try:
        iter(ContinueButton)
        clickableList = ContinueButton
    except:
        clickableList = [ContinueButton]
    for obj in clickableList:
        if obj.contains(mouse_6):
            gotValidClick = True
            mouse_6.clicked_name.append(obj.name)
thisExp.addData('mouse_6.x', x)
thisExp.addData('mouse_6.y', y)
thisExp.addData('mouse_6.leftButton', buttons[0])
thisExp.addData('mouse_6.midButton', buttons[1])
thisExp.addData('mouse_6.rightButton', buttons[2])
if len(mouse_6.clicked_name):
    thisExp.addData('mouse_6.clicked_name', mouse_6.clicked_name[0])
thisExp.addData('mouse_6.started', mouse_6.tStart)
thisExp.addData('mouse_6.stopped', mouse_6.tStop)
thisExp.nextEntry()
# the Routine "Instructions_Begin_2" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "ISI_tutorial"-------
continueRoutine = True
routineTimer.add(0.900000)
# update component parameters for each repeat
ISI1_cross_2.setText('·')
win.setMouseVisible(False)

# keep track of which components have finished
ISI_tutorialComponents = [ISI1_cross_2]
for thisComponent in ISI_tutorialComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
ISI_tutorialClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "ISI_tutorial"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = ISI_tutorialClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=ISI_tutorialClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *ISI1_cross_2* updates
    if ISI1_cross_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        ISI1_cross_2.frameNStart = frameN  # exact frame index
        ISI1_cross_2.tStart = t  # local t and not account for scr refresh
        ISI1_cross_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(ISI1_cross_2, 'tStartRefresh')  # time at next scr refresh
        ISI1_cross_2.setAutoDraw(True)
    if ISI1_cross_2.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > ISI1_cross_2.tStartRefresh + 0.9-frameTolerance:
            # keep track of stop time/frame for later
            ISI1_cross_2.tStop = t  # not accounting for scr refresh
            ISI1_cross_2.frameNStop = frameN  # exact frame index
            win.timeOnFlip(ISI1_cross_2, 'tStopRefresh')  # time at next scr refresh
            ISI1_cross_2.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in ISI_tutorialComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "ISI_tutorial"-------
for thisComponent in ISI_tutorialComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('ISI1_cross_2.started', ISI1_cross_2.tStartRefresh)
thisExp.addData('ISI1_cross_2.stopped', ISI1_cross_2.tStopRefresh)

# ------Prepare to start Routine "Stimulus_disp_tutorial"-------
continueRoutine = True
routineTimer.add(0.300000)
# update component parameters for each repeat
Target_3.setFillColor([0.6000, -0.0510, 0.3098])
Target_3.setPos((0.1,0.1))
Flan1_3.setFillColor([-1.0000, 0.2392, -0.0980])
Flan1_3.setPos((-0.1,-0.1))
Flan2_3.setFillColor([-0.4118, -1.0000, 0.0196])
Flan2_3.setPos((0.1,-0.1))
Flan3_3.setFillColor('')
Flan3_3.setPos((2,2))
Flan4_3.setFillColor('')
Flan4_3.setPos((2,2))
Flan5_3.setFillColor('')
Flan5_3.setPos((2,2))
# keep track of which components have finished
Stimulus_disp_tutorialComponents = [Fixation_Point_3, Target_3, Flan1_3, Flan2_3, Flan3_3, Flan4_3, Flan5_3]
for thisComponent in Stimulus_disp_tutorialComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
Stimulus_disp_tutorialClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "Stimulus_disp_tutorial"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = Stimulus_disp_tutorialClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=Stimulus_disp_tutorialClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *Fixation_Point_3* updates
    if Fixation_Point_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Fixation_Point_3.frameNStart = frameN  # exact frame index
        Fixation_Point_3.tStart = t  # local t and not account for scr refresh
        Fixation_Point_3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Fixation_Point_3, 'tStartRefresh')  # time at next scr refresh
        Fixation_Point_3.setAutoDraw(True)
    if Fixation_Point_3.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > Fixation_Point_3.tStartRefresh + 0.3-frameTolerance:
            # keep track of stop time/frame for later
            Fixation_Point_3.tStop = t  # not accounting for scr refresh
            Fixation_Point_3.frameNStop = frameN  # exact frame index
            win.timeOnFlip(Fixation_Point_3, 'tStopRefresh')  # time at next scr refresh
            Fixation_Point_3.setAutoDraw(False)
    
    # *Target_3* updates
    if Target_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Target_3.frameNStart = frameN  # exact frame index
        Target_3.tStart = t  # local t and not account for scr refresh
        Target_3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Target_3, 'tStartRefresh')  # time at next scr refresh
        Target_3.setAutoDraw(True)
    if Target_3.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > Target_3.tStartRefresh + 0.3-frameTolerance:
            # keep track of stop time/frame for later
            Target_3.tStop = t  # not accounting for scr refresh
            Target_3.frameNStop = frameN  # exact frame index
            win.timeOnFlip(Target_3, 'tStopRefresh')  # time at next scr refresh
            Target_3.setAutoDraw(False)
    
    # *Flan1_3* updates
    if Flan1_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Flan1_3.frameNStart = frameN  # exact frame index
        Flan1_3.tStart = t  # local t and not account for scr refresh
        Flan1_3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Flan1_3, 'tStartRefresh')  # time at next scr refresh
        Flan1_3.setAutoDraw(True)
    if Flan1_3.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > Flan1_3.tStartRefresh + 0.3-frameTolerance:
            # keep track of stop time/frame for later
            Flan1_3.tStop = t  # not accounting for scr refresh
            Flan1_3.frameNStop = frameN  # exact frame index
            win.timeOnFlip(Flan1_3, 'tStopRefresh')  # time at next scr refresh
            Flan1_3.setAutoDraw(False)
    
    # *Flan2_3* updates
    if Flan2_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Flan2_3.frameNStart = frameN  # exact frame index
        Flan2_3.tStart = t  # local t and not account for scr refresh
        Flan2_3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Flan2_3, 'tStartRefresh')  # time at next scr refresh
        Flan2_3.setAutoDraw(True)
    if Flan2_3.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > Flan2_3.tStartRefresh + 0.3-frameTolerance:
            # keep track of stop time/frame for later
            Flan2_3.tStop = t  # not accounting for scr refresh
            Flan2_3.frameNStop = frameN  # exact frame index
            win.timeOnFlip(Flan2_3, 'tStopRefresh')  # time at next scr refresh
            Flan2_3.setAutoDraw(False)
    
    # *Flan3_3* updates
    if Flan3_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Flan3_3.frameNStart = frameN  # exact frame index
        Flan3_3.tStart = t  # local t and not account for scr refresh
        Flan3_3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Flan3_3, 'tStartRefresh')  # time at next scr refresh
        Flan3_3.setAutoDraw(True)
    if Flan3_3.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > Flan3_3.tStartRefresh + 0.3-frameTolerance:
            # keep track of stop time/frame for later
            Flan3_3.tStop = t  # not accounting for scr refresh
            Flan3_3.frameNStop = frameN  # exact frame index
            win.timeOnFlip(Flan3_3, 'tStopRefresh')  # time at next scr refresh
            Flan3_3.setAutoDraw(False)
    
    # *Flan4_3* updates
    if Flan4_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Flan4_3.frameNStart = frameN  # exact frame index
        Flan4_3.tStart = t  # local t and not account for scr refresh
        Flan4_3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Flan4_3, 'tStartRefresh')  # time at next scr refresh
        Flan4_3.setAutoDraw(True)
    if Flan4_3.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > Flan4_3.tStartRefresh + 0.3-frameTolerance:
            # keep track of stop time/frame for later
            Flan4_3.tStop = t  # not accounting for scr refresh
            Flan4_3.frameNStop = frameN  # exact frame index
            win.timeOnFlip(Flan4_3, 'tStopRefresh')  # time at next scr refresh
            Flan4_3.setAutoDraw(False)
    
    # *Flan5_3* updates
    if Flan5_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Flan5_3.frameNStart = frameN  # exact frame index
        Flan5_3.tStart = t  # local t and not account for scr refresh
        Flan5_3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Flan5_3, 'tStartRefresh')  # time at next scr refresh
        Flan5_3.setAutoDraw(True)
    if Flan5_3.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > Flan5_3.tStartRefresh + 0.3-frameTolerance:
            # keep track of stop time/frame for later
            Flan5_3.tStop = t  # not accounting for scr refresh
            Flan5_3.frameNStop = frameN  # exact frame index
            win.timeOnFlip(Flan5_3, 'tStopRefresh')  # time at next scr refresh
            Flan5_3.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Stimulus_disp_tutorialComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Stimulus_disp_tutorial"-------
for thisComponent in Stimulus_disp_tutorialComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('Fixation_Point_3.started', Fixation_Point_3.tStartRefresh)
thisExp.addData('Fixation_Point_3.stopped', Fixation_Point_3.tStopRefresh)
thisExp.addData('Target_3.started', Target_3.tStartRefresh)
thisExp.addData('Target_3.stopped', Target_3.tStopRefresh)
thisExp.addData('Flan1_3.started', Flan1_3.tStartRefresh)
thisExp.addData('Flan1_3.stopped', Flan1_3.tStopRefresh)
thisExp.addData('Flan2_3.started', Flan2_3.tStartRefresh)
thisExp.addData('Flan2_3.stopped', Flan2_3.tStopRefresh)
thisExp.addData('Flan3_3.started', Flan3_3.tStartRefresh)
thisExp.addData('Flan3_3.stopped', Flan3_3.tStopRefresh)
thisExp.addData('Flan4_3.started', Flan4_3.tStartRefresh)
thisExp.addData('Flan4_3.stopped', Flan4_3.tStopRefresh)
thisExp.addData('Flan5_3.started', Flan5_3.tStartRefresh)
thisExp.addData('Flan5_3.stopped', Flan5_3.tStopRefresh)

# ------Prepare to start Routine "ISI_tutorial"-------
continueRoutine = True
routineTimer.add(0.900000)
# update component parameters for each repeat
ISI1_cross_2.setText('·')
win.setMouseVisible(False)

# keep track of which components have finished
ISI_tutorialComponents = [ISI1_cross_2]
for thisComponent in ISI_tutorialComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
ISI_tutorialClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "ISI_tutorial"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = ISI_tutorialClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=ISI_tutorialClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *ISI1_cross_2* updates
    if ISI1_cross_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        ISI1_cross_2.frameNStart = frameN  # exact frame index
        ISI1_cross_2.tStart = t  # local t and not account for scr refresh
        ISI1_cross_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(ISI1_cross_2, 'tStartRefresh')  # time at next scr refresh
        ISI1_cross_2.setAutoDraw(True)
    if ISI1_cross_2.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > ISI1_cross_2.tStartRefresh + 0.9-frameTolerance:
            # keep track of stop time/frame for later
            ISI1_cross_2.tStop = t  # not accounting for scr refresh
            ISI1_cross_2.frameNStop = frameN  # exact frame index
            win.timeOnFlip(ISI1_cross_2, 'tStopRefresh')  # time at next scr refresh
            ISI1_cross_2.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in ISI_tutorialComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "ISI_tutorial"-------
for thisComponent in ISI_tutorialComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('ISI1_cross_2.started', ISI1_cross_2.tStartRefresh)
thisExp.addData('ISI1_cross_2.stopped', ISI1_cross_2.tStopRefresh)

# ------Prepare to start Routine "Loc_choice_tut"-------
continueRoutine = True
# update component parameters for each repeat
# setup some python lists for storing info about the mouse_8
mouse_8.clicked_name = []
gotValidClick = False  # until a click is received
win.setMouseVisible(True)

Target_5.setFillColor([-1.0000, -1.0000, -1.0000])
Target_5.setPos((0.1,0.1))
Flan1_5.setFillColor([-1.0000, 0.2392, -0.0980])
Flan1_5.setPos((-0.1,-0.1))
Flan2_5.setFillColor([-0.4118, -1.0000, 0.0196])
Flan2_5.setPos((0.1,-0.1))
Flan3_5.setFillColor('')
Flan3_5.setPos((2,2))
Flan4_5.setFillColor('')
Flan4_5.setPos((2,2))
Flan5_5.setFillColor('')
Flan5_5.setPos((2,2))
# keep track of which components have finished
Loc_choice_tutComponents = [mouse_8, Fixation_Point_5, Target_5, Flan1_5, Flan2_5, Flan3_5, Flan4_5, Flan5_5, ArrowHead, ArrowBar, InstruText2]
for thisComponent in Loc_choice_tutComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
Loc_choice_tutClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "Loc_choice_tut"-------
while continueRoutine:
    # get current time
    t = Loc_choice_tutClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=Loc_choice_tutClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    # *mouse_8* updates
    if mouse_8.status == NOT_STARTED and t >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        mouse_8.frameNStart = frameN  # exact frame index
        mouse_8.tStart = t  # local t and not account for scr refresh
        mouse_8.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(mouse_8, 'tStartRefresh')  # time at next scr refresh
        mouse_8.status = STARTED
        mouse_8.mouseClock.reset()
        prevButtonState = [0, 0, 0]  # if now button is down we will treat as 'new' click
    if mouse_8.status == STARTED:  # only update if started and not finished!
        buttons = mouse_8.getPressed()
        if buttons != prevButtonState:  # button state changed?
            prevButtonState = buttons
            if sum(buttons) > 0:  # state changed to a new click
                # check if the mouse was inside our 'clickable' objects
                gotValidClick = False
                try:
                    iter(Target_5)
                    clickableList = Target_5
                except:
                    clickableList = [Target_5]
                for obj in clickableList:
                    if obj.contains(mouse_8):
                        gotValidClick = True
                        mouse_8.clicked_name.append(obj.name)
                if gotValidClick:  # abort routine on response
                    continueRoutine = False
    if Target_5.contains(mouse):
        Target_5.lineColor = 'green'
    else:
        Target_5.lineColor = 'grey'
        
    if Flan1_5.contains(mouse):
        Flan1_5.lineColor = 'red'
    else:
        Flan1_5.lineColor = 'grey'
        
    if Flan2_5.contains(mouse):
        Flan2_5.lineColor = 'red'
    else:
        Flan2_5.lineColor = 'grey'
    
    # *Fixation_Point_5* updates
    if Fixation_Point_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Fixation_Point_5.frameNStart = frameN  # exact frame index
        Fixation_Point_5.tStart = t  # local t and not account for scr refresh
        Fixation_Point_5.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Fixation_Point_5, 'tStartRefresh')  # time at next scr refresh
        Fixation_Point_5.setAutoDraw(True)
    
    # *Target_5* updates
    if Target_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Target_5.frameNStart = frameN  # exact frame index
        Target_5.tStart = t  # local t and not account for scr refresh
        Target_5.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Target_5, 'tStartRefresh')  # time at next scr refresh
        Target_5.setAutoDraw(True)
    
    # *Flan1_5* updates
    if Flan1_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Flan1_5.frameNStart = frameN  # exact frame index
        Flan1_5.tStart = t  # local t and not account for scr refresh
        Flan1_5.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Flan1_5, 'tStartRefresh')  # time at next scr refresh
        Flan1_5.setAutoDraw(True)
    
    # *Flan2_5* updates
    if Flan2_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Flan2_5.frameNStart = frameN  # exact frame index
        Flan2_5.tStart = t  # local t and not account for scr refresh
        Flan2_5.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Flan2_5, 'tStartRefresh')  # time at next scr refresh
        Flan2_5.setAutoDraw(True)
    
    # *Flan3_5* updates
    if Flan3_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Flan3_5.frameNStart = frameN  # exact frame index
        Flan3_5.tStart = t  # local t and not account for scr refresh
        Flan3_5.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Flan3_5, 'tStartRefresh')  # time at next scr refresh
        Flan3_5.setAutoDraw(True)
    
    # *Flan4_5* updates
    if Flan4_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Flan4_5.frameNStart = frameN  # exact frame index
        Flan4_5.tStart = t  # local t and not account for scr refresh
        Flan4_5.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Flan4_5, 'tStartRefresh')  # time at next scr refresh
        Flan4_5.setAutoDraw(True)
    
    # *Flan5_5* updates
    if Flan5_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Flan5_5.frameNStart = frameN  # exact frame index
        Flan5_5.tStart = t  # local t and not account for scr refresh
        Flan5_5.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Flan5_5, 'tStartRefresh')  # time at next scr refresh
        Flan5_5.setAutoDraw(True)
    
    # *ArrowHead* updates
    if ArrowHead.status == NOT_STARTED and tThisFlip >= 2-frameTolerance:
        # keep track of start time/frame for later
        ArrowHead.frameNStart = frameN  # exact frame index
        ArrowHead.tStart = t  # local t and not account for scr refresh
        ArrowHead.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(ArrowHead, 'tStartRefresh')  # time at next scr refresh
        ArrowHead.setAutoDraw(True)
    
    # *ArrowBar* updates
    if ArrowBar.status == NOT_STARTED and tThisFlip >= 2-frameTolerance:
        # keep track of start time/frame for later
        ArrowBar.frameNStart = frameN  # exact frame index
        ArrowBar.tStart = t  # local t and not account for scr refresh
        ArrowBar.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(ArrowBar, 'tStartRefresh')  # time at next scr refresh
        ArrowBar.setAutoDraw(True)
    
    # *InstruText2* updates
    if InstruText2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        InstruText2.frameNStart = frameN  # exact frame index
        InstruText2.tStart = t  # local t and not account for scr refresh
        InstruText2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(InstruText2, 'tStartRefresh')  # time at next scr refresh
        InstruText2.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Loc_choice_tutComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Loc_choice_tut"-------
for thisComponent in Loc_choice_tutComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# store data for thisExp (ExperimentHandler)
x, y = mouse_8.getPos()
buttons = mouse_8.getPressed()
if sum(buttons):
    # check if the mouse was inside our 'clickable' objects
    gotValidClick = False
    try:
        iter(Target_5)
        clickableList = Target_5
    except:
        clickableList = [Target_5]
    for obj in clickableList:
        if obj.contains(mouse_8):
            gotValidClick = True
            mouse_8.clicked_name.append(obj.name)
thisExp.addData('mouse_8.x', x)
thisExp.addData('mouse_8.y', y)
thisExp.addData('mouse_8.leftButton', buttons[0])
thisExp.addData('mouse_8.midButton', buttons[1])
thisExp.addData('mouse_8.rightButton', buttons[2])
if len(mouse_8.clicked_name):
    thisExp.addData('mouse_8.clicked_name', mouse_8.clicked_name[0])
thisExp.addData('mouse_8.started', mouse_8.tStart)
thisExp.addData('mouse_8.stopped', mouse_8.tStop)
thisExp.nextEntry()
thisExp.addData('Fixation_Point_5.started', Fixation_Point_5.tStartRefresh)
thisExp.addData('Fixation_Point_5.stopped', Fixation_Point_5.tStopRefresh)
thisExp.addData('Target_5.started', Target_5.tStartRefresh)
thisExp.addData('Target_5.stopped', Target_5.tStopRefresh)
thisExp.addData('Flan1_5.started', Flan1_5.tStartRefresh)
thisExp.addData('Flan1_5.stopped', Flan1_5.tStopRefresh)
thisExp.addData('Flan2_5.started', Flan2_5.tStartRefresh)
thisExp.addData('Flan2_5.stopped', Flan2_5.tStopRefresh)
thisExp.addData('Flan3_5.started', Flan3_5.tStartRefresh)
thisExp.addData('Flan3_5.stopped', Flan3_5.tStopRefresh)
thisExp.addData('Flan4_5.started', Flan4_5.tStartRefresh)
thisExp.addData('Flan4_5.stopped', Flan4_5.tStopRefresh)
thisExp.addData('Flan5_5.started', Flan5_5.tStartRefresh)
thisExp.addData('Flan5_5.stopped', Flan5_5.tStopRefresh)
thisExp.addData('ArrowHead.started', ArrowHead.tStartRefresh)
thisExp.addData('ArrowHead.stopped', ArrowHead.tStopRefresh)
thisExp.addData('ArrowBar.started', ArrowBar.tStartRefresh)
thisExp.addData('ArrowBar.stopped', ArrowBar.tStopRefresh)
thisExp.addData('InstruText2.started', InstruText2.tStartRefresh)
thisExp.addData('InstruText2.stopped', InstruText2.tStopRefresh)
# the Routine "Loc_choice_tut" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "ISI_tutorial"-------
continueRoutine = True
routineTimer.add(0.900000)
# update component parameters for each repeat
ISI1_cross_2.setText('·')
win.setMouseVisible(False)

# keep track of which components have finished
ISI_tutorialComponents = [ISI1_cross_2]
for thisComponent in ISI_tutorialComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
ISI_tutorialClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "ISI_tutorial"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = ISI_tutorialClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=ISI_tutorialClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *ISI1_cross_2* updates
    if ISI1_cross_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        ISI1_cross_2.frameNStart = frameN  # exact frame index
        ISI1_cross_2.tStart = t  # local t and not account for scr refresh
        ISI1_cross_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(ISI1_cross_2, 'tStartRefresh')  # time at next scr refresh
        ISI1_cross_2.setAutoDraw(True)
    if ISI1_cross_2.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > ISI1_cross_2.tStartRefresh + 0.9-frameTolerance:
            # keep track of stop time/frame for later
            ISI1_cross_2.tStop = t  # not accounting for scr refresh
            ISI1_cross_2.frameNStop = frameN  # exact frame index
            win.timeOnFlip(ISI1_cross_2, 'tStopRefresh')  # time at next scr refresh
            ISI1_cross_2.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in ISI_tutorialComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "ISI_tutorial"-------
for thisComponent in ISI_tutorialComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('ISI1_cross_2.started', ISI1_cross_2.tStartRefresh)
thisExp.addData('ISI1_cross_2.stopped', ISI1_cross_2.tStopRefresh)

# ------Prepare to start Routine "Choice_tutorial"-------
continueRoutine = True
# update component parameters for each repeat
win.setMouseVisible(True)


wedgeYellow.setAutoDraw(True)
wedgeWhite.setAutoDraw(True)
wedgeVermilion.setAutoDraw(True)
wedgeRedPurple.setAutoDraw(True)

wedgeBlack.setAutoDraw(True)
wedgeIndigo.setAutoDraw(True)
wedgeSkyBlue.setAutoDraw(True)
wedgeBlueGreen.setAutoDraw(True)

GreyCircle.setAutoDraw(True)

# setup some python lists for storing info about the mouse_9
mouse_9.clicked_name = []
gotValidClick = False  # until a click is received
# keep track of which components have finished
Choice_tutorialComponents = [mouse_9, ArrowHead2, ArrowBar2, InstruText]
for thisComponent in Choice_tutorialComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
Choice_tutorialClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "Choice_tutorial"-------
while continueRoutine:
    # get current time
    t = Choice_tutorialClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=Choice_tutorialClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    if (wedgeYellow.contains(mouse)):
        wedgeYellow.lineColor = 'red'
        GuideYellow.setAutoDraw(True)
    else:
        wedgeYellow.lineColor = 'grey'
        GuideYellow.setAutoDraw(False)
    
    if wedgeWhite.contains(mouse):
        wedgeWhite.lineColor = 'red'
        GuideWhite.setAutoDraw(True)
    else:
        wedgeWhite.lineColor = 'grey'
        GuideWhite.setAutoDraw(False)
        
    if wedgeVermilion.contains(mouse):
        wedgeVermilion.lineColor = 'red'
        GuideVermilion.setAutoDraw(True)
    else:
        wedgeVermilion.lineColor = 'grey'
        GuideVermilion.setAutoDraw(False)
        
    if wedgeRedPurple.contains(mouse):
        wedgeRedPurple.lineColor = 'green'
        GuideRedPurple.setAutoDraw(True)
    else:
        wedgeRedPurple.lineColor = 'grey'
        GuideRedPurple.setAutoDraw(False)
        
    if wedgeBlack.contains(mouse):
        wedgeBlack.lineColor = 'red'
        GuideBlack.setAutoDraw(True)
    else:
        wedgeBlack.lineColor = 'grey'
        GuideBlack.setAutoDraw(False)
        
    if wedgeIndigo.contains(mouse):
        wedgeIndigo.lineColor = 'red'
        GuideIndigo.setAutoDraw(True)
    else:
        wedgeIndigo.lineColor = 'grey'
        GuideIndigo.setAutoDraw(False)
        
    if wedgeSkyBlue.contains(mouse):
        wedgeSkyBlue.lineColor = 'red'
        GuideSkyBlue.setAutoDraw(True)
    else:
        wedgeSkyBlue.lineColor = 'grey'
        GuideSkyBlue.setAutoDraw(False)
        
    if wedgeBlueGreen.contains(mouse):
        wedgeBlueGreen.lineColor = 'red'
        GuideBlueGreen.setAutoDraw(True)
    else:
        wedgeBlueGreen.lineColor = 'grey'
        GuideBlueGreen.setAutoDraw(False)
    # *mouse_9* updates
    if mouse_9.status == NOT_STARTED and t >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        mouse_9.frameNStart = frameN  # exact frame index
        mouse_9.tStart = t  # local t and not account for scr refresh
        mouse_9.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(mouse_9, 'tStartRefresh')  # time at next scr refresh
        mouse_9.status = STARTED
        mouse_9.mouseClock.reset()
        prevButtonState = [0, 0, 0]  # if now button is down we will treat as 'new' click
    if mouse_9.status == STARTED:  # only update if started and not finished!
        buttons = mouse_9.getPressed()
        if buttons != prevButtonState:  # button state changed?
            prevButtonState = buttons
            if sum(buttons) > 0:  # state changed to a new click
                # check if the mouse was inside our 'clickable' objects
                gotValidClick = False
                try:
                    iter(wedgeRedPurple)
                    clickableList = wedgeRedPurple
                except:
                    clickableList = [wedgeRedPurple]
                for obj in clickableList:
                    if obj.contains(mouse_9):
                        gotValidClick = True
                        mouse_9.clicked_name.append(obj.name)
                if gotValidClick:  # abort routine on response
                    continueRoutine = False
    
    # *ArrowHead2* updates
    if ArrowHead2.status == NOT_STARTED and tThisFlip >= 2-frameTolerance:
        # keep track of start time/frame for later
        ArrowHead2.frameNStart = frameN  # exact frame index
        ArrowHead2.tStart = t  # local t and not account for scr refresh
        ArrowHead2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(ArrowHead2, 'tStartRefresh')  # time at next scr refresh
        ArrowHead2.setAutoDraw(True)
    
    # *ArrowBar2* updates
    if ArrowBar2.status == NOT_STARTED and tThisFlip >= 2-frameTolerance:
        # keep track of start time/frame for later
        ArrowBar2.frameNStart = frameN  # exact frame index
        ArrowBar2.tStart = t  # local t and not account for scr refresh
        ArrowBar2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(ArrowBar2, 'tStartRefresh')  # time at next scr refresh
        ArrowBar2.setAutoDraw(True)
    
    # *InstruText* updates
    if InstruText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        InstruText.frameNStart = frameN  # exact frame index
        InstruText.tStart = t  # local t and not account for scr refresh
        InstruText.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(InstruText, 'tStartRefresh')  # time at next scr refresh
        InstruText.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Choice_tutorialComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Choice_tutorial"-------
for thisComponent in Choice_tutorialComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# store data for thisExp (ExperimentHandler)
x, y = mouse_9.getPos()
buttons = mouse_9.getPressed()
if sum(buttons):
    # check if the mouse was inside our 'clickable' objects
    gotValidClick = False
    try:
        iter(wedgeRedPurple)
        clickableList = wedgeRedPurple
    except:
        clickableList = [wedgeRedPurple]
    for obj in clickableList:
        if obj.contains(mouse_9):
            gotValidClick = True
            mouse_9.clicked_name.append(obj.name)
thisExp.addData('mouse_9.x', x)
thisExp.addData('mouse_9.y', y)
thisExp.addData('mouse_9.leftButton', buttons[0])
thisExp.addData('mouse_9.midButton', buttons[1])
thisExp.addData('mouse_9.rightButton', buttons[2])
if len(mouse_9.clicked_name):
    thisExp.addData('mouse_9.clicked_name', mouse_9.clicked_name[0])
thisExp.addData('mouse_9.started', mouse_9.tStart)
thisExp.addData('mouse_9.stopped', mouse_9.tStop)
thisExp.nextEntry()
thisExp.addData('ArrowHead2.started', ArrowHead2.tStartRefresh)
thisExp.addData('ArrowHead2.stopped', ArrowHead2.tStopRefresh)
thisExp.addData('ArrowBar2.started', ArrowBar2.tStartRefresh)
thisExp.addData('ArrowBar2.stopped', ArrowBar2.tStopRefresh)
thisExp.addData('InstruText.started', InstruText.tStartRefresh)
thisExp.addData('InstruText.stopped', InstruText.tStopRefresh)
# the Routine "Choice_tutorial" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "Clear_sc_tut"-------
continueRoutine = True
# update component parameters for each repeat
win.setMouseVisible(False)

GreyCircle.setAutoDraw(False)

wedgeYellow.setAutoDraw(False)
wedgeWhite.setAutoDraw(False)
wedgeVermilion.setAutoDraw(False)
wedgeRedPurple.setAutoDraw(False)

wedgeBlack.setAutoDraw(False)
wedgeIndigo.setAutoDraw(False)
wedgeSkyBlue.setAutoDraw(False)
wedgeBlueGreen.setAutoDraw(False)

GuideYellow.setAutoDraw(False)
GuideWhite.setAutoDraw(False)
GuideVermilion.setAutoDraw(False)
GuideRedPurple.setAutoDraw(False)

GuideBlack.setAutoDraw(False)
GuideIndigo.setAutoDraw(False)
GuideSkyBlue.setAutoDraw(False)
GuideBlueGreen.setAutoDraw(False)
# keep track of which components have finished
Clear_sc_tutComponents = []
for thisComponent in Clear_sc_tutComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
Clear_sc_tutClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "Clear_sc_tut"-------
while continueRoutine:
    # get current time
    t = Clear_sc_tutClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=Clear_sc_tutClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Clear_sc_tutComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Clear_sc_tut"-------
for thisComponent in Clear_sc_tutComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "Clear_sc_tut" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "break_2"-------
continueRoutine = True
routineTimer.add(3.000000)
# update component parameters for each repeat
# keep track of which components have finished
break_2Components = [text_2]
for thisComponent in break_2Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
break_2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "break_2"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = break_2Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=break_2Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_2* updates
    if text_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_2.frameNStart = frameN  # exact frame index
        text_2.tStart = t  # local t and not account for scr refresh
        text_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_2, 'tStartRefresh')  # time at next scr refresh
        text_2.setAutoDraw(True)
    if text_2.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text_2.tStartRefresh + 3.0-frameTolerance:
            # keep track of stop time/frame for later
            text_2.tStop = t  # not accounting for scr refresh
            text_2.frameNStop = frameN  # exact frame index
            win.timeOnFlip(text_2, 'tStopRefresh')  # time at next scr refresh
            text_2.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in break_2Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "break_2"-------
for thisComponent in break_2Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_2.started', text_2.tStartRefresh)
thisExp.addData('text_2.stopped', text_2.tStopRefresh)

# ------Prepare to start Routine "ISI_tutorial_2"-------
continueRoutine = True
routineTimer.add(0.900000)
# update component parameters for each repeat
ISI1_cross_3.setText('·')
win.setMouseVisible(False)

# keep track of which components have finished
ISI_tutorial_2Components = [ISI1_cross_3]
for thisComponent in ISI_tutorial_2Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
ISI_tutorial_2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "ISI_tutorial_2"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = ISI_tutorial_2Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=ISI_tutorial_2Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *ISI1_cross_3* updates
    if ISI1_cross_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        ISI1_cross_3.frameNStart = frameN  # exact frame index
        ISI1_cross_3.tStart = t  # local t and not account for scr refresh
        ISI1_cross_3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(ISI1_cross_3, 'tStartRefresh')  # time at next scr refresh
        ISI1_cross_3.setAutoDraw(True)
    if ISI1_cross_3.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > ISI1_cross_3.tStartRefresh + 0.9-frameTolerance:
            # keep track of stop time/frame for later
            ISI1_cross_3.tStop = t  # not accounting for scr refresh
            ISI1_cross_3.frameNStop = frameN  # exact frame index
            win.timeOnFlip(ISI1_cross_3, 'tStopRefresh')  # time at next scr refresh
            ISI1_cross_3.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in ISI_tutorial_2Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "ISI_tutorial_2"-------
for thisComponent in ISI_tutorial_2Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('ISI1_cross_3.started', ISI1_cross_3.tStartRefresh)
thisExp.addData('ISI1_cross_3.stopped', ISI1_cross_3.tStopRefresh)

# ------Prepare to start Routine "Stimulus_disp_tutorial_2"-------
continueRoutine = True
routineTimer.add(0.300000)
# update component parameters for each repeat
Target_6.setFillColor([-0.3255, 0.4118, 0.8275])
Target_6.setPos((0.2,0.2))
Flan1_6.setFillColor([0.6000, -0.0510, 0.3098])
Flan1_6.setPos((-0.1,-0.1))
Flan2_6.setFillColor([-1.0000, -1.0000, -1.0000])
Flan2_6.setPos((0.1,-0.3))
Flan3_6.setFillColor('')
Flan3_6.setPos((2,2))
Flan4_6.setFillColor('')
Flan4_6.setPos((2,2))
Flan5_6.setFillColor('')
Flan5_6.setPos((2,2))
# keep track of which components have finished
Stimulus_disp_tutorial_2Components = [Fixation_Point_6, Target_6, Flan1_6, Flan2_6, Flan3_6, Flan4_6, Flan5_6]
for thisComponent in Stimulus_disp_tutorial_2Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
Stimulus_disp_tutorial_2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "Stimulus_disp_tutorial_2"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = Stimulus_disp_tutorial_2Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=Stimulus_disp_tutorial_2Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *Fixation_Point_6* updates
    if Fixation_Point_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Fixation_Point_6.frameNStart = frameN  # exact frame index
        Fixation_Point_6.tStart = t  # local t and not account for scr refresh
        Fixation_Point_6.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Fixation_Point_6, 'tStartRefresh')  # time at next scr refresh
        Fixation_Point_6.setAutoDraw(True)
    if Fixation_Point_6.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > Fixation_Point_6.tStartRefresh + 0.3-frameTolerance:
            # keep track of stop time/frame for later
            Fixation_Point_6.tStop = t  # not accounting for scr refresh
            Fixation_Point_6.frameNStop = frameN  # exact frame index
            win.timeOnFlip(Fixation_Point_6, 'tStopRefresh')  # time at next scr refresh
            Fixation_Point_6.setAutoDraw(False)
    
    # *Target_6* updates
    if Target_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Target_6.frameNStart = frameN  # exact frame index
        Target_6.tStart = t  # local t and not account for scr refresh
        Target_6.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Target_6, 'tStartRefresh')  # time at next scr refresh
        Target_6.setAutoDraw(True)
    if Target_6.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > Target_6.tStartRefresh + 0.3-frameTolerance:
            # keep track of stop time/frame for later
            Target_6.tStop = t  # not accounting for scr refresh
            Target_6.frameNStop = frameN  # exact frame index
            win.timeOnFlip(Target_6, 'tStopRefresh')  # time at next scr refresh
            Target_6.setAutoDraw(False)
    
    # *Flan1_6* updates
    if Flan1_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Flan1_6.frameNStart = frameN  # exact frame index
        Flan1_6.tStart = t  # local t and not account for scr refresh
        Flan1_6.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Flan1_6, 'tStartRefresh')  # time at next scr refresh
        Flan1_6.setAutoDraw(True)
    if Flan1_6.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > Flan1_6.tStartRefresh + 0.3-frameTolerance:
            # keep track of stop time/frame for later
            Flan1_6.tStop = t  # not accounting for scr refresh
            Flan1_6.frameNStop = frameN  # exact frame index
            win.timeOnFlip(Flan1_6, 'tStopRefresh')  # time at next scr refresh
            Flan1_6.setAutoDraw(False)
    
    # *Flan2_6* updates
    if Flan2_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Flan2_6.frameNStart = frameN  # exact frame index
        Flan2_6.tStart = t  # local t and not account for scr refresh
        Flan2_6.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Flan2_6, 'tStartRefresh')  # time at next scr refresh
        Flan2_6.setAutoDraw(True)
    if Flan2_6.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > Flan2_6.tStartRefresh + 0.3-frameTolerance:
            # keep track of stop time/frame for later
            Flan2_6.tStop = t  # not accounting for scr refresh
            Flan2_6.frameNStop = frameN  # exact frame index
            win.timeOnFlip(Flan2_6, 'tStopRefresh')  # time at next scr refresh
            Flan2_6.setAutoDraw(False)
    
    # *Flan3_6* updates
    if Flan3_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Flan3_6.frameNStart = frameN  # exact frame index
        Flan3_6.tStart = t  # local t and not account for scr refresh
        Flan3_6.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Flan3_6, 'tStartRefresh')  # time at next scr refresh
        Flan3_6.setAutoDraw(True)
    if Flan3_6.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > Flan3_6.tStartRefresh + 0.3-frameTolerance:
            # keep track of stop time/frame for later
            Flan3_6.tStop = t  # not accounting for scr refresh
            Flan3_6.frameNStop = frameN  # exact frame index
            win.timeOnFlip(Flan3_6, 'tStopRefresh')  # time at next scr refresh
            Flan3_6.setAutoDraw(False)
    
    # *Flan4_6* updates
    if Flan4_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Flan4_6.frameNStart = frameN  # exact frame index
        Flan4_6.tStart = t  # local t and not account for scr refresh
        Flan4_6.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Flan4_6, 'tStartRefresh')  # time at next scr refresh
        Flan4_6.setAutoDraw(True)
    if Flan4_6.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > Flan4_6.tStartRefresh + 0.3-frameTolerance:
            # keep track of stop time/frame for later
            Flan4_6.tStop = t  # not accounting for scr refresh
            Flan4_6.frameNStop = frameN  # exact frame index
            win.timeOnFlip(Flan4_6, 'tStopRefresh')  # time at next scr refresh
            Flan4_6.setAutoDraw(False)
    
    # *Flan5_6* updates
    if Flan5_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Flan5_6.frameNStart = frameN  # exact frame index
        Flan5_6.tStart = t  # local t and not account for scr refresh
        Flan5_6.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Flan5_6, 'tStartRefresh')  # time at next scr refresh
        Flan5_6.setAutoDraw(True)
    if Flan5_6.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > Flan5_6.tStartRefresh + 0.3-frameTolerance:
            # keep track of stop time/frame for later
            Flan5_6.tStop = t  # not accounting for scr refresh
            Flan5_6.frameNStop = frameN  # exact frame index
            win.timeOnFlip(Flan5_6, 'tStopRefresh')  # time at next scr refresh
            Flan5_6.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Stimulus_disp_tutorial_2Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Stimulus_disp_tutorial_2"-------
for thisComponent in Stimulus_disp_tutorial_2Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('Fixation_Point_6.started', Fixation_Point_6.tStartRefresh)
thisExp.addData('Fixation_Point_6.stopped', Fixation_Point_6.tStopRefresh)
thisExp.addData('Target_6.started', Target_6.tStartRefresh)
thisExp.addData('Target_6.stopped', Target_6.tStopRefresh)
thisExp.addData('Flan1_6.started', Flan1_6.tStartRefresh)
thisExp.addData('Flan1_6.stopped', Flan1_6.tStopRefresh)
thisExp.addData('Flan2_6.started', Flan2_6.tStartRefresh)
thisExp.addData('Flan2_6.stopped', Flan2_6.tStopRefresh)
thisExp.addData('Flan3_6.started', Flan3_6.tStartRefresh)
thisExp.addData('Flan3_6.stopped', Flan3_6.tStopRefresh)
thisExp.addData('Flan4_6.started', Flan4_6.tStartRefresh)
thisExp.addData('Flan4_6.stopped', Flan4_6.tStopRefresh)
thisExp.addData('Flan5_6.started', Flan5_6.tStartRefresh)
thisExp.addData('Flan5_6.stopped', Flan5_6.tStopRefresh)

# ------Prepare to start Routine "ISI_tutorial_2"-------
continueRoutine = True
routineTimer.add(0.900000)
# update component parameters for each repeat
ISI1_cross_3.setText('·')
win.setMouseVisible(False)

# keep track of which components have finished
ISI_tutorial_2Components = [ISI1_cross_3]
for thisComponent in ISI_tutorial_2Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
ISI_tutorial_2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "ISI_tutorial_2"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = ISI_tutorial_2Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=ISI_tutorial_2Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *ISI1_cross_3* updates
    if ISI1_cross_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        ISI1_cross_3.frameNStart = frameN  # exact frame index
        ISI1_cross_3.tStart = t  # local t and not account for scr refresh
        ISI1_cross_3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(ISI1_cross_3, 'tStartRefresh')  # time at next scr refresh
        ISI1_cross_3.setAutoDraw(True)
    if ISI1_cross_3.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > ISI1_cross_3.tStartRefresh + 0.9-frameTolerance:
            # keep track of stop time/frame for later
            ISI1_cross_3.tStop = t  # not accounting for scr refresh
            ISI1_cross_3.frameNStop = frameN  # exact frame index
            win.timeOnFlip(ISI1_cross_3, 'tStopRefresh')  # time at next scr refresh
            ISI1_cross_3.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in ISI_tutorial_2Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "ISI_tutorial_2"-------
for thisComponent in ISI_tutorial_2Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('ISI1_cross_3.started', ISI1_cross_3.tStartRefresh)
thisExp.addData('ISI1_cross_3.stopped', ISI1_cross_3.tStopRefresh)

# ------Prepare to start Routine "Loc_choice_tut_2"-------
continueRoutine = True
# update component parameters for each repeat
# setup some python lists for storing info about the mouse_11
mouse_11.clicked_name = []
gotValidClick = False  # until a click is received
win.setMouseVisible(True)

Target_7.setFillColor([0.6706, -0.2627, -1.0000])
Target_7.setPos((0.2,0.2))
Flan1_7.setFillColor([0.6000, -0.0510, 0.3098])
Flan1_7.setPos((-0.1,-0.1))
Flan2_7.setFillColor([-1.0000, -1.0000, -1.0000])
Flan2_7.setPos((0.1,-0.3))
Flan3_7.setFillColor('')
Flan3_7.setPos((2,2))
Flan4_7.setFillColor('')
Flan4_7.setPos((2,2))
Flan5_7.setFillColor('')
Flan5_7.setPos((2,2))
# keep track of which components have finished
Loc_choice_tut_2Components = [mouse_11, Fixation_Point_7, Target_7, Flan1_7, Flan2_7, Flan3_7, Flan4_7, Flan5_7, InstruText2_2]
for thisComponent in Loc_choice_tut_2Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
Loc_choice_tut_2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "Loc_choice_tut_2"-------
while continueRoutine:
    # get current time
    t = Loc_choice_tut_2Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=Loc_choice_tut_2Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    # *mouse_11* updates
    if mouse_11.status == NOT_STARTED and t >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        mouse_11.frameNStart = frameN  # exact frame index
        mouse_11.tStart = t  # local t and not account for scr refresh
        mouse_11.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(mouse_11, 'tStartRefresh')  # time at next scr refresh
        mouse_11.status = STARTED
        mouse_11.mouseClock.reset()
        prevButtonState = [0, 0, 0]  # if now button is down we will treat as 'new' click
    if mouse_11.status == STARTED:  # only update if started and not finished!
        buttons = mouse_11.getPressed()
        if buttons != prevButtonState:  # button state changed?
            prevButtonState = buttons
            if sum(buttons) > 0:  # state changed to a new click
                # check if the mouse was inside our 'clickable' objects
                gotValidClick = False
                try:
                    iter(Target_7)
                    clickableList = Target_7
                except:
                    clickableList = [Target_7]
                for obj in clickableList:
                    if obj.contains(mouse_11):
                        gotValidClick = True
                        mouse_11.clicked_name.append(obj.name)
                if gotValidClick:  # abort routine on response
                    continueRoutine = False
    if Target_7.contains(mouse):
        Target_7.lineColor = 'green'
    else:
        Target_7.lineColor = 'grey'
        
    if Flan1_7.contains(mouse):
        Flan1_7.lineColor = 'red'
    else:
        Flan1_7.lineColor = 'grey'
        
    if Flan2_7.contains(mouse):
        Flan2_7.lineColor = 'red'
    else:
        Flan2_7.lineColor = 'grey'
    
    # *Fixation_Point_7* updates
    if Fixation_Point_7.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Fixation_Point_7.frameNStart = frameN  # exact frame index
        Fixation_Point_7.tStart = t  # local t and not account for scr refresh
        Fixation_Point_7.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Fixation_Point_7, 'tStartRefresh')  # time at next scr refresh
        Fixation_Point_7.setAutoDraw(True)
    
    # *Target_7* updates
    if Target_7.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Target_7.frameNStart = frameN  # exact frame index
        Target_7.tStart = t  # local t and not account for scr refresh
        Target_7.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Target_7, 'tStartRefresh')  # time at next scr refresh
        Target_7.setAutoDraw(True)
    
    # *Flan1_7* updates
    if Flan1_7.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Flan1_7.frameNStart = frameN  # exact frame index
        Flan1_7.tStart = t  # local t and not account for scr refresh
        Flan1_7.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Flan1_7, 'tStartRefresh')  # time at next scr refresh
        Flan1_7.setAutoDraw(True)
    
    # *Flan2_7* updates
    if Flan2_7.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Flan2_7.frameNStart = frameN  # exact frame index
        Flan2_7.tStart = t  # local t and not account for scr refresh
        Flan2_7.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Flan2_7, 'tStartRefresh')  # time at next scr refresh
        Flan2_7.setAutoDraw(True)
    
    # *Flan3_7* updates
    if Flan3_7.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Flan3_7.frameNStart = frameN  # exact frame index
        Flan3_7.tStart = t  # local t and not account for scr refresh
        Flan3_7.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Flan3_7, 'tStartRefresh')  # time at next scr refresh
        Flan3_7.setAutoDraw(True)
    
    # *Flan4_7* updates
    if Flan4_7.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Flan4_7.frameNStart = frameN  # exact frame index
        Flan4_7.tStart = t  # local t and not account for scr refresh
        Flan4_7.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Flan4_7, 'tStartRefresh')  # time at next scr refresh
        Flan4_7.setAutoDraw(True)
    
    # *Flan5_7* updates
    if Flan5_7.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Flan5_7.frameNStart = frameN  # exact frame index
        Flan5_7.tStart = t  # local t and not account for scr refresh
        Flan5_7.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Flan5_7, 'tStartRefresh')  # time at next scr refresh
        Flan5_7.setAutoDraw(True)
    
    # *InstruText2_2* updates
    if InstruText2_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        InstruText2_2.frameNStart = frameN  # exact frame index
        InstruText2_2.tStart = t  # local t and not account for scr refresh
        InstruText2_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(InstruText2_2, 'tStartRefresh')  # time at next scr refresh
        InstruText2_2.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Loc_choice_tut_2Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Loc_choice_tut_2"-------
for thisComponent in Loc_choice_tut_2Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# store data for thisExp (ExperimentHandler)
x, y = mouse_11.getPos()
buttons = mouse_11.getPressed()
if sum(buttons):
    # check if the mouse was inside our 'clickable' objects
    gotValidClick = False
    try:
        iter(Target_7)
        clickableList = Target_7
    except:
        clickableList = [Target_7]
    for obj in clickableList:
        if obj.contains(mouse_11):
            gotValidClick = True
            mouse_11.clicked_name.append(obj.name)
thisExp.addData('mouse_11.x', x)
thisExp.addData('mouse_11.y', y)
thisExp.addData('mouse_11.leftButton', buttons[0])
thisExp.addData('mouse_11.midButton', buttons[1])
thisExp.addData('mouse_11.rightButton', buttons[2])
if len(mouse_11.clicked_name):
    thisExp.addData('mouse_11.clicked_name', mouse_11.clicked_name[0])
thisExp.addData('mouse_11.started', mouse_11.tStart)
thisExp.addData('mouse_11.stopped', mouse_11.tStop)
thisExp.nextEntry()
thisExp.addData('Fixation_Point_7.started', Fixation_Point_7.tStartRefresh)
thisExp.addData('Fixation_Point_7.stopped', Fixation_Point_7.tStopRefresh)
thisExp.addData('Target_7.started', Target_7.tStartRefresh)
thisExp.addData('Target_7.stopped', Target_7.tStopRefresh)
thisExp.addData('Flan1_7.started', Flan1_7.tStartRefresh)
thisExp.addData('Flan1_7.stopped', Flan1_7.tStopRefresh)
thisExp.addData('Flan2_7.started', Flan2_7.tStartRefresh)
thisExp.addData('Flan2_7.stopped', Flan2_7.tStopRefresh)
thisExp.addData('Flan3_7.started', Flan3_7.tStartRefresh)
thisExp.addData('Flan3_7.stopped', Flan3_7.tStopRefresh)
thisExp.addData('Flan4_7.started', Flan4_7.tStartRefresh)
thisExp.addData('Flan4_7.stopped', Flan4_7.tStopRefresh)
thisExp.addData('Flan5_7.started', Flan5_7.tStartRefresh)
thisExp.addData('Flan5_7.stopped', Flan5_7.tStopRefresh)
thisExp.addData('InstruText2_2.started', InstruText2_2.tStartRefresh)
thisExp.addData('InstruText2_2.stopped', InstruText2_2.tStopRefresh)
# the Routine "Loc_choice_tut_2" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "ISI_tutorial_2"-------
continueRoutine = True
routineTimer.add(0.900000)
# update component parameters for each repeat
ISI1_cross_3.setText('·')
win.setMouseVisible(False)

# keep track of which components have finished
ISI_tutorial_2Components = [ISI1_cross_3]
for thisComponent in ISI_tutorial_2Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
ISI_tutorial_2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "ISI_tutorial_2"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = ISI_tutorial_2Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=ISI_tutorial_2Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *ISI1_cross_3* updates
    if ISI1_cross_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        ISI1_cross_3.frameNStart = frameN  # exact frame index
        ISI1_cross_3.tStart = t  # local t and not account for scr refresh
        ISI1_cross_3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(ISI1_cross_3, 'tStartRefresh')  # time at next scr refresh
        ISI1_cross_3.setAutoDraw(True)
    if ISI1_cross_3.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > ISI1_cross_3.tStartRefresh + 0.9-frameTolerance:
            # keep track of stop time/frame for later
            ISI1_cross_3.tStop = t  # not accounting for scr refresh
            ISI1_cross_3.frameNStop = frameN  # exact frame index
            win.timeOnFlip(ISI1_cross_3, 'tStopRefresh')  # time at next scr refresh
            ISI1_cross_3.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in ISI_tutorial_2Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "ISI_tutorial_2"-------
for thisComponent in ISI_tutorial_2Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('ISI1_cross_3.started', ISI1_cross_3.tStartRefresh)
thisExp.addData('ISI1_cross_3.stopped', ISI1_cross_3.tStopRefresh)

# ------Prepare to start Routine "Choice_tutorial_2"-------
continueRoutine = True
# update component parameters for each repeat
win.setMouseVisible(True)


wedgeYellow.setAutoDraw(True)
wedgeWhite.setAutoDraw(True)
wedgeVermilion.setAutoDraw(True)
wedgeRedPurple.setAutoDraw(True)

wedgeBlack.setAutoDraw(True)
wedgeIndigo.setAutoDraw(True)
wedgeSkyBlue.setAutoDraw(True)
wedgeBlueGreen.setAutoDraw(True)

GreyCircle.setAutoDraw(True)

# setup some python lists for storing info about the mouse_12
mouse_12.clicked_name = []
gotValidClick = False  # until a click is received
# keep track of which components have finished
Choice_tutorial_2Components = [mouse_12, InstruText_2]
for thisComponent in Choice_tutorial_2Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
Choice_tutorial_2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "Choice_tutorial_2"-------
while continueRoutine:
    # get current time
    t = Choice_tutorial_2Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=Choice_tutorial_2Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    if (wedgeYellow.contains(mouse)):
        wedgeYellow.lineColor = 'red'
        GuideYellow.setAutoDraw(True)
    else:
        wedgeYellow.lineColor = 'grey'
        GuideYellow.setAutoDraw(False)
    
    if wedgeWhite.contains(mouse):
        wedgeWhite.lineColor = 'red'
        GuideWhite.setAutoDraw(True)
    else:
        wedgeWhite.lineColor = 'grey'
        GuideWhite.setAutoDraw(False)
        
    if wedgeVermilion.contains(mouse):
        wedgeVermilion.lineColor = 'red'
        GuideVermilion.setAutoDraw(True)
    else:
        wedgeVermilion.lineColor = 'grey'
        GuideVermilion.setAutoDraw(False)
        
    if wedgeRedPurple.contains(mouse):
        wedgeRedPurple.lineColor = 'red'
        GuideRedPurple.setAutoDraw(True)
    else:
        wedgeRedPurple.lineColor = 'grey'
        GuideRedPurple.setAutoDraw(False)
        
    if wedgeBlack.contains(mouse):
        wedgeBlack.lineColor = 'red'
        GuideBlack.setAutoDraw(True)
    else:
        wedgeBlack.lineColor = 'grey'
        GuideBlack.setAutoDraw(False)
        
    if wedgeIndigo.contains(mouse):
        wedgeIndigo.lineColor = 'red'
        GuideIndigo.setAutoDraw(True)
    else:
        wedgeIndigo.lineColor = 'grey'
        GuideIndigo.setAutoDraw(False)
        
    if wedgeSkyBlue.contains(mouse):
        wedgeSkyBlue.lineColor = 'green'
        GuideSkyBlue.setAutoDraw(True)
    else:
        wedgeSkyBlue.lineColor = 'grey'
        GuideSkyBlue.setAutoDraw(False)
        
    if wedgeBlueGreen.contains(mouse):
        wedgeBlueGreen.lineColor = 'red'
        GuideBlueGreen.setAutoDraw(True)
    else:
        wedgeBlueGreen.lineColor = 'grey'
        GuideBlueGreen.setAutoDraw(False)
    # *mouse_12* updates
    if mouse_12.status == NOT_STARTED and t >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        mouse_12.frameNStart = frameN  # exact frame index
        mouse_12.tStart = t  # local t and not account for scr refresh
        mouse_12.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(mouse_12, 'tStartRefresh')  # time at next scr refresh
        mouse_12.status = STARTED
        mouse_12.mouseClock.reset()
        prevButtonState = [0, 0, 0]  # if now button is down we will treat as 'new' click
    if mouse_12.status == STARTED:  # only update if started and not finished!
        buttons = mouse_12.getPressed()
        if buttons != prevButtonState:  # button state changed?
            prevButtonState = buttons
            if sum(buttons) > 0:  # state changed to a new click
                # check if the mouse was inside our 'clickable' objects
                gotValidClick = False
                try:
                    iter(wedgeSkyBlue)
                    clickableList = wedgeSkyBlue
                except:
                    clickableList = [wedgeSkyBlue]
                for obj in clickableList:
                    if obj.contains(mouse_12):
                        gotValidClick = True
                        mouse_12.clicked_name.append(obj.name)
                if gotValidClick:  # abort routine on response
                    continueRoutine = False
    
    # *InstruText_2* updates
    if InstruText_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        InstruText_2.frameNStart = frameN  # exact frame index
        InstruText_2.tStart = t  # local t and not account for scr refresh
        InstruText_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(InstruText_2, 'tStartRefresh')  # time at next scr refresh
        InstruText_2.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Choice_tutorial_2Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Choice_tutorial_2"-------
for thisComponent in Choice_tutorial_2Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# store data for thisExp (ExperimentHandler)
x, y = mouse_12.getPos()
buttons = mouse_12.getPressed()
if sum(buttons):
    # check if the mouse was inside our 'clickable' objects
    gotValidClick = False
    try:
        iter(wedgeSkyBlue)
        clickableList = wedgeSkyBlue
    except:
        clickableList = [wedgeSkyBlue]
    for obj in clickableList:
        if obj.contains(mouse_12):
            gotValidClick = True
            mouse_12.clicked_name.append(obj.name)
thisExp.addData('mouse_12.x', x)
thisExp.addData('mouse_12.y', y)
thisExp.addData('mouse_12.leftButton', buttons[0])
thisExp.addData('mouse_12.midButton', buttons[1])
thisExp.addData('mouse_12.rightButton', buttons[2])
if len(mouse_12.clicked_name):
    thisExp.addData('mouse_12.clicked_name', mouse_12.clicked_name[0])
thisExp.addData('mouse_12.started', mouse_12.tStart)
thisExp.addData('mouse_12.stopped', mouse_12.tStop)
thisExp.nextEntry()
thisExp.addData('InstruText_2.started', InstruText_2.tStartRefresh)
thisExp.addData('InstruText_2.stopped', InstruText_2.tStopRefresh)
# the Routine "Choice_tutorial_2" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "Clear_sc_tut"-------
continueRoutine = True
# update component parameters for each repeat
win.setMouseVisible(False)

GreyCircle.setAutoDraw(False)

wedgeYellow.setAutoDraw(False)
wedgeWhite.setAutoDraw(False)
wedgeVermilion.setAutoDraw(False)
wedgeRedPurple.setAutoDraw(False)

wedgeBlack.setAutoDraw(False)
wedgeIndigo.setAutoDraw(False)
wedgeSkyBlue.setAutoDraw(False)
wedgeBlueGreen.setAutoDraw(False)

GuideYellow.setAutoDraw(False)
GuideWhite.setAutoDraw(False)
GuideVermilion.setAutoDraw(False)
GuideRedPurple.setAutoDraw(False)

GuideBlack.setAutoDraw(False)
GuideIndigo.setAutoDraw(False)
GuideSkyBlue.setAutoDraw(False)
GuideBlueGreen.setAutoDraw(False)
# keep track of which components have finished
Clear_sc_tutComponents = []
for thisComponent in Clear_sc_tutComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
Clear_sc_tutClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "Clear_sc_tut"-------
while continueRoutine:
    # get current time
    t = Clear_sc_tutClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=Clear_sc_tutClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Clear_sc_tutComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Clear_sc_tut"-------
for thisComponent in Clear_sc_tutComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "Clear_sc_tut" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "Tutorial_end"-------
continueRoutine = True
# update component parameters for each repeat
NumberOBlocks_7.setText('Well done! You have completed the tutorial.\n\nYou may now begin the main task.\n')
win.setMouseVisible(True)
# setup some python lists for storing info about the mouse_10
mouse_10.clicked_name = []
gotValidClick = False  # until a click is received
# keep track of which components have finished
Tutorial_endComponents = [NumberOBlocks_7, ContinueButtonText_5, ContinueButton_5, mouse_10]
for thisComponent in Tutorial_endComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
Tutorial_endClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "Tutorial_end"-------
while continueRoutine:
    # get current time
    t = Tutorial_endClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=Tutorial_endClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *NumberOBlocks_7* updates
    if NumberOBlocks_7.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        NumberOBlocks_7.frameNStart = frameN  # exact frame index
        NumberOBlocks_7.tStart = t  # local t and not account for scr refresh
        NumberOBlocks_7.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(NumberOBlocks_7, 'tStartRefresh')  # time at next scr refresh
        NumberOBlocks_7.setAutoDraw(True)
    
    # *ContinueButtonText_5* updates
    if ContinueButtonText_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        ContinueButtonText_5.frameNStart = frameN  # exact frame index
        ContinueButtonText_5.tStart = t  # local t and not account for scr refresh
        ContinueButtonText_5.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(ContinueButtonText_5, 'tStartRefresh')  # time at next scr refresh
        ContinueButtonText_5.setAutoDraw(True)
    if ContinueButtonText_5.status == STARTED:  # only update if drawing
        ContinueButtonText_5.setColor('white', colorSpace='rgb', log=False)
    
    # *ContinueButton_5* updates
    if ContinueButton_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        ContinueButton_5.frameNStart = frameN  # exact frame index
        ContinueButton_5.tStart = t  # local t and not account for scr refresh
        ContinueButton_5.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(ContinueButton_5, 'tStartRefresh')  # time at next scr refresh
        ContinueButton_5.setAutoDraw(True)
    if ContinueButton_5.status == STARTED:  # only update if drawing
        ContinueButton_5.setLineColor('white', log=False)
    if ContinueButton_5.contains(mouse):
        ContinueButton_5.lineColor = 'yellow'
        ContinueButtonText_5.color = 'yellow'
    else:
        ContinueButton_5.lineColor = 'white'
        ContinueButtonText_5.color = 'white'
    # *mouse_10* updates
    if mouse_10.status == NOT_STARTED and t >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        mouse_10.frameNStart = frameN  # exact frame index
        mouse_10.tStart = t  # local t and not account for scr refresh
        mouse_10.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(mouse_10, 'tStartRefresh')  # time at next scr refresh
        mouse_10.status = STARTED
        mouse_10.mouseClock.reset()
        prevButtonState = mouse_10.getPressed()  # if button is down already this ISN'T a new click
    if mouse_10.status == STARTED:  # only update if started and not finished!
        buttons = mouse_10.getPressed()
        if buttons != prevButtonState:  # button state changed?
            prevButtonState = buttons
            if sum(buttons) > 0:  # state changed to a new click
                # check if the mouse was inside our 'clickable' objects
                gotValidClick = False
                try:
                    iter(ContinueButton)
                    clickableList = ContinueButton
                except:
                    clickableList = [ContinueButton]
                for obj in clickableList:
                    if obj.contains(mouse_10):
                        gotValidClick = True
                        mouse_10.clicked_name.append(obj.name)
                if gotValidClick:  # abort routine on response
                    continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Tutorial_endComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Tutorial_end"-------
for thisComponent in Tutorial_endComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('NumberOBlocks_7.started', NumberOBlocks_7.tStartRefresh)
thisExp.addData('NumberOBlocks_7.stopped', NumberOBlocks_7.tStopRefresh)
thisExp.addData('ContinueButtonText_5.started', ContinueButtonText_5.tStartRefresh)
thisExp.addData('ContinueButtonText_5.stopped', ContinueButtonText_5.tStopRefresh)
thisExp.addData('ContinueButton_5.started', ContinueButton_5.tStartRefresh)
thisExp.addData('ContinueButton_5.stopped', ContinueButton_5.tStopRefresh)
# store data for thisExp (ExperimentHandler)
x, y = mouse_10.getPos()
buttons = mouse_10.getPressed()
if sum(buttons):
    # check if the mouse was inside our 'clickable' objects
    gotValidClick = False
    try:
        iter(ContinueButton)
        clickableList = ContinueButton
    except:
        clickableList = [ContinueButton]
    for obj in clickableList:
        if obj.contains(mouse_10):
            gotValidClick = True
            mouse_10.clicked_name.append(obj.name)
thisExp.addData('mouse_10.x', x)
thisExp.addData('mouse_10.y', y)
thisExp.addData('mouse_10.leftButton', buttons[0])
thisExp.addData('mouse_10.midButton', buttons[1])
thisExp.addData('mouse_10.rightButton', buttons[2])
if len(mouse_10.clicked_name):
    thisExp.addData('mouse_10.clicked_name', mouse_10.clicked_name[0])
thisExp.addData('mouse_10.started', mouse_10.tStart)
thisExp.addData('mouse_10.stopped', mouse_10.tStop)
thisExp.nextEntry()
# the Routine "Tutorial_end" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "break_3"-------
continueRoutine = True
routineTimer.add(1.000000)
# update component parameters for each repeat
# keep track of which components have finished
break_3Components = [text_3]
for thisComponent in break_3Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
break_3Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "break_3"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = break_3Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=break_3Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_3* updates
    if text_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_3.frameNStart = frameN  # exact frame index
        text_3.tStart = t  # local t and not account for scr refresh
        text_3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_3, 'tStartRefresh')  # time at next scr refresh
        text_3.setAutoDraw(True)
    if text_3.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text_3.tStartRefresh + 1.0-frameTolerance:
            # keep track of stop time/frame for later
            text_3.tStop = t  # not accounting for scr refresh
            text_3.frameNStop = frameN  # exact frame index
            win.timeOnFlip(text_3, 'tStopRefresh')  # time at next scr refresh
            text_3.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in break_3Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "break_3"-------
for thisComponent in break_3Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_3.started', text_3.tStartRefresh)
thisExp.addData('text_3.stopped', text_3.tStopRefresh)

# set up handler to look after randomisation of conditions etc
MasterTrialLoop = data.TrialHandler(nReps=1.0, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('Conditions/CCDT_master.xlsx'),
    seed=None, name='MasterTrialLoop')
thisExp.addLoop(MasterTrialLoop)  # add the loop to the experiment
thisMasterTrialLoop = MasterTrialLoop.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisMasterTrialLoop.rgb)
if thisMasterTrialLoop != None:
    for paramName in thisMasterTrialLoop:
        exec('{} = thisMasterTrialLoop[paramName]'.format(paramName))

for thisMasterTrialLoop in MasterTrialLoop:
    currentLoop = MasterTrialLoop
    # abbreviate parameter names if possible (e.g. rgb = thisMasterTrialLoop.rgb)
    if thisMasterTrialLoop != None:
        for paramName in thisMasterTrialLoop:
            exec('{} = thisMasterTrialLoop[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "MainInstructions"-------
    continueRoutine = True
    # update component parameters for each repeat
    Ins = ("Task block: " + str(BlockNo) + " of 4")
    win.setMouseVisible(True)
    NumberOBlocks_2.setText(Ins)
    InstructionsMainText.setText(Instructions)
    NumberOBlocks.setText(Ins)
    # setup some python lists for storing info about the mouse_3
    mouse_3.clicked_name = []
    gotValidClick = False  # until a click is received
    # keep track of which components have finished
    MainInstructionsComponents = [NumberOBlocks_2, InstructionsMainText, NumberOBlocks, ContinueButtonText, ContinueButton, mouse_3]
    for thisComponent in MainInstructionsComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    MainInstructionsClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "MainInstructions"-------
    while continueRoutine:
        # get current time
        t = MainInstructionsClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=MainInstructionsClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *NumberOBlocks_2* updates
        if NumberOBlocks_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            NumberOBlocks_2.frameNStart = frameN  # exact frame index
            NumberOBlocks_2.tStart = t  # local t and not account for scr refresh
            NumberOBlocks_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(NumberOBlocks_2, 'tStartRefresh')  # time at next scr refresh
            NumberOBlocks_2.setAutoDraw(True)
        
        # *InstructionsMainText* updates
        if InstructionsMainText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            InstructionsMainText.frameNStart = frameN  # exact frame index
            InstructionsMainText.tStart = t  # local t and not account for scr refresh
            InstructionsMainText.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(InstructionsMainText, 'tStartRefresh')  # time at next scr refresh
            InstructionsMainText.setAutoDraw(True)
        
        # *NumberOBlocks* updates
        if NumberOBlocks.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            NumberOBlocks.frameNStart = frameN  # exact frame index
            NumberOBlocks.tStart = t  # local t and not account for scr refresh
            NumberOBlocks.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(NumberOBlocks, 'tStartRefresh')  # time at next scr refresh
            NumberOBlocks.setAutoDraw(True)
        
        # *ContinueButtonText* updates
        if ContinueButtonText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            ContinueButtonText.frameNStart = frameN  # exact frame index
            ContinueButtonText.tStart = t  # local t and not account for scr refresh
            ContinueButtonText.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(ContinueButtonText, 'tStartRefresh')  # time at next scr refresh
            ContinueButtonText.setAutoDraw(True)
        if ContinueButtonText.status == STARTED:  # only update if drawing
            ContinueButtonText.setColor('white', colorSpace='rgb', log=False)
        
        # *ContinueButton* updates
        if ContinueButton.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            ContinueButton.frameNStart = frameN  # exact frame index
            ContinueButton.tStart = t  # local t and not account for scr refresh
            ContinueButton.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(ContinueButton, 'tStartRefresh')  # time at next scr refresh
            ContinueButton.setAutoDraw(True)
        if ContinueButton.status == STARTED:  # only update if drawing
            ContinueButton.setLineColor('white', log=False)
        if ContinueButton.contains(mouse):
            ContinueButton.lineColor = 'yellow'
            ContinueButtonText.color = 'yellow'
        else:
            ContinueButton.lineColor = 'white'
            ContinueButtonText.color = 'white'
        # *mouse_3* updates
        if mouse_3.status == NOT_STARTED and t >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            mouse_3.frameNStart = frameN  # exact frame index
            mouse_3.tStart = t  # local t and not account for scr refresh
            mouse_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(mouse_3, 'tStartRefresh')  # time at next scr refresh
            mouse_3.status = STARTED
            mouse_3.mouseClock.reset()
            prevButtonState = mouse_3.getPressed()  # if button is down already this ISN'T a new click
        if mouse_3.status == STARTED:  # only update if started and not finished!
            buttons = mouse_3.getPressed()
            if buttons != prevButtonState:  # button state changed?
                prevButtonState = buttons
                if sum(buttons) > 0:  # state changed to a new click
                    # check if the mouse was inside our 'clickable' objects
                    gotValidClick = False
                    try:
                        iter(ContinueButton)
                        clickableList = ContinueButton
                    except:
                        clickableList = [ContinueButton]
                    for obj in clickableList:
                        if obj.contains(mouse_3):
                            gotValidClick = True
                            mouse_3.clicked_name.append(obj.name)
                    if gotValidClick:  # abort routine on response
                        continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in MainInstructionsComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "MainInstructions"-------
    for thisComponent in MainInstructionsComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    MasterTrialLoop.addData('NumberOBlocks_2.started', NumberOBlocks_2.tStartRefresh)
    MasterTrialLoop.addData('NumberOBlocks_2.stopped', NumberOBlocks_2.tStopRefresh)
    MasterTrialLoop.addData('InstructionsMainText.started', InstructionsMainText.tStartRefresh)
    MasterTrialLoop.addData('InstructionsMainText.stopped', InstructionsMainText.tStopRefresh)
    MasterTrialLoop.addData('NumberOBlocks.started', NumberOBlocks.tStartRefresh)
    MasterTrialLoop.addData('NumberOBlocks.stopped', NumberOBlocks.tStopRefresh)
    MasterTrialLoop.addData('ContinueButtonText.started', ContinueButtonText.tStartRefresh)
    MasterTrialLoop.addData('ContinueButtonText.stopped', ContinueButtonText.tStopRefresh)
    MasterTrialLoop.addData('ContinueButton.started', ContinueButton.tStartRefresh)
    MasterTrialLoop.addData('ContinueButton.stopped', ContinueButton.tStopRefresh)
    # store data for MasterTrialLoop (TrialHandler)
    x, y = mouse_3.getPos()
    buttons = mouse_3.getPressed()
    if sum(buttons):
        # check if the mouse was inside our 'clickable' objects
        gotValidClick = False
        try:
            iter(ContinueButton)
            clickableList = ContinueButton
        except:
            clickableList = [ContinueButton]
        for obj in clickableList:
            if obj.contains(mouse_3):
                gotValidClick = True
                mouse_3.clicked_name.append(obj.name)
    MasterTrialLoop.addData('mouse_3.x', x)
    MasterTrialLoop.addData('mouse_3.y', y)
    MasterTrialLoop.addData('mouse_3.leftButton', buttons[0])
    MasterTrialLoop.addData('mouse_3.midButton', buttons[1])
    MasterTrialLoop.addData('mouse_3.rightButton', buttons[2])
    if len(mouse_3.clicked_name):
        MasterTrialLoop.addData('mouse_3.clicked_name', mouse_3.clicked_name[0])
    MasterTrialLoop.addData('mouse_3.started', mouse_3.tStart)
    MasterTrialLoop.addData('mouse_3.stopped', mouse_3.tStop)
    # the Routine "MainInstructions" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "Time_gap"-------
    continueRoutine = True
    routineTimer.add(2.000000)
    # update component parameters for each repeat
    win.setMouseVisible(False)
    
    # keep track of which components have finished
    Time_gapComponents = [Focus]
    for thisComponent in Time_gapComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    Time_gapClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "Time_gap"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = Time_gapClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=Time_gapClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *Focus* updates
        if Focus.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Focus.frameNStart = frameN  # exact frame index
            Focus.tStart = t  # local t and not account for scr refresh
            Focus.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Focus, 'tStartRefresh')  # time at next scr refresh
            Focus.setAutoDraw(True)
        if Focus.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Focus.tStartRefresh + 2-frameTolerance:
                # keep track of stop time/frame for later
                Focus.tStop = t  # not accounting for scr refresh
                Focus.frameNStop = frameN  # exact frame index
                win.timeOnFlip(Focus, 'tStopRefresh')  # time at next scr refresh
                Focus.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Time_gapComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Time_gap"-------
    for thisComponent in Time_gapComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    MasterTrialLoop.addData('Focus.started', Focus.tStartRefresh)
    MasterTrialLoop.addData('Focus.stopped', Focus.tStopRefresh)
    
    # set up handler to look after randomisation of conditions etc
    MainTrialLoop = data.TrialHandler(nReps=1.0, method='sequential', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions(CondFile),
        seed=None, name='MainTrialLoop')
    thisExp.addLoop(MainTrialLoop)  # add the loop to the experiment
    thisMainTrialLoop = MainTrialLoop.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisMainTrialLoop.rgb)
    if thisMainTrialLoop != None:
        for paramName in thisMainTrialLoop:
            exec('{} = thisMainTrialLoop[paramName]'.format(paramName))
    
    for thisMainTrialLoop in MainTrialLoop:
        currentLoop = MainTrialLoop
        # abbreviate parameter names if possible (e.g. rgb = thisMainTrialLoop.rgb)
        if thisMainTrialLoop != None:
            for paramName in thisMainTrialLoop:
                exec('{} = thisMainTrialLoop[paramName]'.format(paramName))
        
        # ------Prepare to start Routine "ISI"-------
        continueRoutine = True
        # update component parameters for each repeat
        ISI1_cross.setText('·')
        win.setMouseVisible(False)
        
        # keep track of which components have finished
        ISIComponents = [ISI1_cross]
        for thisComponent in ISIComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        ISIClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "ISI"-------
        while continueRoutine:
            # get current time
            t = ISIClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=ISIClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *ISI1_cross* updates
            if ISI1_cross.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                ISI1_cross.frameNStart = frameN  # exact frame index
                ISI1_cross.tStart = t  # local t and not account for scr refresh
                ISI1_cross.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(ISI1_cross, 'tStartRefresh')  # time at next scr refresh
                ISI1_cross.setAutoDraw(True)
            if ISI1_cross.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > ISI1_cross.tStartRefresh + ISI_1_jitter-frameTolerance:
                    # keep track of stop time/frame for later
                    ISI1_cross.tStop = t  # not accounting for scr refresh
                    ISI1_cross.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(ISI1_cross, 'tStopRefresh')  # time at next scr refresh
                    ISI1_cross.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in ISIComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "ISI"-------
        for thisComponent in ISIComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        MainTrialLoop.addData('ISI1_cross.started', ISI1_cross.tStartRefresh)
        MainTrialLoop.addData('ISI1_cross.stopped', ISI1_cross.tStopRefresh)
        # the Routine "ISI" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # ------Prepare to start Routine "Stimulus_display"-------
        continueRoutine = True
        routineTimer.add(0.325000)
        # update component parameters for each repeat
        Target.setFillColor(Targ_Colour)
        Target.setPos(Targ_Loc)
        Flan1.setFillColor(Flan1_Colour)
        Flan1.setPos(Flan1_Loc)
        Flan2.setFillColor(Flan2_Colour)
        Flan2.setPos(Flan2_Loc)
        Flan3.setFillColor(Flan3_Colour)
        Flan3.setPos(Flan3_Loc)
        Flan4.setFillColor(Flan4_Colour)
        Flan4.setPos(Flan4_Loc)
        Flan5.setFillColor(Flan5_Colour)
        Flan5.setPos(Flan5_Loc)
        # keep track of which components have finished
        Stimulus_displayComponents = [Fixation_Point, Target, Flan1, Flan2, Flan3, Flan4, Flan5]
        for thisComponent in Stimulus_displayComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        Stimulus_displayClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "Stimulus_display"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = Stimulus_displayClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=Stimulus_displayClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *Fixation_Point* updates
            if Fixation_Point.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                Fixation_Point.frameNStart = frameN  # exact frame index
                Fixation_Point.tStart = t  # local t and not account for scr refresh
                Fixation_Point.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(Fixation_Point, 'tStartRefresh')  # time at next scr refresh
                Fixation_Point.setAutoDraw(True)
            if Fixation_Point.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > Fixation_Point.tStartRefresh + 0.325-frameTolerance:
                    # keep track of stop time/frame for later
                    Fixation_Point.tStop = t  # not accounting for scr refresh
                    Fixation_Point.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(Fixation_Point, 'tStopRefresh')  # time at next scr refresh
                    Fixation_Point.setAutoDraw(False)
            
            # *Target* updates
            if Target.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                Target.frameNStart = frameN  # exact frame index
                Target.tStart = t  # local t and not account for scr refresh
                Target.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(Target, 'tStartRefresh')  # time at next scr refresh
                Target.setAutoDraw(True)
            if Target.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > Target.tStartRefresh + 0.325-frameTolerance:
                    # keep track of stop time/frame for later
                    Target.tStop = t  # not accounting for scr refresh
                    Target.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(Target, 'tStopRefresh')  # time at next scr refresh
                    Target.setAutoDraw(False)
            
            # *Flan1* updates
            if Flan1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                Flan1.frameNStart = frameN  # exact frame index
                Flan1.tStart = t  # local t and not account for scr refresh
                Flan1.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(Flan1, 'tStartRefresh')  # time at next scr refresh
                Flan1.setAutoDraw(True)
            if Flan1.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > Flan1.tStartRefresh + 0.325-frameTolerance:
                    # keep track of stop time/frame for later
                    Flan1.tStop = t  # not accounting for scr refresh
                    Flan1.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(Flan1, 'tStopRefresh')  # time at next scr refresh
                    Flan1.setAutoDraw(False)
            
            # *Flan2* updates
            if Flan2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                Flan2.frameNStart = frameN  # exact frame index
                Flan2.tStart = t  # local t and not account for scr refresh
                Flan2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(Flan2, 'tStartRefresh')  # time at next scr refresh
                Flan2.setAutoDraw(True)
            if Flan2.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > Flan2.tStartRefresh + 0.325-frameTolerance:
                    # keep track of stop time/frame for later
                    Flan2.tStop = t  # not accounting for scr refresh
                    Flan2.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(Flan2, 'tStopRefresh')  # time at next scr refresh
                    Flan2.setAutoDraw(False)
            
            # *Flan3* updates
            if Flan3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                Flan3.frameNStart = frameN  # exact frame index
                Flan3.tStart = t  # local t and not account for scr refresh
                Flan3.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(Flan3, 'tStartRefresh')  # time at next scr refresh
                Flan3.setAutoDraw(True)
            if Flan3.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > Flan3.tStartRefresh + 0.325-frameTolerance:
                    # keep track of stop time/frame for later
                    Flan3.tStop = t  # not accounting for scr refresh
                    Flan3.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(Flan3, 'tStopRefresh')  # time at next scr refresh
                    Flan3.setAutoDraw(False)
            
            # *Flan4* updates
            if Flan4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                Flan4.frameNStart = frameN  # exact frame index
                Flan4.tStart = t  # local t and not account for scr refresh
                Flan4.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(Flan4, 'tStartRefresh')  # time at next scr refresh
                Flan4.setAutoDraw(True)
            if Flan4.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > Flan4.tStartRefresh + 0.325-frameTolerance:
                    # keep track of stop time/frame for later
                    Flan4.tStop = t  # not accounting for scr refresh
                    Flan4.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(Flan4, 'tStopRefresh')  # time at next scr refresh
                    Flan4.setAutoDraw(False)
            
            # *Flan5* updates
            if Flan5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                Flan5.frameNStart = frameN  # exact frame index
                Flan5.tStart = t  # local t and not account for scr refresh
                Flan5.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(Flan5, 'tStartRefresh')  # time at next scr refresh
                Flan5.setAutoDraw(True)
            if Flan5.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > Flan5.tStartRefresh + 0.325-frameTolerance:
                    # keep track of stop time/frame for later
                    Flan5.tStop = t  # not accounting for scr refresh
                    Flan5.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(Flan5, 'tStopRefresh')  # time at next scr refresh
                    Flan5.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in Stimulus_displayComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "Stimulus_display"-------
        for thisComponent in Stimulus_displayComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        MainTrialLoop.addData('Fixation_Point.started', Fixation_Point.tStartRefresh)
        MainTrialLoop.addData('Fixation_Point.stopped', Fixation_Point.tStopRefresh)
        MainTrialLoop.addData('Target.started', Target.tStartRefresh)
        MainTrialLoop.addData('Target.stopped', Target.tStopRefresh)
        MainTrialLoop.addData('Flan1.started', Flan1.tStartRefresh)
        MainTrialLoop.addData('Flan1.stopped', Flan1.tStopRefresh)
        MainTrialLoop.addData('Flan2.started', Flan2.tStartRefresh)
        MainTrialLoop.addData('Flan2.stopped', Flan2.tStopRefresh)
        MainTrialLoop.addData('Flan3.started', Flan3.tStartRefresh)
        MainTrialLoop.addData('Flan3.stopped', Flan3.tStopRefresh)
        MainTrialLoop.addData('Flan4.started', Flan4.tStartRefresh)
        MainTrialLoop.addData('Flan4.stopped', Flan4.tStopRefresh)
        MainTrialLoop.addData('Flan5.started', Flan5.tStartRefresh)
        MainTrialLoop.addData('Flan5.stopped', Flan5.tStopRefresh)
        
        # ------Prepare to start Routine "ISI2"-------
        continueRoutine = True
        # update component parameters for each repeat
        ISI2_cross.setText('·')
        # keep track of which components have finished
        ISI2Components = [ISI2_cross]
        for thisComponent in ISI2Components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        ISI2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "ISI2"-------
        while continueRoutine:
            # get current time
            t = ISI2Clock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=ISI2Clock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *ISI2_cross* updates
            if ISI2_cross.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                ISI2_cross.frameNStart = frameN  # exact frame index
                ISI2_cross.tStart = t  # local t and not account for scr refresh
                ISI2_cross.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(ISI2_cross, 'tStartRefresh')  # time at next scr refresh
                ISI2_cross.setAutoDraw(True)
            if ISI2_cross.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > ISI2_cross.tStartRefresh + ISI_2_jitter-frameTolerance:
                    # keep track of stop time/frame for later
                    ISI2_cross.tStop = t  # not accounting for scr refresh
                    ISI2_cross.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(ISI2_cross, 'tStopRefresh')  # time at next scr refresh
                    ISI2_cross.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in ISI2Components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "ISI2"-------
        for thisComponent in ISI2Components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        MainTrialLoop.addData('ISI2_cross.started', ISI2_cross.tStartRefresh)
        MainTrialLoop.addData('ISI2_cross.stopped', ISI2_cross.tStopRefresh)
        time_PreLocalisationEnd = globalClock.getTime()
        
        thisExp.addData('time_PreLocalisationEnd', time_PreLocalisationEnd)
        # the Routine "ISI2" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # ------Prepare to start Routine "Location_choice"-------
        continueRoutine = True
        # update component parameters for each repeat
        # setup some python lists for storing info about the mouse
        mouse.clicked_name = []
        gotValidClick = False  # until a click is received
        win.setMouseVisible(True)
        time_LocalisationBegin = globalClock.getTime()
        
        Target_2.setFillColor(Change_colour)
        Target_2.setPos(Targ_Loc)
        Flan1_2.setFillColor(Flan1_Colour)
        Flan1_2.setPos(Flan1_Loc)
        Flan2_2.setFillColor(Flan2_Colour)
        Flan2_2.setPos(Flan2_Loc)
        Flan3_2.setFillColor(Flan3_Colour)
        Flan3_2.setPos(Flan3_Loc)
        Flan4_2.setFillColor(Flan4_Colour)
        Flan4_2.setPos(Flan4_Loc)
        Flan5_2.setFillColor(Flan5_Colour)
        Flan5_2.setPos(Flan5_Loc)
        # keep track of which components have finished
        Location_choiceComponents = [mouse, Fixation_Point_2, Target_2, Flan1_2, Flan2_2, Flan3_2, Flan4_2, Flan5_2]
        for thisComponent in Location_choiceComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        Location_choiceClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "Location_choice"-------
        while continueRoutine:
            # get current time
            t = Location_choiceClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=Location_choiceClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            # *mouse* updates
            if mouse.status == NOT_STARTED and t >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                mouse.frameNStart = frameN  # exact frame index
                mouse.tStart = t  # local t and not account for scr refresh
                mouse.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(mouse, 'tStartRefresh')  # time at next scr refresh
                mouse.status = STARTED
                mouse.mouseClock.reset()
                prevButtonState = [0, 0, 0]  # if now button is down we will treat as 'new' click
            if mouse.status == STARTED:  # only update if started and not finished!
                buttons = mouse.getPressed()
                if buttons != prevButtonState:  # button state changed?
                    prevButtonState = buttons
                    if sum(buttons) > 0:  # state changed to a new click
                        # check if the mouse was inside our 'clickable' objects
                        gotValidClick = False
                        try:
                            iter([Target_2, Flan1_2, Flan2_2, Flan3_2, Flan4_2, Flan5_2])
                            clickableList = [Target_2, Flan1_2, Flan2_2, Flan3_2, Flan4_2, Flan5_2]
                        except:
                            clickableList = [[Target_2, Flan1_2, Flan2_2, Flan3_2, Flan4_2, Flan5_2]]
                        for obj in clickableList:
                            if obj.contains(mouse):
                                gotValidClick = True
                                mouse.clicked_name.append(obj.name)
                        if gotValidClick:  # abort routine on response
                            continueRoutine = False
            if Target_2.contains(mouse):
                Target_2.lineColor = 'white'
            else:
                Target_2.lineColor = 'grey'
                
            if Flan1_2.contains(mouse):
                Flan1_2.lineColor = 'white'
            else:
                Flan1_2.lineColor = 'grey'
                
            if Flan2_2.contains(mouse):
                Flan2_2.lineColor = 'white'
            else:
                Flan2_2.lineColor = 'grey'
                
            if Flan3_2.contains(mouse):
                Flan3_2.lineColor = 'white'
            else:
                Flan3_2.lineColor = 'grey'
                
            if Flan4_2.contains(mouse):
                Flan4_2.lineColor = 'white'
            else:
                Flan4_2.lineColor = 'grey'
                
            if Flan5_2.contains(mouse):
                Flan5_2.lineColor = 'white'
            else:
                Flan5_2.lineColor = 'grey'
            
            # *Fixation_Point_2* updates
            if Fixation_Point_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                Fixation_Point_2.frameNStart = frameN  # exact frame index
                Fixation_Point_2.tStart = t  # local t and not account for scr refresh
                Fixation_Point_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(Fixation_Point_2, 'tStartRefresh')  # time at next scr refresh
                Fixation_Point_2.setAutoDraw(True)
            
            # *Target_2* updates
            if Target_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                Target_2.frameNStart = frameN  # exact frame index
                Target_2.tStart = t  # local t and not account for scr refresh
                Target_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(Target_2, 'tStartRefresh')  # time at next scr refresh
                Target_2.setAutoDraw(True)
            
            # *Flan1_2* updates
            if Flan1_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                Flan1_2.frameNStart = frameN  # exact frame index
                Flan1_2.tStart = t  # local t and not account for scr refresh
                Flan1_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(Flan1_2, 'tStartRefresh')  # time at next scr refresh
                Flan1_2.setAutoDraw(True)
            
            # *Flan2_2* updates
            if Flan2_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                Flan2_2.frameNStart = frameN  # exact frame index
                Flan2_2.tStart = t  # local t and not account for scr refresh
                Flan2_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(Flan2_2, 'tStartRefresh')  # time at next scr refresh
                Flan2_2.setAutoDraw(True)
            
            # *Flan3_2* updates
            if Flan3_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                Flan3_2.frameNStart = frameN  # exact frame index
                Flan3_2.tStart = t  # local t and not account for scr refresh
                Flan3_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(Flan3_2, 'tStartRefresh')  # time at next scr refresh
                Flan3_2.setAutoDraw(True)
            
            # *Flan4_2* updates
            if Flan4_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                Flan4_2.frameNStart = frameN  # exact frame index
                Flan4_2.tStart = t  # local t and not account for scr refresh
                Flan4_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(Flan4_2, 'tStartRefresh')  # time at next scr refresh
                Flan4_2.setAutoDraw(True)
            
            # *Flan5_2* updates
            if Flan5_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                Flan5_2.frameNStart = frameN  # exact frame index
                Flan5_2.tStart = t  # local t and not account for scr refresh
                Flan5_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(Flan5_2, 'tStartRefresh')  # time at next scr refresh
                Flan5_2.setAutoDraw(True)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in Location_choiceComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "Location_choice"-------
        for thisComponent in Location_choiceComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store data for MainTrialLoop (TrialHandler)
        x, y = mouse.getPos()
        buttons = mouse.getPressed()
        if sum(buttons):
            # check if the mouse was inside our 'clickable' objects
            gotValidClick = False
            try:
                iter([Target_2, Flan1_2, Flan2_2, Flan3_2, Flan4_2, Flan5_2])
                clickableList = [Target_2, Flan1_2, Flan2_2, Flan3_2, Flan4_2, Flan5_2]
            except:
                clickableList = [[Target_2, Flan1_2, Flan2_2, Flan3_2, Flan4_2, Flan5_2]]
            for obj in clickableList:
                if obj.contains(mouse):
                    gotValidClick = True
                    mouse.clicked_name.append(obj.name)
        MainTrialLoop.addData('mouse.x', x)
        MainTrialLoop.addData('mouse.y', y)
        MainTrialLoop.addData('mouse.leftButton', buttons[0])
        MainTrialLoop.addData('mouse.midButton', buttons[1])
        MainTrialLoop.addData('mouse.rightButton', buttons[2])
        if len(mouse.clicked_name):
            MainTrialLoop.addData('mouse.clicked_name', mouse.clicked_name[0])
        MainTrialLoop.addData('mouse.started', mouse.tStart)
        MainTrialLoop.addData('mouse.stopped', mouse.tStop)
        time_LocalisationEnd = globalClock.getTime()
        
        thisExp.addData('time_LocalisationBegin', time_LocalisationBegin)
        thisExp.addData('time_LocalisationEnd', time_LocalisationEnd)
        MainTrialLoop.addData('Fixation_Point_2.started', Fixation_Point_2.tStartRefresh)
        MainTrialLoop.addData('Fixation_Point_2.stopped', Fixation_Point_2.tStopRefresh)
        MainTrialLoop.addData('Target_2.started', Target_2.tStartRefresh)
        MainTrialLoop.addData('Target_2.stopped', Target_2.tStopRefresh)
        MainTrialLoop.addData('Flan1_2.started', Flan1_2.tStartRefresh)
        MainTrialLoop.addData('Flan1_2.stopped', Flan1_2.tStopRefresh)
        MainTrialLoop.addData('Flan2_2.started', Flan2_2.tStartRefresh)
        MainTrialLoop.addData('Flan2_2.stopped', Flan2_2.tStopRefresh)
        MainTrialLoop.addData('Flan3_2.started', Flan3_2.tStartRefresh)
        MainTrialLoop.addData('Flan3_2.stopped', Flan3_2.tStopRefresh)
        MainTrialLoop.addData('Flan4_2.started', Flan4_2.tStartRefresh)
        MainTrialLoop.addData('Flan4_2.stopped', Flan4_2.tStopRefresh)
        MainTrialLoop.addData('Flan5_2.started', Flan5_2.tStartRefresh)
        MainTrialLoop.addData('Flan5_2.stopped', Flan5_2.tStopRefresh)
        # the Routine "Location_choice" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # ------Prepare to start Routine "ISI3"-------
        continueRoutine = True
        # update component parameters for each repeat
        # keep track of which components have finished
        ISI3Components = [ISI3_cross]
        for thisComponent in ISI3Components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        ISI3Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "ISI3"-------
        while continueRoutine:
            # get current time
            t = ISI3Clock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=ISI3Clock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *ISI3_cross* updates
            if ISI3_cross.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                ISI3_cross.frameNStart = frameN  # exact frame index
                ISI3_cross.tStart = t  # local t and not account for scr refresh
                ISI3_cross.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(ISI3_cross, 'tStartRefresh')  # time at next scr refresh
                ISI3_cross.setAutoDraw(True)
            if ISI3_cross.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > ISI3_cross.tStartRefresh + ISI_3_jitter-frameTolerance:
                    # keep track of stop time/frame for later
                    ISI3_cross.tStop = t  # not accounting for scr refresh
                    ISI3_cross.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(ISI3_cross, 'tStopRefresh')  # time at next scr refresh
                    ISI3_cross.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in ISI3Components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "ISI3"-------
        for thisComponent in ISI3Components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        MainTrialLoop.addData('ISI3_cross.started', ISI3_cross.tStartRefresh)
        MainTrialLoop.addData('ISI3_cross.stopped', ISI3_cross.tStopRefresh)
        # the Routine "ISI3" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # ------Prepare to start Routine "Colour_choice"-------
        continueRoutine = True
        # update component parameters for each repeat
        win.setMouseVisible(True)
        
        
        wedgeYellow.setAutoDraw(True)
        wedgeWhite.setAutoDraw(True)
        wedgeVermilion.setAutoDraw(True)
        wedgeRedPurple.setAutoDraw(True)
        
        wedgeBlack.setAutoDraw(True)
        wedgeIndigo.setAutoDraw(True)
        wedgeSkyBlue.setAutoDraw(True)
        wedgeBlueGreen.setAutoDraw(True)
        
        GreyCircle.setAutoDraw(True)
        
        # setup some python lists for storing info about the mouse_2
        mouse_2.clicked_name = []
        mouse_2.clicked_fillColor = []
        gotValidClick = False  # until a click is received
        time_ColourSelectStart = globalClock.getTime()
        # keep track of which components have finished
        Colour_choiceComponents = [mouse_2]
        for thisComponent in Colour_choiceComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        Colour_choiceClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "Colour_choice"-------
        while continueRoutine:
            # get current time
            t = Colour_choiceClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=Colour_choiceClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            if (wedgeYellow.contains(mouse)):
                wedgeYellow.lineColor = 'white'
                GuideYellow.setAutoDraw(True)
            else:
                wedgeYellow.lineColor = 'grey'
                GuideYellow.setAutoDraw(False)
            
            if wedgeWhite.contains(mouse):
                wedgeWhite.lineColor = 'white'
                GuideWhite.setAutoDraw(True)
            else:
                wedgeWhite.lineColor = 'grey'
                GuideWhite.setAutoDraw(False)
                
            if wedgeVermilion.contains(mouse):
                wedgeVermilion.lineColor = 'white'
                GuideVermilion.setAutoDraw(True)
            else:
                wedgeVermilion.lineColor = 'grey'
                GuideVermilion.setAutoDraw(False)
                
            if wedgeRedPurple.contains(mouse):
                wedgeRedPurple.lineColor = 'white'
                GuideRedPurple.setAutoDraw(True)
            else:
                wedgeRedPurple.lineColor = 'grey'
                GuideRedPurple.setAutoDraw(False)
                
            if wedgeBlack.contains(mouse):
                wedgeBlack.lineColor = 'white'
                GuideBlack.setAutoDraw(True)
            else:
                wedgeBlack.lineColor = 'grey'
                GuideBlack.setAutoDraw(False)
                
            if wedgeIndigo.contains(mouse):
                wedgeIndigo.lineColor = 'white'
                GuideIndigo.setAutoDraw(True)
            else:
                wedgeIndigo.lineColor = 'grey'
                GuideIndigo.setAutoDraw(False)
                
            if wedgeSkyBlue.contains(mouse):
                wedgeSkyBlue.lineColor = 'white'
                GuideSkyBlue.setAutoDraw(True)
            else:
                wedgeSkyBlue.lineColor = 'grey'
                GuideSkyBlue.setAutoDraw(False)
                
            if wedgeBlueGreen.contains(mouse):
                wedgeBlueGreen.lineColor = 'white'
                GuideBlueGreen.setAutoDraw(True)
            else:
                wedgeBlueGreen.lineColor = 'grey'
                GuideBlueGreen.setAutoDraw(False)
            # *mouse_2* updates
            if mouse_2.status == NOT_STARTED and t >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                mouse_2.frameNStart = frameN  # exact frame index
                mouse_2.tStart = t  # local t and not account for scr refresh
                mouse_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(mouse_2, 'tStartRefresh')  # time at next scr refresh
                mouse_2.status = STARTED
                mouse_2.mouseClock.reset()
                prevButtonState = [0, 0, 0]  # if now button is down we will treat as 'new' click
            if mouse_2.status == STARTED:  # only update if started and not finished!
                buttons = mouse_2.getPressed()
                if buttons != prevButtonState:  # button state changed?
                    prevButtonState = buttons
                    if sum(buttons) > 0:  # state changed to a new click
                        # check if the mouse was inside our 'clickable' objects
                        gotValidClick = False
                        try:
                            iter([wedgeYellow, wedgeWhite, wedgeVermilion, wedgeRedPurple, wedgeBlack, wedgeIndigo, wedgeSkyBlue, wedgeBlueGreen])
                            clickableList = [wedgeYellow, wedgeWhite, wedgeVermilion, wedgeRedPurple, wedgeBlack, wedgeIndigo, wedgeSkyBlue, wedgeBlueGreen]
                        except:
                            clickableList = [[wedgeYellow, wedgeWhite, wedgeVermilion, wedgeRedPurple, wedgeBlack, wedgeIndigo, wedgeSkyBlue, wedgeBlueGreen]]
                        for obj in clickableList:
                            if obj.contains(mouse_2):
                                gotValidClick = True
                                mouse_2.clicked_name.append(obj.name)
                                mouse_2.clicked_fillColor.append(obj.fillColor)
                        if gotValidClick:  # abort routine on response
                            continueRoutine = False
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in Colour_choiceComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "Colour_choice"-------
        for thisComponent in Colour_choiceComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store data for MainTrialLoop (TrialHandler)
        x, y = mouse_2.getPos()
        buttons = mouse_2.getPressed()
        if sum(buttons):
            # check if the mouse was inside our 'clickable' objects
            gotValidClick = False
            try:
                iter([wedgeYellow, wedgeWhite, wedgeVermilion, wedgeRedPurple, wedgeBlack, wedgeIndigo, wedgeSkyBlue, wedgeBlueGreen])
                clickableList = [wedgeYellow, wedgeWhite, wedgeVermilion, wedgeRedPurple, wedgeBlack, wedgeIndigo, wedgeSkyBlue, wedgeBlueGreen]
            except:
                clickableList = [[wedgeYellow, wedgeWhite, wedgeVermilion, wedgeRedPurple, wedgeBlack, wedgeIndigo, wedgeSkyBlue, wedgeBlueGreen]]
            for obj in clickableList:
                if obj.contains(mouse_2):
                    gotValidClick = True
                    mouse_2.clicked_name.append(obj.name)
                    mouse_2.clicked_fillColor.append(obj.fillColor)
        MainTrialLoop.addData('mouse_2.x', x)
        MainTrialLoop.addData('mouse_2.y', y)
        MainTrialLoop.addData('mouse_2.leftButton', buttons[0])
        MainTrialLoop.addData('mouse_2.midButton', buttons[1])
        MainTrialLoop.addData('mouse_2.rightButton', buttons[2])
        if len(mouse_2.clicked_name):
            MainTrialLoop.addData('mouse_2.clicked_name', mouse_2.clicked_name[0])
        if len(mouse_2.clicked_fillColor):
            MainTrialLoop.addData('mouse_2.clicked_fillColor', mouse_2.clicked_fillColor[0])
        MainTrialLoop.addData('mouse_2.started', mouse_2.tStart)
        MainTrialLoop.addData('mouse_2.stopped', mouse_2.tStop)
        time_ColourSelectEnd = globalClock.getTime()
        
        thisExp.addData('time_ColourSelectStart', time_ColourSelectStart)
        thisExp.addData('time_ColourSelectEnd', time_ColourSelectEnd)
        
        # the Routine "Colour_choice" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # ------Prepare to start Routine "Clear_Screen"-------
        continueRoutine = True
        # update component parameters for each repeat
        win.setMouseVisible(False)
        
        GreyCircle.setAutoDraw(False)
        
        wedgeYellow.setAutoDraw(False)
        wedgeWhite.setAutoDraw(False)
        wedgeVermilion.setAutoDraw(False)
        wedgeRedPurple.setAutoDraw(False)
        
        wedgeBlack.setAutoDraw(False)
        wedgeIndigo.setAutoDraw(False)
        wedgeSkyBlue.setAutoDraw(False)
        wedgeBlueGreen.setAutoDraw(False)
        
        GuideYellow.setAutoDraw(False)
        GuideWhite.setAutoDraw(False)
        GuideVermilion.setAutoDraw(False)
        GuideRedPurple.setAutoDraw(False)
        
        GuideBlack.setAutoDraw(False)
        GuideIndigo.setAutoDraw(False)
        GuideSkyBlue.setAutoDraw(False)
        GuideBlueGreen.setAutoDraw(False)
        # keep track of which components have finished
        Clear_ScreenComponents = []
        for thisComponent in Clear_ScreenComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        Clear_ScreenClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "Clear_Screen"-------
        while continueRoutine:
            # get current time
            t = Clear_ScreenClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=Clear_ScreenClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in Clear_ScreenComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "Clear_Screen"-------
        for thisComponent in Clear_ScreenComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # the Routine "Clear_Screen" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
    # completed 1.0 repeats of 'MainTrialLoop'
    
    
    # ------Prepare to start Routine "BlockAdder"-------
    continueRoutine = True
    routineTimer.add(1.000000)
    # update component parameters for each repeat
    BlockNo = BlockNo + 1
    # keep track of which components have finished
    BlockAdderComponents = [text]
    for thisComponent in BlockAdderComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    BlockAdderClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "BlockAdder"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = BlockAdderClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=BlockAdderClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text* updates
        if text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text.frameNStart = frameN  # exact frame index
            text.tStart = t  # local t and not account for scr refresh
            text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text, 'tStartRefresh')  # time at next scr refresh
            text.setAutoDraw(True)
        if text.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                text.tStop = t  # not accounting for scr refresh
                text.frameNStop = frameN  # exact frame index
                win.timeOnFlip(text, 'tStopRefresh')  # time at next scr refresh
                text.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in BlockAdderComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "BlockAdder"-------
    for thisComponent in BlockAdderComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    MasterTrialLoop.addData('text.started', text.tStartRefresh)
    MasterTrialLoop.addData('text.stopped', text.tStopRefresh)
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'MasterTrialLoop'


# ------Prepare to start Routine "EndScreen"-------
continueRoutine = True
# update component parameters for each repeat
# keep track of which components have finished
EndScreenComponents = [EndScreenText]
for thisComponent in EndScreenComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
EndScreenClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "EndScreen"-------
while continueRoutine:
    # get current time
    t = EndScreenClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=EndScreenClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *EndScreenText* updates
    if EndScreenText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        EndScreenText.frameNStart = frameN  # exact frame index
        EndScreenText.tStart = t  # local t and not account for scr refresh
        EndScreenText.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(EndScreenText, 'tStartRefresh')  # time at next scr refresh
        EndScreenText.setAutoDraw(True)
    keys = event.getKeys()
    if 'q' in keys and 't' in keys:
            core.quit()
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in EndScreenComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "EndScreen"-------
for thisComponent in EndScreenComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('EndScreenText.started', EndScreenText.tStartRefresh)
thisExp.addData('EndScreenText.stopped', EndScreenText.tStopRefresh)
# the Routine "EndScreen" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv', delim='auto')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
