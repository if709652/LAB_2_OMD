import pandas as pd
import Notas_BehavioralFinance.Funciones_BehavioralFinance as fn

# Opciones para visualizar data frames en consola
pd.set_option('display.max_rows', 5000)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)

datos = fn.f_leerarchivo(p0_parametro='Notas_BehavioralFinance/archivo_tradeview_0.json')
