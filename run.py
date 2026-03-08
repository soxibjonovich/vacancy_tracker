import argparse

from api_manager import ApiManager


def setup_parser():
	parser = argparse.ArgumentParser(
	    prog="Vacancy Tracker",
	)
	
	parser.add_argument('query')
	parser.add_argument('-sf', '--search_field', help="Search field (name, company_name) (by default all)")
	parser.add_argument('-f', '--file', help="Save to file")
	
	return parser
	
	
def main():
    parser = setup_parser()
    args = parser.parse_args()
    
    api_manager = ApiManager()
    vacancies = api_manager.get_vacancies(args.query, search_field=args.search_field)
    api_manager.print_vacancies(vacancies)
    
    if args.file:
        api_manager.save_to_json(vacancies)
    
if __name__ == '__main__':
	main()