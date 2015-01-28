import random

# These accents were made possible with huge thanks to Malcolm Brown - @DragonXVI on Twitter
# Owes a debt to Malcolm's #PROCJAM game, The Inquisitor - http://itch.io/jam/procjam/rate/14026
def accent_stutter(input):

	stutter_chance = 0.35

	words = input.split(" ");
	i = 0;
	while i < len(words):
		if random.random() > stutter_chance:
			words[i] = words[i][0]+"-"+words[i]
		i = i+1
	return " ".join(words)

def accent_drunk(input):

	hiccup_chance = 0.5

	index = 0;
	while index < len(input):
		if(input[index] == 's'):
			input = input[0:index+1] + "h" + input[index+1:];
			index = index+1;
		if(random.random() > hiccup_chance and (input[index] == '!' or input[index] == '?' or input[index] == '.')):
			input = input[0:index+1] + " -hic-" + input[index+1:];
			index = index+6;
		index = index+1;

	return input

def test_accents():
	the_string = "You're lying! You're a spy!";
	print accent_stutter(the_string)
	print accent_drunk(the_string)

# Little tics/tells to provide flavour only
def say_tic():
	tics = [
		"*hands shake slightly*",
		"*smiles very broadly*",
		"*flushes pink briefly*",
		"*fidgets slightly in chair*",
		"*"+random.choice(["right", "left"])+" eye twitches slightly*",
		"*clears throat*",
		"*opens mouth to speak, then closes again*",
		"*glances "+random.choice(["right", "left"])+"*",
		"*bites nail on "+random.choice(["index finger", "ring finger", "pinky finger", "thumb", "middle finger"])+"*",
		"*scratches forehead*",
		"*twirls "+random.choice(["pen", "toothpick", "card", "matchstick"])+" in hand*",
	];
	return random.choice(tics);

def test_tics():
	print say_tic();
	print say_tic();
	print say_tic();
	print say_tic();
	print say_tic();

# Names
# TODO: Add in list of strings which it makes sure it doesn't choose from
def generate_name_secretservice():
	#source - http://www.2600.com/secret/more/codes.html
	names = [
		 "Calico", "Cameo", "Cannonball", "Cavalier", "Cedar",
		 "Centurion", "Chessman", "Coppertone", "Dancer", "Dasher",
		 "Diamond", "Digger", "Duchess", "Dynamo", "Evergreen",
		 "Foxcraft", "Hercules", "Hotshot", "Kittyhawk", "Lancer",
		 "Miracle", "Napoleon", "Pinafore", "Radiant", "Rainbow",
		 "Rawhide", "Redfern", "Reliant", "Rosebud", "Scarlet",
		 "Searchlight", "Snapshot", "Snowbank", "Snowstorm",
		 "Sundance", "Swordfish", "Thunder", "Tranquility", 
		 "Trapline", "Unicorn"
	];
	return random.choice(names);

def generate_name_history():
	#source - curated from http://www.biographyonline.net/people/famous/revolutionaries.html
	names = [
		"Spartacus", "Fawkes", "Jeanne", "Cromwell", "Robespierre", "Washington", "Garibaldi",
		"Lenin", "Trotsky", "Castro", "Guevara", 
	];
	return random.choice(names);

def generate_name_jobnicks():
	#source - curated from https://github.com/dariusk/corpora/blob/master/data/humans/occupations.json
	names = ['accountant', 'actor', 'actuary', 'adjudicator', 'agent', 'anesthesiologist', 'animator', 'anthropologist', 'arbitrator', 'archeologist', 'architect', 'archivist', 'artist', 'assembler', 'astronomer', 'athlete', 'attendant', 'audiologist', 'auditor', 'author', 'bailiff', 'baker', 'barback', 'barber', 'bartender', 'bellhop', 'biochemist', 'biophysicist', 'blaster', 'blockmason', 'boilermaker', 'bookkeeper', 'brazer', 'brickmason', 'butcher', 'buyer', 'cabinetmaker', 'carpenter', 'cartographer', 'cashier', 'caster', 'chauffeur', 'checker', 'chef', 'chemist', 'chiropractor', 'choreographer', 'cleaner', 'composer', 'concierge', 'conciliator', 'conservator', 'cook', 'correspondent', 'cosmetologist', 'counselor', 'courier', 'curator', 'cutter', 'dancer', 'demonstrator', 'dentist', 'designer', 'detective', 'dietitian', 'director', 'dishwasher', 'dispatcher', 'drafter', 'dressmaker', 'economist', 'editor', 'electrician', 'embalmer', 'engineer', 'engraver', 'epidemiologist', 'escort', 'etcher', 'fabricator', 'faller', 'farmer', 'farmworker', 'firefighter', 'fisher', 'forester', 'geographer', 'geoscientist', 'glazier', 'groundskeeper', 'gynecologist', 'hairdresser', 'hairstylist', 'historian', 'host', 'hostess', 'hostler', 'hunter', 'hydrologist', 'hydrologist', 'illustrator', 'inspector', 'instructor', 'internist', 'interpreter', 'interviewer', 'investigator', 'jailer', 'janitor', 'jeweler', 'judge', 'lawyer', 'legislator', 'librarian', 'lifeguard', 'locksmith', 'logistician', 'machinist', 'magistrate', 'maid', 'manicurist', 'mathematician', 'measurer', 'mediator', 'messenger', 'microbiologist', 'millwright', 'model', 'molder', 'mortician', 'musician', 'nutritionist', 'obstetrician', 'offbearer', 'optician', 'optometrist', 'orderly', 'orthodontist', 'orthotist', 'paperhanger', 'paralegal', 'paramedic', 'pediatrician', 'pedicurist', 'pharmacist', 'photogrammetrist', 'photographer', 'physician', 'pipefitter', 'pipelayer', 'plasterer', 'plumber', 'podiatrist', 'postmaster', 'priest', 'producer', 'proofreader', 'prosthetist', 'prosthodontist', 'psychiatrist', 'psychologist', 'rancher', 'receptionist', 'referee', 'reporter', 'rigger', 'roofer', 'roustabout', 'sailor', 'sampler', 'scaler', 'sculptor', 'secretary', 'shampooer', 'shaper', 'shipmate', 'singer', 'slaughterer', 'sociologist', 'solderer', 'sorter', 'statistician', 'steamfitter', 'stonemason', 'surgeon', 'surveyor', 'tailor', 'taper', 'teacher', 'telemarketer', 'teller', 'tester', 'therapist', 'translator', 'trapper', 'trimmer', 'tuner', 'typist', 'umpire', 'undertaker', 'upholsterer', 'usher', 'veterinarian', 'waiter', 'waitress', 'weigher', 'welder', 'woodworker', 'writer', 'yardmaster', 'zoologist'];	
	choice = random.choice(names);
	return "The "+choice[:1].upper() + choice[1:];

def generate_name_animals():
	#source - curated from https://github.com/dariusk/corpora/blob/master/data/animals/common.json
	names = ["aardvark","alligator", "alpaca", "antelope", "ape", "armadillo", "baboon", "badger", "bat", "bear", "beaver", "bison", "boar", "buffalo", "bull", "camel", "canary", "capybara", "cat", "chameleon", "cheetah", "chimpanzee", "chinchilla", "chipmunk", "cougar", "cow", "coyote", "crocodile", "crow", "deer", "dingo", "dog", "donkey", "dromedary", "elephant", "elk", "ewe", "ferret", "finch", "fish", "fox", "frog", "gazelle", "giraffe", "gnu", "goat", "gopher", "gorilla", "grizzly", "hog", "guinea Pig", "hamster", "hedgehog", "hippopotamus", "hog", "horse", "hyena", "ibex", "iguana", "impala", "jackal", "jaguar", "kangaroo", "koala", "lamb", "lemur", "leopard", "lion", "lizard", "llama", "lynx", "mandrill", "marmoset", "mink", "mole", "mongoose", "monkey", "moose", "mountain Goat", "mouse", "mule", "muskrat", "mustang", "mynah Bird", "newt", "ocelot", "opossum", "orangutan", "oryx", "otter", "ox", "panda", "panther", "parakeet", "parrot", "pig", "platypus", "polar Bear", "porcupine", "porpoise", "prairie Dog", "puma", "rabbit", "raccoon", "ram", "rat", "reindeer", "reptile", "rhinoceros", "salamander", "seal", "sheep", "shrew", "skunk", "sloth", "snake", "squirrel", "tapir", "tiger", "toad", "turtle", "walrus", "warthog", "weasel", "whale", "wildcat", "wolf", "wolverine", "wombat", "woodchuck", "yak", "zebra"];	
	choice = random.choice(names);

	if(random.random() < 0.2):
		return "The "+random.choice(["White", "Red", "Black", "Blue", "Green", "Silver", "Golden"])+" "+choice[:1].upper() + choice[1:];
	return "The "+choice[:1].upper() + choice[1:];

def test_nicknames():
	print(generate_name_secretservice());
	print(generate_name_history());
	print(generate_name_jobnicks());
	print(generate_name_animals());

#test_nicknames()
