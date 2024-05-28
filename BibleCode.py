import random

# A list of Bible quotations
bible_quotations = [
    "For I know the plans I have for you, declares the Lord, plans for welfare and not for evil, to give you a future and a hope. - Jeremiah 29:11",
    "The Lord is my shepherd; I shall not want. - Psalm 23:1",
    "I can do all things through him who strengthens me. - Philippians 4:13",
    "And we know that in all things God works for the good of those who love him, who have been called according to his purpose. - Romans 8:28",
    "Trust in the Lord with all your heart, and do not lean on your own understanding. - Proverbs 3:5",
    "The righteous cry out, and the Lord hears them; he delivers them from all their troubles. - Psalm 34:17",
    "Be strong and courageous. Do not be afraid; do not be discouraged, for the Lord your God will be with you wherever you go. - Joshua 1:9",
    "But the fruit of the Spirit is love, joy, peace, forbearance, kindness, goodness, faithfulness. - Galatians 5:22",
    "Cast your cares on the Lord and he will sustain you; he will never let the righteous be shaken. - Psalm 55:22",
    "I have been crucified with Christ and I no longer live, but Christ lives in me. The life I now live in the body, I live by faith in the Son of God, who loved me and gave himself for me. - Galatians 2:20",
    # Add more quotations here...
]

def get_random_quotations(num_quotations=1):
    # Select random quotations from the list
    random_quotations = random.sample(bible_quotations, num_quotations)
    return random_quotations

def display_quotations(quotations):
    print("Random Bible Quotations:")
    for idx, quote in enumerate(quotations, start=1):
        print(f"{idx}. {quote}")
        print()

# Get and display multiple random Bible quotations
num_quotations_to_generate = 5  # Change this number to generate more or fewer quotations
random_quotations = get_random_quotations(num_quotations_to_generate)
display_quotations(random_quotations)
