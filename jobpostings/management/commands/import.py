from django.core.management.base import BaseCommand, CommandError
import json
from jobpostings.models import JobPosting, Category

def load_jobs(path):
    with open(path, 'r') as json_file:
        json_list = list(json_file)

        for json_str in json_list:
            result = json.loads(json_str)
            yield result
            
            
def upsert_category(category):
    obj, _ = Category.objects.get_or_create(
        title = category['name'],
        defaults = {
            'title': category['name'],
        }
    )
    
    return obj
   
            
def import_job(job: dict):
    
    category = upsert_category(job['categories'][0])
    # We just use the city as location
    location = next(n for n in job['areas'] if n['type'] == 'CITY')
    
    JobPosting.objects.get_or_create(
        title = job['heading'],
        company = job['company_display_name']['name'],
        defaults = {
            'title': job['heading'],
            'company': job['company_display_name']['name'],
            'category': category,
            'location': location['name'],
            'description': job['description'],
            'summary': job['summary'],
            'logo_url': job['logo_url']
        }
    )
    
    
    

class Command(BaseCommand):
    help = "Import data"
    
    def handle(self, *args, **options):
        
        for next in load_jobs('./fixtures/imports.jsonl'):
            import_job(next)
        