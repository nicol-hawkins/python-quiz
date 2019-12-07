
    ### CREATE
    # Create a single Herb object and save in DB
# herb = Herb.objects.create(
#     common_name="Skullcap",
#     botanical_name="Scutellaria lateriflora",
#     image="static/images/skullcap.png"
#     question="Have you been suffering from nervous exhaustion do to mental overload, nervous breakdowns, depression and/or nerve pain?"
#     info="Skullcap is a is a restorative nervine thats restores the nervous system and can reduce pain caused by neuraligia. It is only mildy sedating, which makes it suitable to take any time of day."
# )





# answers = [yes = {{ herb.id }}]





# Looking up a bunch of things in the DB based on aa list of IDs
# list_of_ids = [1, 3, 10]
# relevant_objects = NameOfModel.objects.filter(id__in=list_of_ids)

# # Splitting a strin by an underscore
# example_string = 'thing_otherthing'
# first_thing, second_thing = example_thing.split('_')

# second_thing = 

# from .models import Herb


list_of_ids = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
relevant_herbs = Herb.objects.filter(id__in=list_of_ids)

# Splitting a string by an underscore
# example_string = 'thing_otherthing'
answer_string = relevant_herbs
answer, herb_id = answer_string.split('_')

herb_id = []
for i in herb_id:
    print


for _id in list_of_ids:
    herb_id = _id
    print(answer_string.split('_'))

herb_id = []
   











