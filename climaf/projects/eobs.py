"""

This module declares the project E-OBS : 
This archive is available on Ciclad (IPSL)

The specific attributes are:
- grid : '*'


"""

from climaf.dataloc import dataloc
from climaf.classes import cproject, calias, cfreqs, cdef
from climaf.site_settings import onCiclad, atTGCC, atIDRIS,atCerfacs,atCNRM

if onCiclad :
    # -- Create E-OBS CliMAF project
    EOBS_pattern = '/bdd/E-OBS/Grid_${grid}/${variable}_${grid}_${PERIOD}_v15.0.nc4'
    cproject('E-OBS','grid', 'frequency', separator='%')
    dataloc(project='E-OBS', organization='generic', url=EOBS_pattern)
    
    # -- Make a 
    cdef('frequency', 'daily', project='E-OBS')
    cdef('grid', '*deg_*', project='E-OBS')
    cdef('period', '*', project='E-OBS')
    cdef('variable', '*', project='E-OBS')
    cfreqs('E-OBS',{'daily':'day'})
    
    calias('E-OBS', 'tasmin', 'tn')
    calias('E-OBS', 'tasmax', 'tx')
    


