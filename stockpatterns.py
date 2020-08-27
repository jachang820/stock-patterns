import argparse, sys
from scripts.variables import hidden_variables
from scripts import database
from scripts import download_stocks as AlphaVantage

if __name__ = "__main__":
  parser = argparse.ArgumentParser(
    prog = "stockpatterns",
    description = "Try out different stock trading strategies.")
  parser.add_argument('--init', 
    action = "store_true", 
    help = "Initialize database")

  api_key = hidden_variables['AV_KEY']
  api_interval = hidden_variables['AV_INTERVAL']  
  db_file = "database/stockpatterns_db.sqlite"

  args = parser.parse_args()

  if args.init:
    # Create database tables
    connection = database.create_db(db_file)

    # Create major forex pairs
    database.create_dailies(connection, 
      AlphaVantage.get_fx_pair("EUR", "USD", api_key, api_interval))
    database.create_dailies(connection, 
      AlphaVantage.get_fx_pair("USD", "JPY", api_key, api_interval))
    database.create_dailies(connection, 
      AlphaVantage.get_fx_pair("GBP", "USD", api_key, api_interval))
    database.create_dailies(connection, 
      AlphaVantage.get_fx_pair("USD", "CNY", api_key, api_interval))

    # Create a default basket of stocks
    database.create_dailies(connection, 
      AlphaVantage.get_stock("FB", api_key, api_interval))
    database.create_dailies(connection, 
      AlphaVantage.get_stock("IBM", api_key, api_interval))
    database.create_dailies(connection, 
      AlphaVantage.get_stock("AAPL", api_key, api_interval))
    database.create_dailies(connection, 
      AlphaVantage.get_stock("TSLA", api_key, api_interval))
    database.create_dailies(connection, 
      AlphaVantage.get_stock("WMT", api_key, api_interval))

    # Download fundamentals
    

  else:
    connection = database.create_connection(db_file)

  # Download data and track new company
  if args.track:
    pass

  # Update data for a company or all
  if args.update:
    pass

