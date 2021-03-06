#!/bin/env python
import os
import sys
from optparse import OptionParser
from array import array
from mapping.channelMaps import *
from mapping.PanChannelMaps import *
from gempython.utils.nesteddict import nesteddict as ndict

from anaoptions import parser

parser.add_option("--fileScurveFitTree", type="string", dest="fileScurveFitTree", default="SCurveFitData.root",
                  help="TFile containing scurveFitTree", metavar="fileScurveFitTree")
parser.add_option("--zscore", type="float", dest="zscore", default=3.5,
                  help="Z-Score for Outlier Identification in MAD Algo", metavar="zscore")
parser.add_option("--pervfat", action="store_true", dest="pervfat",
                  help="Analysis for a per-VFAT scan (default is per-channel)", metavar="pervfat")

parser.set_defaults(outfilename="ThresholdPlots.root")

(options, args) = parser.parse_args()
filename = options.filename[:-5]
os.system("mkdir " + filename)

print filename
outfilename = options.outfilename

import ROOT as r
r.TH1.SetDefaultSumw2(False)
r.gROOT.SetBatch(True)
GEBtype = options.GEBtype
inF = r.TFile(filename+'.root')
outF = r.TFile(filename+'/'+outfilename, 'recreate')

VT1_MAX = 255

#Build the channel to strip mapping from the text file
lookup_table = []
pan_lookup = []
vfatCh_lookup = []
for vfat in range(0,24):
    lookup_table.append([])
    pan_lookup.append([])
    vfatCh_lookup.append([])
    for channel in range(0,128):
        lookup_table[vfat].append(0)
        pan_lookup[vfat].append(0)
        vfatCh_lookup[vfat].append(0)
        pass
    pass

from gempython.utils.wrappers import envCheck
envCheck('GEM_PLOTTING_PROJECT')

projectHome = os.environ.get('GEM_PLOTTING_PROJECT')
if GEBtype == 'long':
    intext = open(projectHome+'/mapping/longChannelMap.txt', 'r')
    pass
if GEBtype == 'short':
    intext = open(projectHome+'/mapping/shortChannelMap.txt', 'r')
    pass

for i, line in enumerate(intext):
    if i == 0: continue
    mapping = line.rsplit('\t')
    lookup_table[int(mapping[0])][int(mapping[2]) -1] = int(mapping[1])
    pan_lookup[int(mapping[0])][int(mapping[2]) -1] = int(mapping[3])

    if not (options.channels or options.PanPin):     #Readout Strips
        vfatCh_lookup[int(mapping[0])][int(mapping[1])]=int(mapping[2]) - 1
        pass
    elif options.channels:                #VFAT Channels
        vfatCh_lookup[int(mapping[0])][int(mapping[2]) -1]=int(mapping[2]) - 1
        pass
    elif options.PanPin:                #Panasonic Connector Pins
        vfatCh_lookup[int(mapping[0])][int(mapping[3])]=int(mapping[2]) - 1
        pass
    pass

print 'Initializing Histograms'
vSum = ndict()
hot_channels = []
for vfat in range(0,24):
    hot_channels.append([])
    if not (options.channels or options.PanPin):
        vSum[vfat] = r.TH2D('h_VT1_vs_ROBstr_VFAT%i'%vfat,'vSum%i;Strip;VThreshold1 [DAC units]'%vfat,128,-0.5,127.5,VT1_MAX+1,-0.5,VT1_MAX+0.5)
        pass
    elif options.channels:
        vSum[vfat] = r.TH2D('h_VT1_vs_vfatCH_VFAT%i'%vfat,'vSum%i;Channel;VThreshold1 [DAC units]'%vfat,128,-0.5,127.5,VT1_MAX+1,-0.5,VT1_MAX+0.5)
        pass
    elif options.PanPin:
        vSum[vfat] = r.TH2D('h_VT1_vs_PanPin_VFAT%i'%vfat,'vSum%i;Panasonic Pin;VThreshold1 [DAC units]'%vfat,128,-0.5,127.5,VT1_MAX+1,-0.5,VT1_MAX+0.5)
        pass
    for chan in range(0,128):
        hot_channels[vfat].append(False)
        pass
    pass

print 'Filling Histograms'
trimRange = dict((vfat,0) for vfat in range(0,24))
dict_vfatID = dict((vfat, 0) for vfat in range(0,24))
listOfBranches = inF.thrTree.GetListOfBranches()
for event in inF.thrTree :
    strip = lookup_table[event.vfatN][event.vfatCH]
    pan_pin = pan_lookup[event.vfatN][event.vfatCH]
    trimRange[int(event.vfatN)] = int(event.trimRange)

    if not (dict_vfatID[event.vfatN] > 0):
        if 'vfatID' in listOfBranches:
            dict_vfatID[event.vfatN] = event.vfatID
        else:
            dict_vfatID[event.vfatN] = 0

    if options.channels:
        vSum[event.vfatN].Fill(event.vfatCH,event.vth1,event.Nhits)
        pass
    elif options.PanPin:
        vSum[event.vfatN].Fill(pan_pin,event.vth1,event.Nhits)
        pass
    else:
        vSum[event.vfatN].Fill(strip,event.vth1,event.Nhits)
        pass
    pass

#Determine Hot Channels
print 'Determining hot channels'
from anautilities import *
import numpy as np
import root_numpy as rp #note need root_numpy-4.7.2 (may need to run 'pip install root_numpy --upgrade')
dict_hMaxVT1 = {}
dict_hMaxVT1_NoOutlier = {}
for vfat in range(0,24):
    dict_hMaxVT1[vfat]          = r.TH1F('vfat%iChanMaxVT1'%vfat,"vfat%i"%vfat,256,-0.5,255.5)
    dict_hMaxVT1_NoOutlier[vfat]= r.TH1F('vfat%iChanMaxVT1_NoOutlier'%vfat,"vfat%i - No Outliers"%vfat,256,-0.5,255.5)
    dict_hMaxVT1_NoOutlier[vfat].SetLineColor(r.kRed)

    #For each channel determine the maximum thresholds
    chanMaxVT1 = np.zeros((2,vSum[vfat].GetNbinsX()))
    for chan in range(0,vSum[vfat].GetNbinsX()):
        chanProj = vSum[vfat].ProjectionY("projY",chan,chan,"")
        for thresh in range(chanProj.GetMaximumBin(),VT1_MAX+1):
            if(chanProj.GetBinContent(thresh) == 0):
                chanMaxVT1[0][chan]=chan
                chanMaxVT1[1][chan]=(thresh-1)
                dict_hMaxVT1[vfat].Fill(thresh-1)
                break
            pass
        pass

    #Determine Outliers (e.g. "hot" channels)
    chanOutliers = isOutlierMADOneSided(chanMaxVT1[1,:], thresh=options.zscore)
    for chan in range(0,len(chanOutliers)):
        hot_channels[vfat][chan] = chanOutliers[chan]

        if not chanOutliers[chan]:
            dict_hMaxVT1_NoOutlier[vfat].Fill(chanMaxVT1[1][chan])
            pass
        pass

    if options.debug:
        print "VFAT%i Max Thresholds By Channel"%vfat
        print chanMaxVT1

        print "VFAT%i Channel Outliers"%vfat
        chanOutliers = np.column_stack((chanMaxVT1[0,:],np.array(hot_channels[vfat]).astype(float)))
        print chanOutliers
        pass
    pass

# Fetch trimDAC & chMask from scurveFitTree
dict_vfatTrimMaskData = {}
if options.chConfigKnown:
    list_bNames = ["vfatN"]
    if not (options.channels or options.PanPin):
        list_bNames.append("ROBstr")
        pass
    elif options.channels:
        #list_bNames.append("vfatCh")
        list_bNames.append("vfatCH")
        pass
    elif options.PanPin:
        list_bNames.append("panPin")
        pass
    list_bNames.append("mask")
    list_bNames.append("trimDAC")

    try:
        array_VFATSCurveData = rp.root2array(options.fileScurveFitTree,treename="scurveFitTree",branches=list_bNames)
        dict_vfatTrimMaskData = dict((idx,initVFATArray(array_VFATSCurveData.dtype)) for idx in np.unique(array_VFATSCurveData[list_bNames[0]]))
        for dataPt in array_VFATSCurveData:
            dict_vfatTrimMaskData[dataPt['vfatN']][dataPt[list_bNames[1]]]['mask'] =  dataPt['mask']
            dict_vfatTrimMaskData[dataPt['vfatN']][dataPt[list_bNames[1]]]['trimDAC'] =  dataPt['trimDAC']
            pass
        pass
    except Exception as e:
        print '%s does not seem to exist'%options.fileScurveFitTree
        print e
        pass
    pass

#Save Output
outF.cd()
saveSummary(dictSummary=vSum, name='%s/ThreshSummary.png'%filename, drawOpt="colz")

vSumProj = {}
for vfat in range(0,24):
    vSumProj[vfat] = vSum[vfat].ProjectionY()
    pass
saveSummary(dictSummary=vSumProj, name='%s/VFATSummary.png'%filename, drawOpt="")

#Save VT1Max Distributions Before/After Outlier Rejection
canv_vt1Max = make3x8Canvas(
        name="canv_vt1Max", 
        initialContent=dict_hMaxVT1, 
        initialDrawOpt="hist",
        secondaryContent=dict_hMaxVT1_NoOutlier,
        secondaryDrawOpt="hist")
canv_vt1Max.SaveAs(filename+'/VT1MaxSummary.png')

#Subtracting off the hot channels, so the projection shows only usable ones.
if not options.pervfat:
    print "Subtracting off hot channels"
    for vfat in range(0,24):
        for chan in range(0,vSum[vfat].GetNbinsX()):
            isHotChan = hot_channels[vfat][chan]

            if options.chConfigKnown:
                isHotChan = (isHotChan or dict_vfatTrimMaskData[vfat][chan]['mask'])
                pass

            if isHotChan:
                print 'VFAT %i Strip %i is noisy'%(vfat,chan)
                for thresh in range(VT1_MAX+1):
                    vSum[vfat].SetBinContent(chan, thresh, 0)
                    # vSum[vfat].SetBinError(chan, thresh, 0)
                    pass
                pass
            pass
        pass
    pass

#Save output with new hot channels subtracted off
saveSummary(dictSummary=vSum, name='%s/ThreshPrunedSummary.png'%filename, drawOpt="colz")

vSumProjPruned = {}
for vfat in range(0,24):
    vSumProjPruned[vfat] = vSum[vfat].ProjectionY("h_VT1_VFAT%i"%vfat)
    vSumProjPruned[vfat].Write()
    pass
saveSummary(dictSummary=vSumProjPruned, name='%s/VFATPrunedSummary.png'%filename, drawOpt="")

#Now determine what VT1 to use for configuration.  The first threshold bin with no entries for now.
#Make a text file readable by TTree::ReadFile
print 'Determining the VT1 values for each VFAT'
vt1 = dict((vfat,0) for vfat in range(0,24))
for vfat in range(0,24):
    proj = vSum[vfat].ProjectionY()
    proj.Draw()
    for thresh in range(VT1_MAX+1,0,-1):
        if (proj.GetBinContent(thresh+1)) > 10.0:
            print 'vt1 for VFAT %i found'%vfat
            vt1[vfat]=(thresh+1)
            break
        pass
    pass

print "trimRange:"
print trimRange
print "vt1:"
print vt1

txt_vfat = open(filename+"/vfatConfig.txt", 'w')
txt_vfat.write("vfatN/I:vfatID/I:vt1/I:trimRange/I\n")
for vfat in range(0,24):
    txt_vfat.write('%i\t%i\t%i\t%i\n'%(vfat,dict_vfatID[vfat],vt1[vfat],trimRange[vfat]))
    pass
txt_vfat.close()

# Make output TTree
myT = r.TTree('thrAnaTree','Tree Holding Analyzed Threshold Data')
myT.ReadFile(filename+"/vfatConfig.txt")
myT.Write()
outF.Close()

#Update channel registers configuration file
if options.chConfigKnown:
    confF = open(filename+'/chConfig_MasksUpdated.txt','w')
    confF.write('vfatN/I:vfatID/I:vfatCH/I:trimDAC/I:mask/I\n')

    if options.debug:
        print 'vfatN/I:vfatID/I:vfatCH/I:trimDAC/I:mask/I\n'
        pass

    for vfat in range (0,24):
        for j in range (0, 128):
            chan = vfatCh_lookup[vfat][j]
            if options.debug:
                print '%i\t%i\t%i\t%i\t%i\n'%(vfat,dict_vfatID[vfat],chan,dict_vfatTrimMaskData[vfat][j]['trimDAC'],int(hot_channels[vfat][j] or dict_vfatTrimMaskData[vfat][j]['mask']))
                pass

            confF.write('%i\t%i\t%i\t%i\t%i\n'%(vfat,dict_vfatID[vfat],chan,dict_vfatTrimMaskData[vfat][j]['trimDAC'],int(hot_channels[vfat][j] or dict_vfatTrimMaskData[vfat][j]['mask'])))
            pass
        pass

    confF.close()
    pass

print 'Analysis Completed Successfully'
