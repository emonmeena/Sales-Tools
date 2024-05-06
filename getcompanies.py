import json


def load_data(filename):
    """Load JSON data from a file"""
    with open(filename, "r") as file:
        data = json.load(file)
    return data


def print_company_info(companies):
    """Print detailed information for each company"""
    for company in companies:
        print(f"Company Name: {company['name']}")
        print(f"URL Name: {company['urlName']}")
        print(f"Logo URL: {company['logoUrl']}")
        print(f"Primary Industry: {company['primaryIndustry']}")
        print(f"Total Employees: {company['totalEmployees']}")
        print(f"Company Rating: {company['companyRating']}")
        print("Critically Rated Aspects:")
        for aspect in company["criticallyRatedFor"]:
            print(f"  - {aspect['name']}: {aspect['ratings']}")
        print("-------------")


def calculate_statistics(companies):
    """Calculate and print some statistics about the companies"""
    total_companies = len(companies)
    total_rating = sum(company["companyRating"] for company in companies)
    average_rating = total_rating / total_companies if total_companies > 0 else 0
    print(f"Total Companies: {total_companies}")
    print(f"Average Company Rating: {average_rating:.2f}")


def main():
    # Assuming the JSON data is stored in a file named 'data.json'
    filename = "public_bpc_companies_example.json"
    data = load_data(filename)

    # Assuming the main key in JSON is 'cards'
    companies = data

    for c in companies:
        for a in c["cards"]:
            print(a["name"])

    # Print detailed information for each company
    # print_company_info(companies)

    # Calculate and print statistics about the companies
    # calculate_statistics(companies)


if __name__ == "__main__":
    main()
