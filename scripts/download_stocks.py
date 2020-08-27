import urllib.request, json
from datetime import date
import time

query = "https://www.alphavantage.co/query"

def _convert_to_digit(n):
  if n == "None":
    return 0
  try:
    return int(n)
  except ValueError:
    return n

def _convert_line_to_list(dict):
  row = []
  for line_item, value in dict:
    row.append(_convert_to_digit(value))
  return row

def _download_data_from_api(url):
  with urllib.request.urlopen(url):
    data = json.loads(url.read().decode())
  return data

def _get_output_size(last_updated):
  if last_updated is not None and date.today() - last_updated < 100:
    output_size = "compact"
  else:
    output_size = "full"
  return output_size

def _download_time_series(symbol, api_key, last_updated = None):
  function = "TIME_SERIES_DAILY_ADJUSTED"
  output_size = _get_output_size(last_updated)
  url = "{0}?function={1}&symbol={2}&outputsize={3}&apikey={4}".format(
    query, function, symbol, output_size, api_key)
  return _download_data_from_api(url)

def _process_stock_to_store(data, last_updated):
  json_header = "Time Series (Daily)"
  symbol = data['Meta Data']['Symbol']
  table = []
  for ticker_date, ticker in data[json_header].items():
    if ticker_date > last_updated:
      table.append((symbol, ticker_date, 
                    float(ticker.open), 
                    float(ticker.high), 
                    float(ticker.low), 
                    float(ticker.close),
                    int(ticker.volume), 
                    float(ticker['dividend amount']), 
                    float(ticker['split coefficient'])))
  return table

def _download_fx_series(from_symbol, to_symbol, api_key, last_updated = None):
  function = "FX_DAILY"
  output_size = _get_output_size(last_updated)
  url = "{0}?function={1}&from_symbol={2}&to_symbol={3}&outputsize={4}&apikey={5}".format(
    query, function, from_symbol, to_symbol, output_size, api_key)
  return _download_data_from_api(url)

def _process_fx_to_store(data, last_updated):
  json_header = "Time Series FX (Daily)"
  from_symbol = data['Meta Data']['From Symbol']
  to_symbol = data['Meta Data']['To Symbol']
  pair = "{0}-{1}".format(from_symbol, to_symbol)
  table = []
  for ticker_date, ticker in data[json_header].items():
    if ticker_date > last_updated:
      table.append((pair, ticker_date, 
                    float(ticker.open), 
                    float(ticker.high), 
                    float(ticker.low), 
                    float(ticker.close), 
                    0, 0, 0))
  return table

def _download_fundamentals(symbol, function, api_key):
  url = "{0}?function={1}&symbol={2}&apikey={3}".format(
    query, function, symbol, api_key)
  return _download_data_from_api(url)

def _process_fundamentals_to_store(data):
  symbol = data['symbol']
  table = []
  for report in data['annualReports']:
    row = [symbol, 'Annual']
    row.extend(_convert_line_to_list(report))
    table.append(tuple(row))
  
  for report in data['quarterlyReports']:
    row = [symbol, 'Quarterly']
    row.extend(_convert_line_to_list(report))
    table.append(tuple(row))

  return table

def get_stock(symbol, api_key, api_interval, last_updated = None):
  data = _download_time_series(symbol, api_key, last_updated)
  print("Downloading data for {0} stock...".format(symbol))
  time.sleep(api_interval)
  return _process_stock_to_store(data, last_updated)

def get_fx_pair(from_symbol, to_symbol, api_key, api_interval, last_updated = None):
  data = _download_fx_series(from_symbol, to_symbol, api_key, last_updated)
  print("Downloading data for {0}-{1} forex pair...".format(from_symbol, to_symbol))
  time.sleep(api_interval)
  return _process_fx_to_store(data, last_updated)

def get_company_overview(symbol, api_key, api_interval, last_updated):
  function = "OVERVIEW"
  data = _download_fundamentals(symbol, function)
  print("Downloading data for {0} company overview...".format(data['Symbol']))
  time.sleep(api_interval)
  return (data['Symbol'], data['Name'], data['Exchange'], data['Sector'],
          last_updated, data['LatestQuarter'])

def get_income_statement(symbol, api_key, api_interval):
  function = "INCOME_STATEMENT"
  data = _download_fundamentals(symbol, function)
  print("Downloading data for {0} income statement...".format(data['symbol']))
  time.sleep(api_interval)
  return _process_fundamentals_to_store(data)

def _download_balance_sheet(symbol, api_key, api_interval):
  function = "BALANCE_SHEET"
  data = _download_fundamentals(symbol, function)
  print("Downloading data for {0} balance sheet...".format(data['symbol']))
  time.sleep(api_interval)
  return _process_fundamentals_to_store(data)

def _download_cash_flow(symbol, api_key, api_interval):
  function = "CASH_FLOW"
  data = _download_fundamentals(symbol, function)
  print("Downloading data for {0} cash flow...".format(data['symbol']))
  time.sleep(api_interval)
  return _process_fundamentals_to_store(data)
