import os, sys
from plotterconf import *
basepath = os.path.abspath(__file__).rsplit('/xuAnalysis/',1)[0]+'/xuAnalysis/'
sys.path.append(basepath)
from ROOT.TMath import Sqrt as sqrt
from ROOT import kRed, kOrange, kBlue, kTeal, kGreen, kGray, kAzure, kPink, kCyan, kBlack, kSpring, kViolet, kYellow
from ROOT import TCanvas, gROOT
gROOT.SetBatch(1)

########## FUNCTION DEFINITIONS
hm = HistoManager(processes, systematics, '', path=path, processDic=processDic, lumi = Lumi)

def Draw(var = 'H_Lep0Pt_ElMu_2jets', ch = '', lev = 'dilepton', rebin = 1, xtit = '', ytit = 'Events', doStackOverflow = False, binlabels = '', setLogY = False, maxscale = 1.6):
  s = Stack(outpath=outpath)
  s.SetColors(colors)
  s.SetProcesses(processes)
  s.SetLumi(Lumi)
  s.SetHistoPadMargins(top = 0.08, bottom = 0.10, right = 0.06, left = 0.10)
  s.SetRatioPadMargins(top = 0.03, bottom = 0.40, right = 0.06, left = 0.10)
  s.SetTextLumi(texlumi = '%2.1f pb^{-1} (5.02 TeV)', texlumiX = 0.62, texlumiY = 0.97, texlumiS = 0.05)
  s.SetBinLabels(binlabels)
  hm.SetStackOverflow(doStackOverflow)
  hm.IsScaled = False
  name = GetName(var, ch, lev)
  hm.SetHisto(name, rebin)
  s.SetHistosFromMH(hm)
  s.SetOutName(name)
  s.SetTextChan('')
  s.SetRatioMin(2-maxscale)
  s.SetRatioMax(maxscale)
  if ch == 'MuMu': tch = '#mu#mu'
  elif ch == 'ElEl': tch = 'ee'
  else: tch = 'e#mu'
  if   lev == '2jets': Tch = tch+', #geq 2 jets'
  elif lev == '1btag': Tch =tch+ ', #geq 2 jets, #geq 1 btag'
  else: Tch=tch
  s.SetTextChan(Tch)
  tch=''
  s.SetLogY(setLogY)
  s.SetPlotMaxScale(maxscale)
  s.DrawStack(xtit, ytit)



########## PLOTS
lev = 'dilepton'
for chan in ['ElEl', 'MuMu']: 
  Draw('Jet0Pt', chan, lev, 2, 'Leading jet p_{T} (GeV)', 'Events', False, maxscale = 1.6 )
  Draw('NJets',  chan, lev, 1, 'Jet multiplicity', 'Events', True)
  Draw('MET', chan, lev, 2, 'MET (GeV)', 'Events', False, maxscale = 1.6)
  Draw('MET', chan, 'ZVeto', 2, 'MET (GeV)', 'Events', False, maxscale = 1.6)
  Draw('MET', chan, '2jetsnomet', 2, 'MET (GeV)', 'Events', False, maxscale = 1.6)
    
for chan in ['ElEl', 'MuMu']: 
  Draw('MET', chan, 'ZVeto', 1, 'MET (GeV)', 'Events', False, maxscale = 1.9)

lev = 'dilepton'
ch = 'ElMu'

Draw('Lep0Eta', 'MuMu', lev, 2, 'Lep #eta', 'Events', False, maxscale = 1.9)
Draw('Lep0Eta', 'ElEl', lev, 2, 'Lep #eta', 'Events', False, maxscale = 1.9)
Draw('DYMass', 'MuMu', lev, 10, 'm_{#mu#mu} (GeV)', 'Events', False, maxscale = 1.9)
Draw('DYMass', 'ElEl', lev, 10, 'm_{ee} ',          'Events', False, maxscale = 1.9)
for chan in ['ElEl', 'MuMu']: 
  Draw('MET', chan, 'ZVeto', 2, 'MET (GeV)', 'Events', False, maxscale = 1.6)
  Draw('MET', chan, '2jetsnomet', 2, 'MET (GeV)', 'Events', False, maxscale = 1.6)
for chan in ['ElEl', 'MuMu', 'ElMu']:
  Draw('NJets',  chan, 'dilepton', 1, 'Jet multiplicity', 'Events', True)
  Draw('Yields', chan, '', 1, 'Level', 'Events', False, maxscale = 1.2)
  Draw('YieldsSS', chan, '', 1, 'Level', 'Events', False, maxscale = 1.2)
  for lev in ['dilepton', '2jets']:
    if lev == '2jets' and chan != 'ElMu': continue
    Draw('Lep0Eta', chan, lev, 2, 'Lep #eta', 'Events', False, maxscale = 1.6)
    Draw('Lep0Pt', chan, lev, 2, 'Leading lep p_{T} (GeV)', 'Events', False, maxscale = 1.6)
    Draw('Lep1Pt', chan, lev, 2, 'Subeading lep p_{T} (GeV)', 'Events', False, maxscale = 1.6)
    Draw('DilepPt', chan, lev, 2, 'Dilepton p_{T} (GeV)', 'Events', False, maxscale = 1.6)
    Draw('DeltaPhi', chan, lev, 2, '#Delta#phi(ll) (GeV)', 'Events', False, maxscale = 1.6)
    Draw('MET', chan, lev, 2, 'MET (GeV)', 'Events', False, maxscale = 1.6)
    Draw('HT', chan, lev, 4, 'H_{T} (GeV)', 'Events', False, maxscale = 1.6)

  lev = 'dilepton'
  Draw('Btags', chan, lev, 1, 'b tag multiplicity', 'Events', True, maxscale = 1.6)
  Draw('NBtagNJets', chan, lev, 1, 'nJets,nbtags', 'Events', True,['[0,0]', '[1,0]', '[1,1]', '[2,0]', '[2,1]', '[2,2]', '[#geq 3,#geq 0]'],maxscale = 1.6 )
  Draw('Vtx', chan, lev, 1, 'Number of vertices', 'Events', False, maxscale = 1.6 )
  for lev in ['dilepton', '2jets']:
    Draw('InvMass', chan, lev, 20, 'm_{e#mu} (GeV)', 'Events', False, maxscale = 1.6 )
  for lev in ['2jets']:
    Draw('Jet0Pt', chan, lev, 4, 'Leading jet p_{T} (GeV)', 'Events', False, maxscale = 1.6 )
    Draw('Jet1Pt', chan, lev, 5, 'Subeading jet p_{T} (GeV)', 'Events', False, maxscale = 1.6 )
    Draw('Jet0Eta', chan, lev, 5, 'Leading jet #eta', 'Events', False, maxscale = 1.6 )
    Draw('Jet1Eta', chan, lev, 5, 'Subleading jet #eta', 'Events', False, maxscale = 1.6 )
