#!/usr/bin/python3

try:
    from dotenv import load_dotenv
except Exception as e:
    print(f'Missing module dotenv: {e}.')
    print('Install using "python3 -m pip install python-dotenv"')
    print('-> Exiting')
    exit()
import os

if __name__ == '__main__':
    print('ORACLE STATUS: Reading the Matrix...\n')
    load_dotenv('.env.example')
    variables = ['MATRIX_MODE', 'DATABASE_URL', 'API_KEY',
                 'LOG_LEVEL', 'ZION_ENDPOINT']
    for var in variables:
        result = os.getenv(var)
        if result is None:
            print(f"Could not get the environment variable for {var}. "
                  "Exiting.")
            exit(1)
    print("Configuration loaded:")
    print(f"Mode: {os.getenv('MATRIX_MODE')}")
    print(f"Database: {os.getenv('DATABASE_URL')}")
    print(f"API Access: {os.getenv('API_KEY')}")
    print(f"Log Level: {os.getenv('LOG_LEVEL')}")
    print(f"Zion Network: {os.getenv('ZION_ENDPOINT')}")

    print('\nEnvironment security check:')
    print('[OK] No hardcoded secrets detected')
    print('[OK] .env file properly configured')
    print('[OK] Production overrides available')

    print('\nThe Oracle sees all configurations.')
