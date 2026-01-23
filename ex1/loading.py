#!/usr/bin/python3

import importlib


def generate_graph() -> None:
    # Generating data points
    # Those are 1000 random values
    print('Analyzing Matrix data...')
    data_points = np.random.randn(1000)

    # Converting datapoints from numpy to dataframes for pandas
    df = pd.DataFrame(data_points, columns=['Data'])
    print('Processing 1000 data points...')

    # One data is one progression through time
    df['Time'] = np.arange(len(df))

    # Creating graph
    plt.figure(figsize=(10, 6))

    # Drawing data
    plt.plot(df['Time'], df['Data'], color='green', linewidth=0.4)

    print('Generating visualization...')
    # Save as...
    plt.savefig('matrix_analysis.png')
    return None


def package_comparison(package) -> str:
    # Checks the package version and compare it to the expected one
    try:
        name = package.__name__
        with open('requirements.txt', 'r') as rq:
            for line in rq:
                expected = 'n/a'
                if name == line.split('==')[0]:
                    expected = line.split('==')[1]
    except Exception:
        return "Couldn't find the module"
    return f"Package {name} -> Current: {package.__version__} "\
        f"| Expected: {expected}"


if __name__ == '__main__':
    modules_present = True
    print('LOADING STATUS: Loading programs...')
    print('')
    print('Checking dependencies:')
    # Checks dependencies. Print uninstalled packages
    try:
        pd = importlib.import_module('pandas')
        name = getattr(pd, '__name__', 'n/a')
        version = getattr(pd, '__version__', 'n/a')
        print(f"[OK] {name} ({version}) - Data manipulation ready")
    except Exception as e:
        modules_present = False
        print(f"[ERROR] pandas - Not found: {e}")
    try:
        requests = importlib.import_module('requests')
        name = getattr(requests, '__name__', 'n/a')
        version = getattr(requests, '__version__', 'n/a')
        print(f"[OK] {name} ({version}) - Network access ready")
    except Exception as e:
        modules_present = False
        print(f"[ERROR] requests - Not found: {e}")
    try:
        matplotlib = importlib.import_module('matplotlib')
        plt = importlib.import_module('matplotlib.pyplot')
        name = getattr(matplotlib, '__name__', 'n/a')
        version = getattr(matplotlib, '__version__', 'n/a')
        print(f"[OK] {name} ({version}) - Virtualization ready")
    except Exception as e:
        modules_present = False
        print(f"[ERROR] matplotlib - Not found: {e}")
    try:
        np = importlib.import_module('numpy')
        name = getattr(np, '__name__', 'n/a')
        version = getattr(np, '__version__', 'n/a')
        print(f"[OK] {name} ({version}) - Numpy ready")
    except Exception as e:
        modules_present = False
        print(f"[ERROR] numpy - Not found: {e}")
    if not modules_present:
        print("[!] Please install the necessary modules")
        print("Exiting.")
        exit(1)
    print('')
    generate_graph()
    print('')
    print(package_comparison(np))
    print(package_comparison(pd))
    print(package_comparison(matplotlib))
    print(package_comparison(requests))
    print('\nAnalysis complete!')
    print('Results saved to: matrix_analysis.png')
