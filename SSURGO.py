# -*- coding: utf-8 -*-
"""
Created on Wed Mar  8 18:46:19 2023

@author: Reena Shrestha
"""

import geopandas as gpd
import fiona
import pandas as pd
import os
from matplotlib import pyplot as plt

#Setting working directory
path ="C:/Users/Reena Shrestha/OneDrive - lamar.edu/Desktop/Machine learning/Project_2/minor_aquifers"
os.chdir(path)

# file for major aquifer
fname = 'Minor_Aquifers.shp'


aquifer = gpd.read_file(fname)
aquifer.columns
aquifer.AQU_NAME.unique()

Name = 'WOODBINE'
woodbine = aquifer.loc[aquifer.AQU_NAME == Name]

espgaea = 5070
wb = woodbine.to_crs(espgaea)
wb.plot()
wb.to_file('woodbine.shp')

#Setting working directory
fname ='C:/Users/Reena Shrestha/OneDrive - lamar.edu/Desktop/Machine learning/Project_2/gSSURGO_TX/gSSURGO_TX.gdb'
layers = fiona.listlayers(fname)

#extracting the layers essential for soil texture
texture = gpd.read_file(fname,layer = 'chtexture')
texturegrp = gpd.read_file(fname,layer = 'chtexturegrp')
horizon = gpd.read_file(fname,layer = 'chorizon')
component = gpd.read_file(fname,layer = 'component')
mapunit = gpd.read_file(fname,layer = 'mapunit')
legend = gpd.read_file(fname,layer = 'legend')
#soilpoly = gpd.read_file(fname,layer = 'MUPOLYGON')

path1 = "C:/Users/Reena Shrestha/OneDrive - lamar.edu/Desktop/Machine learning/Project_2"
os.chdir(path1)
fname1 = 'Mu_WB.shp'
soilpoly = gpd.read_file(fname1)


#soilpoly.crs
#clipped_polygon = gpd.clip(soilpoly, oggaea)
#clipped_polygon.to_file('clipped_polygon.shp')
#clipped_polygon.plot()
#Plot the soil polygon
plotx = soilpoly.plot()
plotx.set_xlabel('Easting')
plotx.set_ylabel('Northing')



#perform joins to get soil texture with the map
texturegrp1 = pd.merge(texturegrp,texture[['texcl','chtgkey']], on='chtgkey',how='left')
horizon1 = pd.merge(horizon,texturegrp1[['texcl','chkey']], on='chkey',how='left')
component1 = pd.merge(component,horizon1[['texcl','cokey']], on='cokey',how='left')
mapunit1 = pd.merge(mapunit,component1[['texcl','mukey']], on='mukey',how='left')


mukey = soilpoly['MUKEY']
soilpoly = soilpoly.assign(mukey=mukey)

#extract the crs and geometry
crsx = soilpoly.crs
geomx = soilpoly.geometry


soilpoly1 = pd.merge(soilpoly,mapunit1,on='mukey',how='inner')
soilpoly1.set_geometry(geomx,inplace=True,crs = crsx)
soilpoly1.plot('texcl')
soilpoly1
