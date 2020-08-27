import sqlite3
from sqlite3 import Error

def create_connection(db_file):
  connection = None
  try:
    connection = sqlite3.connect(db_file)
    print(sqlite3.version)
  except Error as e:
    print(e)
  
  return connection

def close_connection(connection):
  if connection:
    connection.close()

def create_table(connection, create_table_sql):
  try:
    cursor = connection.cursor()
    cursor.execute(create_table_sql)
  except Error as e:
    print(e)

def create_db(db_file):
  sql_create_symbols_table = """CREATE TABLE IF NOT EXISTS symbols (
                                    id integer PRIMARY_KEY,
                                    symbol text NOT NULL,
                                    name text NOT NULL,
                                    exchange text,
                                    sector text,
                                    daily_updated text NOT NULL,
                                    report_updated text NOT NULL,
                                );"""

  sql_create_dailies_table = """CREATE TABLE IF NOT EXISTS dailies (
                                    id integer PRIMARY_KEY,
                                    symbol text NOT NULL,
                                    date text NOT NULL,
                                    open real NOT NULL,
                                    high real NOT NULL,
                                    low real NOT NULL,
                                    close real NOT NULL,
                                    volume integer NOT NULL,
                                    dividend real,
                                    split real
                                );"""

  sql_create_targets_table = """CREATE TABLE IF NOT EXISTS targets (
                                    id integer PRIMARY_KEY,
                                    name text NOT NULL,
                                    days integer NOT NULL,
                                    gain_threshold real NOT NULL,
                                    pattern_in_target_rate real NOT NULL,
                                    target_in_pattern_rate real NOT NULL
                                );"""

  sql_create_income_table = """CREATE TABLE IF NOT EXISTS income (
                                    id integer PRIMARY_KEY,
                                    symbol text NOT NULL,
                                    report_type text NOT NULL,
                                    fiscal_ending_date text NOT NULL,
                                    reported_currency text,
                                    total_revenue integer,
                                    total_operating_expense integer,
                                    cost_of_revenue integer,
                                    gross_profit integer,
                                    ebit integer,
                                    net_income integer,
                                    research_development integer,
                                    effect_of_accounting_charges integer,
                                    income_before_tax integer,
                                    minority_interest integer
                                    selling_general_administrative integer,
                                    other_non_operating_income integer,
                                    operating_income integer,
                                    interest_expense integer,
                                    tax_provision integer,
                                    interest_income integer,
                                    net_interest_income integer,
                                    extraordinary_items integer,
                                    non_recurring integer,
                                    other_items integer,
                                    income_tax_expense integer,
                                    total_other_income_expense integer,
                                    discontinued_operations integer,
                                    net_income_continuing_operations integer,
                                    net_income_applicable_to_common_shares integer,
                                    preferred_stock_other_adjustments integer
                                );"""

  sql_create_balance_table = """CREATE TABLE IF NOT EXISTS balance (
                                    id integer PRIMARY_KEY,
                                    symbol text NOT NULL,
                                    report_type text NOT NULL,
                                    fiscal_ending_date text NOT NULL,
                                    reported_currency text,
                                    total_assets integer,
                                    intangible_assets integer,
                                    other_current_assets integer,
                                    earning_assets integer,
                                    other_current_assets integer,
                                    total_liabilities integer,
                                    total_shareholder_equity integer,
                                    deferred_longterm_liabilities integer,
                                    other_current_liabilities integer,
                                    common_stock integer,
                                    retained_earnings integer,
                                    other_liabilities integer,
                                    goodwill integer,
                                    other_assets integer,
                                    cash integer,
                                    total_current_liabilities integer,
                                    short_term_debt integer,
                                    current_long_term_debt integer,
                                    other_shareholder_equity integer,
                                    property_plant_equipment integer,
                                    total_current_assets integer,
                                    longterm_investments integer,
                                    net_tangible_assets integer,
                                    shorterm_investments integer,
                                    net_receivables integer,
                                    longterm_debt integer,
                                    inventory integer,
                                    accounts_payable integer,
                                    total_permanent_equity integer,
                                    additional_paid_in_capital integer,
                                    common_stock_total_equity integer,
                                    preferred_stock_total_equity integer,
                                    retained_earnings_total_equity integer,
                                    treasury_stock integer,
                                    accumulated_amortization integer,
                                    other_non_current_assets integer,
                                    deferred_longterm_asset_changes integer,
                                    total_non_current_assets integer,
                                    capital_lease_obligations integer,
                                    total_longterm_debt integer,
                                    other_non_current_liabilities integer,
                                    total_non_current_liabilities integer,
                                    negative_goodwill integer,
                                    warrants integer,
                                    preferred_stock_redeemable integer,
                                    capital_surplus integer,
                                    liabilities_shareholder_equity integer,
                                    cash_shortterm_investments integer,
                                    accumulated_depreciation integer,
                                    common_stock_shares_outstanding integer
                                );"""

  sql_create_cashflow_table = """CREATE TABLE IF NOT EXISTS cashflow (
                                    id integer PRIMARY_KEY,
                                    symbol text NOT NULL,
                                    report_type text NOT NULL,
                                    fiscal_ending_date text NOT NULL,
                                    reported_currency text,
                                    investments integer,
                                    change_in_liabilities integer,
                                    cashflow_from_investments integer,
                                    other_cashflow_from_investments integer,
                                    net_borrowings integer,
                                    cashflow_from_financing integer,
                                    other_cashflow_from_financing integer,
                                    change_in_operating_activities integer,
                                    net_income integer,
                                    change_in_cash integer,
                                    operating_cash_flow integer,
                                    depreciation integer,
                                    dividend_payout integer,
                                    stock_sale_and_purchase integer,
                                    change_in_inventory integer,
                                    change_in_account_receivables integer,
                                    change_in_net_income integer,
                                    capital_expenditures integer,
                                    change_in_receivables integer,
                                    change_in_exchange_rate integer,
                                    change_in_cash_equivalents integer
                                );"""

  sql_create_indicators_table = """CREATE TABLE IF NOT EXISTS indicators (
                                    id integer PRIMARY_KEY,
                                    symbol text NOT NULL,
                                    date text NOT NULL,
                                    SMA_30 real,
                                    SMA_200 real,
                                    EMA_30 real,
                                    EMA_200 real,
                                    MAMA real,
                                    S_MACD real,
                                    E_MACD real,
                                    M_MACD real,
                                    S_STOCH real,
                                    E_STOCH real,
                                    M_STOCH real,
                                    RSI real,
                                    STOCH_RSI real,
                                    ADX real,
                                    BOP real,
                                    CCI real,
                                    CMO real,
                                    AROON_UP real,
                                    AROON_DOWN real,
                                    MFI real,
                                    MINUS_DI real,
                                    PLUS_DI real,
                                    BBANDS_HIGH real,
                                    BBANDS_LOW real,
                                    SAR real,
                                    ADLINE real,
                                    OBV real
                                );"""

  connection = create_connection(db_file)

  if connection is not None:
    create_table(connection, sql_create_symbols_table)
    create_table(connection, sql_create_dailies_table)
    create_table(connection, sql_create_targets_table)
    create_table(connection, sql_create_income_table)
    create_table(connection, sql_create_balance_table)
    create_table(connection, sql_create_cashflow_table)
    create_table(connection, sql_create_indicators_table)
  else:
    print("Error: Database connection failed.")

  return connection

def update_table(connection, sql, row_data):
  cursor = connection.cursor()
  if type(row_data) == 'tuple':
    cursor.execute(sql, row_data)
  else: # list
    cursor.executemany(sql, row_data)
  connection.commit()
  return cursor.lastrowid

def create_symbols(connection, symbols):
  sql = 'INSERT INTO symbols VALUES(?,?,?,?,?,?)'
  return update_table(connection, sql, symbols)

def create_dailies(connection, dailies):
  sql = 'INSERT INTO dailies VALUES(?,?,?,?,?,?,?,?)'
  return update_table(connection, sql, dailies)

def create_targets(connection, targets):
  sql = 'INSERT INTO targets VALUES(?,?,?,?,?)'
  return update_table(connection, targets)

def create_income_statements(connection, income):
  sql = 'INSERT INTO income VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)'
  return update_table(connection, income)

def create_balance_sheets(connection, balance):
  sql = 'INSERT INTO balance VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)'
  return update_table(connection, balance)

def create_cashflows(connection, cashflows):
  sql = 'INSERT INTO cashflow VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)'
  return update_table(connection, cashflows)

def create_indicators(connection, indicators):
  sql = 'INSERT INTO indicators VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)'
  return update_table(connection, indicators)

def last_updated(connection, symbol):
  sql = 'SELECT updated FROM symbols WHERE symbol=?'
  cursor = connection.cursor()
  cursor.execute(sql, (symbol,))
  return cursor.fetch()



