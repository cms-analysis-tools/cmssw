import FWCore.ParameterSet.Config as cms

muonPFNoPileUpIsolation = cms.EDProducer(
    "CITKPFIsolationSumProducer",
    srcToIsolate = cms.InputTag("muons"),
    srcForIsolationCone = cms.InputTag('pfNoPileUpCandidates'),
    isolationConeDefinitions = cms.VPSet(
        cms.PSet( isolationAlgo = cms.string('MuonPFIsolationWithConeVeto'), 
                  coneSize = cms.double(0.3),
                  VetoThreshold = cms.double(0.0),
                  VetoConeSize = cms.double(0.0),
                  isolateAgainst = cms.string('h+'),
                  miniAODVertexCodes = cms.vuint32(2,3) ),
        cms.PSet( isolationAlgo = cms.string('MuonPFIsolationWithConeVeto'), 
                  coneSize = cms.double(0.3),
                  VetoThreshold = cms.double(0.5),
                  VetoConeSize = cms.double(0.0),
                  isolateAgainst = cms.string('h0'),
                  miniAODVertexCodes = cms.vuint32(2,3) ),
        cms.PSet( isolationAlgo = cms.string('MuonPFIsolationWithConeVeto'), 
                  coneSize = cms.double(0.3),
                  VetoThreshold = cms.double(0.5),
                  VetoConeSize = cms.double(0.0),
                  isolateAgainst = cms.string('gamma'),
                  miniAODVertexCodes = cms.vuint32(2,3) )
        )
    )

muonPFPileUpIsolation = cms.EDProducer(
    "CITKPFIsolationSumProducer",
    srcToIsolate = cms.InputTag("muons"),
    srcForIsolationCone = cms.InputTag('pfPileUpAllChargedParticles'),
    isolationConeDefinitions = cms.VPSet(
        cms.PSet( isolationAlgo = cms.string('MuonPFIsolationWithConeVeto'), 
                  coneSize = cms.double(0.3),
                  VetoThreshold = cms.double(0.5),
                  VetoConeSize = cms.double(0.0),
                  isolateAgainst = cms.string('h+'),
                  miniAODVertexCodes = cms.vuint32(0,1) )
        )
    )
