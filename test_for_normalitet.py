# -*- coding: utf-8 -*-
"""
Created on Mon Feb 10 11:03:08 2025

@author: 47968
"""
# Denne koden er generert av ChatGPT (OpenAI) basert på mine instruksjoner.
# Ingen linjer er skrevet manuelt, men enkelte deler kan være redigert i etterkant.

import pandas as pd
from scipy.stats import shapiro, normaltest

# Les inn Excel-fil
df = pd.read_excel('ph_redox_ledningsevne_data.xlsx', sheet_name='toc')
 
# Test hver kolonne for normalitet
normalitetsresultater = {}
for kolonne in df.columns:
    data = df[kolonne].dropna()

    # Sjekk at datasettet er stort nok og har variasjon
    if len(data) < 3 or data.nunique() == 1:
        stat, p_verdi = float('nan'), float('nan')  # Ikke nok variasjon/data
        test_navn = "Ikke nok data"
    elif len(data) < 5000:
        stat, p_verdi = shapiro(data)
        test_navn = "Shapiro-Wilk"
    else:
        stat, p_verdi = normaltest(data)  # Alternativ for store datasett
        test_navn = "D’Agostino’s K²"

    normalitetsresultater[kolonne] = {'Test': test_navn, 'Test-statistikk': stat, 'p-verdi': p_verdi}

# Skriv ut resultatene
for kolonne, resultater in normalitetsresultater.items():
    print(f"Kolonne: {kolonne}")
    print(f"  Test: {resultater['Test']}")
    print(f"  Test-statistikk: {resultater['Test-statistikk']}")
    print(f"  p-verdi: {resultater['p-verdi']}")
    if resultater['p-verdi'] > 0.05:
        print("  ✅ Normalfordelt (ikke signifikant)")
    elif resultater['p-verdi'] <= 0.05:
        print("  ❌ Ikke normalfordelt (signifikant)")
    else:
        print("  ⚠️ Ikke nok data til å teste normalitet")
    print()
