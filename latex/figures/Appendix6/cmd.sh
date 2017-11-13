#jets='jets2 jets3 jets4'
#leptons='electron muon'
for j in jets2 jets3 jets4; do for l in electron muon; do mkdir -p ${j}/${l}; scp aperloff@cmslpc-sl6.fnal.gov:/uscms_data/d2/aperloff/Summer12ME8TeV/2017_09_18_LimitHistograms_PU_CSV_TTbar_QCDEta_Scale/nominal_AllPlots/${j}/${l}/*.eps ${j}/${l}/; done; done
