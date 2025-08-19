#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2024.2.4),
    on August 18, 2025, at 17:25
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

# --- Import packages ---
from psychopy import locale_setup
from psychopy import prefs
from psychopy import plugins
plugins.activatePlugins()
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors, layout, hardware
from psychopy.tools import environmenttools
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER, priority)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os  # handy system and path functions
import sys  # to get file system encoding

import psychopy.iohub as io
from psychopy.hardware import keyboard

# Run 'Before Experiment' code from Definitions
win = visual.Window(viewScale=[100,100])
# --- Setup global variables (available in all functions) ---
# create a device manager to handle hardware (keyboards, mice, mirophones, speakers, etc.)
deviceManager = hardware.DeviceManager()
# ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
# store info about the experiment session
psychopyVersion = '2024.2.4'
expName = 'Colour Change Detection Task Oxford PERL'  # from the Builder filename that created this script
# information about this experiment
expInfo = {
    'participant': '',
    'Study_name': '',
    'PREPOST': '',
    'Task Version (required to run)': '1 or 2',
    'date|hid': data.getDateStr(),
    'expName|hid': expName,
    'psychopyVersion|hid': psychopyVersion,
}

# --- Define some variables which will change depending on pilot mode ---
'''
To run in pilot mode, either use the run/pilot toggle in Builder, Coder and Runner, 
or run the experiment with `--pilot` as an argument. To change what pilot 
#mode does, check out the 'Pilot mode' tab in preferences.
'''
# work out from system args whether we are running in pilot mode
PILOTING = core.setPilotModeFromArgs()
# start off with values from experiment settings
_fullScr = False
_winSize = [1400, 1400]
# if in pilot mode, apply overrides according to preferences
if PILOTING:
    # force windowed mode
    if prefs.piloting['forceWindowed']:
        _fullScr = False
        # set window size
        _winSize = prefs.piloting['forcedWindowSize']

def showExpInfoDlg(expInfo):
    """
    Show participant info dialog.
    Parameters
    ==========
    expInfo : dict
        Information about this experiment.
    
    Returns
    ==========
    dict
        Information about this experiment.
    """
    # show participant info dialog
    dlg = gui.DlgFromDict(
        dictionary=expInfo, sortKeys=False, title=expName, alwaysOnTop=True
    )
    if dlg.OK == False:
        core.quit()  # user pressed cancel
    # return expInfo
    return expInfo


def setupData(expInfo, dataDir=None):
    """
    Make an ExperimentHandler to handle trials and saving.
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    dataDir : Path, str or None
        Folder to save the data to, leave as None to create a folder in the current directory.    
    Returns
    ==========
    psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    """
    # remove dialog-specific syntax from expInfo
    for key, val in expInfo.copy().items():
        newKey, _ = data.utils.parsePipeSyntax(key)
        expInfo[newKey] = expInfo.pop(key)
    
    # data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
    if dataDir is None:
        dataDir = _thisDir
    filename = u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])
    # make sure filename is relative to dataDir
    if os.path.isabs(filename):
        dataDir = os.path.commonprefix([dataDir, filename])
        filename = os.path.relpath(filename, dataDir)
    
    # an ExperimentHandler isn't essential but helps with data saving
    thisExp = data.ExperimentHandler(
        name=expName, version='',
        extraInfo=expInfo, runtimeInfo=None,
        originPath='C:\\Users\\PERLadmin\\Desktop\\DOREA_Task_Battery\\CDT\\Colour Change Detection Task Oxford PERL_lastrun.py',
        savePickle=True, saveWideText=True,
        dataFileName=dataDir + os.sep + filename, sortColumns='time'
    )
    thisExp.setPriority('thisRow.t', priority.CRITICAL)
    thisExp.setPriority('expName', priority.LOW)
    # return experiment handler
    return thisExp


def setupLogging(filename):
    """
    Setup a log file and tell it what level to log at.
    
    Parameters
    ==========
    filename : str or pathlib.Path
        Filename to save log file and data files as, doesn't need an extension.
    
    Returns
    ==========
    psychopy.logging.LogFile
        Text stream to receive inputs from the logging system.
    """
    # set how much information should be printed to the console / app
    if PILOTING:
        logging.console.setLevel(
            prefs.piloting['pilotConsoleLoggingLevel']
        )
    else:
        logging.console.setLevel('warning')
    # save a log file for detail verbose info
    logFile = logging.LogFile(filename+'.log')
    if PILOTING:
        logFile.setLevel(
            prefs.piloting['pilotLoggingLevel']
        )
    else:
        logFile.setLevel(
            logging.getLevel('exp')
        )
    
    return logFile


def setupWindow(expInfo=None, win=None):
    """
    Setup the Window
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    win : psychopy.visual.Window
        Window to setup - leave as None to create a new window.
    
    Returns
    ==========
    psychopy.visual.Window
        Window in which to run this experiment.
    """
    if win is None:
        # if not given a window to setup, make one
        win = visual.Window(
            size=_winSize, fullscr=_fullScr, screen=0,
            winType='pyglet', allowGUI=True, allowStencil=False,
            monitor='labMonitor', color=[-0.4667, -0.4667, -0.4510], colorSpace='rgb',
            backgroundImage='', backgroundFit='none',
            blendMode='avg', useFBO=True,
            units=None,
            checkTiming=False  # we're going to do this ourselves in a moment
        )
    else:
        # if we have a window, just set the attributes which are safe to set
        win.color = [-0.4667, -0.4667, -0.4510]
        win.colorSpace = 'rgb'
        win.backgroundImage = ''
        win.backgroundFit = 'none'
        win.units = None
    if expInfo is not None:
        # get/measure frame rate if not already in expInfo
        if win._monitorFrameRate is None:
            win._monitorFrameRate = win.getActualFrameRate(infoMsg='')
        expInfo['frameRate'] = win._monitorFrameRate
    win.hideMessage()
    # show a visual indicator if we're in piloting mode
    if PILOTING and prefs.piloting['showPilotingIndicator']:
        win.showPilotingIndicator()
    
    return win


def setupDevices(expInfo, thisExp, win):
    """
    Setup whatever devices are available (mouse, keyboard, speaker, eyetracker, etc.) and add them to 
    the device manager (deviceManager)
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    win : psychopy.visual.Window
        Window in which to run this experiment.
    Returns
    ==========
    bool
        True if completed successfully.
    """
    # --- Setup input devices ---
    ioConfig = {}
    
    # Setup iohub keyboard
    ioConfig['Keyboard'] = dict(use_keymap='psychopy')
    
    # Setup iohub experiment
    ioConfig['Experiment'] = dict(filename=thisExp.dataFileName)
    
    # Start ioHub server
    ioServer = io.launchHubServer(window=win, **ioConfig)
    
    # store ioServer object in the device manager
    deviceManager.ioServer = ioServer
    
    # create a default keyboard (e.g. to check for escape)
    if deviceManager.getDevice('defaultKeyboard') is None:
        deviceManager.addDevice(
            deviceClass='keyboard', deviceName='defaultKeyboard', backend='iohub'
        )
    # return True if completed successfully
    return True

def pauseExperiment(thisExp, win=None, timers=[], playbackComponents=[]):
    """
    Pause this experiment, preventing the flow from advancing to the next routine until resumed.
    
    Parameters
    ==========
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    win : psychopy.visual.Window
        Window for this experiment.
    timers : list, tuple
        List of timers to reset once pausing is finished.
    playbackComponents : list, tuple
        List of any components with a `pause` method which need to be paused.
    """
    # if we are not paused, do nothing
    if thisExp.status != PAUSED:
        return
    
    # start a timer to figure out how long we're paused for
    pauseTimer = core.Clock()
    # pause any playback components
    for comp in playbackComponents:
        comp.pause()
    # make sure we have a keyboard
    defaultKeyboard = deviceManager.getDevice('defaultKeyboard')
    if defaultKeyboard is None:
        defaultKeyboard = deviceManager.addKeyboard(
            deviceClass='keyboard',
            deviceName='defaultKeyboard',
            backend='ioHub',
        )
    # run a while loop while we wait to unpause
    while thisExp.status == PAUSED:
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=['escape']):
            endExperiment(thisExp, win=win)
        # sleep 1ms so other threads can execute
        clock.time.sleep(0.001)
    # if stop was requested while paused, quit
    if thisExp.status == FINISHED:
        endExperiment(thisExp, win=win)
    # resume any playback components
    for comp in playbackComponents:
        comp.play()
    # reset any timers
    for timer in timers:
        timer.addTime(-pauseTimer.getTime())


def run(expInfo, thisExp, win, globalClock=None, thisSession=None):
    """
    Run the experiment flow.
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    psychopy.visual.Window
        Window in which to run this experiment.
    globalClock : psychopy.core.clock.Clock or None
        Clock to get global time from - supply None to make a new one.
    thisSession : psychopy.session.Session or None
        Handle of the Session object this experiment is being run from, if any.
    """
    # mark experiment as started
    thisExp.status = STARTED
    # make sure window is set to foreground to prevent losing focus
    win.winHandle.activate()
    # make sure variables created by exec are available globally
    exec = environmenttools.setExecEnvironment(globals())
    # get device handles from dict of input devices
    ioServer = deviceManager.ioServer
    # get/create a default keyboard (e.g. to check for escape)
    defaultKeyboard = deviceManager.getDevice('defaultKeyboard')
    if defaultKeyboard is None:
        deviceManager.addDevice(
            deviceClass='keyboard', deviceName='defaultKeyboard', backend='ioHub'
        )
    eyetracker = deviceManager.getDevice('eyetracker')
    # make sure we're running in the directory for this experiment
    os.chdir(_thisDir)
    # get filename from ExperimentHandler for convenience
    filename = thisExp.dataFileName
    frameTolerance = 0.001  # how close to onset before 'same' frame
    endExpNow = False  # flag for 'escape' or other condition => quit the exp
    # get frame duration from frame rate in expInfo
    if 'frameRate' in expInfo and expInfo['frameRate'] is not None:
        frameDur = 1.0 / round(expInfo['frameRate'])
    else:
        frameDur = 1.0 / 60.0  # could not measure, so guess
    
    # Start Code - component code to be run after the window creation
    
    # --- Initialize components for Routine "Startup_code" ---
    # Run 'Begin Experiment' code from Definitions
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
    # Run 'Begin Experiment' code from Loading_wheel
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
    
    # Run 'Begin Experiment' code from Background_border
    box_width = 0.95
    box_height = 0.95
    stripe_height = 0.02
    num_stripes = int(box_height / stripe_height)
    
    # Original grey and a slightly darker one
    colors = [[0.0, 0.0, 0.0], [-0.05, -0.05, -0.05]]
    
    stripes = []
    for i in range(num_stripes):
        y_offset = (i + 0.5) * stripe_height - (box_height / 2)
        stripe = visual.Rect(
            win=win,
            width=box_width,
            height=stripe_height,
            pos=(0, y_offset),
            fillColor=colors[i % 2],
            fillColorSpace='rgb',
            lineColor=None
        )
        stripe.setAutoDraw(True)
        stripes.append(stripe)
    
    # Run 'Begin Experiment' code from Task_V_Selection
    # Get and clean version input
    TaskVersion = str(expInfo.get('Task Version (required to run)', '')).strip()
    
    # Choose path based on version
    if TaskVersion == '1':
        basePath = 'Conditions/'
    elif TaskVersion == '2':
        basePath = 'Conditions/'
    else:
        # show error and exit
        errMsg = visual.TextStim(
            win=win,
            text="Warning: Must enter a valid task version number\n(i.e., 1, or 2). \n\n Press any key to quit.",
            color='black',
            height=0.025
        )
        errMsg.draw()
        win.flip()
        event.waitKeys()
        core.quit()
    
    # Construct filename
    VersionSelection = basePath + f'CCDT_master_{TaskVersion}.xlsx'
    
    # --- Initialize components for Routine "Startup_screen" ---
    NumberOBlocks_4 = visual.TextStim(win=win, name='NumberOBlocks_4',
        text='',
        font='Open Sans',
        pos=(0.0, 0.01), draggable=False, height=0.04, wrapWidth=0.75, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    ContinueButtonText_2 = visual.TextStim(win=win, name='ContinueButtonText_2',
        text='Click here to continue',
        font='Open Sans',
        pos=(0, -0.3), draggable=False, height=0.03, wrapWidth=0.75, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-1.0);
    Version_Text = visual.TextStim(win=win, name='Version_Text',
        text=TaskVersion,
        font='Arial',
        pos=(0.2625, 0.061675), draggable=False, height=0.04, wrapWidth=None, ori=0.0, 
        color='black', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-2.0);
    ContinueButton_2 = visual.Rect(
        win=win, name='ContinueButton_2',
        width=(0.37, 0.09)[0], height=(0.37, 0.09)[1],
        ori=0.0, pos=(0, -0.3), draggable=False, anchor='center',
        lineWidth=1.0,
        colorSpace='rgb', lineColor='white', fillColor=None,
        opacity=None, depth=-3.0, interpolate=True)
    mouse_4 = event.Mouse(win=win)
    x, y = [None, None]
    mouse_4.mouseClock = core.Clock()
    
    # --- Initialize components for Routine "Instructions_Begin" ---
    NumberOBlocks_5 = visual.TextStim(win=win, name='NumberOBlocks_5',
        text='',
        font='Open Sans',
        pos=(0.00, 0.01), draggable=False, height=0.035, wrapWidth=0.75, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    ContinueButtonText_3 = visual.TextStim(win=win, name='ContinueButtonText_3',
        text='Click here to continue',
        font='Open Sans',
        pos=(0, -0.3), draggable=False, height=0.03, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-1.0);
    ContinueButton_3 = visual.Rect(
        win=win, name='ContinueButton_3',
        width=(0.37, 0.09)[0], height=(0.37, 0.09)[1],
        ori=0.0, pos=(0, -0.3), draggable=False, anchor='center',
        lineWidth=1.0,
        colorSpace='rgb', lineColor='white', fillColor=None,
        opacity=None, depth=-2.0, interpolate=True)
    mouse_5 = event.Mouse(win=win)
    x, y = [None, None]
    mouse_5.mouseClock = core.Clock()
    
    # --- Initialize components for Routine "Instructions_Begin_2" ---
    NumberOBlocks_6 = visual.TextStim(win=win, name='NumberOBlocks_6',
        text='',
        font='Open Sans',
        pos=(0.00, 0.01), draggable=False, height=0.04, wrapWidth=0.75, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    ContinueButtonText_4 = visual.TextStim(win=win, name='ContinueButtonText_4',
        text='Click to start the tutorial',
        font='Open Sans',
        pos=(0, -0.3), draggable=False, height=0.03, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-1.0);
    ContinueButton_4 = visual.Rect(
        win=win, name='ContinueButton_4',
        width=(0.37, 0.09)[0], height=(0.37, 0.09)[1],
        ori=0.0, pos=(0, -0.3), draggable=False, anchor='center',
        lineWidth=1.0,
        colorSpace='rgb', lineColor='white', fillColor=None,
        opacity=None, depth=-2.0, interpolate=True)
    mouse_6 = event.Mouse(win=win)
    x, y = [None, None]
    mouse_6.mouseClock = core.Clock()
    
    # --- Initialize components for Routine "ISI_tutorial" ---
    ISI1_cross_2 = visual.TextStim(win=win, name='ISI1_cross_2',
        text='',
        font='Open Sans',
        pos=(0, 0), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    
    # --- Initialize components for Routine "Stimulus_disp_tutorial" ---
    Fixation_Point_3 = visual.TextStim(win=win, name='Fixation_Point_3',
        text='·',
        font='Open Sans',
        pos=(0, 0), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    Target_3 = visual.Rect(
        win=win, name='Target_3',
        width=(0.125, 0.125)[0], height=(0.125, 0.125)[1],
        ori=0.0, pos=[0,0], draggable=False, anchor='center',
        lineWidth=1.0,
        colorSpace='rgb', lineColor=None, fillColor='white',
        opacity=None, depth=-1.0, interpolate=True)
    Flan1_3 = visual.Rect(
        win=win, name='Flan1_3',
        width=(0.125, 0.125)[0], height=(0.125, 0.125)[1],
        ori=0.0, pos=[0,0], draggable=False, anchor='center',
        lineWidth=1.0,
        colorSpace='rgb', lineColor=None, fillColor='white',
        opacity=None, depth=-2.0, interpolate=True)
    Flan2_3 = visual.Rect(
        win=win, name='Flan2_3',
        width=(0.125, 0.125)[0], height=(0.125, 0.125)[1],
        ori=0.0, pos=[0,0], draggable=False, anchor='center',
        lineWidth=1.0,
        colorSpace='rgb', lineColor=None, fillColor='white',
        opacity=None, depth=-3.0, interpolate=True)
    Flan3_3 = visual.Rect(
        win=win, name='Flan3_3',
        width=(0.125, 0.125)[0], height=(0.125, 0.125)[1],
        ori=0.0, pos=[0,0], draggable=False, anchor='center',
        lineWidth=1.0,
        colorSpace='rgb', lineColor=None, fillColor=None,
        opacity=None, depth=-4.0, interpolate=True)
    Flan4_3 = visual.Rect(
        win=win, name='Flan4_3',
        width=(0.125, 0.125)[0], height=(0.125, 0.125)[1],
        ori=0.0, pos=[0,0], draggable=False, anchor='center',
        lineWidth=1.0,
        colorSpace='rgb', lineColor=None, fillColor=None,
        opacity=None, depth=-5.0, interpolate=True)
    Flan5_3 = visual.Rect(
        win=win, name='Flan5_3',
        width=(0.125, 0.125)[0], height=(0.125, 0.125)[1],
        ori=0.0, pos=[0,0], draggable=False, anchor='center',
        lineWidth=1.0,
        colorSpace='rgb', lineColor=None, fillColor=None,
        opacity=None, depth=-6.0, interpolate=True)
    
    # --- Initialize components for Routine "ISI_tutorial" ---
    ISI1_cross_2 = visual.TextStim(win=win, name='ISI1_cross_2',
        text='',
        font='Open Sans',
        pos=(0, 0), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    
    # --- Initialize components for Routine "Loc_choice_tut" ---
    mouse_8 = event.Mouse(win=win)
    x, y = [None, None]
    mouse_8.mouseClock = core.Clock()
    Fixation_Point_5 = visual.TextStim(win=win, name='Fixation_Point_5',
        text='·',
        font='Open Sans',
        pos=(0, 0), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-2.0);
    Target_5 = visual.Rect(
        win=win, name='Target_5',
        width=(0.125, 0.125)[0], height=(0.125, 0.125)[1],
        ori=0.0, pos=[0,0], draggable=False, anchor='center',
        lineWidth=3.5,
        colorSpace='rgb', lineColor=None, fillColor='white',
        opacity=None, depth=-3.0, interpolate=True)
    Flan1_5 = visual.Rect(
        win=win, name='Flan1_5',
        width=(0.125, 0.125)[0], height=(0.125, 0.125)[1],
        ori=0.0, pos=[0,0], draggable=False, anchor='center',
        lineWidth=3.5,
        colorSpace='rgb', lineColor=None, fillColor='white',
        opacity=None, depth=-4.0, interpolate=True)
    Flan2_5 = visual.Rect(
        win=win, name='Flan2_5',
        width=(0.125, 0.125)[0], height=(0.125, 0.125)[1],
        ori=0.0, pos=[0,0], draggable=False, anchor='center',
        lineWidth=3.5,
        colorSpace='rgb', lineColor=None, fillColor='white',
        opacity=None, depth=-5.0, interpolate=True)
    Flan3_5 = visual.Rect(
        win=win, name='Flan3_5',
        width=(0.125, 0.125)[0], height=(0.125, 0.125)[1],
        ori=0.0, pos=[0,0], draggable=False, anchor='center',
        lineWidth=3.5,
        colorSpace='rgb', lineColor=None, fillColor=None,
        opacity=None, depth=-6.0, interpolate=True)
    Flan4_5 = visual.Rect(
        win=win, name='Flan4_5',
        width=(0.125, 0.125)[0], height=(0.125, 0.125)[1],
        ori=0.0, pos=[0,0], draggable=False, anchor='center',
        lineWidth=3.5,
        colorSpace='rgb', lineColor=None, fillColor=None,
        opacity=None, depth=-7.0, interpolate=True)
    Flan5_5 = visual.Rect(
        win=win, name='Flan5_5',
        width=(0.125, 0.125)[0], height=(0.125, 0.125)[1],
        ori=0.0, pos=[0,0], draggable=False, anchor='center',
        lineWidth=3.5,
        colorSpace='rgb', lineColor=None, fillColor=None,
        opacity=None, depth=-8.0, interpolate=True)
    ArrowHead = visual.ShapeStim(
        win=win, name='ArrowHead',
        size=(0.05, 0.05), vertices='triangle',
        ori=270.0, pos=(0.19, 0.1), draggable=False, anchor='center',
        lineWidth=1.0,
        colorSpace='rgb', lineColor=None, fillColor='green',
        opacity=None, depth=-9.0, interpolate=True)
    ArrowBar = visual.Rect(
        win=win, name='ArrowBar',
        width=(0.07, 0.008)[0], height=(0.07, 0.008)[1],
        ori=0.0, pos=(0.24, 0.1), draggable=False, anchor='center',
        lineWidth=2.0,
        colorSpace='rgb', lineColor=None, fillColor='green',
        opacity=None, depth=-10.0, interpolate=True)
    InstruText2 = visual.TextStim(win=win, name='InstruText2',
        text='Select the square which changed colour.',
        font='Open Sans',
        pos=(0, 0.3), draggable=False, height=0.03, wrapWidth=0.75, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-11.0);
    
    # --- Initialize components for Routine "ISI_tutorial" ---
    ISI1_cross_2 = visual.TextStim(win=win, name='ISI1_cross_2',
        text='',
        font='Open Sans',
        pos=(0, 0), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    
    # --- Initialize components for Routine "Choice_tutorial" ---
    mouse_9 = event.Mouse(win=win)
    x, y = [None, None]
    mouse_9.mouseClock = core.Clock()
    ArrowHead2 = visual.ShapeStim(
        win=win, name='ArrowHead2',
        size=(0.05, 0.05), vertices='triangle',
        ori=90.0, pos=(0.165, -0.33), draggable=False, anchor='center',
        lineWidth=1.0,
        colorSpace='rgb', lineColor=None, fillColor='green',
        opacity=None, depth=-2.0, interpolate=True)
    ArrowBar2 = visual.Rect(
        win=win, name='ArrowBar2',
        width=(0.07, 0.01)[0], height=(0.07, 0.01)[1],
        ori=53.0, pos=(0.1831, -0.365), draggable=False, anchor='center',
        lineWidth=1.0,
        colorSpace='rgb', lineColor=None, fillColor='green',
        opacity=None, depth=-3.0, interpolate=True)
    InstruText = visual.TextStim(win=win, name='InstruText',
        text='Select the original colour of the square.',
        font='Open Sans',
        pos=(0, 0.35), draggable=False, height=0.03, wrapWidth=0.65, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-4.0);
    
    # --- Initialize components for Routine "Clear_sc_tut" ---
    
    # --- Initialize components for Routine "break_2" ---
    text_2 = visual.TextStim(win=win, name='text_2',
        text="Well done! Let's try another.",
        font='Open Sans',
        pos=(0, 0), draggable=False, height=0.04, wrapWidth=0.65, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    
    # --- Initialize components for Routine "ISI_tutorial_2" ---
    ISI1_cross_3 = visual.TextStim(win=win, name='ISI1_cross_3',
        text='',
        font='Open Sans',
        pos=(0, 0), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    
    # --- Initialize components for Routine "Stimulus_disp_tutorial_2" ---
    Fixation_Point_6 = visual.TextStim(win=win, name='Fixation_Point_6',
        text='·',
        font='Open Sans',
        pos=(0, 0), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    Target_6 = visual.Rect(
        win=win, name='Target_6',
        width=(0.125, 0.125)[0], height=(0.125, 0.125)[1],
        ori=0.0, pos=[0,0], draggable=False, anchor='center',
        lineWidth=1.0,
        colorSpace='rgb', lineColor=None, fillColor='white',
        opacity=None, depth=-1.0, interpolate=True)
    Flan1_6 = visual.Rect(
        win=win, name='Flan1_6',
        width=(0.125, 0.125)[0], height=(0.125, 0.125)[1],
        ori=0.0, pos=[0,0], draggable=False, anchor='center',
        lineWidth=1.0,
        colorSpace='rgb', lineColor=None, fillColor='white',
        opacity=None, depth=-2.0, interpolate=True)
    Flan2_6 = visual.Rect(
        win=win, name='Flan2_6',
        width=(0.125, 0.125)[0], height=(0.125, 0.125)[1],
        ori=0.0, pos=[0,0], draggable=False, anchor='center',
        lineWidth=1.0,
        colorSpace='rgb', lineColor=None, fillColor='white',
        opacity=None, depth=-3.0, interpolate=True)
    Flan3_6 = visual.Rect(
        win=win, name='Flan3_6',
        width=(0.125, 0.125)[0], height=(0.125, 0.125)[1],
        ori=0.0, pos=[0,0], draggable=False, anchor='center',
        lineWidth=1.0,
        colorSpace='rgb', lineColor=None, fillColor=None,
        opacity=None, depth=-4.0, interpolate=True)
    Flan4_6 = visual.Rect(
        win=win, name='Flan4_6',
        width=(0.125, 0.125)[0], height=(0.125, 0.125)[1],
        ori=0.0, pos=[0,0], draggable=False, anchor='center',
        lineWidth=1.0,
        colorSpace='rgb', lineColor=None, fillColor=None,
        opacity=None, depth=-5.0, interpolate=True)
    Flan5_6 = visual.Rect(
        win=win, name='Flan5_6',
        width=(0.125, 0.125)[0], height=(0.125, 0.125)[1],
        ori=0.0, pos=[0,0], draggable=False, anchor='center',
        lineWidth=1.0,
        colorSpace='rgb', lineColor=None, fillColor=None,
        opacity=None, depth=-6.0, interpolate=True)
    
    # --- Initialize components for Routine "ISI_tutorial_2" ---
    ISI1_cross_3 = visual.TextStim(win=win, name='ISI1_cross_3',
        text='',
        font='Open Sans',
        pos=(0, 0), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    
    # --- Initialize components for Routine "Loc_choice_tut_2" ---
    mouse_11 = event.Mouse(win=win)
    x, y = [None, None]
    mouse_11.mouseClock = core.Clock()
    Fixation_Point_7 = visual.TextStim(win=win, name='Fixation_Point_7',
        text='·',
        font='Open Sans',
        pos=(0, 0), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-2.0);
    Target_7 = visual.Rect(
        win=win, name='Target_7',
        width=(0.125, 0.125)[0], height=(0.125, 0.125)[1],
        ori=0.0, pos=[0,0], draggable=False, anchor='center',
        lineWidth=3.5,
        colorSpace='rgb', lineColor=None, fillColor='white',
        opacity=None, depth=-3.0, interpolate=True)
    Flan1_7 = visual.Rect(
        win=win, name='Flan1_7',
        width=(0.125, 0.125)[0], height=(0.125, 0.125)[1],
        ori=0.0, pos=[0,0], draggable=False, anchor='center',
        lineWidth=3.5,
        colorSpace='rgb', lineColor=None, fillColor='white',
        opacity=None, depth=-4.0, interpolate=True)
    Flan2_7 = visual.Rect(
        win=win, name='Flan2_7',
        width=(0.125, 0.125)[0], height=(0.125, 0.125)[1],
        ori=0.0, pos=[0,0], draggable=False, anchor='center',
        lineWidth=3.5,
        colorSpace='rgb', lineColor=None, fillColor='white',
        opacity=None, depth=-5.0, interpolate=True)
    Flan3_7 = visual.Rect(
        win=win, name='Flan3_7',
        width=(0.125, 0.125)[0], height=(0.125, 0.125)[1],
        ori=0.0, pos=[0,0], draggable=False, anchor='center',
        lineWidth=3.5,
        colorSpace='rgb', lineColor=None, fillColor=None,
        opacity=None, depth=-6.0, interpolate=True)
    Flan4_7 = visual.Rect(
        win=win, name='Flan4_7',
        width=(0.125, 0.125)[0], height=(0.125, 0.125)[1],
        ori=0.0, pos=[0,0], draggable=False, anchor='center',
        lineWidth=3.5,
        colorSpace='rgb', lineColor=None, fillColor=None,
        opacity=None, depth=-7.0, interpolate=True)
    Flan5_7 = visual.Rect(
        win=win, name='Flan5_7',
        width=(0.125, 0.125)[0], height=(0.125, 0.125)[1],
        ori=0.0, pos=[0,0], draggable=False, anchor='center',
        lineWidth=3.5,
        colorSpace='rgb', lineColor=None, fillColor=None,
        opacity=None, depth=-8.0, interpolate=True)
    InstruText2_2 = visual.TextStim(win=win, name='InstruText2_2',
        text='Select the square which changed colour.',
        font='Open Sans',
        pos=(0, 0.3), draggable=False, height=0.03, wrapWidth=0.75, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-9.0);
    
    # --- Initialize components for Routine "ISI_tutorial_2" ---
    ISI1_cross_3 = visual.TextStim(win=win, name='ISI1_cross_3',
        text='',
        font='Open Sans',
        pos=(0, 0), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    
    # --- Initialize components for Routine "Choice_tutorial_2" ---
    mouse_12 = event.Mouse(win=win)
    x, y = [None, None]
    mouse_12.mouseClock = core.Clock()
    InstruText_2 = visual.TextStim(win=win, name='InstruText_2',
        text='Select the original colour of the square.',
        font='Open Sans',
        pos=(0, 0.35), draggable=False, height=0.03, wrapWidth=0.65, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-2.0);
    
    # --- Initialize components for Routine "Clear_sc_tut" ---
    
    # --- Initialize components for Routine "Tutorial_end" ---
    NumberOBlocks_7 = visual.TextStim(win=win, name='NumberOBlocks_7',
        text='',
        font='Open Sans',
        pos=(0.00, 0.01), draggable=False, height=0.04, wrapWidth=0.85, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    ContinueButtonText_5 = visual.TextStim(win=win, name='ContinueButtonText_5',
        text='Click to begin the task',
        font='Open Sans',
        pos=(0, -0.3), draggable=False, height=0.03, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-1.0);
    ContinueButton_5 = visual.Rect(
        win=win, name='ContinueButton_5',
        width=(0.37, 0.09)[0], height=(0.37, 0.09)[1],
        ori=0.0, pos=(0, -0.3), draggable=False, anchor='center',
        lineWidth=1.0,
        colorSpace='rgb', lineColor='white', fillColor=None,
        opacity=None, depth=-2.0, interpolate=True)
    mouse_10 = event.Mouse(win=win)
    x, y = [None, None]
    mouse_10.mouseClock = core.Clock()
    
    # --- Initialize components for Routine "break_3" ---
    text_3 = visual.TextStim(win=win, name='text_3',
        text=None,
        font='Open Sans',
        pos=(0, 0), draggable=False, height=0.1, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    
    # --- Initialize components for Routine "MainInstructions" ---
    NumberOBlocks_2 = visual.TextStim(win=win, name='NumberOBlocks_2',
        text='',
        font='Open Sans',
        pos=(0.001, 0.24449), draggable=False, height=0.06, wrapWidth=0.75, ori=0.0, 
        color='black', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-1.0);
    InstructionsMainText = visual.TextStim(win=win, name='InstructionsMainText',
        text='',
        font='Open Sans',
        pos=(0, -0.0), draggable=False, height=0.04, wrapWidth=0.75, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-2.0);
    NumberOBlocks = visual.TextStim(win=win, name='NumberOBlocks',
        text='',
        font='Open Sans',
        pos=(0.00, 0.25), draggable=False, height=0.06, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-3.0);
    ContinueButtonText = visual.TextStim(win=win, name='ContinueButtonText',
        text='Click here to begin',
        font='Open Sans',
        pos=(0, -0.3), draggable=False, height=0.03, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-4.0);
    ContinueButton = visual.Rect(
        win=win, name='ContinueButton',
        width=(0.37, 0.09)[0], height=(0.37, 0.09)[1],
        ori=0.0, pos=(0, -0.3), draggable=False, anchor='center',
        lineWidth=1.0,
        colorSpace='rgb', lineColor='white', fillColor=None,
        opacity=None, depth=-5.0, interpolate=True)
    mouse_3 = event.Mouse(win=win)
    x, y = [None, None]
    mouse_3.mouseClock = core.Clock()
    
    # --- Initialize components for Routine "Time_gap" ---
    Focus = visual.TextStim(win=win, name='Focus',
        text='·',
        font='Open Sans',
        pos=(0, 0), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    
    # --- Initialize components for Routine "ISI" ---
    ISI1_cross = visual.TextStim(win=win, name='ISI1_cross',
        text='',
        font='Open Sans',
        pos=(0, 0), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    
    # --- Initialize components for Routine "Stimulus_display" ---
    Fixation_Point = visual.TextStim(win=win, name='Fixation_Point',
        text='·',
        font='Open Sans',
        pos=(0, 0), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    Target = visual.Rect(
        win=win, name='Target',
        width=(0.15, 0.15)[0], height=(0.15, 0.15)[1],
        ori=0.0, pos=[0,0], draggable=False, anchor='center',
        lineWidth=2.0,
        colorSpace='rgb', lineColor=None, fillColor='white',
        opacity=None, depth=-1.0, interpolate=True)
    Flan1 = visual.Rect(
        win=win, name='Flan1',
        width=(0.15, 0.15)[0], height=(0.15, 0.15)[1],
        ori=0.0, pos=[0,0], draggable=False, anchor='center',
        lineWidth=2.0,
        colorSpace='rgb', lineColor=None, fillColor='white',
        opacity=None, depth=-2.0, interpolate=True)
    Flan2 = visual.Rect(
        win=win, name='Flan2',
        width=(0.15, 0.15)[0], height=(0.15, 0.15)[1],
        ori=0.0, pos=[0,0], draggable=False, anchor='center',
        lineWidth=2.0,
        colorSpace='rgb', lineColor=None, fillColor='white',
        opacity=None, depth=-3.0, interpolate=True)
    Flan3 = visual.Rect(
        win=win, name='Flan3',
        width=(0.15, 0.15)[0], height=(0.15, 0.15)[1],
        ori=0.0, pos=[0,0], draggable=False, anchor='center',
        lineWidth=2.0,
        colorSpace='rgb', lineColor=None, fillColor='white',
        opacity=None, depth=-4.0, interpolate=True)
    Flan4 = visual.Rect(
        win=win, name='Flan4',
        width=(0.15, 0.15)[0], height=(0.15, 0.15)[1],
        ori=0.0, pos=[0,0], draggable=False, anchor='center',
        lineWidth=2.0,
        colorSpace='rgb', lineColor=None, fillColor='white',
        opacity=None, depth=-5.0, interpolate=True)
    Flan5 = visual.Rect(
        win=win, name='Flan5',
        width=(0.15, 0.15)[0], height=(0.15, 0.15)[1],
        ori=0.0, pos=[0,0], draggable=False, anchor='center',
        lineWidth=2.0,
        colorSpace='rgb', lineColor=None, fillColor='white',
        opacity=None, depth=-6.0, interpolate=True)
    
    # --- Initialize components for Routine "ISI2" ---
    ISI2_cross = visual.TextStim(win=win, name='ISI2_cross',
        text='',
        font='Open Sans',
        pos=(0, 0), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    
    # --- Initialize components for Routine "Location_choice" ---
    mouse = event.Mouse(win=win)
    x, y = [None, None]
    mouse.mouseClock = core.Clock()
    Fixation_Point_2 = visual.TextStim(win=win, name='Fixation_Point_2',
        text='·',
        font='Open Sans',
        pos=(0, 0), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-2.0);
    Target_2 = visual.Rect(
        win=win, name='Target_2',
        width=(0.15, 0.15)[0], height=(0.15, 0.15)[1],
        ori=0.0, pos=[0,0], draggable=False, anchor='center',
        lineWidth=2.0,
        colorSpace='rgb', lineColor=None, fillColor='white',
        opacity=None, depth=-3.0, interpolate=True)
    Flan1_2 = visual.Rect(
        win=win, name='Flan1_2',
        width=(0.15, 0.15)[0], height=(0.15, 0.15)[1],
        ori=0.0, pos=[0,0], draggable=False, anchor='center',
        lineWidth=2.0,
        colorSpace='rgb', lineColor=None, fillColor='white',
        opacity=None, depth=-4.0, interpolate=True)
    Flan2_2 = visual.Rect(
        win=win, name='Flan2_2',
        width=(0.15, 0.15)[0], height=(0.15, 0.15)[1],
        ori=0.0, pos=[0,0], draggable=False, anchor='center',
        lineWidth=2.0,
        colorSpace='rgb', lineColor=None, fillColor='white',
        opacity=None, depth=-5.0, interpolate=True)
    Flan3_2 = visual.Rect(
        win=win, name='Flan3_2',
        width=(0.15, 0.15)[0], height=(0.15, 0.15)[1],
        ori=0.0, pos=[0,0], draggable=False, anchor='center',
        lineWidth=2.0,
        colorSpace='rgb', lineColor=None, fillColor='white',
        opacity=None, depth=-6.0, interpolate=True)
    Flan4_2 = visual.Rect(
        win=win, name='Flan4_2',
        width=(0.15, 0.15)[0], height=(0.15, 0.15)[1],
        ori=0.0, pos=[0,0], draggable=False, anchor='center',
        lineWidth=2.0,
        colorSpace='rgb', lineColor=None, fillColor='white',
        opacity=None, depth=-7.0, interpolate=True)
    Flan5_2 = visual.Rect(
        win=win, name='Flan5_2',
        width=(0.15, 0.15)[0], height=(0.15, 0.15)[1],
        ori=0.0, pos=[0,0], draggable=False, anchor='center',
        lineWidth=2.0,
        colorSpace='rgb', lineColor=None, fillColor='white',
        opacity=None, depth=-8.0, interpolate=True)
    
    # --- Initialize components for Routine "ISI3" ---
    ISI3_cross = visual.TextStim(win=win, name='ISI3_cross',
        text=' ',
        font='Open Sans',
        pos=(0, 0), draggable=False, height=0.075, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    
    # --- Initialize components for Routine "Colour_choice" ---
    mouse_2 = event.Mouse(win=win)
    x, y = [None, None]
    mouse_2.mouseClock = core.Clock()
    
    # --- Initialize components for Routine "Clear_Screen" ---
    
    # --- Initialize components for Routine "BlockAdder" ---
    text = visual.TextStim(win=win, name='text',
        text=' ',
        font='Open Sans',
        pos=(0, 0), draggable=False, height=0.1, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-1.0);
    
    # --- Initialize components for Routine "EndScreen" ---
    EndScreenText = visual.TextStim(win=win, name='EndScreenText',
        text="You have now completed the experiment. Thank you.\n\nPlease inform the researcher.\n\nPress 'qt' to close this window.",
        font='Open Sans',
        pos=(0, 0), draggable=False, height=0.05, wrapWidth=0.65, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    
    # create some handy timers
    
    # global clock to track the time since experiment started
    if globalClock is None:
        # create a clock if not given one
        globalClock = core.Clock()
    if isinstance(globalClock, str):
        # if given a string, make a clock accoridng to it
        if globalClock == 'float':
            # get timestamps as a simple value
            globalClock = core.Clock(format='float')
        elif globalClock == 'iso':
            # get timestamps in ISO format
            globalClock = core.Clock(format='%Y-%m-%d_%H:%M:%S.%f%z')
        else:
            # get timestamps in a custom format
            globalClock = core.Clock(format=globalClock)
    if ioServer is not None:
        ioServer.syncClock(globalClock)
    logging.setDefaultClock(globalClock)
    # routine timer to track time remaining of each (possibly non-slip) routine
    routineTimer = core.Clock()
    win.flip()  # flip window to reset last flip timer
    # store the exact time the global clock started
    expInfo['expStart'] = data.getDateStr(
        format='%Y-%m-%d %Hh%M.%S.%f %z', fractionalSecondDigits=6
    )
    
    # --- Prepare to start Routine "Startup_code" ---
    # create an object to store info about Routine Startup_code
    Startup_code = data.Routine(
        name='Startup_code',
        components=[],
    )
    Startup_code.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # Run 'Begin Routine' code from Definitions
    win.setMouseVisible(False)
    mouse.setPos(newPos=(0,0))
    # store start times for Startup_code
    Startup_code.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    Startup_code.tStart = globalClock.getTime(format='float')
    Startup_code.status = STARTED
    thisExp.addData('Startup_code.started', Startup_code.tStart)
    Startup_code.maxDuration = None
    # keep track of which components have finished
    Startup_codeComponents = Startup_code.components
    for thisComponent in Startup_code.components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "Startup_code" ---
    Startup_code.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer], 
                playbackComponents=[]
            )
            # skip the frame we paused on
            continue
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            Startup_code.forceEnded = routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Startup_code.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "Startup_code" ---
    for thisComponent in Startup_code.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for Startup_code
    Startup_code.tStop = globalClock.getTime(format='float')
    Startup_code.tStopRefresh = tThisFlipGlobal
    thisExp.addData('Startup_code.stopped', Startup_code.tStop)
    thisExp.nextEntry()
    # the Routine "Startup_code" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "Startup_screen" ---
    # create an object to store info about Routine Startup_screen
    Startup_screen = data.Routine(
        name='Startup_screen',
        components=[NumberOBlocks_4, ContinueButtonText_2, Version_Text, ContinueButton_2, mouse_4],
    )
    Startup_screen.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    NumberOBlocks_4.setText("Welcome to the 'Colour Change Detection Task'. Version \n\nInstructions for this task will appear on the next screen.")
    # Run 'Begin Routine' code from Button_Animation_2
    win.setMouseVisible(True)
    # setup some python lists for storing info about the mouse_4
    mouse_4.clicked_name = []
    gotValidClick = False  # until a click is received
    # store start times for Startup_screen
    Startup_screen.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    Startup_screen.tStart = globalClock.getTime(format='float')
    Startup_screen.status = STARTED
    thisExp.addData('Startup_screen.started', Startup_screen.tStart)
    Startup_screen.maxDuration = None
    # keep track of which components have finished
    Startup_screenComponents = Startup_screen.components
    for thisComponent in Startup_screen.components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "Startup_screen" ---
    Startup_screen.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *NumberOBlocks_4* updates
        
        # if NumberOBlocks_4 is starting this frame...
        if NumberOBlocks_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            NumberOBlocks_4.frameNStart = frameN  # exact frame index
            NumberOBlocks_4.tStart = t  # local t and not account for scr refresh
            NumberOBlocks_4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(NumberOBlocks_4, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'NumberOBlocks_4.started')
            # update status
            NumberOBlocks_4.status = STARTED
            NumberOBlocks_4.setAutoDraw(True)
        
        # if NumberOBlocks_4 is active this frame...
        if NumberOBlocks_4.status == STARTED:
            # update params
            pass
        
        # *ContinueButtonText_2* updates
        
        # if ContinueButtonText_2 is starting this frame...
        if ContinueButtonText_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            ContinueButtonText_2.frameNStart = frameN  # exact frame index
            ContinueButtonText_2.tStart = t  # local t and not account for scr refresh
            ContinueButtonText_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(ContinueButtonText_2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'ContinueButtonText_2.started')
            # update status
            ContinueButtonText_2.status = STARTED
            ContinueButtonText_2.setAutoDraw(True)
        
        # if ContinueButtonText_2 is active this frame...
        if ContinueButtonText_2.status == STARTED:
            # update params
            ContinueButtonText_2.setColor('white', colorSpace='rgb', log=False)
        
        # *Version_Text* updates
        
        # if Version_Text is starting this frame...
        if Version_Text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Version_Text.frameNStart = frameN  # exact frame index
            Version_Text.tStart = t  # local t and not account for scr refresh
            Version_Text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Version_Text, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'Version_Text.started')
            # update status
            Version_Text.status = STARTED
            Version_Text.setAutoDraw(True)
        
        # if Version_Text is active this frame...
        if Version_Text.status == STARTED:
            # update params
            pass
        
        # *ContinueButton_2* updates
        
        # if ContinueButton_2 is starting this frame...
        if ContinueButton_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            ContinueButton_2.frameNStart = frameN  # exact frame index
            ContinueButton_2.tStart = t  # local t and not account for scr refresh
            ContinueButton_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(ContinueButton_2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'ContinueButton_2.started')
            # update status
            ContinueButton_2.status = STARTED
            ContinueButton_2.setAutoDraw(True)
        
        # if ContinueButton_2 is active this frame...
        if ContinueButton_2.status == STARTED:
            # update params
            ContinueButton_2.setLineColor('white', log=False)
        # Run 'Each Frame' code from Button_Animation_2
        if ContinueButton_2.contains(mouse):
            ContinueButton_2.lineColor = 'yellow'
            ContinueButtonText_2.color = 'yellow'
        else:
            ContinueButton_2.lineColor = 'white'
            ContinueButtonText_2.color = 'white'
        # *mouse_4* updates
        
        # if mouse_4 is starting this frame...
        if mouse_4.status == NOT_STARTED and t >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            mouse_4.frameNStart = frameN  # exact frame index
            mouse_4.tStart = t  # local t and not account for scr refresh
            mouse_4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(mouse_4, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.addData('mouse_4.started', t)
            # update status
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
                    clickableList = environmenttools.getFromNames(ContinueButton, namespace=locals())
                    for obj in clickableList:
                        # is this object clicked on?
                        if obj.contains(mouse_4):
                            gotValidClick = True
                            mouse_4.clicked_name.append(obj.name)
                    if not gotValidClick:
                        mouse_4.clicked_name.append(None)
                    if gotValidClick:  
                        continueRoutine = False  # end routine on response
        # Run 'Each Frame' code from QuitChecker
        keys = event.getKeys()
        if 'q' in keys and 't' in keys:
                core.quit()
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer], 
                playbackComponents=[]
            )
            # skip the frame we paused on
            continue
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            Startup_screen.forceEnded = routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Startup_screen.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "Startup_screen" ---
    for thisComponent in Startup_screen.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for Startup_screen
    Startup_screen.tStop = globalClock.getTime(format='float')
    Startup_screen.tStopRefresh = tThisFlipGlobal
    thisExp.addData('Startup_screen.stopped', Startup_screen.tStop)
    # store data for thisExp (ExperimentHandler)
    x, y = mouse_4.getPos()
    buttons = mouse_4.getPressed()
    if sum(buttons):
        # check if the mouse was inside our 'clickable' objects
        gotValidClick = False
        clickableList = environmenttools.getFromNames(ContinueButton, namespace=locals())
        for obj in clickableList:
            # is this object clicked on?
            if obj.contains(mouse_4):
                gotValidClick = True
                mouse_4.clicked_name.append(obj.name)
        if not gotValidClick:
            mouse_4.clicked_name.append(None)
    thisExp.addData('mouse_4.x', x)
    thisExp.addData('mouse_4.y', y)
    thisExp.addData('mouse_4.leftButton', buttons[0])
    thisExp.addData('mouse_4.midButton', buttons[1])
    thisExp.addData('mouse_4.rightButton', buttons[2])
    if len(mouse_4.clicked_name):
        thisExp.addData('mouse_4.clicked_name', mouse_4.clicked_name[0])
    thisExp.nextEntry()
    # the Routine "Startup_screen" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "Instructions_Begin" ---
    # create an object to store info about Routine Instructions_Begin
    Instructions_Begin = data.Routine(
        name='Instructions_Begin',
        components=[NumberOBlocks_5, ContinueButtonText_3, ContinueButton_3, mouse_5],
    )
    Instructions_Begin.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    NumberOBlocks_5.setText('In this task, you must detect changes which appear onscreen.\n\nA set of squares will appear for a short period. After, the squares will reappear with one square having a new colour.\n\nPlease remember the original colour of the square.')
    # Run 'Begin Routine' code from Button_Animation_3
    win.setMouseVisible(True)
    # setup some python lists for storing info about the mouse_5
    mouse_5.clicked_name = []
    gotValidClick = False  # until a click is received
    # store start times for Instructions_Begin
    Instructions_Begin.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    Instructions_Begin.tStart = globalClock.getTime(format='float')
    Instructions_Begin.status = STARTED
    thisExp.addData('Instructions_Begin.started', Instructions_Begin.tStart)
    Instructions_Begin.maxDuration = None
    # keep track of which components have finished
    Instructions_BeginComponents = Instructions_Begin.components
    for thisComponent in Instructions_Begin.components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "Instructions_Begin" ---
    Instructions_Begin.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *NumberOBlocks_5* updates
        
        # if NumberOBlocks_5 is starting this frame...
        if NumberOBlocks_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            NumberOBlocks_5.frameNStart = frameN  # exact frame index
            NumberOBlocks_5.tStart = t  # local t and not account for scr refresh
            NumberOBlocks_5.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(NumberOBlocks_5, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'NumberOBlocks_5.started')
            # update status
            NumberOBlocks_5.status = STARTED
            NumberOBlocks_5.setAutoDraw(True)
        
        # if NumberOBlocks_5 is active this frame...
        if NumberOBlocks_5.status == STARTED:
            # update params
            pass
        
        # *ContinueButtonText_3* updates
        
        # if ContinueButtonText_3 is starting this frame...
        if ContinueButtonText_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            ContinueButtonText_3.frameNStart = frameN  # exact frame index
            ContinueButtonText_3.tStart = t  # local t and not account for scr refresh
            ContinueButtonText_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(ContinueButtonText_3, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'ContinueButtonText_3.started')
            # update status
            ContinueButtonText_3.status = STARTED
            ContinueButtonText_3.setAutoDraw(True)
        
        # if ContinueButtonText_3 is active this frame...
        if ContinueButtonText_3.status == STARTED:
            # update params
            ContinueButtonText_3.setColor('white', colorSpace='rgb', log=False)
        
        # *ContinueButton_3* updates
        
        # if ContinueButton_3 is starting this frame...
        if ContinueButton_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            ContinueButton_3.frameNStart = frameN  # exact frame index
            ContinueButton_3.tStart = t  # local t and not account for scr refresh
            ContinueButton_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(ContinueButton_3, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'ContinueButton_3.started')
            # update status
            ContinueButton_3.status = STARTED
            ContinueButton_3.setAutoDraw(True)
        
        # if ContinueButton_3 is active this frame...
        if ContinueButton_3.status == STARTED:
            # update params
            ContinueButton_3.setLineColor('white', log=False)
        # Run 'Each Frame' code from Button_Animation_3
        if ContinueButton_3.contains(mouse):
            ContinueButton_3.lineColor = 'yellow'
            ContinueButtonText_3.color = 'yellow'
        else:
            ContinueButton_3.lineColor = 'white'
            ContinueButtonText_3.color = 'white'
        # *mouse_5* updates
        
        # if mouse_5 is starting this frame...
        if mouse_5.status == NOT_STARTED and t >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            mouse_5.frameNStart = frameN  # exact frame index
            mouse_5.tStart = t  # local t and not account for scr refresh
            mouse_5.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(mouse_5, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.addData('mouse_5.started', t)
            # update status
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
                    clickableList = environmenttools.getFromNames(ContinueButton, namespace=locals())
                    for obj in clickableList:
                        # is this object clicked on?
                        if obj.contains(mouse_5):
                            gotValidClick = True
                            mouse_5.clicked_name.append(obj.name)
                    if not gotValidClick:
                        mouse_5.clicked_name.append(None)
                    if gotValidClick:  
                        continueRoutine = False  # end routine on response
        # Run 'Each Frame' code from QuitChecker_2
        keys = event.getKeys()
        if 'q' in keys and 't' in keys:
                core.quit()
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer], 
                playbackComponents=[]
            )
            # skip the frame we paused on
            continue
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            Instructions_Begin.forceEnded = routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Instructions_Begin.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "Instructions_Begin" ---
    for thisComponent in Instructions_Begin.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for Instructions_Begin
    Instructions_Begin.tStop = globalClock.getTime(format='float')
    Instructions_Begin.tStopRefresh = tThisFlipGlobal
    thisExp.addData('Instructions_Begin.stopped', Instructions_Begin.tStop)
    # store data for thisExp (ExperimentHandler)
    x, y = mouse_5.getPos()
    buttons = mouse_5.getPressed()
    if sum(buttons):
        # check if the mouse was inside our 'clickable' objects
        gotValidClick = False
        clickableList = environmenttools.getFromNames(ContinueButton, namespace=locals())
        for obj in clickableList:
            # is this object clicked on?
            if obj.contains(mouse_5):
                gotValidClick = True
                mouse_5.clicked_name.append(obj.name)
        if not gotValidClick:
            mouse_5.clicked_name.append(None)
    thisExp.addData('mouse_5.x', x)
    thisExp.addData('mouse_5.y', y)
    thisExp.addData('mouse_5.leftButton', buttons[0])
    thisExp.addData('mouse_5.midButton', buttons[1])
    thisExp.addData('mouse_5.rightButton', buttons[2])
    if len(mouse_5.clicked_name):
        thisExp.addData('mouse_5.clicked_name', mouse_5.clicked_name[0])
    thisExp.nextEntry()
    # the Routine "Instructions_Begin" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "Instructions_Begin_2" ---
    # create an object to store info about Routine Instructions_Begin_2
    Instructions_Begin_2 = data.Routine(
        name='Instructions_Begin_2',
        components=[NumberOBlocks_6, ContinueButtonText_4, ContinueButton_4, mouse_6],
    )
    Instructions_Begin_2.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    NumberOBlocks_6.setText('Once the squares reappear, click on the square which changed.\n\nThen, identify the original colour of the square using the colour wheel.\n\nYou are being timed.\n\nYou will now complete a quick tutorial.\n\n')
    # Run 'Begin Routine' code from Button_Animation_4
    win.setMouseVisible(True)
    # setup some python lists for storing info about the mouse_6
    mouse_6.clicked_name = []
    gotValidClick = False  # until a click is received
    # store start times for Instructions_Begin_2
    Instructions_Begin_2.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    Instructions_Begin_2.tStart = globalClock.getTime(format='float')
    Instructions_Begin_2.status = STARTED
    thisExp.addData('Instructions_Begin_2.started', Instructions_Begin_2.tStart)
    Instructions_Begin_2.maxDuration = None
    # keep track of which components have finished
    Instructions_Begin_2Components = Instructions_Begin_2.components
    for thisComponent in Instructions_Begin_2.components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "Instructions_Begin_2" ---
    Instructions_Begin_2.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *NumberOBlocks_6* updates
        
        # if NumberOBlocks_6 is starting this frame...
        if NumberOBlocks_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            NumberOBlocks_6.frameNStart = frameN  # exact frame index
            NumberOBlocks_6.tStart = t  # local t and not account for scr refresh
            NumberOBlocks_6.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(NumberOBlocks_6, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'NumberOBlocks_6.started')
            # update status
            NumberOBlocks_6.status = STARTED
            NumberOBlocks_6.setAutoDraw(True)
        
        # if NumberOBlocks_6 is active this frame...
        if NumberOBlocks_6.status == STARTED:
            # update params
            pass
        
        # *ContinueButtonText_4* updates
        
        # if ContinueButtonText_4 is starting this frame...
        if ContinueButtonText_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            ContinueButtonText_4.frameNStart = frameN  # exact frame index
            ContinueButtonText_4.tStart = t  # local t and not account for scr refresh
            ContinueButtonText_4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(ContinueButtonText_4, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'ContinueButtonText_4.started')
            # update status
            ContinueButtonText_4.status = STARTED
            ContinueButtonText_4.setAutoDraw(True)
        
        # if ContinueButtonText_4 is active this frame...
        if ContinueButtonText_4.status == STARTED:
            # update params
            ContinueButtonText_4.setColor('white', colorSpace='rgb', log=False)
        
        # *ContinueButton_4* updates
        
        # if ContinueButton_4 is starting this frame...
        if ContinueButton_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            ContinueButton_4.frameNStart = frameN  # exact frame index
            ContinueButton_4.tStart = t  # local t and not account for scr refresh
            ContinueButton_4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(ContinueButton_4, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'ContinueButton_4.started')
            # update status
            ContinueButton_4.status = STARTED
            ContinueButton_4.setAutoDraw(True)
        
        # if ContinueButton_4 is active this frame...
        if ContinueButton_4.status == STARTED:
            # update params
            ContinueButton_4.setLineColor('white', log=False)
        # Run 'Each Frame' code from Button_Animation_4
        if ContinueButton_4.contains(mouse):
            ContinueButton_4.lineColor = 'yellow'
            ContinueButtonText_4.color = 'yellow'
        else:
            ContinueButton_4.lineColor = 'white'
            ContinueButtonText_4.color = 'white'
        # *mouse_6* updates
        
        # if mouse_6 is starting this frame...
        if mouse_6.status == NOT_STARTED and t >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            mouse_6.frameNStart = frameN  # exact frame index
            mouse_6.tStart = t  # local t and not account for scr refresh
            mouse_6.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(mouse_6, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.addData('mouse_6.started', t)
            # update status
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
                    clickableList = environmenttools.getFromNames(ContinueButton, namespace=locals())
                    for obj in clickableList:
                        # is this object clicked on?
                        if obj.contains(mouse_6):
                            gotValidClick = True
                            mouse_6.clicked_name.append(obj.name)
                    if not gotValidClick:
                        mouse_6.clicked_name.append(None)
                    if gotValidClick:  
                        continueRoutine = False  # end routine on response
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer], 
                playbackComponents=[]
            )
            # skip the frame we paused on
            continue
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            Instructions_Begin_2.forceEnded = routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Instructions_Begin_2.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "Instructions_Begin_2" ---
    for thisComponent in Instructions_Begin_2.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for Instructions_Begin_2
    Instructions_Begin_2.tStop = globalClock.getTime(format='float')
    Instructions_Begin_2.tStopRefresh = tThisFlipGlobal
    thisExp.addData('Instructions_Begin_2.stopped', Instructions_Begin_2.tStop)
    # store data for thisExp (ExperimentHandler)
    x, y = mouse_6.getPos()
    buttons = mouse_6.getPressed()
    if sum(buttons):
        # check if the mouse was inside our 'clickable' objects
        gotValidClick = False
        clickableList = environmenttools.getFromNames(ContinueButton, namespace=locals())
        for obj in clickableList:
            # is this object clicked on?
            if obj.contains(mouse_6):
                gotValidClick = True
                mouse_6.clicked_name.append(obj.name)
        if not gotValidClick:
            mouse_6.clicked_name.append(None)
    thisExp.addData('mouse_6.x', x)
    thisExp.addData('mouse_6.y', y)
    thisExp.addData('mouse_6.leftButton', buttons[0])
    thisExp.addData('mouse_6.midButton', buttons[1])
    thisExp.addData('mouse_6.rightButton', buttons[2])
    if len(mouse_6.clicked_name):
        thisExp.addData('mouse_6.clicked_name', mouse_6.clicked_name[0])
    thisExp.nextEntry()
    # the Routine "Instructions_Begin_2" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "ISI_tutorial" ---
    # create an object to store info about Routine ISI_tutorial
    ISI_tutorial = data.Routine(
        name='ISI_tutorial',
        components=[ISI1_cross_2],
    )
    ISI_tutorial.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    ISI1_cross_2.setText('·')
    # Run 'Begin Routine' code from Mouse_wipe_3
    win.setMouseVisible(False)
    
    # store start times for ISI_tutorial
    ISI_tutorial.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    ISI_tutorial.tStart = globalClock.getTime(format='float')
    ISI_tutorial.status = STARTED
    thisExp.addData('ISI_tutorial.started', ISI_tutorial.tStart)
    ISI_tutorial.maxDuration = None
    # keep track of which components have finished
    ISI_tutorialComponents = ISI_tutorial.components
    for thisComponent in ISI_tutorial.components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "ISI_tutorial" ---
    ISI_tutorial.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine and routineTimer.getTime() < 0.9:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *ISI1_cross_2* updates
        
        # if ISI1_cross_2 is starting this frame...
        if ISI1_cross_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            ISI1_cross_2.frameNStart = frameN  # exact frame index
            ISI1_cross_2.tStart = t  # local t and not account for scr refresh
            ISI1_cross_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(ISI1_cross_2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'ISI1_cross_2.started')
            # update status
            ISI1_cross_2.status = STARTED
            ISI1_cross_2.setAutoDraw(True)
        
        # if ISI1_cross_2 is active this frame...
        if ISI1_cross_2.status == STARTED:
            # update params
            pass
        
        # if ISI1_cross_2 is stopping this frame...
        if ISI1_cross_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > ISI1_cross_2.tStartRefresh + 0.9-frameTolerance:
                # keep track of stop time/frame for later
                ISI1_cross_2.tStop = t  # not accounting for scr refresh
                ISI1_cross_2.tStopRefresh = tThisFlipGlobal  # on global time
                ISI1_cross_2.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'ISI1_cross_2.stopped')
                # update status
                ISI1_cross_2.status = FINISHED
                ISI1_cross_2.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer], 
                playbackComponents=[]
            )
            # skip the frame we paused on
            continue
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            ISI_tutorial.forceEnded = routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in ISI_tutorial.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "ISI_tutorial" ---
    for thisComponent in ISI_tutorial.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for ISI_tutorial
    ISI_tutorial.tStop = globalClock.getTime(format='float')
    ISI_tutorial.tStopRefresh = tThisFlipGlobal
    thisExp.addData('ISI_tutorial.stopped', ISI_tutorial.tStop)
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if ISI_tutorial.maxDurationReached:
        routineTimer.addTime(-ISI_tutorial.maxDuration)
    elif ISI_tutorial.forceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-0.900000)
    thisExp.nextEntry()
    
    # --- Prepare to start Routine "Stimulus_disp_tutorial" ---
    # create an object to store info about Routine Stimulus_disp_tutorial
    Stimulus_disp_tutorial = data.Routine(
        name='Stimulus_disp_tutorial',
        components=[Fixation_Point_3, Target_3, Flan1_3, Flan2_3, Flan3_3, Flan4_3, Flan5_3],
    )
    Stimulus_disp_tutorial.status = NOT_STARTED
    continueRoutine = True
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
    # store start times for Stimulus_disp_tutorial
    Stimulus_disp_tutorial.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    Stimulus_disp_tutorial.tStart = globalClock.getTime(format='float')
    Stimulus_disp_tutorial.status = STARTED
    thisExp.addData('Stimulus_disp_tutorial.started', Stimulus_disp_tutorial.tStart)
    Stimulus_disp_tutorial.maxDuration = None
    # keep track of which components have finished
    Stimulus_disp_tutorialComponents = Stimulus_disp_tutorial.components
    for thisComponent in Stimulus_disp_tutorial.components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "Stimulus_disp_tutorial" ---
    Stimulus_disp_tutorial.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine and routineTimer.getTime() < 0.3:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *Fixation_Point_3* updates
        
        # if Fixation_Point_3 is starting this frame...
        if Fixation_Point_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Fixation_Point_3.frameNStart = frameN  # exact frame index
            Fixation_Point_3.tStart = t  # local t and not account for scr refresh
            Fixation_Point_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Fixation_Point_3, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'Fixation_Point_3.started')
            # update status
            Fixation_Point_3.status = STARTED
            Fixation_Point_3.setAutoDraw(True)
        
        # if Fixation_Point_3 is active this frame...
        if Fixation_Point_3.status == STARTED:
            # update params
            pass
        
        # if Fixation_Point_3 is stopping this frame...
        if Fixation_Point_3.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Fixation_Point_3.tStartRefresh + 0.3-frameTolerance:
                # keep track of stop time/frame for later
                Fixation_Point_3.tStop = t  # not accounting for scr refresh
                Fixation_Point_3.tStopRefresh = tThisFlipGlobal  # on global time
                Fixation_Point_3.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'Fixation_Point_3.stopped')
                # update status
                Fixation_Point_3.status = FINISHED
                Fixation_Point_3.setAutoDraw(False)
        
        # *Target_3* updates
        
        # if Target_3 is starting this frame...
        if Target_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Target_3.frameNStart = frameN  # exact frame index
            Target_3.tStart = t  # local t and not account for scr refresh
            Target_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Target_3, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'Target_3.started')
            # update status
            Target_3.status = STARTED
            Target_3.setAutoDraw(True)
        
        # if Target_3 is active this frame...
        if Target_3.status == STARTED:
            # update params
            pass
        
        # if Target_3 is stopping this frame...
        if Target_3.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Target_3.tStartRefresh + 0.3-frameTolerance:
                # keep track of stop time/frame for later
                Target_3.tStop = t  # not accounting for scr refresh
                Target_3.tStopRefresh = tThisFlipGlobal  # on global time
                Target_3.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'Target_3.stopped')
                # update status
                Target_3.status = FINISHED
                Target_3.setAutoDraw(False)
        
        # *Flan1_3* updates
        
        # if Flan1_3 is starting this frame...
        if Flan1_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Flan1_3.frameNStart = frameN  # exact frame index
            Flan1_3.tStart = t  # local t and not account for scr refresh
            Flan1_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Flan1_3, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'Flan1_3.started')
            # update status
            Flan1_3.status = STARTED
            Flan1_3.setAutoDraw(True)
        
        # if Flan1_3 is active this frame...
        if Flan1_3.status == STARTED:
            # update params
            pass
        
        # if Flan1_3 is stopping this frame...
        if Flan1_3.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Flan1_3.tStartRefresh + 0.3-frameTolerance:
                # keep track of stop time/frame for later
                Flan1_3.tStop = t  # not accounting for scr refresh
                Flan1_3.tStopRefresh = tThisFlipGlobal  # on global time
                Flan1_3.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'Flan1_3.stopped')
                # update status
                Flan1_3.status = FINISHED
                Flan1_3.setAutoDraw(False)
        
        # *Flan2_3* updates
        
        # if Flan2_3 is starting this frame...
        if Flan2_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Flan2_3.frameNStart = frameN  # exact frame index
            Flan2_3.tStart = t  # local t and not account for scr refresh
            Flan2_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Flan2_3, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'Flan2_3.started')
            # update status
            Flan2_3.status = STARTED
            Flan2_3.setAutoDraw(True)
        
        # if Flan2_3 is active this frame...
        if Flan2_3.status == STARTED:
            # update params
            pass
        
        # if Flan2_3 is stopping this frame...
        if Flan2_3.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Flan2_3.tStartRefresh + 0.3-frameTolerance:
                # keep track of stop time/frame for later
                Flan2_3.tStop = t  # not accounting for scr refresh
                Flan2_3.tStopRefresh = tThisFlipGlobal  # on global time
                Flan2_3.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'Flan2_3.stopped')
                # update status
                Flan2_3.status = FINISHED
                Flan2_3.setAutoDraw(False)
        
        # *Flan3_3* updates
        
        # if Flan3_3 is starting this frame...
        if Flan3_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Flan3_3.frameNStart = frameN  # exact frame index
            Flan3_3.tStart = t  # local t and not account for scr refresh
            Flan3_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Flan3_3, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'Flan3_3.started')
            # update status
            Flan3_3.status = STARTED
            Flan3_3.setAutoDraw(True)
        
        # if Flan3_3 is active this frame...
        if Flan3_3.status == STARTED:
            # update params
            pass
        
        # if Flan3_3 is stopping this frame...
        if Flan3_3.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Flan3_3.tStartRefresh + 0.3-frameTolerance:
                # keep track of stop time/frame for later
                Flan3_3.tStop = t  # not accounting for scr refresh
                Flan3_3.tStopRefresh = tThisFlipGlobal  # on global time
                Flan3_3.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'Flan3_3.stopped')
                # update status
                Flan3_3.status = FINISHED
                Flan3_3.setAutoDraw(False)
        
        # *Flan4_3* updates
        
        # if Flan4_3 is starting this frame...
        if Flan4_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Flan4_3.frameNStart = frameN  # exact frame index
            Flan4_3.tStart = t  # local t and not account for scr refresh
            Flan4_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Flan4_3, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'Flan4_3.started')
            # update status
            Flan4_3.status = STARTED
            Flan4_3.setAutoDraw(True)
        
        # if Flan4_3 is active this frame...
        if Flan4_3.status == STARTED:
            # update params
            pass
        
        # if Flan4_3 is stopping this frame...
        if Flan4_3.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Flan4_3.tStartRefresh + 0.3-frameTolerance:
                # keep track of stop time/frame for later
                Flan4_3.tStop = t  # not accounting for scr refresh
                Flan4_3.tStopRefresh = tThisFlipGlobal  # on global time
                Flan4_3.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'Flan4_3.stopped')
                # update status
                Flan4_3.status = FINISHED
                Flan4_3.setAutoDraw(False)
        
        # *Flan5_3* updates
        
        # if Flan5_3 is starting this frame...
        if Flan5_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Flan5_3.frameNStart = frameN  # exact frame index
            Flan5_3.tStart = t  # local t and not account for scr refresh
            Flan5_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Flan5_3, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'Flan5_3.started')
            # update status
            Flan5_3.status = STARTED
            Flan5_3.setAutoDraw(True)
        
        # if Flan5_3 is active this frame...
        if Flan5_3.status == STARTED:
            # update params
            pass
        
        # if Flan5_3 is stopping this frame...
        if Flan5_3.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Flan5_3.tStartRefresh + 0.3-frameTolerance:
                # keep track of stop time/frame for later
                Flan5_3.tStop = t  # not accounting for scr refresh
                Flan5_3.tStopRefresh = tThisFlipGlobal  # on global time
                Flan5_3.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'Flan5_3.stopped')
                # update status
                Flan5_3.status = FINISHED
                Flan5_3.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer], 
                playbackComponents=[]
            )
            # skip the frame we paused on
            continue
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            Stimulus_disp_tutorial.forceEnded = routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Stimulus_disp_tutorial.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "Stimulus_disp_tutorial" ---
    for thisComponent in Stimulus_disp_tutorial.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for Stimulus_disp_tutorial
    Stimulus_disp_tutorial.tStop = globalClock.getTime(format='float')
    Stimulus_disp_tutorial.tStopRefresh = tThisFlipGlobal
    thisExp.addData('Stimulus_disp_tutorial.stopped', Stimulus_disp_tutorial.tStop)
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if Stimulus_disp_tutorial.maxDurationReached:
        routineTimer.addTime(-Stimulus_disp_tutorial.maxDuration)
    elif Stimulus_disp_tutorial.forceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-0.300000)
    thisExp.nextEntry()
    
    # --- Prepare to start Routine "ISI_tutorial" ---
    # create an object to store info about Routine ISI_tutorial
    ISI_tutorial = data.Routine(
        name='ISI_tutorial',
        components=[ISI1_cross_2],
    )
    ISI_tutorial.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    ISI1_cross_2.setText('·')
    # Run 'Begin Routine' code from Mouse_wipe_3
    win.setMouseVisible(False)
    
    # store start times for ISI_tutorial
    ISI_tutorial.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    ISI_tutorial.tStart = globalClock.getTime(format='float')
    ISI_tutorial.status = STARTED
    thisExp.addData('ISI_tutorial.started', ISI_tutorial.tStart)
    ISI_tutorial.maxDuration = None
    # keep track of which components have finished
    ISI_tutorialComponents = ISI_tutorial.components
    for thisComponent in ISI_tutorial.components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "ISI_tutorial" ---
    ISI_tutorial.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine and routineTimer.getTime() < 0.9:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *ISI1_cross_2* updates
        
        # if ISI1_cross_2 is starting this frame...
        if ISI1_cross_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            ISI1_cross_2.frameNStart = frameN  # exact frame index
            ISI1_cross_2.tStart = t  # local t and not account for scr refresh
            ISI1_cross_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(ISI1_cross_2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'ISI1_cross_2.started')
            # update status
            ISI1_cross_2.status = STARTED
            ISI1_cross_2.setAutoDraw(True)
        
        # if ISI1_cross_2 is active this frame...
        if ISI1_cross_2.status == STARTED:
            # update params
            pass
        
        # if ISI1_cross_2 is stopping this frame...
        if ISI1_cross_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > ISI1_cross_2.tStartRefresh + 0.9-frameTolerance:
                # keep track of stop time/frame for later
                ISI1_cross_2.tStop = t  # not accounting for scr refresh
                ISI1_cross_2.tStopRefresh = tThisFlipGlobal  # on global time
                ISI1_cross_2.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'ISI1_cross_2.stopped')
                # update status
                ISI1_cross_2.status = FINISHED
                ISI1_cross_2.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer], 
                playbackComponents=[]
            )
            # skip the frame we paused on
            continue
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            ISI_tutorial.forceEnded = routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in ISI_tutorial.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "ISI_tutorial" ---
    for thisComponent in ISI_tutorial.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for ISI_tutorial
    ISI_tutorial.tStop = globalClock.getTime(format='float')
    ISI_tutorial.tStopRefresh = tThisFlipGlobal
    thisExp.addData('ISI_tutorial.stopped', ISI_tutorial.tStop)
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if ISI_tutorial.maxDurationReached:
        routineTimer.addTime(-ISI_tutorial.maxDuration)
    elif ISI_tutorial.forceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-0.900000)
    thisExp.nextEntry()
    
    # --- Prepare to start Routine "Loc_choice_tut" ---
    # create an object to store info about Routine Loc_choice_tut
    Loc_choice_tut = data.Routine(
        name='Loc_choice_tut',
        components=[mouse_8, Fixation_Point_5, Target_5, Flan1_5, Flan2_5, Flan3_5, Flan4_5, Flan5_5, ArrowHead, ArrowBar, InstruText2],
    )
    Loc_choice_tut.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # setup some python lists for storing info about the mouse_8
    mouse_8.clicked_name = []
    gotValidClick = False  # until a click is received
    # Run 'Begin Routine' code from code_3
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
    # store start times for Loc_choice_tut
    Loc_choice_tut.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    Loc_choice_tut.tStart = globalClock.getTime(format='float')
    Loc_choice_tut.status = STARTED
    thisExp.addData('Loc_choice_tut.started', Loc_choice_tut.tStart)
    Loc_choice_tut.maxDuration = None
    # keep track of which components have finished
    Loc_choice_tutComponents = Loc_choice_tut.components
    for thisComponent in Loc_choice_tut.components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "Loc_choice_tut" ---
    Loc_choice_tut.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        # *mouse_8* updates
        
        # if mouse_8 is starting this frame...
        if mouse_8.status == NOT_STARTED and t >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            mouse_8.frameNStart = frameN  # exact frame index
            mouse_8.tStart = t  # local t and not account for scr refresh
            mouse_8.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(mouse_8, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.addData('mouse_8.started', t)
            # update status
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
                    clickableList = environmenttools.getFromNames(Target_5, namespace=locals())
                    for obj in clickableList:
                        # is this object clicked on?
                        if obj.contains(mouse_8):
                            gotValidClick = True
                            mouse_8.clicked_name.append(obj.name)
                    if not gotValidClick:
                        mouse_8.clicked_name.append(None)
                    if gotValidClick:  
                        continueRoutine = False  # end routine on response
        # Run 'Each Frame' code from code_3
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
        
        # if Fixation_Point_5 is starting this frame...
        if Fixation_Point_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Fixation_Point_5.frameNStart = frameN  # exact frame index
            Fixation_Point_5.tStart = t  # local t and not account for scr refresh
            Fixation_Point_5.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Fixation_Point_5, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'Fixation_Point_5.started')
            # update status
            Fixation_Point_5.status = STARTED
            Fixation_Point_5.setAutoDraw(True)
        
        # if Fixation_Point_5 is active this frame...
        if Fixation_Point_5.status == STARTED:
            # update params
            pass
        
        # *Target_5* updates
        
        # if Target_5 is starting this frame...
        if Target_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Target_5.frameNStart = frameN  # exact frame index
            Target_5.tStart = t  # local t and not account for scr refresh
            Target_5.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Target_5, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'Target_5.started')
            # update status
            Target_5.status = STARTED
            Target_5.setAutoDraw(True)
        
        # if Target_5 is active this frame...
        if Target_5.status == STARTED:
            # update params
            pass
        
        # *Flan1_5* updates
        
        # if Flan1_5 is starting this frame...
        if Flan1_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Flan1_5.frameNStart = frameN  # exact frame index
            Flan1_5.tStart = t  # local t and not account for scr refresh
            Flan1_5.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Flan1_5, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'Flan1_5.started')
            # update status
            Flan1_5.status = STARTED
            Flan1_5.setAutoDraw(True)
        
        # if Flan1_5 is active this frame...
        if Flan1_5.status == STARTED:
            # update params
            pass
        
        # *Flan2_5* updates
        
        # if Flan2_5 is starting this frame...
        if Flan2_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Flan2_5.frameNStart = frameN  # exact frame index
            Flan2_5.tStart = t  # local t and not account for scr refresh
            Flan2_5.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Flan2_5, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'Flan2_5.started')
            # update status
            Flan2_5.status = STARTED
            Flan2_5.setAutoDraw(True)
        
        # if Flan2_5 is active this frame...
        if Flan2_5.status == STARTED:
            # update params
            pass
        
        # *Flan3_5* updates
        
        # if Flan3_5 is starting this frame...
        if Flan3_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Flan3_5.frameNStart = frameN  # exact frame index
            Flan3_5.tStart = t  # local t and not account for scr refresh
            Flan3_5.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Flan3_5, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'Flan3_5.started')
            # update status
            Flan3_5.status = STARTED
            Flan3_5.setAutoDraw(True)
        
        # if Flan3_5 is active this frame...
        if Flan3_5.status == STARTED:
            # update params
            pass
        
        # *Flan4_5* updates
        
        # if Flan4_5 is starting this frame...
        if Flan4_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Flan4_5.frameNStart = frameN  # exact frame index
            Flan4_5.tStart = t  # local t and not account for scr refresh
            Flan4_5.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Flan4_5, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'Flan4_5.started')
            # update status
            Flan4_5.status = STARTED
            Flan4_5.setAutoDraw(True)
        
        # if Flan4_5 is active this frame...
        if Flan4_5.status == STARTED:
            # update params
            pass
        
        # *Flan5_5* updates
        
        # if Flan5_5 is starting this frame...
        if Flan5_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Flan5_5.frameNStart = frameN  # exact frame index
            Flan5_5.tStart = t  # local t and not account for scr refresh
            Flan5_5.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Flan5_5, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'Flan5_5.started')
            # update status
            Flan5_5.status = STARTED
            Flan5_5.setAutoDraw(True)
        
        # if Flan5_5 is active this frame...
        if Flan5_5.status == STARTED:
            # update params
            pass
        
        # *ArrowHead* updates
        
        # if ArrowHead is starting this frame...
        if ArrowHead.status == NOT_STARTED and tThisFlip >= 2-frameTolerance:
            # keep track of start time/frame for later
            ArrowHead.frameNStart = frameN  # exact frame index
            ArrowHead.tStart = t  # local t and not account for scr refresh
            ArrowHead.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(ArrowHead, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'ArrowHead.started')
            # update status
            ArrowHead.status = STARTED
            ArrowHead.setAutoDraw(True)
        
        # if ArrowHead is active this frame...
        if ArrowHead.status == STARTED:
            # update params
            pass
        
        # *ArrowBar* updates
        
        # if ArrowBar is starting this frame...
        if ArrowBar.status == NOT_STARTED and tThisFlip >= 2-frameTolerance:
            # keep track of start time/frame for later
            ArrowBar.frameNStart = frameN  # exact frame index
            ArrowBar.tStart = t  # local t and not account for scr refresh
            ArrowBar.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(ArrowBar, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'ArrowBar.started')
            # update status
            ArrowBar.status = STARTED
            ArrowBar.setAutoDraw(True)
        
        # if ArrowBar is active this frame...
        if ArrowBar.status == STARTED:
            # update params
            pass
        
        # *InstruText2* updates
        
        # if InstruText2 is starting this frame...
        if InstruText2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            InstruText2.frameNStart = frameN  # exact frame index
            InstruText2.tStart = t  # local t and not account for scr refresh
            InstruText2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(InstruText2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'InstruText2.started')
            # update status
            InstruText2.status = STARTED
            InstruText2.setAutoDraw(True)
        
        # if InstruText2 is active this frame...
        if InstruText2.status == STARTED:
            # update params
            pass
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer], 
                playbackComponents=[]
            )
            # skip the frame we paused on
            continue
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            Loc_choice_tut.forceEnded = routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Loc_choice_tut.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "Loc_choice_tut" ---
    for thisComponent in Loc_choice_tut.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for Loc_choice_tut
    Loc_choice_tut.tStop = globalClock.getTime(format='float')
    Loc_choice_tut.tStopRefresh = tThisFlipGlobal
    thisExp.addData('Loc_choice_tut.stopped', Loc_choice_tut.tStop)
    # store data for thisExp (ExperimentHandler)
    x, y = mouse_8.getPos()
    buttons = mouse_8.getPressed()
    if sum(buttons):
        # check if the mouse was inside our 'clickable' objects
        gotValidClick = False
        clickableList = environmenttools.getFromNames(Target_5, namespace=locals())
        for obj in clickableList:
            # is this object clicked on?
            if obj.contains(mouse_8):
                gotValidClick = True
                mouse_8.clicked_name.append(obj.name)
        if not gotValidClick:
            mouse_8.clicked_name.append(None)
    thisExp.addData('mouse_8.x', x)
    thisExp.addData('mouse_8.y', y)
    thisExp.addData('mouse_8.leftButton', buttons[0])
    thisExp.addData('mouse_8.midButton', buttons[1])
    thisExp.addData('mouse_8.rightButton', buttons[2])
    if len(mouse_8.clicked_name):
        thisExp.addData('mouse_8.clicked_name', mouse_8.clicked_name[0])
    thisExp.nextEntry()
    # the Routine "Loc_choice_tut" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "ISI_tutorial" ---
    # create an object to store info about Routine ISI_tutorial
    ISI_tutorial = data.Routine(
        name='ISI_tutorial',
        components=[ISI1_cross_2],
    )
    ISI_tutorial.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    ISI1_cross_2.setText('·')
    # Run 'Begin Routine' code from Mouse_wipe_3
    win.setMouseVisible(False)
    
    # store start times for ISI_tutorial
    ISI_tutorial.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    ISI_tutorial.tStart = globalClock.getTime(format='float')
    ISI_tutorial.status = STARTED
    thisExp.addData('ISI_tutorial.started', ISI_tutorial.tStart)
    ISI_tutorial.maxDuration = None
    # keep track of which components have finished
    ISI_tutorialComponents = ISI_tutorial.components
    for thisComponent in ISI_tutorial.components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "ISI_tutorial" ---
    ISI_tutorial.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine and routineTimer.getTime() < 0.9:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *ISI1_cross_2* updates
        
        # if ISI1_cross_2 is starting this frame...
        if ISI1_cross_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            ISI1_cross_2.frameNStart = frameN  # exact frame index
            ISI1_cross_2.tStart = t  # local t and not account for scr refresh
            ISI1_cross_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(ISI1_cross_2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'ISI1_cross_2.started')
            # update status
            ISI1_cross_2.status = STARTED
            ISI1_cross_2.setAutoDraw(True)
        
        # if ISI1_cross_2 is active this frame...
        if ISI1_cross_2.status == STARTED:
            # update params
            pass
        
        # if ISI1_cross_2 is stopping this frame...
        if ISI1_cross_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > ISI1_cross_2.tStartRefresh + 0.9-frameTolerance:
                # keep track of stop time/frame for later
                ISI1_cross_2.tStop = t  # not accounting for scr refresh
                ISI1_cross_2.tStopRefresh = tThisFlipGlobal  # on global time
                ISI1_cross_2.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'ISI1_cross_2.stopped')
                # update status
                ISI1_cross_2.status = FINISHED
                ISI1_cross_2.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer], 
                playbackComponents=[]
            )
            # skip the frame we paused on
            continue
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            ISI_tutorial.forceEnded = routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in ISI_tutorial.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "ISI_tutorial" ---
    for thisComponent in ISI_tutorial.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for ISI_tutorial
    ISI_tutorial.tStop = globalClock.getTime(format='float')
    ISI_tutorial.tStopRefresh = tThisFlipGlobal
    thisExp.addData('ISI_tutorial.stopped', ISI_tutorial.tStop)
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if ISI_tutorial.maxDurationReached:
        routineTimer.addTime(-ISI_tutorial.maxDuration)
    elif ISI_tutorial.forceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-0.900000)
    thisExp.nextEntry()
    
    # --- Prepare to start Routine "Choice_tutorial" ---
    # create an object to store info about Routine Choice_tutorial
    Choice_tutorial = data.Routine(
        name='Choice_tutorial',
        components=[mouse_9, ArrowHead2, ArrowBar2, InstruText],
    )
    Choice_tutorial.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # Run 'Begin Routine' code from ColourChoice_2
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
    # store start times for Choice_tutorial
    Choice_tutorial.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    Choice_tutorial.tStart = globalClock.getTime(format='float')
    Choice_tutorial.status = STARTED
    thisExp.addData('Choice_tutorial.started', Choice_tutorial.tStart)
    Choice_tutorial.maxDuration = None
    # keep track of which components have finished
    Choice_tutorialComponents = Choice_tutorial.components
    for thisComponent in Choice_tutorial.components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "Choice_tutorial" ---
    Choice_tutorial.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        # Run 'Each Frame' code from ColourChoice_2
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
        
        # if mouse_9 is starting this frame...
        if mouse_9.status == NOT_STARTED and t >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            mouse_9.frameNStart = frameN  # exact frame index
            mouse_9.tStart = t  # local t and not account for scr refresh
            mouse_9.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(mouse_9, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.addData('mouse_9.started', t)
            # update status
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
                    clickableList = environmenttools.getFromNames(wedgeRedPurple, namespace=locals())
                    for obj in clickableList:
                        # is this object clicked on?
                        if obj.contains(mouse_9):
                            gotValidClick = True
                            mouse_9.clicked_name.append(obj.name)
                    if not gotValidClick:
                        mouse_9.clicked_name.append(None)
                    if gotValidClick:  
                        continueRoutine = False  # end routine on response
        
        # *ArrowHead2* updates
        
        # if ArrowHead2 is starting this frame...
        if ArrowHead2.status == NOT_STARTED and tThisFlip >= 2-frameTolerance:
            # keep track of start time/frame for later
            ArrowHead2.frameNStart = frameN  # exact frame index
            ArrowHead2.tStart = t  # local t and not account for scr refresh
            ArrowHead2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(ArrowHead2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'ArrowHead2.started')
            # update status
            ArrowHead2.status = STARTED
            ArrowHead2.setAutoDraw(True)
        
        # if ArrowHead2 is active this frame...
        if ArrowHead2.status == STARTED:
            # update params
            pass
        
        # *ArrowBar2* updates
        
        # if ArrowBar2 is starting this frame...
        if ArrowBar2.status == NOT_STARTED and tThisFlip >= 2-frameTolerance:
            # keep track of start time/frame for later
            ArrowBar2.frameNStart = frameN  # exact frame index
            ArrowBar2.tStart = t  # local t and not account for scr refresh
            ArrowBar2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(ArrowBar2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'ArrowBar2.started')
            # update status
            ArrowBar2.status = STARTED
            ArrowBar2.setAutoDraw(True)
        
        # if ArrowBar2 is active this frame...
        if ArrowBar2.status == STARTED:
            # update params
            pass
        
        # *InstruText* updates
        
        # if InstruText is starting this frame...
        if InstruText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            InstruText.frameNStart = frameN  # exact frame index
            InstruText.tStart = t  # local t and not account for scr refresh
            InstruText.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(InstruText, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'InstruText.started')
            # update status
            InstruText.status = STARTED
            InstruText.setAutoDraw(True)
        
        # if InstruText is active this frame...
        if InstruText.status == STARTED:
            # update params
            pass
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer], 
                playbackComponents=[]
            )
            # skip the frame we paused on
            continue
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            Choice_tutorial.forceEnded = routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Choice_tutorial.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "Choice_tutorial" ---
    for thisComponent in Choice_tutorial.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for Choice_tutorial
    Choice_tutorial.tStop = globalClock.getTime(format='float')
    Choice_tutorial.tStopRefresh = tThisFlipGlobal
    thisExp.addData('Choice_tutorial.stopped', Choice_tutorial.tStop)
    # store data for thisExp (ExperimentHandler)
    x, y = mouse_9.getPos()
    buttons = mouse_9.getPressed()
    if sum(buttons):
        # check if the mouse was inside our 'clickable' objects
        gotValidClick = False
        clickableList = environmenttools.getFromNames(wedgeRedPurple, namespace=locals())
        for obj in clickableList:
            # is this object clicked on?
            if obj.contains(mouse_9):
                gotValidClick = True
                mouse_9.clicked_name.append(obj.name)
        if not gotValidClick:
            mouse_9.clicked_name.append(None)
    thisExp.addData('mouse_9.x', x)
    thisExp.addData('mouse_9.y', y)
    thisExp.addData('mouse_9.leftButton', buttons[0])
    thisExp.addData('mouse_9.midButton', buttons[1])
    thisExp.addData('mouse_9.rightButton', buttons[2])
    if len(mouse_9.clicked_name):
        thisExp.addData('mouse_9.clicked_name', mouse_9.clicked_name[0])
    thisExp.nextEntry()
    # the Routine "Choice_tutorial" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "Clear_sc_tut" ---
    # create an object to store info about Routine Clear_sc_tut
    Clear_sc_tut = data.Routine(
        name='Clear_sc_tut',
        components=[],
    )
    Clear_sc_tut.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # Run 'Begin Routine' code from Clear_Screen_3
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
    # store start times for Clear_sc_tut
    Clear_sc_tut.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    Clear_sc_tut.tStart = globalClock.getTime(format='float')
    Clear_sc_tut.status = STARTED
    thisExp.addData('Clear_sc_tut.started', Clear_sc_tut.tStart)
    Clear_sc_tut.maxDuration = None
    # keep track of which components have finished
    Clear_sc_tutComponents = Clear_sc_tut.components
    for thisComponent in Clear_sc_tut.components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "Clear_sc_tut" ---
    Clear_sc_tut.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer], 
                playbackComponents=[]
            )
            # skip the frame we paused on
            continue
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            Clear_sc_tut.forceEnded = routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Clear_sc_tut.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "Clear_sc_tut" ---
    for thisComponent in Clear_sc_tut.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for Clear_sc_tut
    Clear_sc_tut.tStop = globalClock.getTime(format='float')
    Clear_sc_tut.tStopRefresh = tThisFlipGlobal
    thisExp.addData('Clear_sc_tut.stopped', Clear_sc_tut.tStop)
    thisExp.nextEntry()
    # the Routine "Clear_sc_tut" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "break_2" ---
    # create an object to store info about Routine break_2
    break_2 = data.Routine(
        name='break_2',
        components=[text_2],
    )
    break_2.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # store start times for break_2
    break_2.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    break_2.tStart = globalClock.getTime(format='float')
    break_2.status = STARTED
    thisExp.addData('break_2.started', break_2.tStart)
    break_2.maxDuration = None
    # keep track of which components have finished
    break_2Components = break_2.components
    for thisComponent in break_2.components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "break_2" ---
    break_2.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine and routineTimer.getTime() < 3.0:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_2* updates
        
        # if text_2 is starting this frame...
        if text_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_2.frameNStart = frameN  # exact frame index
            text_2.tStart = t  # local t and not account for scr refresh
            text_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'text_2.started')
            # update status
            text_2.status = STARTED
            text_2.setAutoDraw(True)
        
        # if text_2 is active this frame...
        if text_2.status == STARTED:
            # update params
            pass
        
        # if text_2 is stopping this frame...
        if text_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_2.tStartRefresh + 3.0-frameTolerance:
                # keep track of stop time/frame for later
                text_2.tStop = t  # not accounting for scr refresh
                text_2.tStopRefresh = tThisFlipGlobal  # on global time
                text_2.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'text_2.stopped')
                # update status
                text_2.status = FINISHED
                text_2.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer], 
                playbackComponents=[]
            )
            # skip the frame we paused on
            continue
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break_2.forceEnded = routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in break_2.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "break_2" ---
    for thisComponent in break_2.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for break_2
    break_2.tStop = globalClock.getTime(format='float')
    break_2.tStopRefresh = tThisFlipGlobal
    thisExp.addData('break_2.stopped', break_2.tStop)
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if break_2.maxDurationReached:
        routineTimer.addTime(-break_2.maxDuration)
    elif break_2.forceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-3.000000)
    thisExp.nextEntry()
    
    # --- Prepare to start Routine "ISI_tutorial_2" ---
    # create an object to store info about Routine ISI_tutorial_2
    ISI_tutorial_2 = data.Routine(
        name='ISI_tutorial_2',
        components=[ISI1_cross_3],
    )
    ISI_tutorial_2.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    ISI1_cross_3.setText('·')
    # Run 'Begin Routine' code from Mouse_wipe_4
    win.setMouseVisible(False)
    
    # store start times for ISI_tutorial_2
    ISI_tutorial_2.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    ISI_tutorial_2.tStart = globalClock.getTime(format='float')
    ISI_tutorial_2.status = STARTED
    thisExp.addData('ISI_tutorial_2.started', ISI_tutorial_2.tStart)
    ISI_tutorial_2.maxDuration = None
    # keep track of which components have finished
    ISI_tutorial_2Components = ISI_tutorial_2.components
    for thisComponent in ISI_tutorial_2.components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "ISI_tutorial_2" ---
    ISI_tutorial_2.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine and routineTimer.getTime() < 0.9:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *ISI1_cross_3* updates
        
        # if ISI1_cross_3 is starting this frame...
        if ISI1_cross_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            ISI1_cross_3.frameNStart = frameN  # exact frame index
            ISI1_cross_3.tStart = t  # local t and not account for scr refresh
            ISI1_cross_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(ISI1_cross_3, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'ISI1_cross_3.started')
            # update status
            ISI1_cross_3.status = STARTED
            ISI1_cross_3.setAutoDraw(True)
        
        # if ISI1_cross_3 is active this frame...
        if ISI1_cross_3.status == STARTED:
            # update params
            pass
        
        # if ISI1_cross_3 is stopping this frame...
        if ISI1_cross_3.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > ISI1_cross_3.tStartRefresh + 0.9-frameTolerance:
                # keep track of stop time/frame for later
                ISI1_cross_3.tStop = t  # not accounting for scr refresh
                ISI1_cross_3.tStopRefresh = tThisFlipGlobal  # on global time
                ISI1_cross_3.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'ISI1_cross_3.stopped')
                # update status
                ISI1_cross_3.status = FINISHED
                ISI1_cross_3.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer], 
                playbackComponents=[]
            )
            # skip the frame we paused on
            continue
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            ISI_tutorial_2.forceEnded = routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in ISI_tutorial_2.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "ISI_tutorial_2" ---
    for thisComponent in ISI_tutorial_2.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for ISI_tutorial_2
    ISI_tutorial_2.tStop = globalClock.getTime(format='float')
    ISI_tutorial_2.tStopRefresh = tThisFlipGlobal
    thisExp.addData('ISI_tutorial_2.stopped', ISI_tutorial_2.tStop)
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if ISI_tutorial_2.maxDurationReached:
        routineTimer.addTime(-ISI_tutorial_2.maxDuration)
    elif ISI_tutorial_2.forceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-0.900000)
    thisExp.nextEntry()
    
    # --- Prepare to start Routine "Stimulus_disp_tutorial_2" ---
    # create an object to store info about Routine Stimulus_disp_tutorial_2
    Stimulus_disp_tutorial_2 = data.Routine(
        name='Stimulus_disp_tutorial_2',
        components=[Fixation_Point_6, Target_6, Flan1_6, Flan2_6, Flan3_6, Flan4_6, Flan5_6],
    )
    Stimulus_disp_tutorial_2.status = NOT_STARTED
    continueRoutine = True
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
    # store start times for Stimulus_disp_tutorial_2
    Stimulus_disp_tutorial_2.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    Stimulus_disp_tutorial_2.tStart = globalClock.getTime(format='float')
    Stimulus_disp_tutorial_2.status = STARTED
    thisExp.addData('Stimulus_disp_tutorial_2.started', Stimulus_disp_tutorial_2.tStart)
    Stimulus_disp_tutorial_2.maxDuration = None
    # keep track of which components have finished
    Stimulus_disp_tutorial_2Components = Stimulus_disp_tutorial_2.components
    for thisComponent in Stimulus_disp_tutorial_2.components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "Stimulus_disp_tutorial_2" ---
    Stimulus_disp_tutorial_2.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine and routineTimer.getTime() < 0.3:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *Fixation_Point_6* updates
        
        # if Fixation_Point_6 is starting this frame...
        if Fixation_Point_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Fixation_Point_6.frameNStart = frameN  # exact frame index
            Fixation_Point_6.tStart = t  # local t and not account for scr refresh
            Fixation_Point_6.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Fixation_Point_6, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'Fixation_Point_6.started')
            # update status
            Fixation_Point_6.status = STARTED
            Fixation_Point_6.setAutoDraw(True)
        
        # if Fixation_Point_6 is active this frame...
        if Fixation_Point_6.status == STARTED:
            # update params
            pass
        
        # if Fixation_Point_6 is stopping this frame...
        if Fixation_Point_6.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Fixation_Point_6.tStartRefresh + 0.3-frameTolerance:
                # keep track of stop time/frame for later
                Fixation_Point_6.tStop = t  # not accounting for scr refresh
                Fixation_Point_6.tStopRefresh = tThisFlipGlobal  # on global time
                Fixation_Point_6.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'Fixation_Point_6.stopped')
                # update status
                Fixation_Point_6.status = FINISHED
                Fixation_Point_6.setAutoDraw(False)
        
        # *Target_6* updates
        
        # if Target_6 is starting this frame...
        if Target_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Target_6.frameNStart = frameN  # exact frame index
            Target_6.tStart = t  # local t and not account for scr refresh
            Target_6.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Target_6, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'Target_6.started')
            # update status
            Target_6.status = STARTED
            Target_6.setAutoDraw(True)
        
        # if Target_6 is active this frame...
        if Target_6.status == STARTED:
            # update params
            pass
        
        # if Target_6 is stopping this frame...
        if Target_6.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Target_6.tStartRefresh + 0.3-frameTolerance:
                # keep track of stop time/frame for later
                Target_6.tStop = t  # not accounting for scr refresh
                Target_6.tStopRefresh = tThisFlipGlobal  # on global time
                Target_6.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'Target_6.stopped')
                # update status
                Target_6.status = FINISHED
                Target_6.setAutoDraw(False)
        
        # *Flan1_6* updates
        
        # if Flan1_6 is starting this frame...
        if Flan1_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Flan1_6.frameNStart = frameN  # exact frame index
            Flan1_6.tStart = t  # local t and not account for scr refresh
            Flan1_6.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Flan1_6, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'Flan1_6.started')
            # update status
            Flan1_6.status = STARTED
            Flan1_6.setAutoDraw(True)
        
        # if Flan1_6 is active this frame...
        if Flan1_6.status == STARTED:
            # update params
            pass
        
        # if Flan1_6 is stopping this frame...
        if Flan1_6.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Flan1_6.tStartRefresh + 0.3-frameTolerance:
                # keep track of stop time/frame for later
                Flan1_6.tStop = t  # not accounting for scr refresh
                Flan1_6.tStopRefresh = tThisFlipGlobal  # on global time
                Flan1_6.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'Flan1_6.stopped')
                # update status
                Flan1_6.status = FINISHED
                Flan1_6.setAutoDraw(False)
        
        # *Flan2_6* updates
        
        # if Flan2_6 is starting this frame...
        if Flan2_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Flan2_6.frameNStart = frameN  # exact frame index
            Flan2_6.tStart = t  # local t and not account for scr refresh
            Flan2_6.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Flan2_6, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'Flan2_6.started')
            # update status
            Flan2_6.status = STARTED
            Flan2_6.setAutoDraw(True)
        
        # if Flan2_6 is active this frame...
        if Flan2_6.status == STARTED:
            # update params
            pass
        
        # if Flan2_6 is stopping this frame...
        if Flan2_6.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Flan2_6.tStartRefresh + 0.3-frameTolerance:
                # keep track of stop time/frame for later
                Flan2_6.tStop = t  # not accounting for scr refresh
                Flan2_6.tStopRefresh = tThisFlipGlobal  # on global time
                Flan2_6.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'Flan2_6.stopped')
                # update status
                Flan2_6.status = FINISHED
                Flan2_6.setAutoDraw(False)
        
        # *Flan3_6* updates
        
        # if Flan3_6 is starting this frame...
        if Flan3_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Flan3_6.frameNStart = frameN  # exact frame index
            Flan3_6.tStart = t  # local t and not account for scr refresh
            Flan3_6.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Flan3_6, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'Flan3_6.started')
            # update status
            Flan3_6.status = STARTED
            Flan3_6.setAutoDraw(True)
        
        # if Flan3_6 is active this frame...
        if Flan3_6.status == STARTED:
            # update params
            pass
        
        # if Flan3_6 is stopping this frame...
        if Flan3_6.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Flan3_6.tStartRefresh + 0.3-frameTolerance:
                # keep track of stop time/frame for later
                Flan3_6.tStop = t  # not accounting for scr refresh
                Flan3_6.tStopRefresh = tThisFlipGlobal  # on global time
                Flan3_6.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'Flan3_6.stopped')
                # update status
                Flan3_6.status = FINISHED
                Flan3_6.setAutoDraw(False)
        
        # *Flan4_6* updates
        
        # if Flan4_6 is starting this frame...
        if Flan4_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Flan4_6.frameNStart = frameN  # exact frame index
            Flan4_6.tStart = t  # local t and not account for scr refresh
            Flan4_6.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Flan4_6, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'Flan4_6.started')
            # update status
            Flan4_6.status = STARTED
            Flan4_6.setAutoDraw(True)
        
        # if Flan4_6 is active this frame...
        if Flan4_6.status == STARTED:
            # update params
            pass
        
        # if Flan4_6 is stopping this frame...
        if Flan4_6.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Flan4_6.tStartRefresh + 0.3-frameTolerance:
                # keep track of stop time/frame for later
                Flan4_6.tStop = t  # not accounting for scr refresh
                Flan4_6.tStopRefresh = tThisFlipGlobal  # on global time
                Flan4_6.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'Flan4_6.stopped')
                # update status
                Flan4_6.status = FINISHED
                Flan4_6.setAutoDraw(False)
        
        # *Flan5_6* updates
        
        # if Flan5_6 is starting this frame...
        if Flan5_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Flan5_6.frameNStart = frameN  # exact frame index
            Flan5_6.tStart = t  # local t and not account for scr refresh
            Flan5_6.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Flan5_6, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'Flan5_6.started')
            # update status
            Flan5_6.status = STARTED
            Flan5_6.setAutoDraw(True)
        
        # if Flan5_6 is active this frame...
        if Flan5_6.status == STARTED:
            # update params
            pass
        
        # if Flan5_6 is stopping this frame...
        if Flan5_6.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Flan5_6.tStartRefresh + 0.3-frameTolerance:
                # keep track of stop time/frame for later
                Flan5_6.tStop = t  # not accounting for scr refresh
                Flan5_6.tStopRefresh = tThisFlipGlobal  # on global time
                Flan5_6.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'Flan5_6.stopped')
                # update status
                Flan5_6.status = FINISHED
                Flan5_6.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer], 
                playbackComponents=[]
            )
            # skip the frame we paused on
            continue
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            Stimulus_disp_tutorial_2.forceEnded = routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Stimulus_disp_tutorial_2.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "Stimulus_disp_tutorial_2" ---
    for thisComponent in Stimulus_disp_tutorial_2.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for Stimulus_disp_tutorial_2
    Stimulus_disp_tutorial_2.tStop = globalClock.getTime(format='float')
    Stimulus_disp_tutorial_2.tStopRefresh = tThisFlipGlobal
    thisExp.addData('Stimulus_disp_tutorial_2.stopped', Stimulus_disp_tutorial_2.tStop)
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if Stimulus_disp_tutorial_2.maxDurationReached:
        routineTimer.addTime(-Stimulus_disp_tutorial_2.maxDuration)
    elif Stimulus_disp_tutorial_2.forceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-0.300000)
    thisExp.nextEntry()
    
    # --- Prepare to start Routine "ISI_tutorial_2" ---
    # create an object to store info about Routine ISI_tutorial_2
    ISI_tutorial_2 = data.Routine(
        name='ISI_tutorial_2',
        components=[ISI1_cross_3],
    )
    ISI_tutorial_2.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    ISI1_cross_3.setText('·')
    # Run 'Begin Routine' code from Mouse_wipe_4
    win.setMouseVisible(False)
    
    # store start times for ISI_tutorial_2
    ISI_tutorial_2.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    ISI_tutorial_2.tStart = globalClock.getTime(format='float')
    ISI_tutorial_2.status = STARTED
    thisExp.addData('ISI_tutorial_2.started', ISI_tutorial_2.tStart)
    ISI_tutorial_2.maxDuration = None
    # keep track of which components have finished
    ISI_tutorial_2Components = ISI_tutorial_2.components
    for thisComponent in ISI_tutorial_2.components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "ISI_tutorial_2" ---
    ISI_tutorial_2.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine and routineTimer.getTime() < 0.9:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *ISI1_cross_3* updates
        
        # if ISI1_cross_3 is starting this frame...
        if ISI1_cross_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            ISI1_cross_3.frameNStart = frameN  # exact frame index
            ISI1_cross_3.tStart = t  # local t and not account for scr refresh
            ISI1_cross_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(ISI1_cross_3, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'ISI1_cross_3.started')
            # update status
            ISI1_cross_3.status = STARTED
            ISI1_cross_3.setAutoDraw(True)
        
        # if ISI1_cross_3 is active this frame...
        if ISI1_cross_3.status == STARTED:
            # update params
            pass
        
        # if ISI1_cross_3 is stopping this frame...
        if ISI1_cross_3.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > ISI1_cross_3.tStartRefresh + 0.9-frameTolerance:
                # keep track of stop time/frame for later
                ISI1_cross_3.tStop = t  # not accounting for scr refresh
                ISI1_cross_3.tStopRefresh = tThisFlipGlobal  # on global time
                ISI1_cross_3.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'ISI1_cross_3.stopped')
                # update status
                ISI1_cross_3.status = FINISHED
                ISI1_cross_3.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer], 
                playbackComponents=[]
            )
            # skip the frame we paused on
            continue
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            ISI_tutorial_2.forceEnded = routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in ISI_tutorial_2.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "ISI_tutorial_2" ---
    for thisComponent in ISI_tutorial_2.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for ISI_tutorial_2
    ISI_tutorial_2.tStop = globalClock.getTime(format='float')
    ISI_tutorial_2.tStopRefresh = tThisFlipGlobal
    thisExp.addData('ISI_tutorial_2.stopped', ISI_tutorial_2.tStop)
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if ISI_tutorial_2.maxDurationReached:
        routineTimer.addTime(-ISI_tutorial_2.maxDuration)
    elif ISI_tutorial_2.forceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-0.900000)
    thisExp.nextEntry()
    
    # --- Prepare to start Routine "Loc_choice_tut_2" ---
    # create an object to store info about Routine Loc_choice_tut_2
    Loc_choice_tut_2 = data.Routine(
        name='Loc_choice_tut_2',
        components=[mouse_11, Fixation_Point_7, Target_7, Flan1_7, Flan2_7, Flan3_7, Flan4_7, Flan5_7, InstruText2_2],
    )
    Loc_choice_tut_2.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # setup some python lists for storing info about the mouse_11
    mouse_11.clicked_name = []
    gotValidClick = False  # until a click is received
    # Run 'Begin Routine' code from code_4
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
    # store start times for Loc_choice_tut_2
    Loc_choice_tut_2.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    Loc_choice_tut_2.tStart = globalClock.getTime(format='float')
    Loc_choice_tut_2.status = STARTED
    thisExp.addData('Loc_choice_tut_2.started', Loc_choice_tut_2.tStart)
    Loc_choice_tut_2.maxDuration = None
    # keep track of which components have finished
    Loc_choice_tut_2Components = Loc_choice_tut_2.components
    for thisComponent in Loc_choice_tut_2.components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "Loc_choice_tut_2" ---
    Loc_choice_tut_2.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        # *mouse_11* updates
        
        # if mouse_11 is starting this frame...
        if mouse_11.status == NOT_STARTED and t >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            mouse_11.frameNStart = frameN  # exact frame index
            mouse_11.tStart = t  # local t and not account for scr refresh
            mouse_11.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(mouse_11, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.addData('mouse_11.started', t)
            # update status
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
                    clickableList = environmenttools.getFromNames(Target_7, namespace=locals())
                    for obj in clickableList:
                        # is this object clicked on?
                        if obj.contains(mouse_11):
                            gotValidClick = True
                            mouse_11.clicked_name.append(obj.name)
                    if not gotValidClick:
                        mouse_11.clicked_name.append(None)
                    if gotValidClick:  
                        continueRoutine = False  # end routine on response
        # Run 'Each Frame' code from code_4
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
        
        # if Fixation_Point_7 is starting this frame...
        if Fixation_Point_7.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Fixation_Point_7.frameNStart = frameN  # exact frame index
            Fixation_Point_7.tStart = t  # local t and not account for scr refresh
            Fixation_Point_7.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Fixation_Point_7, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'Fixation_Point_7.started')
            # update status
            Fixation_Point_7.status = STARTED
            Fixation_Point_7.setAutoDraw(True)
        
        # if Fixation_Point_7 is active this frame...
        if Fixation_Point_7.status == STARTED:
            # update params
            pass
        
        # *Target_7* updates
        
        # if Target_7 is starting this frame...
        if Target_7.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Target_7.frameNStart = frameN  # exact frame index
            Target_7.tStart = t  # local t and not account for scr refresh
            Target_7.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Target_7, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'Target_7.started')
            # update status
            Target_7.status = STARTED
            Target_7.setAutoDraw(True)
        
        # if Target_7 is active this frame...
        if Target_7.status == STARTED:
            # update params
            pass
        
        # *Flan1_7* updates
        
        # if Flan1_7 is starting this frame...
        if Flan1_7.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Flan1_7.frameNStart = frameN  # exact frame index
            Flan1_7.tStart = t  # local t and not account for scr refresh
            Flan1_7.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Flan1_7, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'Flan1_7.started')
            # update status
            Flan1_7.status = STARTED
            Flan1_7.setAutoDraw(True)
        
        # if Flan1_7 is active this frame...
        if Flan1_7.status == STARTED:
            # update params
            pass
        
        # *Flan2_7* updates
        
        # if Flan2_7 is starting this frame...
        if Flan2_7.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Flan2_7.frameNStart = frameN  # exact frame index
            Flan2_7.tStart = t  # local t and not account for scr refresh
            Flan2_7.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Flan2_7, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'Flan2_7.started')
            # update status
            Flan2_7.status = STARTED
            Flan2_7.setAutoDraw(True)
        
        # if Flan2_7 is active this frame...
        if Flan2_7.status == STARTED:
            # update params
            pass
        
        # *Flan3_7* updates
        
        # if Flan3_7 is starting this frame...
        if Flan3_7.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Flan3_7.frameNStart = frameN  # exact frame index
            Flan3_7.tStart = t  # local t and not account for scr refresh
            Flan3_7.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Flan3_7, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'Flan3_7.started')
            # update status
            Flan3_7.status = STARTED
            Flan3_7.setAutoDraw(True)
        
        # if Flan3_7 is active this frame...
        if Flan3_7.status == STARTED:
            # update params
            pass
        
        # *Flan4_7* updates
        
        # if Flan4_7 is starting this frame...
        if Flan4_7.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Flan4_7.frameNStart = frameN  # exact frame index
            Flan4_7.tStart = t  # local t and not account for scr refresh
            Flan4_7.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Flan4_7, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'Flan4_7.started')
            # update status
            Flan4_7.status = STARTED
            Flan4_7.setAutoDraw(True)
        
        # if Flan4_7 is active this frame...
        if Flan4_7.status == STARTED:
            # update params
            pass
        
        # *Flan5_7* updates
        
        # if Flan5_7 is starting this frame...
        if Flan5_7.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Flan5_7.frameNStart = frameN  # exact frame index
            Flan5_7.tStart = t  # local t and not account for scr refresh
            Flan5_7.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Flan5_7, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'Flan5_7.started')
            # update status
            Flan5_7.status = STARTED
            Flan5_7.setAutoDraw(True)
        
        # if Flan5_7 is active this frame...
        if Flan5_7.status == STARTED:
            # update params
            pass
        
        # *InstruText2_2* updates
        
        # if InstruText2_2 is starting this frame...
        if InstruText2_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            InstruText2_2.frameNStart = frameN  # exact frame index
            InstruText2_2.tStart = t  # local t and not account for scr refresh
            InstruText2_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(InstruText2_2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'InstruText2_2.started')
            # update status
            InstruText2_2.status = STARTED
            InstruText2_2.setAutoDraw(True)
        
        # if InstruText2_2 is active this frame...
        if InstruText2_2.status == STARTED:
            # update params
            pass
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer], 
                playbackComponents=[]
            )
            # skip the frame we paused on
            continue
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            Loc_choice_tut_2.forceEnded = routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Loc_choice_tut_2.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "Loc_choice_tut_2" ---
    for thisComponent in Loc_choice_tut_2.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for Loc_choice_tut_2
    Loc_choice_tut_2.tStop = globalClock.getTime(format='float')
    Loc_choice_tut_2.tStopRefresh = tThisFlipGlobal
    thisExp.addData('Loc_choice_tut_2.stopped', Loc_choice_tut_2.tStop)
    # store data for thisExp (ExperimentHandler)
    x, y = mouse_11.getPos()
    buttons = mouse_11.getPressed()
    if sum(buttons):
        # check if the mouse was inside our 'clickable' objects
        gotValidClick = False
        clickableList = environmenttools.getFromNames(Target_7, namespace=locals())
        for obj in clickableList:
            # is this object clicked on?
            if obj.contains(mouse_11):
                gotValidClick = True
                mouse_11.clicked_name.append(obj.name)
        if not gotValidClick:
            mouse_11.clicked_name.append(None)
    thisExp.addData('mouse_11.x', x)
    thisExp.addData('mouse_11.y', y)
    thisExp.addData('mouse_11.leftButton', buttons[0])
    thisExp.addData('mouse_11.midButton', buttons[1])
    thisExp.addData('mouse_11.rightButton', buttons[2])
    if len(mouse_11.clicked_name):
        thisExp.addData('mouse_11.clicked_name', mouse_11.clicked_name[0])
    thisExp.nextEntry()
    # the Routine "Loc_choice_tut_2" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "ISI_tutorial_2" ---
    # create an object to store info about Routine ISI_tutorial_2
    ISI_tutorial_2 = data.Routine(
        name='ISI_tutorial_2',
        components=[ISI1_cross_3],
    )
    ISI_tutorial_2.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    ISI1_cross_3.setText('·')
    # Run 'Begin Routine' code from Mouse_wipe_4
    win.setMouseVisible(False)
    
    # store start times for ISI_tutorial_2
    ISI_tutorial_2.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    ISI_tutorial_2.tStart = globalClock.getTime(format='float')
    ISI_tutorial_2.status = STARTED
    thisExp.addData('ISI_tutorial_2.started', ISI_tutorial_2.tStart)
    ISI_tutorial_2.maxDuration = None
    # keep track of which components have finished
    ISI_tutorial_2Components = ISI_tutorial_2.components
    for thisComponent in ISI_tutorial_2.components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "ISI_tutorial_2" ---
    ISI_tutorial_2.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine and routineTimer.getTime() < 0.9:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *ISI1_cross_3* updates
        
        # if ISI1_cross_3 is starting this frame...
        if ISI1_cross_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            ISI1_cross_3.frameNStart = frameN  # exact frame index
            ISI1_cross_3.tStart = t  # local t and not account for scr refresh
            ISI1_cross_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(ISI1_cross_3, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'ISI1_cross_3.started')
            # update status
            ISI1_cross_3.status = STARTED
            ISI1_cross_3.setAutoDraw(True)
        
        # if ISI1_cross_3 is active this frame...
        if ISI1_cross_3.status == STARTED:
            # update params
            pass
        
        # if ISI1_cross_3 is stopping this frame...
        if ISI1_cross_3.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > ISI1_cross_3.tStartRefresh + 0.9-frameTolerance:
                # keep track of stop time/frame for later
                ISI1_cross_3.tStop = t  # not accounting for scr refresh
                ISI1_cross_3.tStopRefresh = tThisFlipGlobal  # on global time
                ISI1_cross_3.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'ISI1_cross_3.stopped')
                # update status
                ISI1_cross_3.status = FINISHED
                ISI1_cross_3.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer], 
                playbackComponents=[]
            )
            # skip the frame we paused on
            continue
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            ISI_tutorial_2.forceEnded = routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in ISI_tutorial_2.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "ISI_tutorial_2" ---
    for thisComponent in ISI_tutorial_2.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for ISI_tutorial_2
    ISI_tutorial_2.tStop = globalClock.getTime(format='float')
    ISI_tutorial_2.tStopRefresh = tThisFlipGlobal
    thisExp.addData('ISI_tutorial_2.stopped', ISI_tutorial_2.tStop)
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if ISI_tutorial_2.maxDurationReached:
        routineTimer.addTime(-ISI_tutorial_2.maxDuration)
    elif ISI_tutorial_2.forceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-0.900000)
    thisExp.nextEntry()
    
    # --- Prepare to start Routine "Choice_tutorial_2" ---
    # create an object to store info about Routine Choice_tutorial_2
    Choice_tutorial_2 = data.Routine(
        name='Choice_tutorial_2',
        components=[mouse_12, InstruText_2],
    )
    Choice_tutorial_2.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # Run 'Begin Routine' code from ColourChoice_3
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
    # store start times for Choice_tutorial_2
    Choice_tutorial_2.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    Choice_tutorial_2.tStart = globalClock.getTime(format='float')
    Choice_tutorial_2.status = STARTED
    thisExp.addData('Choice_tutorial_2.started', Choice_tutorial_2.tStart)
    Choice_tutorial_2.maxDuration = None
    # keep track of which components have finished
    Choice_tutorial_2Components = Choice_tutorial_2.components
    for thisComponent in Choice_tutorial_2.components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "Choice_tutorial_2" ---
    Choice_tutorial_2.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        # Run 'Each Frame' code from ColourChoice_3
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
        
        # if mouse_12 is starting this frame...
        if mouse_12.status == NOT_STARTED and t >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            mouse_12.frameNStart = frameN  # exact frame index
            mouse_12.tStart = t  # local t and not account for scr refresh
            mouse_12.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(mouse_12, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.addData('mouse_12.started', t)
            # update status
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
                    clickableList = environmenttools.getFromNames(wedgeSkyBlue, namespace=locals())
                    for obj in clickableList:
                        # is this object clicked on?
                        if obj.contains(mouse_12):
                            gotValidClick = True
                            mouse_12.clicked_name.append(obj.name)
                    if not gotValidClick:
                        mouse_12.clicked_name.append(None)
                    if gotValidClick:  
                        continueRoutine = False  # end routine on response
        
        # *InstruText_2* updates
        
        # if InstruText_2 is starting this frame...
        if InstruText_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            InstruText_2.frameNStart = frameN  # exact frame index
            InstruText_2.tStart = t  # local t and not account for scr refresh
            InstruText_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(InstruText_2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'InstruText_2.started')
            # update status
            InstruText_2.status = STARTED
            InstruText_2.setAutoDraw(True)
        
        # if InstruText_2 is active this frame...
        if InstruText_2.status == STARTED:
            # update params
            pass
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer], 
                playbackComponents=[]
            )
            # skip the frame we paused on
            continue
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            Choice_tutorial_2.forceEnded = routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Choice_tutorial_2.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "Choice_tutorial_2" ---
    for thisComponent in Choice_tutorial_2.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for Choice_tutorial_2
    Choice_tutorial_2.tStop = globalClock.getTime(format='float')
    Choice_tutorial_2.tStopRefresh = tThisFlipGlobal
    thisExp.addData('Choice_tutorial_2.stopped', Choice_tutorial_2.tStop)
    # store data for thisExp (ExperimentHandler)
    x, y = mouse_12.getPos()
    buttons = mouse_12.getPressed()
    if sum(buttons):
        # check if the mouse was inside our 'clickable' objects
        gotValidClick = False
        clickableList = environmenttools.getFromNames(wedgeSkyBlue, namespace=locals())
        for obj in clickableList:
            # is this object clicked on?
            if obj.contains(mouse_12):
                gotValidClick = True
                mouse_12.clicked_name.append(obj.name)
        if not gotValidClick:
            mouse_12.clicked_name.append(None)
    thisExp.addData('mouse_12.x', x)
    thisExp.addData('mouse_12.y', y)
    thisExp.addData('mouse_12.leftButton', buttons[0])
    thisExp.addData('mouse_12.midButton', buttons[1])
    thisExp.addData('mouse_12.rightButton', buttons[2])
    if len(mouse_12.clicked_name):
        thisExp.addData('mouse_12.clicked_name', mouse_12.clicked_name[0])
    thisExp.nextEntry()
    # the Routine "Choice_tutorial_2" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "Clear_sc_tut" ---
    # create an object to store info about Routine Clear_sc_tut
    Clear_sc_tut = data.Routine(
        name='Clear_sc_tut',
        components=[],
    )
    Clear_sc_tut.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # Run 'Begin Routine' code from Clear_Screen_3
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
    # store start times for Clear_sc_tut
    Clear_sc_tut.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    Clear_sc_tut.tStart = globalClock.getTime(format='float')
    Clear_sc_tut.status = STARTED
    thisExp.addData('Clear_sc_tut.started', Clear_sc_tut.tStart)
    Clear_sc_tut.maxDuration = None
    # keep track of which components have finished
    Clear_sc_tutComponents = Clear_sc_tut.components
    for thisComponent in Clear_sc_tut.components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "Clear_sc_tut" ---
    Clear_sc_tut.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer], 
                playbackComponents=[]
            )
            # skip the frame we paused on
            continue
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            Clear_sc_tut.forceEnded = routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Clear_sc_tut.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "Clear_sc_tut" ---
    for thisComponent in Clear_sc_tut.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for Clear_sc_tut
    Clear_sc_tut.tStop = globalClock.getTime(format='float')
    Clear_sc_tut.tStopRefresh = tThisFlipGlobal
    thisExp.addData('Clear_sc_tut.stopped', Clear_sc_tut.tStop)
    thisExp.nextEntry()
    # the Routine "Clear_sc_tut" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "Tutorial_end" ---
    # create an object to store info about Routine Tutorial_end
    Tutorial_end = data.Routine(
        name='Tutorial_end',
        components=[NumberOBlocks_7, ContinueButtonText_5, ContinueButton_5, mouse_10],
    )
    Tutorial_end.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    NumberOBlocks_7.setText('Well done! You have completed the tutorial.\n\nYou may now begin the main task.\n')
    # Run 'Begin Routine' code from Button_Animation_5
    win.setMouseVisible(True)
    # setup some python lists for storing info about the mouse_10
    mouse_10.clicked_name = []
    gotValidClick = False  # until a click is received
    # store start times for Tutorial_end
    Tutorial_end.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    Tutorial_end.tStart = globalClock.getTime(format='float')
    Tutorial_end.status = STARTED
    thisExp.addData('Tutorial_end.started', Tutorial_end.tStart)
    Tutorial_end.maxDuration = None
    # keep track of which components have finished
    Tutorial_endComponents = Tutorial_end.components
    for thisComponent in Tutorial_end.components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "Tutorial_end" ---
    Tutorial_end.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *NumberOBlocks_7* updates
        
        # if NumberOBlocks_7 is starting this frame...
        if NumberOBlocks_7.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            NumberOBlocks_7.frameNStart = frameN  # exact frame index
            NumberOBlocks_7.tStart = t  # local t and not account for scr refresh
            NumberOBlocks_7.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(NumberOBlocks_7, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'NumberOBlocks_7.started')
            # update status
            NumberOBlocks_7.status = STARTED
            NumberOBlocks_7.setAutoDraw(True)
        
        # if NumberOBlocks_7 is active this frame...
        if NumberOBlocks_7.status == STARTED:
            # update params
            pass
        
        # *ContinueButtonText_5* updates
        
        # if ContinueButtonText_5 is starting this frame...
        if ContinueButtonText_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            ContinueButtonText_5.frameNStart = frameN  # exact frame index
            ContinueButtonText_5.tStart = t  # local t and not account for scr refresh
            ContinueButtonText_5.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(ContinueButtonText_5, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'ContinueButtonText_5.started')
            # update status
            ContinueButtonText_5.status = STARTED
            ContinueButtonText_5.setAutoDraw(True)
        
        # if ContinueButtonText_5 is active this frame...
        if ContinueButtonText_5.status == STARTED:
            # update params
            ContinueButtonText_5.setColor('white', colorSpace='rgb', log=False)
        
        # *ContinueButton_5* updates
        
        # if ContinueButton_5 is starting this frame...
        if ContinueButton_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            ContinueButton_5.frameNStart = frameN  # exact frame index
            ContinueButton_5.tStart = t  # local t and not account for scr refresh
            ContinueButton_5.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(ContinueButton_5, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'ContinueButton_5.started')
            # update status
            ContinueButton_5.status = STARTED
            ContinueButton_5.setAutoDraw(True)
        
        # if ContinueButton_5 is active this frame...
        if ContinueButton_5.status == STARTED:
            # update params
            ContinueButton_5.setLineColor('white', log=False)
        # Run 'Each Frame' code from Button_Animation_5
        if ContinueButton_5.contains(mouse):
            ContinueButton_5.lineColor = 'yellow'
            ContinueButtonText_5.color = 'yellow'
        else:
            ContinueButton_5.lineColor = 'white'
            ContinueButtonText_5.color = 'white'
        # *mouse_10* updates
        
        # if mouse_10 is starting this frame...
        if mouse_10.status == NOT_STARTED and t >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            mouse_10.frameNStart = frameN  # exact frame index
            mouse_10.tStart = t  # local t and not account for scr refresh
            mouse_10.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(mouse_10, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.addData('mouse_10.started', t)
            # update status
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
                    clickableList = environmenttools.getFromNames(ContinueButton, namespace=locals())
                    for obj in clickableList:
                        # is this object clicked on?
                        if obj.contains(mouse_10):
                            gotValidClick = True
                            mouse_10.clicked_name.append(obj.name)
                    if not gotValidClick:
                        mouse_10.clicked_name.append(None)
                    if gotValidClick:  
                        continueRoutine = False  # end routine on response
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer], 
                playbackComponents=[]
            )
            # skip the frame we paused on
            continue
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            Tutorial_end.forceEnded = routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Tutorial_end.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "Tutorial_end" ---
    for thisComponent in Tutorial_end.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for Tutorial_end
    Tutorial_end.tStop = globalClock.getTime(format='float')
    Tutorial_end.tStopRefresh = tThisFlipGlobal
    thisExp.addData('Tutorial_end.stopped', Tutorial_end.tStop)
    # store data for thisExp (ExperimentHandler)
    x, y = mouse_10.getPos()
    buttons = mouse_10.getPressed()
    if sum(buttons):
        # check if the mouse was inside our 'clickable' objects
        gotValidClick = False
        clickableList = environmenttools.getFromNames(ContinueButton, namespace=locals())
        for obj in clickableList:
            # is this object clicked on?
            if obj.contains(mouse_10):
                gotValidClick = True
                mouse_10.clicked_name.append(obj.name)
        if not gotValidClick:
            mouse_10.clicked_name.append(None)
    thisExp.addData('mouse_10.x', x)
    thisExp.addData('mouse_10.y', y)
    thisExp.addData('mouse_10.leftButton', buttons[0])
    thisExp.addData('mouse_10.midButton', buttons[1])
    thisExp.addData('mouse_10.rightButton', buttons[2])
    if len(mouse_10.clicked_name):
        thisExp.addData('mouse_10.clicked_name', mouse_10.clicked_name[0])
    thisExp.nextEntry()
    # the Routine "Tutorial_end" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "break_3" ---
    # create an object to store info about Routine break_3
    break_3 = data.Routine(
        name='break_3',
        components=[text_3],
    )
    break_3.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # store start times for break_3
    break_3.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    break_3.tStart = globalClock.getTime(format='float')
    break_3.status = STARTED
    thisExp.addData('break_3.started', break_3.tStart)
    break_3.maxDuration = None
    # keep track of which components have finished
    break_3Components = break_3.components
    for thisComponent in break_3.components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "break_3" ---
    break_3.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine and routineTimer.getTime() < 1.0:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_3* updates
        
        # if text_3 is starting this frame...
        if text_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_3.frameNStart = frameN  # exact frame index
            text_3.tStart = t  # local t and not account for scr refresh
            text_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_3, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'text_3.started')
            # update status
            text_3.status = STARTED
            text_3.setAutoDraw(True)
        
        # if text_3 is active this frame...
        if text_3.status == STARTED:
            # update params
            pass
        
        # if text_3 is stopping this frame...
        if text_3.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_3.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                text_3.tStop = t  # not accounting for scr refresh
                text_3.tStopRefresh = tThisFlipGlobal  # on global time
                text_3.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'text_3.stopped')
                # update status
                text_3.status = FINISHED
                text_3.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer], 
                playbackComponents=[]
            )
            # skip the frame we paused on
            continue
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break_3.forceEnded = routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in break_3.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "break_3" ---
    for thisComponent in break_3.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for break_3
    break_3.tStop = globalClock.getTime(format='float')
    break_3.tStopRefresh = tThisFlipGlobal
    thisExp.addData('break_3.stopped', break_3.tStop)
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if break_3.maxDurationReached:
        routineTimer.addTime(-break_3.maxDuration)
    elif break_3.forceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-1.000000)
    thisExp.nextEntry()
    
    # set up handler to look after randomisation of conditions etc
    MasterTrialLoop = data.TrialHandler2(
        name='MasterTrialLoop',
        nReps=1.0, 
        method='sequential', 
        extraInfo=expInfo, 
        originPath=-1, 
        trialList=data.importConditions(VersionSelection), 
        seed=None, 
    )
    thisExp.addLoop(MasterTrialLoop)  # add the loop to the experiment
    thisMasterTrialLoop = MasterTrialLoop.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisMasterTrialLoop.rgb)
    if thisMasterTrialLoop != None:
        for paramName in thisMasterTrialLoop:
            globals()[paramName] = thisMasterTrialLoop[paramName]
    if thisSession is not None:
        # if running in a Session with a Liaison client, send data up to now
        thisSession.sendExperimentData()
    
    for thisMasterTrialLoop in MasterTrialLoop:
        currentLoop = MasterTrialLoop
        thisExp.timestampOnFlip(win, 'thisRow.t', format=globalClock.format)
        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
        # abbreviate parameter names if possible (e.g. rgb = thisMasterTrialLoop.rgb)
        if thisMasterTrialLoop != None:
            for paramName in thisMasterTrialLoop:
                globals()[paramName] = thisMasterTrialLoop[paramName]
        
        # --- Prepare to start Routine "MainInstructions" ---
        # create an object to store info about Routine MainInstructions
        MainInstructions = data.Routine(
            name='MainInstructions',
            components=[NumberOBlocks_2, InstructionsMainText, NumberOBlocks, ContinueButtonText, ContinueButton, mouse_3],
        )
        MainInstructions.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        # Run 'Begin Routine' code from TaskBlockTotal
        Ins = ("Task block: " + str(BlockNo) + " of 4")
        win.setMouseVisible(True)
        NumberOBlocks_2.setText(Ins)
        InstructionsMainText.setText(Instructions)
        NumberOBlocks.setText(Ins)
        # setup some python lists for storing info about the mouse_3
        mouse_3.clicked_name = []
        gotValidClick = False  # until a click is received
        # store start times for MainInstructions
        MainInstructions.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        MainInstructions.tStart = globalClock.getTime(format='float')
        MainInstructions.status = STARTED
        thisExp.addData('MainInstructions.started', MainInstructions.tStart)
        MainInstructions.maxDuration = None
        # keep track of which components have finished
        MainInstructionsComponents = MainInstructions.components
        for thisComponent in MainInstructions.components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "MainInstructions" ---
        # if trial has changed, end Routine now
        if isinstance(MasterTrialLoop, data.TrialHandler2) and thisMasterTrialLoop.thisN != MasterTrialLoop.thisTrial.thisN:
            continueRoutine = False
        MainInstructions.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *NumberOBlocks_2* updates
            
            # if NumberOBlocks_2 is starting this frame...
            if NumberOBlocks_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                NumberOBlocks_2.frameNStart = frameN  # exact frame index
                NumberOBlocks_2.tStart = t  # local t and not account for scr refresh
                NumberOBlocks_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(NumberOBlocks_2, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'NumberOBlocks_2.started')
                # update status
                NumberOBlocks_2.status = STARTED
                NumberOBlocks_2.setAutoDraw(True)
            
            # if NumberOBlocks_2 is active this frame...
            if NumberOBlocks_2.status == STARTED:
                # update params
                pass
            
            # *InstructionsMainText* updates
            
            # if InstructionsMainText is starting this frame...
            if InstructionsMainText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                InstructionsMainText.frameNStart = frameN  # exact frame index
                InstructionsMainText.tStart = t  # local t and not account for scr refresh
                InstructionsMainText.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(InstructionsMainText, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'InstructionsMainText.started')
                # update status
                InstructionsMainText.status = STARTED
                InstructionsMainText.setAutoDraw(True)
            
            # if InstructionsMainText is active this frame...
            if InstructionsMainText.status == STARTED:
                # update params
                pass
            
            # *NumberOBlocks* updates
            
            # if NumberOBlocks is starting this frame...
            if NumberOBlocks.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                NumberOBlocks.frameNStart = frameN  # exact frame index
                NumberOBlocks.tStart = t  # local t and not account for scr refresh
                NumberOBlocks.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(NumberOBlocks, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'NumberOBlocks.started')
                # update status
                NumberOBlocks.status = STARTED
                NumberOBlocks.setAutoDraw(True)
            
            # if NumberOBlocks is active this frame...
            if NumberOBlocks.status == STARTED:
                # update params
                pass
            
            # *ContinueButtonText* updates
            
            # if ContinueButtonText is starting this frame...
            if ContinueButtonText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                ContinueButtonText.frameNStart = frameN  # exact frame index
                ContinueButtonText.tStart = t  # local t and not account for scr refresh
                ContinueButtonText.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(ContinueButtonText, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'ContinueButtonText.started')
                # update status
                ContinueButtonText.status = STARTED
                ContinueButtonText.setAutoDraw(True)
            
            # if ContinueButtonText is active this frame...
            if ContinueButtonText.status == STARTED:
                # update params
                ContinueButtonText.setColor('white', colorSpace='rgb', log=False)
            
            # *ContinueButton* updates
            
            # if ContinueButton is starting this frame...
            if ContinueButton.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                ContinueButton.frameNStart = frameN  # exact frame index
                ContinueButton.tStart = t  # local t and not account for scr refresh
                ContinueButton.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(ContinueButton, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'ContinueButton.started')
                # update status
                ContinueButton.status = STARTED
                ContinueButton.setAutoDraw(True)
            
            # if ContinueButton is active this frame...
            if ContinueButton.status == STARTED:
                # update params
                ContinueButton.setLineColor('white', log=False)
            # Run 'Each Frame' code from Button_Animation
            if ContinueButton.contains(mouse):
                ContinueButton.lineColor = 'yellow'
                ContinueButtonText.color = 'yellow'
            else:
                ContinueButton.lineColor = 'white'
                ContinueButtonText.color = 'white'
            # *mouse_3* updates
            
            # if mouse_3 is starting this frame...
            if mouse_3.status == NOT_STARTED and t >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                mouse_3.frameNStart = frameN  # exact frame index
                mouse_3.tStart = t  # local t and not account for scr refresh
                mouse_3.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(mouse_3, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.addData('mouse_3.started', t)
                # update status
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
                        clickableList = environmenttools.getFromNames(ContinueButton, namespace=locals())
                        for obj in clickableList:
                            # is this object clicked on?
                            if obj.contains(mouse_3):
                                gotValidClick = True
                                mouse_3.clicked_name.append(obj.name)
                        if not gotValidClick:
                            mouse_3.clicked_name.append(None)
                        if gotValidClick:  
                            continueRoutine = False  # end routine on response
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer], 
                    playbackComponents=[]
                )
                # skip the frame we paused on
                continue
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                MainInstructions.forceEnded = routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in MainInstructions.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "MainInstructions" ---
        for thisComponent in MainInstructions.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for MainInstructions
        MainInstructions.tStop = globalClock.getTime(format='float')
        MainInstructions.tStopRefresh = tThisFlipGlobal
        thisExp.addData('MainInstructions.stopped', MainInstructions.tStop)
        # store data for MasterTrialLoop (TrialHandler)
        x, y = mouse_3.getPos()
        buttons = mouse_3.getPressed()
        if sum(buttons):
            # check if the mouse was inside our 'clickable' objects
            gotValidClick = False
            clickableList = environmenttools.getFromNames(ContinueButton, namespace=locals())
            for obj in clickableList:
                # is this object clicked on?
                if obj.contains(mouse_3):
                    gotValidClick = True
                    mouse_3.clicked_name.append(obj.name)
            if not gotValidClick:
                mouse_3.clicked_name.append(None)
        MasterTrialLoop.addData('mouse_3.x', x)
        MasterTrialLoop.addData('mouse_3.y', y)
        MasterTrialLoop.addData('mouse_3.leftButton', buttons[0])
        MasterTrialLoop.addData('mouse_3.midButton', buttons[1])
        MasterTrialLoop.addData('mouse_3.rightButton', buttons[2])
        if len(mouse_3.clicked_name):
            MasterTrialLoop.addData('mouse_3.clicked_name', mouse_3.clicked_name[0])
        # the Routine "MainInstructions" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # --- Prepare to start Routine "Time_gap" ---
        # create an object to store info about Routine Time_gap
        Time_gap = data.Routine(
            name='Time_gap',
            components=[Focus],
        )
        Time_gap.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        # Run 'Begin Routine' code from Mouse_wipe_2
        win.setMouseVisible(False)
        
        # store start times for Time_gap
        Time_gap.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        Time_gap.tStart = globalClock.getTime(format='float')
        Time_gap.status = STARTED
        thisExp.addData('Time_gap.started', Time_gap.tStart)
        Time_gap.maxDuration = None
        # keep track of which components have finished
        Time_gapComponents = Time_gap.components
        for thisComponent in Time_gap.components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "Time_gap" ---
        # if trial has changed, end Routine now
        if isinstance(MasterTrialLoop, data.TrialHandler2) and thisMasterTrialLoop.thisN != MasterTrialLoop.thisTrial.thisN:
            continueRoutine = False
        Time_gap.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine and routineTimer.getTime() < 2.0:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *Focus* updates
            
            # if Focus is starting this frame...
            if Focus.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                Focus.frameNStart = frameN  # exact frame index
                Focus.tStart = t  # local t and not account for scr refresh
                Focus.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(Focus, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'Focus.started')
                # update status
                Focus.status = STARTED
                Focus.setAutoDraw(True)
            
            # if Focus is active this frame...
            if Focus.status == STARTED:
                # update params
                pass
            
            # if Focus is stopping this frame...
            if Focus.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > Focus.tStartRefresh + 2-frameTolerance:
                    # keep track of stop time/frame for later
                    Focus.tStop = t  # not accounting for scr refresh
                    Focus.tStopRefresh = tThisFlipGlobal  # on global time
                    Focus.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'Focus.stopped')
                    # update status
                    Focus.status = FINISHED
                    Focus.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer], 
                    playbackComponents=[]
                )
                # skip the frame we paused on
                continue
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                Time_gap.forceEnded = routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in Time_gap.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "Time_gap" ---
        for thisComponent in Time_gap.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for Time_gap
        Time_gap.tStop = globalClock.getTime(format='float')
        Time_gap.tStopRefresh = tThisFlipGlobal
        thisExp.addData('Time_gap.stopped', Time_gap.tStop)
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if Time_gap.maxDurationReached:
            routineTimer.addTime(-Time_gap.maxDuration)
        elif Time_gap.forceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-2.000000)
        
        # set up handler to look after randomisation of conditions etc
        MainTrialLoop = data.TrialHandler2(
            name='MainTrialLoop',
            nReps=1.0, 
            method='sequential', 
            extraInfo=expInfo, 
            originPath=-1, 
            trialList=data.importConditions(CondFile), 
            seed=None, 
        )
        thisExp.addLoop(MainTrialLoop)  # add the loop to the experiment
        thisMainTrialLoop = MainTrialLoop.trialList[0]  # so we can initialise stimuli with some values
        # abbreviate parameter names if possible (e.g. rgb = thisMainTrialLoop.rgb)
        if thisMainTrialLoop != None:
            for paramName in thisMainTrialLoop:
                globals()[paramName] = thisMainTrialLoop[paramName]
        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
        
        for thisMainTrialLoop in MainTrialLoop:
            currentLoop = MainTrialLoop
            thisExp.timestampOnFlip(win, 'thisRow.t', format=globalClock.format)
            if thisSession is not None:
                # if running in a Session with a Liaison client, send data up to now
                thisSession.sendExperimentData()
            # abbreviate parameter names if possible (e.g. rgb = thisMainTrialLoop.rgb)
            if thisMainTrialLoop != None:
                for paramName in thisMainTrialLoop:
                    globals()[paramName] = thisMainTrialLoop[paramName]
            
            # --- Prepare to start Routine "ISI" ---
            # create an object to store info about Routine ISI
            ISI = data.Routine(
                name='ISI',
                components=[ISI1_cross],
            )
            ISI.status = NOT_STARTED
            continueRoutine = True
            # update component parameters for each repeat
            ISI1_cross.setText('·')
            # Run 'Begin Routine' code from Mouse_wipe
            win.setMouseVisible(False)
            
            # store start times for ISI
            ISI.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
            ISI.tStart = globalClock.getTime(format='float')
            ISI.status = STARTED
            thisExp.addData('ISI.started', ISI.tStart)
            ISI.maxDuration = None
            # keep track of which components have finished
            ISIComponents = ISI.components
            for thisComponent in ISI.components:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            frameN = -1
            
            # --- Run Routine "ISI" ---
            # if trial has changed, end Routine now
            if isinstance(MainTrialLoop, data.TrialHandler2) and thisMainTrialLoop.thisN != MainTrialLoop.thisTrial.thisN:
                continueRoutine = False
            ISI.forceEnded = routineForceEnded = not continueRoutine
            while continueRoutine:
                # get current time
                t = routineTimer.getTime()
                tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *ISI1_cross* updates
                
                # if ISI1_cross is starting this frame...
                if ISI1_cross.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    ISI1_cross.frameNStart = frameN  # exact frame index
                    ISI1_cross.tStart = t  # local t and not account for scr refresh
                    ISI1_cross.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(ISI1_cross, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'ISI1_cross.started')
                    # update status
                    ISI1_cross.status = STARTED
                    ISI1_cross.setAutoDraw(True)
                
                # if ISI1_cross is active this frame...
                if ISI1_cross.status == STARTED:
                    # update params
                    pass
                
                # if ISI1_cross is stopping this frame...
                if ISI1_cross.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > ISI1_cross.tStartRefresh + ISI_1_jitter-frameTolerance:
                        # keep track of stop time/frame for later
                        ISI1_cross.tStop = t  # not accounting for scr refresh
                        ISI1_cross.tStopRefresh = tThisFlipGlobal  # on global time
                        ISI1_cross.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'ISI1_cross.stopped')
                        # update status
                        ISI1_cross.status = FINISHED
                        ISI1_cross.setAutoDraw(False)
                
                # check for quit (typically the Esc key)
                if defaultKeyboard.getKeys(keyList=["escape"]):
                    thisExp.status = FINISHED
                if thisExp.status == FINISHED or endExpNow:
                    endExperiment(thisExp, win=win)
                    return
                # pause experiment here if requested
                if thisExp.status == PAUSED:
                    pauseExperiment(
                        thisExp=thisExp, 
                        win=win, 
                        timers=[routineTimer], 
                        playbackComponents=[]
                    )
                    # skip the frame we paused on
                    continue
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    ISI.forceEnded = routineForceEnded = True
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in ISI.components:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # --- Ending Routine "ISI" ---
            for thisComponent in ISI.components:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            # store stop times for ISI
            ISI.tStop = globalClock.getTime(format='float')
            ISI.tStopRefresh = tThisFlipGlobal
            thisExp.addData('ISI.stopped', ISI.tStop)
            # the Routine "ISI" was not non-slip safe, so reset the non-slip timer
            routineTimer.reset()
            
            # --- Prepare to start Routine "Stimulus_display" ---
            # create an object to store info about Routine Stimulus_display
            Stimulus_display = data.Routine(
                name='Stimulus_display',
                components=[Fixation_Point, Target, Flan1, Flan2, Flan3, Flan4, Flan5],
            )
            Stimulus_display.status = NOT_STARTED
            continueRoutine = True
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
            # store start times for Stimulus_display
            Stimulus_display.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
            Stimulus_display.tStart = globalClock.getTime(format='float')
            Stimulus_display.status = STARTED
            thisExp.addData('Stimulus_display.started', Stimulus_display.tStart)
            Stimulus_display.maxDuration = None
            # keep track of which components have finished
            Stimulus_displayComponents = Stimulus_display.components
            for thisComponent in Stimulus_display.components:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            frameN = -1
            
            # --- Run Routine "Stimulus_display" ---
            # if trial has changed, end Routine now
            if isinstance(MainTrialLoop, data.TrialHandler2) and thisMainTrialLoop.thisN != MainTrialLoop.thisTrial.thisN:
                continueRoutine = False
            Stimulus_display.forceEnded = routineForceEnded = not continueRoutine
            while continueRoutine and routineTimer.getTime() < 0.325:
                # get current time
                t = routineTimer.getTime()
                tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *Fixation_Point* updates
                
                # if Fixation_Point is starting this frame...
                if Fixation_Point.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    Fixation_Point.frameNStart = frameN  # exact frame index
                    Fixation_Point.tStart = t  # local t and not account for scr refresh
                    Fixation_Point.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(Fixation_Point, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'Fixation_Point.started')
                    # update status
                    Fixation_Point.status = STARTED
                    Fixation_Point.setAutoDraw(True)
                
                # if Fixation_Point is active this frame...
                if Fixation_Point.status == STARTED:
                    # update params
                    pass
                
                # if Fixation_Point is stopping this frame...
                if Fixation_Point.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > Fixation_Point.tStartRefresh + 0.325-frameTolerance:
                        # keep track of stop time/frame for later
                        Fixation_Point.tStop = t  # not accounting for scr refresh
                        Fixation_Point.tStopRefresh = tThisFlipGlobal  # on global time
                        Fixation_Point.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'Fixation_Point.stopped')
                        # update status
                        Fixation_Point.status = FINISHED
                        Fixation_Point.setAutoDraw(False)
                
                # *Target* updates
                
                # if Target is starting this frame...
                if Target.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    Target.frameNStart = frameN  # exact frame index
                    Target.tStart = t  # local t and not account for scr refresh
                    Target.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(Target, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'Target.started')
                    # update status
                    Target.status = STARTED
                    Target.setAutoDraw(True)
                
                # if Target is active this frame...
                if Target.status == STARTED:
                    # update params
                    pass
                
                # if Target is stopping this frame...
                if Target.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > Target.tStartRefresh + 0.325-frameTolerance:
                        # keep track of stop time/frame for later
                        Target.tStop = t  # not accounting for scr refresh
                        Target.tStopRefresh = tThisFlipGlobal  # on global time
                        Target.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'Target.stopped')
                        # update status
                        Target.status = FINISHED
                        Target.setAutoDraw(False)
                
                # *Flan1* updates
                
                # if Flan1 is starting this frame...
                if Flan1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    Flan1.frameNStart = frameN  # exact frame index
                    Flan1.tStart = t  # local t and not account for scr refresh
                    Flan1.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(Flan1, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'Flan1.started')
                    # update status
                    Flan1.status = STARTED
                    Flan1.setAutoDraw(True)
                
                # if Flan1 is active this frame...
                if Flan1.status == STARTED:
                    # update params
                    pass
                
                # if Flan1 is stopping this frame...
                if Flan1.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > Flan1.tStartRefresh + 0.325-frameTolerance:
                        # keep track of stop time/frame for later
                        Flan1.tStop = t  # not accounting for scr refresh
                        Flan1.tStopRefresh = tThisFlipGlobal  # on global time
                        Flan1.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'Flan1.stopped')
                        # update status
                        Flan1.status = FINISHED
                        Flan1.setAutoDraw(False)
                
                # *Flan2* updates
                
                # if Flan2 is starting this frame...
                if Flan2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    Flan2.frameNStart = frameN  # exact frame index
                    Flan2.tStart = t  # local t and not account for scr refresh
                    Flan2.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(Flan2, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'Flan2.started')
                    # update status
                    Flan2.status = STARTED
                    Flan2.setAutoDraw(True)
                
                # if Flan2 is active this frame...
                if Flan2.status == STARTED:
                    # update params
                    pass
                
                # if Flan2 is stopping this frame...
                if Flan2.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > Flan2.tStartRefresh + 0.325-frameTolerance:
                        # keep track of stop time/frame for later
                        Flan2.tStop = t  # not accounting for scr refresh
                        Flan2.tStopRefresh = tThisFlipGlobal  # on global time
                        Flan2.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'Flan2.stopped')
                        # update status
                        Flan2.status = FINISHED
                        Flan2.setAutoDraw(False)
                
                # *Flan3* updates
                
                # if Flan3 is starting this frame...
                if Flan3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    Flan3.frameNStart = frameN  # exact frame index
                    Flan3.tStart = t  # local t and not account for scr refresh
                    Flan3.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(Flan3, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'Flan3.started')
                    # update status
                    Flan3.status = STARTED
                    Flan3.setAutoDraw(True)
                
                # if Flan3 is active this frame...
                if Flan3.status == STARTED:
                    # update params
                    pass
                
                # if Flan3 is stopping this frame...
                if Flan3.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > Flan3.tStartRefresh + 0.325-frameTolerance:
                        # keep track of stop time/frame for later
                        Flan3.tStop = t  # not accounting for scr refresh
                        Flan3.tStopRefresh = tThisFlipGlobal  # on global time
                        Flan3.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'Flan3.stopped')
                        # update status
                        Flan3.status = FINISHED
                        Flan3.setAutoDraw(False)
                
                # *Flan4* updates
                
                # if Flan4 is starting this frame...
                if Flan4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    Flan4.frameNStart = frameN  # exact frame index
                    Flan4.tStart = t  # local t and not account for scr refresh
                    Flan4.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(Flan4, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'Flan4.started')
                    # update status
                    Flan4.status = STARTED
                    Flan4.setAutoDraw(True)
                
                # if Flan4 is active this frame...
                if Flan4.status == STARTED:
                    # update params
                    pass
                
                # if Flan4 is stopping this frame...
                if Flan4.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > Flan4.tStartRefresh + 0.325-frameTolerance:
                        # keep track of stop time/frame for later
                        Flan4.tStop = t  # not accounting for scr refresh
                        Flan4.tStopRefresh = tThisFlipGlobal  # on global time
                        Flan4.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'Flan4.stopped')
                        # update status
                        Flan4.status = FINISHED
                        Flan4.setAutoDraw(False)
                
                # *Flan5* updates
                
                # if Flan5 is starting this frame...
                if Flan5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    Flan5.frameNStart = frameN  # exact frame index
                    Flan5.tStart = t  # local t and not account for scr refresh
                    Flan5.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(Flan5, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'Flan5.started')
                    # update status
                    Flan5.status = STARTED
                    Flan5.setAutoDraw(True)
                
                # if Flan5 is active this frame...
                if Flan5.status == STARTED:
                    # update params
                    pass
                
                # if Flan5 is stopping this frame...
                if Flan5.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > Flan5.tStartRefresh + 0.325-frameTolerance:
                        # keep track of stop time/frame for later
                        Flan5.tStop = t  # not accounting for scr refresh
                        Flan5.tStopRefresh = tThisFlipGlobal  # on global time
                        Flan5.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'Flan5.stopped')
                        # update status
                        Flan5.status = FINISHED
                        Flan5.setAutoDraw(False)
                
                # check for quit (typically the Esc key)
                if defaultKeyboard.getKeys(keyList=["escape"]):
                    thisExp.status = FINISHED
                if thisExp.status == FINISHED or endExpNow:
                    endExperiment(thisExp, win=win)
                    return
                # pause experiment here if requested
                if thisExp.status == PAUSED:
                    pauseExperiment(
                        thisExp=thisExp, 
                        win=win, 
                        timers=[routineTimer], 
                        playbackComponents=[]
                    )
                    # skip the frame we paused on
                    continue
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    Stimulus_display.forceEnded = routineForceEnded = True
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in Stimulus_display.components:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # --- Ending Routine "Stimulus_display" ---
            for thisComponent in Stimulus_display.components:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            # store stop times for Stimulus_display
            Stimulus_display.tStop = globalClock.getTime(format='float')
            Stimulus_display.tStopRefresh = tThisFlipGlobal
            thisExp.addData('Stimulus_display.stopped', Stimulus_display.tStop)
            # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
            if Stimulus_display.maxDurationReached:
                routineTimer.addTime(-Stimulus_display.maxDuration)
            elif Stimulus_display.forceEnded:
                routineTimer.reset()
            else:
                routineTimer.addTime(-0.325000)
            
            # --- Prepare to start Routine "ISI2" ---
            # create an object to store info about Routine ISI2
            ISI2 = data.Routine(
                name='ISI2',
                components=[ISI2_cross],
            )
            ISI2.status = NOT_STARTED
            continueRoutine = True
            # update component parameters for each repeat
            ISI2_cross.setText('·')
            # store start times for ISI2
            ISI2.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
            ISI2.tStart = globalClock.getTime(format='float')
            ISI2.status = STARTED
            thisExp.addData('ISI2.started', ISI2.tStart)
            ISI2.maxDuration = None
            # keep track of which components have finished
            ISI2Components = ISI2.components
            for thisComponent in ISI2.components:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            frameN = -1
            
            # --- Run Routine "ISI2" ---
            # if trial has changed, end Routine now
            if isinstance(MainTrialLoop, data.TrialHandler2) and thisMainTrialLoop.thisN != MainTrialLoop.thisTrial.thisN:
                continueRoutine = False
            ISI2.forceEnded = routineForceEnded = not continueRoutine
            while continueRoutine:
                # get current time
                t = routineTimer.getTime()
                tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *ISI2_cross* updates
                
                # if ISI2_cross is starting this frame...
                if ISI2_cross.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    ISI2_cross.frameNStart = frameN  # exact frame index
                    ISI2_cross.tStart = t  # local t and not account for scr refresh
                    ISI2_cross.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(ISI2_cross, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'ISI2_cross.started')
                    # update status
                    ISI2_cross.status = STARTED
                    ISI2_cross.setAutoDraw(True)
                
                # if ISI2_cross is active this frame...
                if ISI2_cross.status == STARTED:
                    # update params
                    pass
                
                # if ISI2_cross is stopping this frame...
                if ISI2_cross.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > ISI2_cross.tStartRefresh + ISI_2_jitter-frameTolerance:
                        # keep track of stop time/frame for later
                        ISI2_cross.tStop = t  # not accounting for scr refresh
                        ISI2_cross.tStopRefresh = tThisFlipGlobal  # on global time
                        ISI2_cross.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'ISI2_cross.stopped')
                        # update status
                        ISI2_cross.status = FINISHED
                        ISI2_cross.setAutoDraw(False)
                
                # check for quit (typically the Esc key)
                if defaultKeyboard.getKeys(keyList=["escape"]):
                    thisExp.status = FINISHED
                if thisExp.status == FINISHED or endExpNow:
                    endExperiment(thisExp, win=win)
                    return
                # pause experiment here if requested
                if thisExp.status == PAUSED:
                    pauseExperiment(
                        thisExp=thisExp, 
                        win=win, 
                        timers=[routineTimer], 
                        playbackComponents=[]
                    )
                    # skip the frame we paused on
                    continue
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    ISI2.forceEnded = routineForceEnded = True
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in ISI2.components:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # --- Ending Routine "ISI2" ---
            for thisComponent in ISI2.components:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            # store stop times for ISI2
            ISI2.tStop = globalClock.getTime(format='float')
            ISI2.tStopRefresh = tThisFlipGlobal
            thisExp.addData('ISI2.stopped', ISI2.tStop)
            # Run 'End Routine' code from Timer
            time_PreLocalisationEnd = globalClock.getTime()
            
            thisExp.addData('time_PreLocalisationEnd', time_PreLocalisationEnd)
            # the Routine "ISI2" was not non-slip safe, so reset the non-slip timer
            routineTimer.reset()
            
            # --- Prepare to start Routine "Location_choice" ---
            # create an object to store info about Routine Location_choice
            Location_choice = data.Routine(
                name='Location_choice',
                components=[mouse, Fixation_Point_2, Target_2, Flan1_2, Flan2_2, Flan3_2, Flan4_2, Flan5_2],
            )
            Location_choice.status = NOT_STARTED
            continueRoutine = True
            # update component parameters for each repeat
            # setup some python lists for storing info about the mouse
            mouse.clicked_name = []
            gotValidClick = False  # until a click is received
            # Run 'Begin Routine' code from code_and_timer
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
            # store start times for Location_choice
            Location_choice.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
            Location_choice.tStart = globalClock.getTime(format='float')
            Location_choice.status = STARTED
            thisExp.addData('Location_choice.started', Location_choice.tStart)
            Location_choice.maxDuration = None
            # keep track of which components have finished
            Location_choiceComponents = Location_choice.components
            for thisComponent in Location_choice.components:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            frameN = -1
            
            # --- Run Routine "Location_choice" ---
            # if trial has changed, end Routine now
            if isinstance(MainTrialLoop, data.TrialHandler2) and thisMainTrialLoop.thisN != MainTrialLoop.thisTrial.thisN:
                continueRoutine = False
            Location_choice.forceEnded = routineForceEnded = not continueRoutine
            while continueRoutine:
                # get current time
                t = routineTimer.getTime()
                tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                # *mouse* updates
                
                # if mouse is starting this frame...
                if mouse.status == NOT_STARTED and t >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    mouse.frameNStart = frameN  # exact frame index
                    mouse.tStart = t  # local t and not account for scr refresh
                    mouse.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(mouse, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.addData('mouse.started', t)
                    # update status
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
                            clickableList = environmenttools.getFromNames([Target_2, Flan1_2, Flan2_2, Flan3_2, Flan4_2, Flan5_2], namespace=locals())
                            for obj in clickableList:
                                # is this object clicked on?
                                if obj.contains(mouse):
                                    gotValidClick = True
                                    mouse.clicked_name.append(obj.name)
                            if not gotValidClick:
                                mouse.clicked_name.append(None)
                            if gotValidClick:  
                                continueRoutine = False  # end routine on response
                # Run 'Each Frame' code from code_and_timer
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
                
                # if Fixation_Point_2 is starting this frame...
                if Fixation_Point_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    Fixation_Point_2.frameNStart = frameN  # exact frame index
                    Fixation_Point_2.tStart = t  # local t and not account for scr refresh
                    Fixation_Point_2.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(Fixation_Point_2, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'Fixation_Point_2.started')
                    # update status
                    Fixation_Point_2.status = STARTED
                    Fixation_Point_2.setAutoDraw(True)
                
                # if Fixation_Point_2 is active this frame...
                if Fixation_Point_2.status == STARTED:
                    # update params
                    pass
                
                # *Target_2* updates
                
                # if Target_2 is starting this frame...
                if Target_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    Target_2.frameNStart = frameN  # exact frame index
                    Target_2.tStart = t  # local t and not account for scr refresh
                    Target_2.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(Target_2, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'Target_2.started')
                    # update status
                    Target_2.status = STARTED
                    Target_2.setAutoDraw(True)
                
                # if Target_2 is active this frame...
                if Target_2.status == STARTED:
                    # update params
                    pass
                
                # *Flan1_2* updates
                
                # if Flan1_2 is starting this frame...
                if Flan1_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    Flan1_2.frameNStart = frameN  # exact frame index
                    Flan1_2.tStart = t  # local t and not account for scr refresh
                    Flan1_2.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(Flan1_2, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'Flan1_2.started')
                    # update status
                    Flan1_2.status = STARTED
                    Flan1_2.setAutoDraw(True)
                
                # if Flan1_2 is active this frame...
                if Flan1_2.status == STARTED:
                    # update params
                    pass
                
                # *Flan2_2* updates
                
                # if Flan2_2 is starting this frame...
                if Flan2_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    Flan2_2.frameNStart = frameN  # exact frame index
                    Flan2_2.tStart = t  # local t and not account for scr refresh
                    Flan2_2.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(Flan2_2, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'Flan2_2.started')
                    # update status
                    Flan2_2.status = STARTED
                    Flan2_2.setAutoDraw(True)
                
                # if Flan2_2 is active this frame...
                if Flan2_2.status == STARTED:
                    # update params
                    pass
                
                # *Flan3_2* updates
                
                # if Flan3_2 is starting this frame...
                if Flan3_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    Flan3_2.frameNStart = frameN  # exact frame index
                    Flan3_2.tStart = t  # local t and not account for scr refresh
                    Flan3_2.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(Flan3_2, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'Flan3_2.started')
                    # update status
                    Flan3_2.status = STARTED
                    Flan3_2.setAutoDraw(True)
                
                # if Flan3_2 is active this frame...
                if Flan3_2.status == STARTED:
                    # update params
                    pass
                
                # *Flan4_2* updates
                
                # if Flan4_2 is starting this frame...
                if Flan4_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    Flan4_2.frameNStart = frameN  # exact frame index
                    Flan4_2.tStart = t  # local t and not account for scr refresh
                    Flan4_2.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(Flan4_2, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'Flan4_2.started')
                    # update status
                    Flan4_2.status = STARTED
                    Flan4_2.setAutoDraw(True)
                
                # if Flan4_2 is active this frame...
                if Flan4_2.status == STARTED:
                    # update params
                    pass
                
                # *Flan5_2* updates
                
                # if Flan5_2 is starting this frame...
                if Flan5_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    Flan5_2.frameNStart = frameN  # exact frame index
                    Flan5_2.tStart = t  # local t and not account for scr refresh
                    Flan5_2.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(Flan5_2, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'Flan5_2.started')
                    # update status
                    Flan5_2.status = STARTED
                    Flan5_2.setAutoDraw(True)
                
                # if Flan5_2 is active this frame...
                if Flan5_2.status == STARTED:
                    # update params
                    pass
                
                # check for quit (typically the Esc key)
                if defaultKeyboard.getKeys(keyList=["escape"]):
                    thisExp.status = FINISHED
                if thisExp.status == FINISHED or endExpNow:
                    endExperiment(thisExp, win=win)
                    return
                # pause experiment here if requested
                if thisExp.status == PAUSED:
                    pauseExperiment(
                        thisExp=thisExp, 
                        win=win, 
                        timers=[routineTimer], 
                        playbackComponents=[]
                    )
                    # skip the frame we paused on
                    continue
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    Location_choice.forceEnded = routineForceEnded = True
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in Location_choice.components:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # --- Ending Routine "Location_choice" ---
            for thisComponent in Location_choice.components:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            # store stop times for Location_choice
            Location_choice.tStop = globalClock.getTime(format='float')
            Location_choice.tStopRefresh = tThisFlipGlobal
            thisExp.addData('Location_choice.stopped', Location_choice.tStop)
            # store data for MainTrialLoop (TrialHandler)
            x, y = mouse.getPos()
            buttons = mouse.getPressed()
            if sum(buttons):
                # check if the mouse was inside our 'clickable' objects
                gotValidClick = False
                clickableList = environmenttools.getFromNames([Target_2, Flan1_2, Flan2_2, Flan3_2, Flan4_2, Flan5_2], namespace=locals())
                for obj in clickableList:
                    # is this object clicked on?
                    if obj.contains(mouse):
                        gotValidClick = True
                        mouse.clicked_name.append(obj.name)
                if not gotValidClick:
                    mouse.clicked_name.append(None)
            MainTrialLoop.addData('mouse.x', x)
            MainTrialLoop.addData('mouse.y', y)
            MainTrialLoop.addData('mouse.leftButton', buttons[0])
            MainTrialLoop.addData('mouse.midButton', buttons[1])
            MainTrialLoop.addData('mouse.rightButton', buttons[2])
            if len(mouse.clicked_name):
                MainTrialLoop.addData('mouse.clicked_name', mouse.clicked_name[0])
            # Run 'End Routine' code from code_and_timer
            time_LocalisationEnd = globalClock.getTime()
            
            thisExp.addData('time_LocalisationBegin', time_LocalisationBegin)
            thisExp.addData('time_LocalisationEnd', time_LocalisationEnd)
            # the Routine "Location_choice" was not non-slip safe, so reset the non-slip timer
            routineTimer.reset()
            
            # --- Prepare to start Routine "ISI3" ---
            # create an object to store info about Routine ISI3
            ISI3 = data.Routine(
                name='ISI3',
                components=[ISI3_cross],
            )
            ISI3.status = NOT_STARTED
            continueRoutine = True
            # update component parameters for each repeat
            # store start times for ISI3
            ISI3.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
            ISI3.tStart = globalClock.getTime(format='float')
            ISI3.status = STARTED
            thisExp.addData('ISI3.started', ISI3.tStart)
            ISI3.maxDuration = None
            # keep track of which components have finished
            ISI3Components = ISI3.components
            for thisComponent in ISI3.components:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            frameN = -1
            
            # --- Run Routine "ISI3" ---
            # if trial has changed, end Routine now
            if isinstance(MainTrialLoop, data.TrialHandler2) and thisMainTrialLoop.thisN != MainTrialLoop.thisTrial.thisN:
                continueRoutine = False
            ISI3.forceEnded = routineForceEnded = not continueRoutine
            while continueRoutine:
                # get current time
                t = routineTimer.getTime()
                tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *ISI3_cross* updates
                
                # if ISI3_cross is starting this frame...
                if ISI3_cross.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    ISI3_cross.frameNStart = frameN  # exact frame index
                    ISI3_cross.tStart = t  # local t and not account for scr refresh
                    ISI3_cross.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(ISI3_cross, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'ISI3_cross.started')
                    # update status
                    ISI3_cross.status = STARTED
                    ISI3_cross.setAutoDraw(True)
                
                # if ISI3_cross is active this frame...
                if ISI3_cross.status == STARTED:
                    # update params
                    pass
                
                # if ISI3_cross is stopping this frame...
                if ISI3_cross.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > ISI3_cross.tStartRefresh + ISI_3_jitter-frameTolerance:
                        # keep track of stop time/frame for later
                        ISI3_cross.tStop = t  # not accounting for scr refresh
                        ISI3_cross.tStopRefresh = tThisFlipGlobal  # on global time
                        ISI3_cross.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'ISI3_cross.stopped')
                        # update status
                        ISI3_cross.status = FINISHED
                        ISI3_cross.setAutoDraw(False)
                
                # check for quit (typically the Esc key)
                if defaultKeyboard.getKeys(keyList=["escape"]):
                    thisExp.status = FINISHED
                if thisExp.status == FINISHED or endExpNow:
                    endExperiment(thisExp, win=win)
                    return
                # pause experiment here if requested
                if thisExp.status == PAUSED:
                    pauseExperiment(
                        thisExp=thisExp, 
                        win=win, 
                        timers=[routineTimer], 
                        playbackComponents=[]
                    )
                    # skip the frame we paused on
                    continue
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    ISI3.forceEnded = routineForceEnded = True
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in ISI3.components:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # --- Ending Routine "ISI3" ---
            for thisComponent in ISI3.components:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            # store stop times for ISI3
            ISI3.tStop = globalClock.getTime(format='float')
            ISI3.tStopRefresh = tThisFlipGlobal
            thisExp.addData('ISI3.stopped', ISI3.tStop)
            # the Routine "ISI3" was not non-slip safe, so reset the non-slip timer
            routineTimer.reset()
            
            # --- Prepare to start Routine "Colour_choice" ---
            # create an object to store info about Routine Colour_choice
            Colour_choice = data.Routine(
                name='Colour_choice',
                components=[mouse_2],
            )
            Colour_choice.status = NOT_STARTED
            continueRoutine = True
            # update component parameters for each repeat
            # Run 'Begin Routine' code from ColourChoice
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
            # Run 'Begin Routine' code from Timer_2
            time_ColourSelectStart = globalClock.getTime()
            # store start times for Colour_choice
            Colour_choice.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
            Colour_choice.tStart = globalClock.getTime(format='float')
            Colour_choice.status = STARTED
            thisExp.addData('Colour_choice.started', Colour_choice.tStart)
            Colour_choice.maxDuration = None
            # keep track of which components have finished
            Colour_choiceComponents = Colour_choice.components
            for thisComponent in Colour_choice.components:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            frameN = -1
            
            # --- Run Routine "Colour_choice" ---
            # if trial has changed, end Routine now
            if isinstance(MainTrialLoop, data.TrialHandler2) and thisMainTrialLoop.thisN != MainTrialLoop.thisTrial.thisN:
                continueRoutine = False
            Colour_choice.forceEnded = routineForceEnded = not continueRoutine
            while continueRoutine:
                # get current time
                t = routineTimer.getTime()
                tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                # Run 'Each Frame' code from ColourChoice
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
                
                # if mouse_2 is starting this frame...
                if mouse_2.status == NOT_STARTED and t >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    mouse_2.frameNStart = frameN  # exact frame index
                    mouse_2.tStart = t  # local t and not account for scr refresh
                    mouse_2.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(mouse_2, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.addData('mouse_2.started', t)
                    # update status
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
                            clickableList = environmenttools.getFromNames([wedgeYellow, wedgeWhite, wedgeVermilion, wedgeRedPurple, wedgeBlack, wedgeIndigo, wedgeSkyBlue, wedgeBlueGreen], namespace=locals())
                            for obj in clickableList:
                                # is this object clicked on?
                                if obj.contains(mouse_2):
                                    gotValidClick = True
                                    mouse_2.clicked_name.append(obj.name)
                                    mouse_2.clicked_fillColor.append(obj.fillColor)
                            if not gotValidClick:
                                mouse_2.clicked_name.append(None)
                                mouse_2.clicked_fillColor.append(None)
                            if gotValidClick:  
                                continueRoutine = False  # end routine on response
                
                # check for quit (typically the Esc key)
                if defaultKeyboard.getKeys(keyList=["escape"]):
                    thisExp.status = FINISHED
                if thisExp.status == FINISHED or endExpNow:
                    endExperiment(thisExp, win=win)
                    return
                # pause experiment here if requested
                if thisExp.status == PAUSED:
                    pauseExperiment(
                        thisExp=thisExp, 
                        win=win, 
                        timers=[routineTimer], 
                        playbackComponents=[]
                    )
                    # skip the frame we paused on
                    continue
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    Colour_choice.forceEnded = routineForceEnded = True
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in Colour_choice.components:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # --- Ending Routine "Colour_choice" ---
            for thisComponent in Colour_choice.components:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            # store stop times for Colour_choice
            Colour_choice.tStop = globalClock.getTime(format='float')
            Colour_choice.tStopRefresh = tThisFlipGlobal
            thisExp.addData('Colour_choice.stopped', Colour_choice.tStop)
            # store data for MainTrialLoop (TrialHandler)
            x, y = mouse_2.getPos()
            buttons = mouse_2.getPressed()
            if sum(buttons):
                # check if the mouse was inside our 'clickable' objects
                gotValidClick = False
                clickableList = environmenttools.getFromNames([wedgeYellow, wedgeWhite, wedgeVermilion, wedgeRedPurple, wedgeBlack, wedgeIndigo, wedgeSkyBlue, wedgeBlueGreen], namespace=locals())
                for obj in clickableList:
                    # is this object clicked on?
                    if obj.contains(mouse_2):
                        gotValidClick = True
                        mouse_2.clicked_name.append(obj.name)
                        mouse_2.clicked_fillColor.append(obj.fillColor)
                if not gotValidClick:
                    mouse_2.clicked_name.append(None)
                    mouse_2.clicked_fillColor.append(None)
            MainTrialLoop.addData('mouse_2.x', x)
            MainTrialLoop.addData('mouse_2.y', y)
            MainTrialLoop.addData('mouse_2.leftButton', buttons[0])
            MainTrialLoop.addData('mouse_2.midButton', buttons[1])
            MainTrialLoop.addData('mouse_2.rightButton', buttons[2])
            if len(mouse_2.clicked_name):
                MainTrialLoop.addData('mouse_2.clicked_name', mouse_2.clicked_name[0])
            if len(mouse_2.clicked_fillColor):
                MainTrialLoop.addData('mouse_2.clicked_fillColor', mouse_2.clicked_fillColor[0])
            # Run 'End Routine' code from Timer_2
            time_ColourSelectEnd = globalClock.getTime()
            
            thisExp.addData('time_ColourSelectStart', time_ColourSelectStart)
            thisExp.addData('time_ColourSelectEnd', time_ColourSelectEnd)
            
            # the Routine "Colour_choice" was not non-slip safe, so reset the non-slip timer
            routineTimer.reset()
            
            # --- Prepare to start Routine "Clear_Screen" ---
            # create an object to store info about Routine Clear_Screen
            Clear_Screen = data.Routine(
                name='Clear_Screen',
                components=[],
            )
            Clear_Screen.status = NOT_STARTED
            continueRoutine = True
            # update component parameters for each repeat
            # Run 'Begin Routine' code from Clear_Screen_2
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
            # store start times for Clear_Screen
            Clear_Screen.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
            Clear_Screen.tStart = globalClock.getTime(format='float')
            Clear_Screen.status = STARTED
            thisExp.addData('Clear_Screen.started', Clear_Screen.tStart)
            Clear_Screen.maxDuration = None
            # keep track of which components have finished
            Clear_ScreenComponents = Clear_Screen.components
            for thisComponent in Clear_Screen.components:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            frameN = -1
            
            # --- Run Routine "Clear_Screen" ---
            # if trial has changed, end Routine now
            if isinstance(MainTrialLoop, data.TrialHandler2) and thisMainTrialLoop.thisN != MainTrialLoop.thisTrial.thisN:
                continueRoutine = False
            Clear_Screen.forceEnded = routineForceEnded = not continueRoutine
            while continueRoutine:
                # get current time
                t = routineTimer.getTime()
                tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # check for quit (typically the Esc key)
                if defaultKeyboard.getKeys(keyList=["escape"]):
                    thisExp.status = FINISHED
                if thisExp.status == FINISHED or endExpNow:
                    endExperiment(thisExp, win=win)
                    return
                # pause experiment here if requested
                if thisExp.status == PAUSED:
                    pauseExperiment(
                        thisExp=thisExp, 
                        win=win, 
                        timers=[routineTimer], 
                        playbackComponents=[]
                    )
                    # skip the frame we paused on
                    continue
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    Clear_Screen.forceEnded = routineForceEnded = True
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in Clear_Screen.components:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # --- Ending Routine "Clear_Screen" ---
            for thisComponent in Clear_Screen.components:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            # store stop times for Clear_Screen
            Clear_Screen.tStop = globalClock.getTime(format='float')
            Clear_Screen.tStopRefresh = tThisFlipGlobal
            thisExp.addData('Clear_Screen.stopped', Clear_Screen.tStop)
            # the Routine "Clear_Screen" was not non-slip safe, so reset the non-slip timer
            routineTimer.reset()
            thisExp.nextEntry()
            
        # completed 1.0 repeats of 'MainTrialLoop'
        
        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
        
        # --- Prepare to start Routine "BlockAdder" ---
        # create an object to store info about Routine BlockAdder
        BlockAdder = data.Routine(
            name='BlockAdder',
            components=[text],
        )
        BlockAdder.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        # Run 'Begin Routine' code from Adder
        BlockNo = BlockNo + 1
        # store start times for BlockAdder
        BlockAdder.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        BlockAdder.tStart = globalClock.getTime(format='float')
        BlockAdder.status = STARTED
        thisExp.addData('BlockAdder.started', BlockAdder.tStart)
        BlockAdder.maxDuration = None
        # keep track of which components have finished
        BlockAdderComponents = BlockAdder.components
        for thisComponent in BlockAdder.components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "BlockAdder" ---
        # if trial has changed, end Routine now
        if isinstance(MasterTrialLoop, data.TrialHandler2) and thisMasterTrialLoop.thisN != MasterTrialLoop.thisTrial.thisN:
            continueRoutine = False
        BlockAdder.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine and routineTimer.getTime() < 1.0:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *text* updates
            
            # if text is starting this frame...
            if text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text.frameNStart = frameN  # exact frame index
                text.tStart = t  # local t and not account for scr refresh
                text.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'text.started')
                # update status
                text.status = STARTED
                text.setAutoDraw(True)
            
            # if text is active this frame...
            if text.status == STARTED:
                # update params
                pass
            
            # if text is stopping this frame...
            if text.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > text.tStartRefresh + 1.0-frameTolerance:
                    # keep track of stop time/frame for later
                    text.tStop = t  # not accounting for scr refresh
                    text.tStopRefresh = tThisFlipGlobal  # on global time
                    text.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'text.stopped')
                    # update status
                    text.status = FINISHED
                    text.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer], 
                    playbackComponents=[]
                )
                # skip the frame we paused on
                continue
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                BlockAdder.forceEnded = routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in BlockAdder.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "BlockAdder" ---
        for thisComponent in BlockAdder.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for BlockAdder
        BlockAdder.tStop = globalClock.getTime(format='float')
        BlockAdder.tStopRefresh = tThisFlipGlobal
        thisExp.addData('BlockAdder.stopped', BlockAdder.tStop)
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if BlockAdder.maxDurationReached:
            routineTimer.addTime(-BlockAdder.maxDuration)
        elif BlockAdder.forceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-1.000000)
        thisExp.nextEntry()
        
    # completed 1.0 repeats of 'MasterTrialLoop'
    
    if thisSession is not None:
        # if running in a Session with a Liaison client, send data up to now
        thisSession.sendExperimentData()
    
    # --- Prepare to start Routine "EndScreen" ---
    # create an object to store info about Routine EndScreen
    EndScreen = data.Routine(
        name='EndScreen',
        components=[EndScreenText],
    )
    EndScreen.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # store start times for EndScreen
    EndScreen.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    EndScreen.tStart = globalClock.getTime(format='float')
    EndScreen.status = STARTED
    thisExp.addData('EndScreen.started', EndScreen.tStart)
    EndScreen.maxDuration = None
    # keep track of which components have finished
    EndScreenComponents = EndScreen.components
    for thisComponent in EndScreen.components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "EndScreen" ---
    EndScreen.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *EndScreenText* updates
        
        # if EndScreenText is starting this frame...
        if EndScreenText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            EndScreenText.frameNStart = frameN  # exact frame index
            EndScreenText.tStart = t  # local t and not account for scr refresh
            EndScreenText.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(EndScreenText, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'EndScreenText.started')
            # update status
            EndScreenText.status = STARTED
            EndScreenText.setAutoDraw(True)
        
        # if EndScreenText is active this frame...
        if EndScreenText.status == STARTED:
            # update params
            pass
        # Run 'Each Frame' code from QuitChecker_3
        keys = event.getKeys()
        if 'q' in keys and 't' in keys:
                core.quit()
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer], 
                playbackComponents=[]
            )
            # skip the frame we paused on
            continue
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            EndScreen.forceEnded = routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in EndScreen.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "EndScreen" ---
    for thisComponent in EndScreen.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for EndScreen
    EndScreen.tStop = globalClock.getTime(format='float')
    EndScreen.tStopRefresh = tThisFlipGlobal
    thisExp.addData('EndScreen.stopped', EndScreen.tStop)
    thisExp.nextEntry()
    # the Routine "EndScreen" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # mark experiment as finished
    endExperiment(thisExp, win=win)


def saveData(thisExp):
    """
    Save data from this experiment
    
    Parameters
    ==========
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    """
    filename = thisExp.dataFileName
    # these shouldn't be strictly necessary (should auto-save)
    thisExp.saveAsWideText(filename + '.csv', delim='auto')
    thisExp.saveAsPickle(filename)


def endExperiment(thisExp, win=None):
    """
    End this experiment, performing final shut down operations.
    
    This function does NOT close the window or end the Python process - use `quit` for this.
    
    Parameters
    ==========
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    win : psychopy.visual.Window
        Window for this experiment.
    """
    if win is not None:
        # remove autodraw from all current components
        win.clearAutoDraw()
        # Flip one final time so any remaining win.callOnFlip() 
        # and win.timeOnFlip() tasks get executed
        win.flip()
    # return console logger level to WARNING
    logging.console.setLevel(logging.WARNING)
    # mark experiment handler as finished
    thisExp.status = FINISHED
    logging.flush()


def quit(thisExp, win=None, thisSession=None):
    """
    Fully quit, closing the window and ending the Python process.
    
    Parameters
    ==========
    win : psychopy.visual.Window
        Window to close.
    thisSession : psychopy.session.Session or None
        Handle of the Session object this experiment is being run from, if any.
    """
    thisExp.abort()  # or data files will save again on exit
    # make sure everything is closed down
    if win is not None:
        # Flip one final time so any remaining win.callOnFlip() 
        # and win.timeOnFlip() tasks get executed before quitting
        win.flip()
        win.close()
    logging.flush()
    if thisSession is not None:
        thisSession.stop()
    # terminate Python process
    core.quit()


# if running this experiment as a script...
if __name__ == '__main__':
    # call all functions in order
    expInfo = showExpInfoDlg(expInfo=expInfo)
    thisExp = setupData(expInfo=expInfo)
    logFile = setupLogging(filename=thisExp.dataFileName)
    win = setupWindow(expInfo=expInfo)
    setupDevices(expInfo=expInfo, thisExp=thisExp, win=win)
    run(
        expInfo=expInfo, 
        thisExp=thisExp, 
        win=win,
        globalClock='float'
    )
    saveData(thisExp=thisExp)
    quit(thisExp=thisExp, win=win)
