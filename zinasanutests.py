def analyze_data():
    file_path = r'C:\Users\daniels\Downloads\data.txt'
    results = {}

    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    header = lines[0].strip().split(',')
    data = [line.strip().split(',') for line in lines[1:]]

    header_index = {column: idx for idx, column in enumerate(header)}

    founded_years = []
    for row in data:
        try:
            founded_years.append(int(row[header_index['Founded']]))
        except ValueError:
            continue
    results['oldest_company_year'] = min(founded_years)

    total_employees_latvia = sum(
        int(row[header_index['Number of employees']])
        for row in data
        if row[header_index['Country']] == 'Latvia' and row[header_index['Number of employees']].isdigit()
    )
    results['total_employees_latvia'] = total_employees_latvia

    total_employees_telecom_latvia = sum(
        int(row[header_index['Number of employees']])
        for row in data
        if row[header_index['Country']] == 'Latvia' and row[header_index['Industry']] == 'Telecommunications' and row[header_index['Number of employees']].isdigit()
    )
    results['total_employees_telecom_latvia'] = total_employees_telecom_latvia

    ssl_certified_count = sum(
        1
        for row in data
        if row[header_index['Country']] == 'Latvia' and row[header_index['Website']].startswith('https://')
    )
    results['ssl_certified_count'] = ssl_certified_count

    org_domain_count = sum(
        1
        for row in data
        if row[header_index['Country']] == 'Latvia' and row[header_index['Website']].endswith('.org')
    )
    results['org_domain_count'] = org_domain_count

    return results

results = analyze_data()
print("Vecākā uzņēmuma dibināšanas gads:", results['oldest_company_year'])
print("Darbinieku skaits Latvijā:", results['total_employees_latvia'])
print("Darbinieku skaits telekomunikāciju nozarē Latvijā:", results['total_employees_telecom_latvia'])
print("Latvijas uzņēmumu ar SSL sertifikātu skaits:", results['ssl_certified_count'])
print(".org domēnu skaits Latvijā:", results['org_domain_count'])
