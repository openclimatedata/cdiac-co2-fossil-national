# encoding: UTF-8

import os

import pandas as pd


path = os.path.dirname(os.path.realpath(__file__))
cdiac_csv = os.path.join(path, "../archive/nation.1751_2013.csv")

cdiac = pd.read_csv(
    cdiac_csv,
    skiprows=[1,2,3],
    na_values="."
)

cdiac = cdiac.rename(columns={
    'Year': "Year",
    'Total CO2 emissions from fossil-fuels and cement production (thousand metric tons of C)': "Total",
    'Emissions from solid fuel consumption': "Solid-Fuel",
    'Emissions from liquid fuel consumption': "Liquid-Fuel",
    'Emissions from gas fuel consumption': "Gas-Fuel",
    'Emissions from cement production': "Cement",
    'Emissions from gas flaring': "Gas-Flaring",
    'Per capita CO2 emissions (metric tons of carbon)': 'Per-Capita',
    'Emissions from bunker fuels (not included in the totals)': 'Bunkers'
})

cdiac.to_csv(
    os.path.join(path,"../data/cdiac-fossil-fuel-cement-national.csv"),
    encoding="UTF-8",
    index=False
)
