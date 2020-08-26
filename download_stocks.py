import urllib.request, json
from datetime import date
from variables.py import hidden_variables

query = "https://www.alphavantage.co/query"
api_key = hidden_variables['AV_KEY']

def _download_data_from_api(url):
  with urllib.request.urlopen(url):
    data = json.loads(url.read().decode())
  return data

def _get_output_size(symbol, last_updated):
  if date.today() - last_updated < 100:
    output_size = "compact"
  else:
    output_size = "full"
  return output_size

def download_time_series(symbol, last_updated):
  function = "TIME_SERIES_DAILY_ADJUSTED"
  output_size = _get_output_size(symbol, last_updated)
  url = "{0}?function={1}&symbol={2}&outputsize={3}&apikey={4}".format(
    query, function, symbol, output_size, api_key)
  return _download_data_from_api(url)

def download_fx_series(from_symbol, to_symbol, last_updated):
  function = "FX_DAILY"
  output_size = _get_output_size("{0}-{1}".format(from_symbol, to_symbol), last_updated)
  url = "{0}?function={1}&from_symbol={2}&to_symbol={3}&outputsize={4}&apikey={5}".format(
    query, function, from_symbol, to_symbol, output_size, api_key)
  return _download_data_from_api(url)

def _download_fundamentals(symbol, function):
  url = "{0}?function={1}&symbol={2}&apikey={3}".format(
    query, function, symbol, api_key)
  return _download_data_from_api(url)

def download_company_overview(symbol):
  function = "OVERVIEW"
  return _download_fundamentals(symbol, function)

def download_income_statement(symbol):
  function = "INCOME_STATEMENT"
  return _download_fundamentals(symbol, function)

def download_balance_sheet(symbol):
  function = "BALANCE_SHEET"
  return _download_fundamentals(symbol, function)

def download_cash_flow(symbol):
  function = "CASH_FLOW"
  return _download_fundamentals(symbol, function)

