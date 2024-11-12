# run_banks.py

import importlib

# List of bank scraping files (without the .py extension)
bank_files = [
    'bank_of_india', 
    'bank_of_maharashtra', 
    'canara_bank', 
    'central_bank_of_india',
    'state_bank_of_india',  # State Bank of India
    'axis_bank',            # Axis Bank
    'bandhan_bank',         # Bandhan Bank
    'federal_bank',         # Federal Bank
    'hdfc_bank',            # HDFC Bank
    'dcb_bank',             # DCB Bank
    'indusind_bank',        # IndusInd Bank
    'idfc_bank',      # IDFC First Bank
    'jammu_and_kashmir_bank',   # Jammu & Kashmir Bank
    'karur_vysya_bank',     # Karur Vysya Bank
    'kotak_mahindra_bank',  # Kotak Mahindra Bank
    'nainital_bank',        # Nainital Bank
    'rbl_bank',             # RBL Bank
    'tamilnad_mercantile_bank',  # Tamilnad Mercantile Bank
    'idbi_bank',            # IDBI Bank
    'capital_small_finance_bank',  # Capital Small Finance Bank
    'suryoday_small_finance_bank',  # Suryoday Small Finance Bank
    'ujjivan_small_finance_bank',    # Ujjivan Small Finance Bank
    'utkarsh_small_finance_bank',     # Utkarsh Small Finance Bank
    'esaf_small_finance_bank',        # ESAF Small Finance Bank
    'north_east_small_finance_bank',  # North East Small Finance Bank
    'unity_small_finance_bank',        # Unity Small Finance Bank
    'citibank_india',                  # Citibank India
    'dbs_bank_india',                  # DBS Bank India
    'deutsche_bank',                   # Deutsche Bank
    'hsbc_bank',                            # HSBC
    'standard_chartered_bank',         # Standard Chartered Bank
    # Add more bank files here
]

for bank in bank_files:
    print(f"Running {bank}.py...")
    importlib.import_module(bank)
    print(f"Finished running {bank}.py.")
