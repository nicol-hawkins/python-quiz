from django.db import models


class Herb(models.Model):
    common_name = models.CharField(max_length=255)
    botanical_name = models.CharField(max_length=255)
    image = models.CharField(max_length=255)
    question = models.CharField(max_length=255)
    info = models.CharField(max_length=255)




# skullcap = Herb.objects.create(
#     common_name="Skullcap",
#     botanical_name="Scutellaria lateriflora",
#     image="static/images/skullcap.png",
#     question="Have you been suffering from nervous exhaustion do to mental overload, nervous breakdowns, depression and/or nerve pain?",
#     info="Skullcap is a is a restorative nervine thats restores the nervous system and can reduce pain caused by neuraligia. It is only mildy sedating, which makes it suitable to take any time of day.",
# )    


# mullein = Herb.objects.create(
#     common_name="Mullein",
#     botanical_name="Verbascum thapus",
#     image="static/images/skullcap.png",
#     question="Question about Mullein",
#     info="Skullcap is a is a restorative nervine thats restores the nervous system and can reduce pain caused by neuraligia. It is only mildy sedating, which makes it suitable to take any time of day.",
# )    


# oat_seed = Herb.objects.create(
#     common_name="Oat Seed",
#     botanical_name="Avena Sativa",
#     image="static/images/skullcap.png",
#     question="Question about oat seed",
#     info="Skullcap is a is a restorative nervine thats restores the nervous system and can reduce pain caused by neuraligia. It is only mildy sedating, which makes it suitable to take any time of day.",
# )    


# passionflower = Herb.objects.create(
#     common_name="Passionflower",
#     botanical_name="Passiflora incarnata",
#     image="static/images/skullcap.png",
#     question="Passion flower",
# )    



# pau_darco = Herb.objects.create(
#     common_name="Pau d'arco",
#     botanical_name="Tabebuia impettiginosa",
#     image="static/images/skullcap.png",
#     question="Have you been suffering from nervous exhaustion do to mental overload, nervous breakdowns, depression and/or nerve pain?",
#     info="Skullcap is a is a restorative nervine thats restores the nervous system and can reduce pain caused by neuraligia. It is only mildy sedating, which makes it suitable to take any time of day.",
# )    


# valerian = Herb.objects.create(
#     common_name="Valerian",
#     botanical_name="Dionaea muscipula",
#     image="static/images/skullcap.png",
#     question="Have you been suffering from nervous exhaustion do to mental overload, nervous breakdowns, depression and/or nerve pain?",
#     info="Skullcap is a is a restorative nervine thats restores the nervous system and can reduce pain caused by neuraligia. It is only mildy sedating, which makes it suitable to take any time of day.",
# )    


# meadowseet = Herb.objects.create(
#     common_name="Meadowsweet",
#     botanical_name="Filipendula ulmaria",
#     image="static/images/skullcap.png",
#     question="Have you been suffering from nervous exhaustion do to mental overload, nervous breakdowns, depression and/or nerve pain?",
#     info="Skullcap is a is a restorative nervine thats restores the nervous system and can reduce pain caused by neuraligia. It is only mildy sedating, which makes it suitable to take any time of day.",
# )    


# burdock = Herb.objects.create(
#     common_name="Burdock Root",
#     botanical_name="Arcticum lappa",
#     image="static/images/skullcap.png",
#     question="Have you been suffering from nervous exhaustion do to mental overload, nervous breakdowns, depression and/or nerve pain?",
#     info="Skullcap is a is a restorative nervine thats restores the nervous system and can reduce pain caused by neuraligia. It is only mildy sedating, which makes it suitable to take any time of day.",
# )    



# astragalus = Herb.objects.create(
#     common_name="Astragalus",
#     botanical_name="Astagalus membranaceus",
#     image="static/images/skullcap.png",
#     question="Have you been suffering from nervous exhaustion do to mental overload, nervous breakdowns, depression and/or nerve pain?",
#     info="Skullcap is a is a restorative nervine thats restores the nervous system and can reduce pain caused by neuraligia. It is only mildy sedating, which makes it suitable to take any time of day.",
# )    



# ashwagandha = Herb.objects.create(
#     common_name="Ashwagandha",
#     botanical_name="Withania somnifera",
#     image="static/images/skullcap.png",
#     question="Have you been suffering from nervous exhaustion do to mental overload, nervous breakdowns, depression and/or nerve pain?",
#     info="Skullcap is a is a restorative nervine thats restores the nervous system and can reduce pain caused by neuraligia. It is only mildy sedating, which makes it suitable to take any time of day.",
# )    



    #Do I need to add the 'question' to the objects create?
    #Makes more sense to be in template because it is unchanging.

    ### CREATE
    # Create a single Herb object and save in DB


    # File "/Users/hello/Desktop/herb_quiz/apps/core/models.py", line 17, in Herb
    # herb = Herb.objects.create(
    # NameError: name 'Herb' is not defined

    # herb = Herb.objects.create(
    #     common_name="Skullcap",
    #     botanical_name="Scutellaria lateriflora",
    #     image="static/images/skullcap.png",
    #     question="Have you been suffering from nervous exhaustion do to mental overload, nervous breakdowns, depression and/or nerve pain?",
    #     info="Skullcap is a is a restorative nervine thats restores the nervous system and can reduce pain caused by neuraligia. It is only mildy sedating, which makes it suitable to take any time of day.",
    # )



# views.py


