#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy2 Experiment Builder (v1.85.2),
    on Wed Oct 17 16:27:42 2018
If you publish work using this script please cite the PsychoPy publications:
    Peirce, JW (2007) PsychoPy - Psychophysics software in Python.
        Journal of Neuroscience Methods, 162(1-2), 8-13.
    Peirce, JW (2009) Generating stimuli for neuroscience using PsychoPy.
        Frontiers in Neuroinformatics, 2:10. doi: 10.3389/neuro.11.010.2008
"""

from __future__ import absolute_import, division

import psychopy
psychopy.useVersion('1.85.2')

from psychopy import locale_setup, sound, gui, visual, core, data, event, logging
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)
import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle
import os  # handy system and path functions
import sys  # to get file system encoding

# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__)).decode(sys.getfilesystemencoding())
os.chdir(_thisDir)

# Store info about the experiment session
expName = 'BART_draft_practice'  # from the Builder filename that created this script
expInfo = {u'session': u'001', u'participant': u''}
dlg = gui.DlgFromDict(dictionary=expInfo, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath=None,
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp

# Start Code - component code to be run before the window creation

# Setup the Window
win = visual.Window(
    size=(1440, 900), fullscr=True, screen=0,
    allowGUI=False, allowStencil=False,
    monitor='macbook', color=[1.000,1.000,1.000], colorSpace='rgb',
    blendMode='avg', useFBO=True)
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# Initialize components for Routine "setup"
setupClock = core.Clock()
import csv

maxpumps=[10,10,7,14,11,7,5,9,9,13,10,8,9,4,9,11,16,5,5,4,10,9,8,9,
6,13,11,6,8,7,8,12,12,14,16,10,5,8,10,4,11,5,8,7,8,12,14,6,6,14]

shuffle(maxpumps)

ineq=["inequality_L.jpg","inequality_L.jpg","inequality_M.jpg","inequality_H.jpg","inequality_H.jpg"]

chart=[]

for k in range(10):
    shuffle(ineq)
    chart+=ineq

#chartdict={"inequality_L.jpg":"pinkballoon","inequality_H.jpg":"orangeballoon","inequality_M.jpg":"blueballoon"}
#popdict={"inequality_L.jpg":"pink_exploded.jpg","inequality_H.jpg":"orange_exploded.jpg","inequality_M.jpg":"blue_exploded.jpg"}

fields=["trial","chart","imgroot","maxpumps","pop_image"]

out=[]
for k in range(50):
    out.append([str(k+1),chart[k],"orangeballoon",maxpumps[k],"orange_exploded.jpg"])

with open("Conditions.csv","wb") as outfile:
    writer=csv.writer(outfile)
    writer.writerow(fields)
    for row in out:
        writer.writerow(row)
breakwait=15
breakClock = core.CountdownTimer(breakwait)

# Initialize components for Routine "trigger"
triggerClock = core.Clock()
text = visual.TextStim(win=win, name='text',
    text=u'Get Ready!',
    font=u'Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color=u'black', colorSpace='rgb', opacity=1,
    depth=0.0);

# Initialize components for Routine "prep"
prepClock = core.Clock()
cross1 = visual.TextStim(win=win, name='cross1',
    text='+',
    font='Arial',
    units='pix', pos=(0, 0), height=70, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1,
    depth=0.0);

cross2 = visual.TextStim(win=win, name='cross2',
    text='\n\n+',
    font='Arial',
    units='pix', pos=(0, 0), height=70, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1,
    depth=-2.0);
ineq_chart = visual.ImageStim(
    win=win, name='ineq_chart',
    image='sin', mask=None,
    ori=0, pos=(0, 0.56), size=(0.88, 0.88),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-3.0)


# Initialize components for Routine "trial"
trialClock = core.Clock()
cumscore=0

balloon = visual.ImageStim(
    win=win, name='balloon',
    image='sin', mask=None,
    ori=0, pos=(0, -0.4), size=(1,1),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)
instr=u'      Pump        Cash Out'
inequality_chart = visual.ImageStim(
    win=win, name='inequality_chart',
    image='sin', mask=None,
    ori=0, pos=(-0.54, 0.54), size=(0.72, 0.72),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-5.0)
instructions = visual.TextStim(win=win, name='instructions',
    text='default text',
    font='Arial',
    pos=(0, -0.7), height=0.1, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1,
    depth=-6.0);

# Initialize components for Routine "score"
scoreClock = core.Clock()
score_text = visual.TextStim(win=win, name='score_text',
    text='default text',
    font='Arial',
    pos=(0, 0.7), height=0.1, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1,
    depth=0.0);

result = visual.ImageStim(
    win=win, name='result',
    image='sin', mask=None,
    ori=0, pos=(0, -0.25), size=(1.12, 1.12),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)

# Initialize components for Routine "break_2"
break_2Clock = core.Clock()
breaktext = visual.TextStim(win=win, name='breaktext',
    text='default text',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1,
    depth=0.0);
breakfile = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])+"_BREAKS.csv"
breakslist=[]
breakct=0

# Initialize components for Routine "trigger_2"
trigger_2Clock = core.Clock()
getready = visual.TextStim(win=win, name='getready',
    text=u'Get Ready!',
    font=u'Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color=u'black', colorSpace='rgb', opacity=1,
    depth=0.0);

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "setup"-------
t = 0
setupClock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat


# keep track of which components have finished
setupComponents = []
for thisComponent in setupComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "setup"-------
while continueRoutine:
    # get current time
    t = setupClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in setupComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "setup"-------
for thisComponent in setupComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)


# the Routine "setup" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "trigger"-------
t = 0
triggerClock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
key_resp_2 = event.BuilderKeyResponse()
# keep track of which components have finished
triggerComponents = [text, key_resp_2]
for thisComponent in triggerComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "trigger"-------
while continueRoutine:
    # get current time
    t = triggerClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text* updates
    if t >= 0.0 and text.status == NOT_STARTED:
        # keep track of start time/frame for later
        text.tStart = t
        text.frameNStart = frameN  # exact frame index
        text.setAutoDraw(True)
    
    # *key_resp_2* updates
    if t >= 0.0 and key_resp_2.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp_2.tStart = t
        key_resp_2.frameNStart = frameN  # exact frame index
        key_resp_2.status = STARTED
        # keyboard checking is just starting
        win.callOnFlip(key_resp_2.clock.reset)  # t=0 on next screen flip
        event.clearEvents(eventType='keyboard')
    if key_resp_2.status == STARTED:
        theseKeys = event.getKeys(keyList=['o'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            key_resp_2.keys = theseKeys[-1]  # just the last key pressed
            key_resp_2.rt = key_resp_2.clock.getTime()
            # a response ends the routine
            continueRoutine = False
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in triggerComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "trigger"-------
for thisComponent in triggerComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if key_resp_2.keys in ['', [], None]:  # No response was made
    key_resp_2.keys=None
thisExp.addData('key_resp_2.keys',key_resp_2.keys)
if key_resp_2.keys != None:  # we had a response
    thisExp.addData('key_resp_2.rt', key_resp_2.rt)
thisExp.nextEntry()
# the Routine "trigger" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trials = data.TrialHandler(nReps=1, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('Conditions.csv'),
    seed=None, name='trials')
thisExp.addLoop(trials)  # add the loop to the experiment
thisTrial = trials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
if thisTrial != None:
    for paramName in thisTrial.keys():
        exec(paramName + '= thisTrial.' + paramName)

for thisTrial in trials:
    currentLoop = trials
    # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
    if thisTrial != None:
        for paramName in thisTrial.keys():
            exec(paramName + '= thisTrial.' + paramName)
    
    # ------Prepare to start Routine "prep"-------
    t = 0
    prepClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    # update component parameters for each repeat
    cross_dur=randint(500,4000)/1000
    ineq_chart.setImage(chart)
    if breakClock.getTime()<=0:
        breakClock = core.CountdownTimer(breakwait)
    else:
        pass
    
    # keep track of which components have finished
    prepComponents = [cross1, cross2, ineq_chart]
    for thisComponent in prepComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "prep"-------
    while continueRoutine:
        # get current time
        t = prepClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *cross1* updates
        if t >= 0.0 and cross1.status == NOT_STARTED:
            # keep track of start time/frame for later
            cross1.tStart = t
            cross1.frameNStart = frameN  # exact frame index
            cross1.setAutoDraw(True)
        frameRemains = cross_dur - win.monitorFramePeriod * 0.75  # most of one frame period left
        if cross1.status == STARTED and t >= frameRemains:
            cross1.setAutoDraw(False)
        cross_dur=randint(500,4000)/1000
        
        # *cross2* updates
        if t >= cross_dur+5 and cross2.status == NOT_STARTED:
            # keep track of start time/frame for later
            cross2.tStart = t
            cross2.frameNStart = frameN  # exact frame index
            cross2.setAutoDraw(True)
        frameRemains = cross_dur+6.43 - win.monitorFramePeriod * 0.75  # most of one frame period left
        if cross2.status == STARTED and t >= frameRemains:
            cross2.setAutoDraw(False)
        
        # *ineq_chart* updates
        if t >= cross_dur and ineq_chart.status == NOT_STARTED:
            # keep track of start time/frame for later
            ineq_chart.tStart = t
            ineq_chart.frameNStart = frameN  # exact frame index
            ineq_chart.setAutoDraw(True)
        frameRemains = cross_dur+6.43 - win.monitorFramePeriod * 0.75  # most of one frame period left
        if ineq_chart.status == STARTED and t >= frameRemains:
            ineq_chart.setAutoDraw(False)
        
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in prepComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "prep"-------
    for thisComponent in prepComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    
    
    # the Routine "prep" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "trial"-------
    t = 0
    trialClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    # update component parameters for each repeat
    bscore=0
    img=imgroot+"01"+".JPG"
    popped=False
    npumps=0
    instr=u'      Pump        Cash Out'
    delay=0
    returned=False
    event.getKeys()
    timer = core.Clock()
    rt_list=[]
    end = event.BuilderKeyResponse()
    inequality_chart.setImage(chart)
    # keep track of which components have finished
    trialComponents = [balloon, end, inequality_chart, instructions]
    for thisComponent in trialComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "trial"-------
    while continueRoutine:
        # get current time
        t = trialClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        if npumps+1<10:
            n="0"+str(npumps+1)
        else:
            n=str(npumps+1)
        
        
        
        # *balloon* updates
        if t >= 0.0 and balloon.status == NOT_STARTED:
            # keep track of start time/frame for later
            balloon.tStart = t
            balloon.frameNStart = frameN  # exact frame index
            balloon.setAutoDraw(True)
        if balloon.status == STARTED:  # only update if drawing
            balloon.setImage(img, log=False)
        core.wait(secs=delay)
        if delay>0:
            delay=0
            event.getKeys()
            instr=u'      Pump        Cash Out'
            timer = core.Clock()
        if returned:
            continueRoutine=False
        if event.getKeys(['1']):
            rt_list.append(timer.getTime())
            npumps+=1
            instr=u''
            if npumps>=maxpumps:
                popped=True
                delay=randint(500,4000)/1000
                returned=True
            else:
                if npumps+1<10:
                    n="0"+str(npumps+1)
                else:
                    n=str(npumps+1)
                img=imgroot+n+".JPG"
                delay=randint(500,4000)/1000
            event.getKeys()
        elif event.getKeys(['2']):
            rt_list.append(timer.getTime())
            instr=u''
            delay=randint(500,4000)/1000
            returned=True
        
        # *end* updates
        if t >= 0.0 and end.status == NOT_STARTED:
            # keep track of start time/frame for later
            end.tStart = t
            end.frameNStart = frameN  # exact frame index
            end.status = STARTED
            # keyboard checking is just starting
            event.clearEvents(eventType='keyboard')
        if end.status == STARTED:
            theseKeys = event.getKeys(keyList=['return'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                # a response ends the routine
                continueRoutine = False
        
        # *inequality_chart* updates
        if t >= 0.0 and inequality_chart.status == NOT_STARTED:
            # keep track of start time/frame for later
            inequality_chart.tStart = t
            inequality_chart.frameNStart = frameN  # exact frame index
            inequality_chart.setAutoDraw(True)
        
        # *instructions* updates
        if t >= 0.0 and instructions.status == NOT_STARTED:
            # keep track of start time/frame for later
            instructions.tStart = t
            instructions.frameNStart = frameN  # exact frame index
            instructions.setAutoDraw(True)
        if instructions.status == STARTED:  # only update if drawing
            instructions.setText(instr, log=False)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in trialComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "trial"-------
    for thisComponent in trialComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    bscore=npumps*5
    if popped:
        bscore=0
    else: pass
    cumscore+=bscore
    #trials.addData("nPumps",npumps)
    #trials.addData("balloonscore",balloonscore)
    trials.addData("nPumps",npumps)
    trials.addData("balloonscore",bscore)
    trials.addData("popped",popped)
    trials.addData("cum_score",cumscore)
    
    
    total_response_time=sum(rt_list)
    trials.addData("total_response_time",total_response_time)
    
    for r in range(len(rt_list)):
        field="rt_"+str(r+1)
        trials.addData(field,rt_list[r])
    
    # the Routine "trial" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "score"-------
    t = 0
    scoreClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    routineTimer.add(2.000000)
    # update component parameters for each repeat
    score_text.setText(u"You got %i points." %bscore)
    img=pop_image
    if popped:
        result.opacity=1
    else:
        result.opacity=0
    
    # keep track of which components have finished
    scoreComponents = [score_text, result]
    for thisComponent in scoreComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "score"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = scoreClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *score_text* updates
        if t >= 0 and score_text.status == NOT_STARTED:
            # keep track of start time/frame for later
            score_text.tStart = t
            score_text.frameNStart = frameN  # exact frame index
            score_text.setAutoDraw(True)
        frameRemains = 2 - win.monitorFramePeriod * 0.75  # most of one frame period left
        if score_text.status == STARTED and t >= frameRemains:
            score_text.setAutoDraw(False)
        
        
        # *result* updates
        if t >= 0 and result.status == NOT_STARTED:
            # keep track of start time/frame for later
            result.tStart = t
            result.frameNStart = frameN  # exact frame index
            result.setAutoDraw(True)
        frameRemains = 2 - win.monitorFramePeriod * 0.75  # most of one frame period left
        if result.status == STARTED and t >= frameRemains:
            result.setAutoDraw(False)
        if result.status == STARTED:  # only update if drawing
            result.setImage(img, log=False)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in scoreComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "score"-------
    for thisComponent in scoreComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    
    
    # ------Prepare to start Routine "break_2"-------
    t = 0
    break_2Clock.reset()  # clock
    frameN = -1
    continueRoutine = True
    # update component parameters for each repeat
    scanner_end = event.BuilderKeyResponse()
    if breakClock.getTime()<=0:
        breakdur=60000
    else:
        breakdur=0
    if breakClock.getTime()<=0:
        isbreak=True
        breakdur=60000
        break_start=globalClock.getTime()
    else:
        isbreak=False
        breakdur=0
    # keep track of which components have finished
    break_2Components = [breaktext, scanner_end]
    for thisComponent in break_2Components:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "break_2"-------
    while continueRoutine:
        # get current time
        t = break_2Clock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *breaktext* updates
        if t >= 0.0 and breaktext.status == NOT_STARTED:
            # keep track of start time/frame for later
            breaktext.tStart = t
            breaktext.frameNStart = frameN  # exact frame index
            breaktext.setAutoDraw(True)
        frameRemains = breakdur - win.monitorFramePeriod * 0.75  # most of one frame period left
        if breaktext.status == STARTED and t >= frameRemains:
            breaktext.setAutoDraw(False)
        if breaktext.status == STARTED:  # only update if drawing
            breaktext.setText('BREAK', log=False)
        
        # *scanner_end* updates
        if t >= 0.0 and scanner_end.status == NOT_STARTED:
            # keep track of start time/frame for later
            scanner_end.tStart = t
            scanner_end.frameNStart = frameN  # exact frame index
            scanner_end.status = STARTED
            # keyboard checking is just starting
            event.clearEvents(eventType='keyboard')
        frameRemains = breakdur - win.monitorFramePeriod * 0.75  # most of one frame period left
        if scanner_end.status == STARTED and t >= frameRemains:
            scanner_end.status = STOPPED
        if scanner_end.status == STARTED:
            theseKeys = event.getKeys(keyList=['r'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                # a response ends the routine
                continueRoutine = False
        
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in break_2Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "break_2"-------
    for thisComponent in break_2Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    if isbreak:
        break_end=globalClock.getTime()
        breakct+=1
        breakslist.append({"break_num":breakct,"break_start":break_start,"break_end":break_end})
    # the Routine "break_2" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "trigger_2"-------
    t = 0
    trigger_2Clock.reset()  # clock
    frameN = -1
    continueRoutine = True
    # update component parameters for each repeat
    key_resp_3 = event.BuilderKeyResponse()
    # keep track of which components have finished
    trigger_2Components = [getready, key_resp_3]
    for thisComponent in trigger_2Components:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "trigger_2"-------
    while continueRoutine:
        # get current time
        t = trigger_2Clock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *getready* updates
        if t >= 0.0 and getready.status == NOT_STARTED:
            # keep track of start time/frame for later
            getready.tStart = t
            getready.frameNStart = frameN  # exact frame index
            getready.setAutoDraw(True)
        
        # *key_resp_3* updates
        if t >= 0.0 and key_resp_3.status == NOT_STARTED:
            # keep track of start time/frame for later
            key_resp_3.tStart = t
            key_resp_3.frameNStart = frameN  # exact frame index
            key_resp_3.status = STARTED
            # keyboard checking is just starting
            win.callOnFlip(key_resp_3.clock.reset)  # t=0 on next screen flip
            event.clearEvents(eventType='keyboard')
        if key_resp_3.status == STARTED:
            theseKeys = event.getKeys(keyList=['o'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                key_resp_3.keys = theseKeys[-1]  # just the last key pressed
                key_resp_3.rt = key_resp_3.clock.getTime()
                # a response ends the routine
                continueRoutine = False
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in trigger_2Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "trigger_2"-------
    for thisComponent in trigger_2Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if key_resp_3.keys in ['', [], None]:  # No response was made
        key_resp_3.keys=None
    trials.addData('key_resp_3.keys',key_resp_3.keys)
    if key_resp_3.keys != None:  # we had a response
        trials.addData('key_resp_3.rt', key_resp_3.rt)
    # the Routine "trigger_2" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1 repeats of 'trials'

# get names of stimulus parameters
if trials.trialList in ([], [None], None):
    params = []
else:
    params = trials.trialList[0].keys()
# save data for this loop
trials.saveAsExcel(filename + '.xlsx', sheetName='trials',
    stimOut=params,
    dataOut=['n','all_mean','all_std', 'all_raw'])
trials.saveAsText(filename + 'trials.csv', delim=',',
    stimOut=params,
    dataOut=['n','all_mean','all_std', 'all_raw'])








import csv
 
with open(breakfile,"wb") as csvfile:
    writer=csv.DictWriter(csvfile,fieldnames=["break_num","break_start","break_end"])
    writer.writeheader()
    for row in breakslist:
        writer.writerow(row)
# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
