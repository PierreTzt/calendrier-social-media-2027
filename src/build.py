# -*- coding: utf-8 -*-
"""Génère index.html (le générateur en ligne) et build/calendrier-social-media-2027.html (version imprimable)."""
import calendar, datetime as dt, html, re
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent

YEAR = 2027
MONTHS = ["JANVIER", "FÉVRIER", "MARS", "AVRIL", "MAI", "JUIN", "JUILLET",
          "AOÛT", "SEPTEMBRE", "OCTOBRE", "NOVEMBRE", "DÉCEMBRE"]
DAYS = ["LUNDI", "MARDI", "MERCREDI", "JEUDI", "VENDREDI", "SAMEDI", "DIMANCHE"]

def nth(month, weekday, n):
    """n-ième jour de semaine (0=lundi) du mois ; n=-1 pour le dernier."""
    days = [d for d in calendar.Calendar().itermonthdates(YEAR, month)
            if d.month == month and d.weekday() == weekday]
    return days[n].day

MON, TUE, WED, THU, FRI, SAT, SUN = range(7)

# (mois, jour) -> (liste d'événements, emoji facultatif)
# « * » = date à confirmer ; « (…) » est mis en italique automatiquement.
E = {}
def ev(m, d, *items, emoji=None):
    E.setdefault((m, d), [[], None])
    E[(m, d)][0].extend(items)
    if emoji:
        E[(m, d)][1] = emoji

# ---------------- JANVIER ----------------
ev(1, 1, "Jour de l'an (férié)", "Journée mondiale de la Paix", "Dry January (mois sans alcool)", emoji="🎉")
ev(1, 2, "Journée mondiale de la science-fiction")
ev(1, 3, "Galette des Rois (Épiphanie fêtée)", emoji="👑")
ev(1, 4, "Rentrée scolaire (toutes zones)", "Journée mondiale du braille")
ev(1, 6, "Épiphanie", "Début des Soldes d'hiver (jusqu'au 02/02)", "CES Las Vegas*")
ev(1, 8, "Journée internationale du bain moussant")
ev(1, 10, "Journée mondiale de Tintin")
ev(1, 11, "Journée mondiale du « merci »")
ev(1, 12, "Kiss a Ginger Day")
ev(1, 13, "Journée nationale de l'hypersensibilité", "Mondial de handball masculin en Allemagne (jusqu'au 31/01)")
ev(1, 14, "Journée mondiale de la logique")
ev(1, 16, "Journée internationale de la nourriture pimentée/épicée", emoji="🌶️")
ev(1, 17, "Journée internationale de la cuisine italienne")
ev(1, nth(1, MON, 2), "Blue Monday")
ev(1, 19, "Journée internationale du pop-corn", emoji="🍿")
ev(1, 21, "Journée internationale des câlins")
ev(1, 22, "Journée franco-allemande")
ev(1, 23, "Journée mondiale de l'écriture manuscrite")
ev(1, 24, "Journée internationale de l'éducation", "Journée mondiale de la culture africaine et afro-descendante")
ev(1, nth(1, MON, 3), "Journée des Community Managers", emoji="🥳")
ev(1, 27, "Journée internationale dédiée à la mémoire des victimes de l'Holocauste")
ev(1, 28, "Journée européenne de la protection des données")
ev(1, 29, "Journée du puzzle", emoji="🧩")
ev(1, nth(1, SUN, -1), "Journée mondiale des lépreux")

# ---------------- FÉVRIER ----------------
ev(2, 2, "Chandeleur", "Journée mondiale des zones humides", "Jour de la marmotte", emoji="🥞")
ev(2, 3, "Journée internationale sans paille")
ev(2, 4, "Journée mondiale contre le cancer", "Journée internationale de la fraternité humaine")
ev(2, 5, "Carnaval de Rio (jusqu'au 09/02)")
ev(2, 6, "Nouvel An chinois (année de la Chèvre)", "Début vacances scolaires Zone C (jusqu'au 22/02)", "Journée mondiale sans téléphone portable", emoji="🧧")
ev(2, 7, "Grammy Awards 2027")
ev(2, nth(2, MON, 1), "Début du Ramadan* (jusqu'au 09/03)", "Journée internationale de l'épilepsie")
ev(2, nth(2, TUE, 1), "Mardi gras", "Safer Internet Day")
ev(2, 10, "Mercredi des Cendres", "Journée mondiale des légumineuses")
ev(2, 11, "Journée internationale des femmes et des filles de science", "Journée européenne du 112")
ev(2, 13, "Début vacances scolaires Zone A (jusqu'au 01/03)", "Journée mondiale de la radio", emoji="📻")
ev(2, 14, "Saint-Valentin", "Super Bowl LXI (Los Angeles)", emoji="❤️")
ev(2, 15, "Journée internationale du cancer de l'enfant")
ev(2, 17, "Journée des actes de gentillesse")
ev(2, 20, "Début vacances scolaires Zone B (jusqu'au 08/03)", "Journée mondiale de la justice sociale")
ev(2, 21, "Journée internationale de la langue maternelle")
ev(2, 22, "Journée mondiale du scoutisme")
ev(2, 26, "Journée internationale du conte de fées")
ev(2, 27, "Journée internationale de l'ours polaire", "Journée mondiale des ONG", emoji="🐻‍❄️")
ev(2, 28, "Journée mondiale des maladies rares", "Journée mondiale sans Facebook")

# ---------------- MARS ----------------
ev(3, 1, "Journée mondiale du compliment", "Journée zéro discrimination")
ev(3, 3, "Journée mondiale de la vie sauvage")
ev(3, 4, "Journée mondiale de lutte contre l'obésité")
ev(3, nth(3, SUN, 0), "Fête des Grands-Mères", emoji="👵")
ev(3, 8, "Journée internationale des droits des femmes", emoji="💜")
ev(3, 10, "Aïd el-Fitr*", "Journée internationale des femmes juges")
ev(3, 11, "Journée mondiale de la plomberie")
ev(3, 12, "Journée mondiale contre la censure sur Internet")
ev(3, 14, "Cérémonie des Oscars", "Journée de Pi (π)", emoji="🏆")
ev(3, 15, "Journée mondiale des droits des consommateurs")
ev(3, 17, "Saint-Patrick", emoji="☘️")
ev(3, 18, "Journée mondiale du recyclage")
ev(3, 19, "Journée mondiale du sommeil", emoji="😴")
ev(3, 20, "Printemps", "Journée internationale du bonheur", "Journée mondiale sans viande", "Digital Cleanup Day", emoji="🌸")
ev(3, 21, "Dimanche des Rameaux", "Journée mondiale de la trisomie 21", "Journée internationale des forêts")
ev(3, 22, "Journée mondiale de l'eau")
ev(3, 23, "Journée météorologique mondiale")
ev(3, 24, "Journée mondiale de lutte contre la tuberculose", "Journée européenne de la glace artisanale")
ev(3, 25, "Journée de commémoration des victimes de l'esclavage", "Journée de la procrastination")
ev(3, 26, "Journée violette (« Purple Day »)")
ev(3, nth(3, SAT, -1), "Earth Hour", "Journée mondiale du théâtre", emoji="🌍")
ev(3, 28, "Pâques", "Passage à l'heure d'été", emoji="🐣")
ev(3, 29, "Lundi de Pâques (férié)", "Journée du piano")
ev(3, 30, "Journée mondiale de la bipolarité")
ev(3, 31, "Journée mondiale de la sauvegarde informatique", "Journée internationale de la visibilité trans")

# ---------------- AVRIL ----------------
ev(4, 1, "Poisson d'avril", emoji="🐟")
ev(4, 2, "Journée mondiale de sensibilisation à l'autisme")
ev(4, nth(4, SAT, 0), "Début vacances scolaires Zone C (jusqu'au 19/04)", "Journée mondiale des batailles d'oreillers")
ev(4, 5, "Journée internationale de la conscience")
ev(4, 6, "Journée internationale du sport au service du développement et de la paix")
ev(4, 7, "Journée mondiale de la santé")
ev(4, 9, "Journée mondiale de la licorne", emoji="🦄")
ev(4, 10, "Début vacances scolaires Zone A (jusqu'au 26/04)")
ev(4, 11, "Journée mondiale de la maladie de Parkinson", "Marathon de Paris*")
ev(4, 12, "Journée internationale du vol spatial habité", emoji="🚀")
ev(4, nth(4, THU, 2), "Journée mondiale de l'art", "Fête des secrétaires", emoji="🎨")
ev(4, 17, "Début vacances scolaires Zone B (jusqu'au 03/05)")
ev(4, 18, "Élection présidentielle : 1er tour", "Journée du patrimoine mondial", emoji="🗳️")
ev(4, 20, "Journée de la langue chinoise")
ev(4, 21, "Journée mondiale de la créativité et de l'innovation", emoji="💡")
ev(4, 22, "Journée internationale de la Terre nourricière")
ev(4, 23, "Journée mondiale du livre et du droit d'auteur", "Journée de la langue anglaise et espagnole", emoji="📚")
ev(4, 25, "Journée mondiale de lutte contre le paludisme", "Journée mondiale des manchots")
ev(4, 26, "Journée mondiale de la propriété intellectuelle")
ev(4, 28, "Journée mondiale de la sécurité et de la santé au travail")
ev(4, 29, "Journée internationale de la danse", emoji="💃")
ev(4, 30, "Journée internationale du jazz", emoji="🎷")

# ---------------- MAI ----------------
ev(5, 1, "Fête du Travail (férié)", emoji="🌼")
ev(5, 2, "Élection présidentielle : 2nd tour", "Journée mondiale du rire", emoji="🗳️")
ev(5, 3, "Journée mondiale de la liberté de la presse")
ev(5, 4, "Star Wars Day", "Journée internationale des pompiers")
ev(5, 5, "Journée internationale des sages-femmes", "Journée mondiale de la langue portugaise")
ev(5, 6, "Ascension (férié)", "Journée mondiale du mot de passe", emoji="🔐")
ev(5, nth(5, FRI, 0), "Journée mondiale sans pantalon")
ev(5, 8, "Victoire du 8 mai 1945 (férié)", "Journée mondiale de la Croix-Rouge", "Journée mondiale du commerce équitable et des oiseaux migrateurs")
ev(5, 9, "Journée de l'Europe", emoji="🇪🇺")
ev(5, 10, "Journée des mémoires de la traite, de l'esclavage et de leurs abolitions")
ev(5, 11, "Festival de Cannes, 80e édition (jusqu'au 22/05)", "Eurovision : 1re demi-finale", emoji="🎬")
ev(5, 12, "Journée internationale des infirmières")
ev(5, 13, "Eurovision : 2e demi-finale")
ev(5, 15, "Finale de l'Eurovision (Burgas)", "Nuit européenne des musées*", "Journée internationale des familles", emoji="🎤")
ev(5, 16, "Pentecôte", "Journée internationale de la lumière")
ev(5, 17, "Lundi de Pentecôte (férié)", "Journée mondiale des télécommunications", "Journée contre l'homophobie et la transphobie", emoji="🏳️‍🌈")
ev(5, 18, "Journée internationale des musées")
ev(5, 20, "Journée mondiale des abeilles", emoji="🐝")
ev(5, 21, "Journée internationale du thé", emoji="🍵")
ev(5, 22, "Journée internationale de la biodiversité")
ev(5, 23, "Roland-Garros* (jusqu'au 06/06)", "Journée mondiale de la tortue", emoji="🎾")
ev(5, 25, "Journée de l'Afrique", "Geek Pride Day")
ev(5, 27, "Journée nationale de la Résistance")
ev(5, nth(5, FRI, -1), "Fête des voisins", "Journée mondiale de l'hygiène menstruelle")
ev(5, 29, "Journée internationale des Casques bleus")
ev(5, 30, "Fête des Mères", "Journée mondiale de la sclérose en plaques", emoji="💐")
ev(5, 31, "Journée mondiale sans tabac")

# ---------------- JUIN ----------------
ev(6, 1, "Journée mondiale des parents", "Journée mondiale du lait")
ev(6, nth(6, WED, 0), "Journée mondiale du running", emoji="🏃")
ev(6, 3, "Journée mondiale de la bicyclette", emoji="🚲")
ev(6, nth(6, FRI, 0), "National Donut Day", emoji="🍩")
ev(6, 5, "Finale de la Ligue des champions (Madrid)", "Journée mondiale de l'environnement", emoji="⚽")
ev(6, 8, "Journée mondiale de l'océan", emoji="🌊")
ev(6, 10, "Fête nationale du Portugal")
ev(6, 12, "Journée mondiale contre le travail des enfants")
ev(6, 13, "Journée internationale de sensibilisation à l'albinisme")
ev(6, 14, "Journée mondiale du donneur de sang")
ev(6, 17, "Hellfest (jusqu'au 20/06)", "Journée mondiale de lutte contre la désertification", emoji="🤘")
ev(6, 18, "International Sushi Day", "Journée de la gastronomie durable", emoji="🍣")
ev(6, nth(6, SAT, 2), "Journée internationale du surf", "Journée mondiale de lutte contre la drépanocytose", emoji="🏄")
ev(6, nth(6, SUN, 2), "Fête des Pères", "Journée mondiale des réfugiés", emoji="👔")
ev(6, 21, "Fête de la musique", "Été", "Journée internationale du yoga", emoji="🎸")
ev(6, 23, "Début des Soldes d'été (jusqu'au 20/07)", "Fête nationale du Luxembourg", "Journée de la fonction publique (ONU)", emoji="🛍️")
ev(6, 24, "Coupe du monde féminine de football au Brésil (jusqu'au 25/07)", "Fête nationale du Québec")
ev(6, 26, "Journée contre l'abus et le trafic de drogues", "Journée de soutien aux victimes de la torture")
ev(6, 27, "Journée des micro, petites et moyennes entreprises")
ev(6, 29, "Journée internationale des tropiques", "Journée de l'appareil photo")
ev(6, 30, "Journée mondiale des réseaux sociaux", "Journée internationale des astéroïdes", emoji="📱")

# ---------------- JUILLET ----------------
ev(7, 1, "Journée mondiale du reggae")
ev(7, 2, "Tour de France : Grand Départ d'Édimbourg (jusqu'au 25/07)", "Journée mondiale des OVNIS", emoji="🚴")
ev(7, 3, "Vacances d'été (toutes zones)", "Journée internationale sans sac plastique", emoji="🏖️")
ev(7, 6, "Journée internationale du baiser", emoji="💋")
ev(7, 11, "Journée mondiale de la population")
ev(7, 14, "Fête nationale (férié)", emoji="🎆")
ev(7, 15, "Festival des Vieilles Charrues à Carhaix (jusqu'au 18/07)", "Journée mondiale des compétences des jeunes")
ev(7, 16, "Journée mondiale des serpents")
ev(7, 17, "Journée mondiale des émojis (World Emoji Day)", emoji="😎")
ev(7, 20, "Journée internationale de la Lune", "Journée mondiale des échecs", emoji="🌙")
ev(7, 21, "Fête nationale belge")
ev(7, 23, "Journée mondiale des dauphins")
ev(7, 24, "Journée internationale des cousins et cousines")
ev(7, nth(7, SUN, 3), "Journée mondiale des grands-parents et des personnes âgées", "Journée mondiale de la prévention de la noyade")
ev(7, 28, "Journée mondiale contre l'hépatite")
ev(7, 29, "Journée internationale du tigre", emoji="🐯")
ev(7, 30, "Journée internationale de l'amitié", "Journée mondiale contre la traite des êtres humains", "SysAdmin Day", emoji="🤝")

# ---------------- AOÛT ----------------
ev(8, 1, "Fête nationale suisse", "Journée du World Wide Web")
ev(8, 2, "Éclipse totale de Soleil (partielle en France, vers 11 h)", emoji="🌒")
ev(8, 3, "Journée de la pastèque", emoji="🍉")
ev(8, nth(8, FRI, 0), "Journée internationale de la bière", emoji="🍺")
ev(8, 8, "Journée internationale du chat", emoji="🐱")
ev(8, 9, "Journée internationale des peuples autochtones")
ev(8, 10, "Journée mondiale du lion", emoji="🦁")
ev(8, 12, "Journée internationale de la jeunesse", "Journée mondiale de l'éléphant")
ev(8, 13, "Journée internationale des gauchers")
ev(8, 15, "Assomption (férié)")
ev(8, 17, "Journée internationale du chat noir")
ev(8, 19, "Journée mondiale de l'aide humanitaire, des orangs-outans et de la photographie", emoji="📸")
ev(8, 20, "Journée mondiale du moustique")
ev(8, 21, "Journée internationale du souvenir, en hommage aux victimes du terrorisme")
ev(8, 23, "Journée internationale du souvenir de la traite négrière et de son abolition")
ev(8, 26, "Journée mondiale du chien", emoji="🐶")
ev(8, 28, "Journée du nœud papillon")
ev(8, 30, "US Open de tennis* (jusqu'au 12/09)", "Journée internationale des victimes de disparition forcée")
ev(8, 31, "Journée mondiale du blog", emoji="✍️")

# ---------------- SEPTEMBRE ----------------
ev(9, 2, "Rentrée des classes", emoji="🎒")
ev(9, 4, "Journée mondiale de la santé sexuelle", "Journée mondiale de la barbe", "Grande Braderie de Lille* (jusqu'au 05/09)")
ev(9, 5, "Journée internationale de la charité")
ev(9, 7, "Journée internationale de l'air pur pour des ciels bleus")
ev(9, 8, "Journée internationale de l'alphabétisation", "Fête nationale d'Andorre")
ev(9, 9, "Journée mondiale de la peluche (Teddy Bear Day)", emoji="🧸")
ev(9, nth(9, SAT, 1), "Journée mondiale des premiers secours")
ev(9, 13, "Journée des programmeurs et développeurs", emoji="💻")
ev(9, 15, "Journée internationale de la démocratie", "Journée mondiale des lymphomes")
ev(9, 16, "Journée internationale de la protection de la couche d'ozone", "Semaine européenne de la mobilité (jusqu'au 22/09)")
ev(9, nth(9, SAT, 2), "Journées européennes du patrimoine (jusqu'au 19/09)", emoji="🏛️")
ev(9, 19, "Journée internationale du parler pirate", emoji="🏴‍☠️")
ev(9, 21, "Journée internationale de la paix", "Journée mondiale de la maladie d'Alzheimer", emoji="🕊️")
ev(9, 22, "Journée mondiale sans voiture")
ev(9, 23, "Automne", "Journée internationale des langues des signes", emoji="🍂")
ev(9, 25, "Journée mondiale du rêve")
ev(9, 26, "Journée mondiale de la contraception", "Journée internationale pour l'élimination totale des armes nucléaires")
ev(9, 27, "Journée mondiale du tourisme", emoji="✈️")
ev(9, 28, "Journée mondiale du droit à l'avortement", "Journée internationale de l'accès universel à l'information")
ev(9, 29, "Journée mondiale du cœur", "Journée de sensibilisation aux pertes et gaspillages de nourriture")
ev(9, 30, "Journée internationale du podcast", "Journée internationale de la traduction", emoji="🎙️")

# ---------------- OCTOBRE ----------------
ev(10, 1, "Début d'Octobre Rose (jusqu'au 31/10)", "Coupe du monde de rugby en Australie (jusqu'au 13/11)", "Journée du café, du sourire et du végétarisme", emoji="☕")
ev(10, 2, "Journée internationale de la non-violence")
ev(10, nth(10, SUN, 0), "Fête des Grands-Pères", "Jour de l'Unité allemande")
ev(10, nth(10, MON, 0), "Journée mondiale des animaux", "Journée mondiale de l'habitat et de l'architecture", emoji="🐾")
ev(10, 5, "Journée mondiale des enseignants")
ev(10, 7, "Journée mondiale du coton")
ev(10, nth(10, FRI, 1), "Journée mondiale de l'œuf", "Journée mondiale du poulpe", emoji="🐙")
ev(10, 9, "Journée mondiale de la poste")
ev(10, 10, "Journée mondiale de la santé mentale", "Journée nationale des Dys", emoji="💚")
ev(10, 12, "Fête nationale espagnole")
ev(10, nth(10, THU, 1), "Journée mondiale de la vue")
ev(10, 15, "Journée mondiale de sensibilisation au deuil périnatal")
ev(10, 16, "Journée mondiale de l'alimentation", "Journée mondiale du pain", emoji="🥖")
ev(10, nth(10, SUN, 2), "Fête des parrains et marraines")
ev(10, 18, "Journée mondiale de la ménopause")
ev(10, 19, "Journée mondiale contre le cancer du sein", emoji="🎗️")
ev(10, 20, "Journée internationale des cuisiniers")
ev(10, nth(10, FRI, 3), "Journée mondiale du champagne", emoji="🥂")
ev(10, 23, "Vacances de la Toussaint (jusqu'au 08/11)")
ev(10, 24, "Journée des Nations unies")
ev(10, 25, "Journée mondiale des pâtes", emoji="🍝")
ev(10, 27, "Journée mondiale du patrimoine audiovisuel")
ev(10, 28, "Journée internationale de la langue et de la culture créoles")
ev(10, 31, "Halloween", "Passage à l'heure d'hiver", "Journée mondiale des villes", emoji="🎃")

# ---------------- NOVEMBRE ----------------
ev(11, 1, "Toussaint (férié)", "Journée mondiale du véganisme", "Movember et Mois sans tabac", emoji="🥸")
ev(11, 3, "Journée de la gentillesse")
ev(11, nth(11, THU, 0), "Journée nationale de lutte contre le harcèlement scolaire")
ev(11, nth(11, FRI, 0), "Journée mondiale sans papier (World Paper Free Day)")
ev(11, 8, "Journée internationale de la radiologie")
ev(11, 10, "Journée mondiale de la science au service de la paix")
ev(11, 11, "Armistice 1918 (férié)", "Singles' Day (fête des célibataires)")
ev(11, 13, "Finale de la Coupe du monde de rugby", emoji="🏉")
ev(11, 14, "Journée mondiale du diabète")
ev(11, 16, "Journée internationale de la tolérance")
ev(11, 17, "Journée mondiale de la prématurité")
ev(11, nth(11, THU, 2), "Journée mondiale de la philosophie", "Journée pour la protection des enfants contre l'exploitation et les abus sexuels")
ev(11, 19, "Journée mondiale des toilettes", "Fête nationale monégasque")
ev(11, 20, "Journée internationale des droits de l'enfant")
ev(11, 21, "Journée mondiale de la télévision", emoji="📺")
ev(11, nth(11, THU, 3), "Thanksgiving", "Journée internationale pour l'élimination de la violence à l'égard des femmes", emoji="🦃")
ev(11, 26, "Black Friday", emoji="🛍️")
ev(11, 27, "Journée mondiale sans achat")
ev(11, 29, "Cyber Monday")
ev(11, 30, "Giving Tuesday", "Saint-Andrew's Day (fête nationale écossaise)", "Mondial de handball féminin en Hongrie (jusqu'au 19/12)")

# ---------------- DÉCEMBRE ----------------
ev(12, 1, "Début du calendrier de l'Avent", "Journée mondiale de lutte contre le sida", emoji="🎁")
ev(12, 2, "Journée internationale pour l'abolition de l'esclavage")
ev(12, 3, "Journée internationale des personnes handicapées")
ev(12, 4, "Journée internationale des banques")
ev(12, 5, "Journée mondiale du bénévolat et des sols")
ev(12, 6, "Saint-Nicolas")
ev(12, 7, "Journée de l'aviation civile internationale")
ev(12, 9, "Journée nationale de la laïcité")
ev(12, 10, "Journée des droits de l'Homme", "Journée internationale des droits des animaux")
ev(12, 11, "Journée internationale de la montagne", emoji="🏔️")
ev(12, 13, "Journée de la raclette", emoji="🧀")
ev(12, 15, "Journée de l'espéranto")
ev(12, nth(12, FRI, 2), "Journée du pull de Noël*", emoji="🎄")
ev(12, 18, "Vacances de Noël (jusqu'au 03/01/2028)", "Journée mondiale de la langue arabe")
ev(12, 20, "Journée internationale de la solidarité humaine")
ev(12, 22, "Hiver", emoji="❄️")
ev(12, 24, "Réveillon de Noël")
ev(12, 25, "Noël (férié)", emoji="🎅")
ev(12, 27, "Journée internationale de la préparation aux épidémies")
ev(12, 31, "Saint-Sylvestre", emoji="🥳")

# Sanity checks (dates calculées = attendues)
assert nth(1, MON, 3) == 25 and nth(3, SUN, 0) == 7 and nth(6, SUN, 2) == 20
assert nth(11, THU, 3) == 25 and nth(5, FRI, -1) == 28 and nth(10, SUN, 0) == 3
for (m, d) in E:
    dt.date(YEAR, m, d)

TIPS = [
    ("Faites le bilan de 2026 avant de planifier 2027.",
     " Analysez vos 10 meilleures publications de l'année : format, sujet, jour et heure de publication. Ce sont vos meilleurs indices pour construire votre ligne éditoriale."),
    ("Constituez une réserve de contenus « evergreen ».",
     " Astuces, FAQ, coulisses… Des posts intemporels, prêts à dégainer les semaines où l'actu vous manque ou le temps vous fait défaut."),
    ("Un contenu, plusieurs formats !",
     " Un article de blog peut devenir un carrousel, une vidéo courte, un post LinkedIn et une newsletter. Recyclez vos meilleures idées plutôt que de repartir de zéro."),
    ("Période électorale : préparez votre ligne de conduite.",
     " Avec la présidentielle, le climat en ligne sera tendu. Définissez à l'avance les sujets à éviter, vos règles de modération et vos réponses types."),
    ("Soignez vos 3 premières secondes.",
     " Sur les vidéos courtes, tout se joue dès l'accroche : un texte à l'écran, une question, un mouvement. Testez plusieurs « hooks » pour un même contenu."),
    ("Anticipez l'été dès maintenant.",
     " Programmez vos publications de juillet-août avant de partir et organisez un relais pour la modération. Votre communauté, elle, ne part pas en vacances !"),
    ("Donnez la parole à votre communauté.",
     " Avis clients, reposts, contenus créés par vos abonnés (UGC) : c'est la preuve sociale la plus crédible. Demandez toujours l'autorisation et créditez les auteurs."),
    ("Profitez du calme estival pour faire un audit.",
     " Bios, liens, photos de profil, stories à la une, posts épinglés : vérifiez que tout est à jour et cohérent sur l'ensemble de vos comptes."),
    ("Fixez des objectifs mesurables.",
     " Plutôt que « gagner en visibilité », visez « +15 % d'engagement sur LinkedIn d'ici décembre ». Un objectif clair rend chaque décision plus simple."),
    ("Préparez votre plan de gestion de crise.",
     " Qui répond ? En combien de temps ? Avec quel message ? Un bad buzz se gère beaucoup mieux quand le process est écrit à l'avance."),
    ("Black Friday, fêtes : planifiez tôt !",
     " Visuels, codes promo, calendrier de publication… Fin novembre et décembre sont les semaines les plus chargées : bloquez vos contenus clés dès maintenant."),
    ("Remerciez votre communauté.",
     " Un récap de l'année, un best-of, un merci sincère : les contenus de fin d'année créent de la proximité. Et ensuite… déconnectez ! 🎄"),
]




# ======================= DATES DÉCALÉES (préfixe « ~ ») =======================
FUNNY = [
    (1, 2, "Journée mondiale des introvertis"), (1, 3, "Festival du sommeil"),
    (1, 4, "Journée du spaghetti"), (1, 17, "Journée où l'on abandonne ses bonnes résolutions"),
    (1, 18, "Journée de Winnie l'Ourson"), (1, nth(1, MON, -1), "Journée du papier bulle"),
    (1, 28, "Journée du LEGO"), (1, 31, "Journée internationale du zèbre"),
    (2, 5, "Journée mondiale du Nutella"), (2, 9, "Journée de la pizza"),
    (2, 13, "Galentine's Day (la Saint-Valentin entre copines)"), (2, 20, "Journée « Aimez votre animal »"),
    (2, 22, "Journée du chat au Japon (« nyan nyan nyan »)"), (2, 27, "Journée Pokémon"),
    (3, 10, "MAR10 Day (journée de Mario)"), (3, 16, "Journée du panda"),
    (3, 25, "Journée internationale de la gaufre"), (3, 26, "Journée pour inventer sa propre journée"),
    (4, 11, "Journée des animaux de compagnie"), (4, 12, "Journée du croque-monsieur (Grilled Cheese Day)"),
    (4, 13, "Journée du Scrabble"), (4, 26, "Alien Day (LV-426)"), (4, 30, "Journée de l'honnêteté"),
    (5, 2, "Journée mondiale du thon"), (5, 14, "Journée de la danse du poulet"),
    (5, 25, "Towel Day (journée de la serviette)"),
    (6, 4, "Journée « Faites un câlin à votre chat »"), (6, 6, "Journée du yo-yo"),
    (6, 8, "Journée des meilleurs amis"), (6, 16, "Bloomsday"), (6, 19, "Anniversaire de Garfield"),
    (6, 28, "Journée de Tau (τ = 6,28)"),
    (7, 2, "Journée de l'oubli (I Forgot Day)"), (7, 7, "Journée mondiale du chocolat"),
    (7, 13, "Journée mondiale du rock"), (7, 22, "Journée de l'approximation de Pi (22/7)"),
    (7, 27, "Journée « Promenez vos plantes vertes »"),
    (8, 16, "Journée de la blague"), (8, 18, "Journée du mauvais poète"),
    (9, 6, "Journée « Lisez un livre »"), (9, 22, "Journée des Hobbits"),
    (10, 4, "Journée du roulé à la cannelle"), (10, 6, "Journée du Chapelier fou (10/6)"),
    (10, 21, "Journée « Retour vers le futur »"),
    (11, 21, "Journée mondiale du « Bonjour »"), (11, 23, "Journée de Fibonacci (1-1-2-3)"),
    (12, 4, "Journée du cookie"), (12, 8, "Fête des Lumières à Lyon*"), (12, 21, "Journée des mots croisés"),
    (12, 23, "Festivus (« la fête pour le reste d'entre nous »)"), (12, 26, "Boxing Day"),
    (12, 31, "Journée « Décidez-vous enfin »"),
]
for m, d, t in FUNNY:
    dt.date(YEAR, m, d)
    ev(m, d, "~" + t)

# Événements existants déjà décalés : on les marque aussi.
FUN_KEYS = ["Kiss a Ginger", "bain moussant", "Tintin", "pop-corn", "câlins", "puzzle", "marmotte",
            "conte de fées", "ours polaire", "Journée de Pi", "procrastination", "Poisson d'avril",
            "batailles d'oreillers", "licorne", "manchots", "sans pantalon", "Star Wars", "Geek Pride",
            "Donut", "Sushi", "OVNIS", "baiser", "émojis", "pastèque", "bière", "chat noir", "nœud papillon",
            "barbe", "peluche", "parler pirate", "rêve", "poulpe", "champagne", "pâtes", "Halloween",
            "raclette", "pull de Noël", "Singles' Day", "Galette", "nourriture pimentée", "Blue Monday"]
for key, (items, _) in E.items():
    for i, t in enumerate(items):
        if not t.startswith("~") and any(k in t for k in FUN_KEYS):
            items[i] = "~" + t

# Une idée de post par mois, tirée d'une date décalée
PERLES = [
    ((1, 17), "Journée où l'on abandonne ses bonnes résolutions",
     "Sondage en story : « Votre résolution a tenu combien de jours ? » 1 · 7 · 17 · Elle tient encore."),
    ((2, 22), "Journée du chat au Japon",
     "Demandez à votre communauté la photo de son chat en plein télétravail. Du contenu UGC sans effort."),
    ((3, 26), "Journée pour inventer sa propre journée",
     "Inventez la journée mondiale de votre marque et laissez vos abonnés voter pour son nom."),
    ((4, 13), "Journée du Scrabble",
     "Un mot de votre secteur posé sur un plateau : le premier qui calcule le bon score gagne."),
    ((5, 25), "Towel Day",
     "Montrez l'objet dont chaque membre de l'équipe ne se sépare jamais. Clin d'œil geek, 10 minutes de prépa."),
    ((6, 19), "Anniversaire de Garfield",
     "Lundi, lasagnes, sieste : le mème « nous, le lundi matin » avec vos propres visuels."),
    ((7, 27), "Journée « Promenez vos plantes vertes »",
     "Baladez la plante du bureau et filmez-la façon documentaire animalier. Absurde, donc partagé."),
    ((8, 18), "Journée du mauvais poète",
     "Concours du pire poème sur votre produit. Les pires en story, le « gagnant » en post."),
    ((9, 22), "Journée des Hobbits",
     "Célébrez le second petit-déjeuner : photo du plateau de l'équipe et sondage « 1 ou 2 petits-déj ? »."),
    ((10, 21), "Journée « Retour vers le futur »",
     "Carrousel avant/après : votre marque en 2015, aujourd'hui, et comment vous l'imaginez en 2045."),
    ((11, 21), "Journée mondiale du « Bonjour »",
     "Allez dire bonjour en commentaire à 10 comptes que vous suivez sans jamais interagir."),
    ((12, 23), "Festivus",
     "Version douce du « déballage des griefs » : vos abonnés listent les petits agacements de 2027, vous répondez avec humour."),
]
for (m, d), name, _ in PERLES:
    assert any(name.split("«")[0].strip(" «»") in t for t in E[(m, d)][0]), name

# ======================= RENDU (identité « riso ») =======================
MONTH_NAMES = ["Janvier", "Février", "Mars", "Avril", "Mai", "Juin", "Juillet",
               "Août", "Septembre", "Octobre", "Novembre", "Décembre"]
WD = ["lun", "mar", "mer", "jeu", "ven", "sam", "dim"]


def fr(t):
    t = t.replace("'", "’")
    for a, b in ((" ?", " ?"), (" !", " !"), (" :", " :"), (" ;", " ;"),
                 ("« ", "« "), (" »", " »")):
        t = t.replace(a, b)
    return t


def fmt(text):
    t = fr(html.escape(text.lstrip("~"), quote=False))
    t = re.sub(r"\(([^)]*)\)", r"<i>(\1)</i>", t)
    t = t.replace("*", '<sup class="ast">*</sup>')
    return t


def ov(text, cls=""):
    """Texte imprimé deux fois (bleu + rose fluo décalé), comme un tirage riso mal calé."""
    return f'<span class="ov {cls}"><span class="b">{text}</span><span class="p" aria-hidden="true">{text}</span></span>'


def is_ferie(m, d):
    return any("(férié)" in x for x in E.get((m, d), [[], None])[0])


def day_row(d):
    m = d.month
    items, _ = E.get((m, d.day), [[], None])
    cls = ["day"]
    if d.weekday() >= 5:
        cls.append("we")
    num_cls = "num fer" if is_ferie(m, d.day) else "num"
    evs = "".join(f'<p class="{"fun" if x.startswith("~") else ""}">{fmt(x)}</p>' for x in items)
    return (f'<div class="{" ".join(cls)}"><div class="dn"><span class="{num_cls}">{d.day:02d}</span>'
            f'<span class="wd">{WD[d.weekday()]}</span></div><div class="evs">{evs}</div></div>')


def month_page(m):
    ndays = calendar.monthrange(YEAR, m)[1]
    days = [dt.date(YEAR, m, i) for i in range(1, ndays + 1)]
    per = -(-ndays // 3)
    cols = [days[:per], days[per:2 * per], days[2 * per:]]
    col_html = []
    for c in cols:
        parts = []
        for i, d in enumerate(c):
            if d.weekday() == 0 or i == 0:
                parts.append(f'<div class="wk">sem. {d.isocalendar()[1]:02d}</div>')
            parts.append(day_row(d))
        col_html.append(f'<div class="col">{"".join(parts)}</div>')
    ouvres = sum(1 for d in days if d.weekday() < 5 and not is_ferie(m, d.day))
    nb_fun = sum(1 for (mm, _), (its, _) in E.items() if mm == m for x in its if x.startswith("~"))
    has_ast = any("*" in x for (mm, _), (its, _) in E.items() if mm == m for x in its)
    (pm, pd), pname, pidea = PERLES[m - 1]
    tip_b, tip_r = TIPS[m - 1]
    name = MONTH_NAMES[m - 1]
    fs = min(40, 178 / (len(name) * 0.74))
    ast = '<span><sup class="ast">*</sup> date à confirmer</span>' if has_ast else ""
    return f"""
<section class="page month">
  <div class="vt" style="font-size:{fs:.1f}mm">{ov(name)}</div>
  <div class="info">
    <div class="meta">{YEAR}<br>{ndays} jours · {ouvres} ouvrés<br>{nb_fun} dates décalées</div>
    <div class="blk">
      <div class="lbl">Le conseil</div>
      <p class="tip"><b>{fr(html.escape(tip_b))}</b>{fr(html.escape(tip_r))}</p>
    </div>
    <div class="perle">
      <div class="lbl">Idée de post</div>
      <div class="pdate">{ov(f"{pd:02d}.{pm:02d}")}</div>
      <div class="pname">{fr(html.escape(pname))}</div>
      <p>{fr(html.escape(pidea))}</p>
    </div>
    <div class="legend">
      <span><i class="dot"></i> date décalée</span>
      <span><i class="fr">01</i> férié</span>
      {ast}
    </div>
  </div>
  <div class="cols">{''.join(col_html)}</div>
</section>"""


def count_all():
    tot = sum(len(its) for its, _ in E.values())
    fun = sum(1 for its, _ in E.values() for x in its if x.startswith("~"))
    return tot, fun


def cover():
    tot, fun = count_all()
    return f"""
<section class="page cover">
  <div class="cyear">{ov("20", "l1")}{ov("27", "l2")}</div>
  <div class="cright">
    <div class="lbl">Calendrier social media</div>
    <h1>{tot} dates pour publier en {YEAR}.</h1>
    <p>Des journées officielles, des événements à ne pas rater, et {fun} dates franchement décalées pour les jours où l'inspiration fait grève.</p>
    <ul>
      <li>12 mois, jour par jour</li>
      <li>Un conseil et une idée de post par mois</li>
      <li>Fériés, vacances scolaires, grands rendez-vous</li>
    </ul>
  </div>
</section>"""


def back():
    return f"""
<section class="page back">
  <div class="bmsg">{ov("À l’année<br>prochaine.")}</div>
  <div class="bfoot">Calendrier social media {YEAR} · rendez-vous en 2028</div>
</section>"""


def recap():
    feries = [("01.01", "ven", "Jour de l'an"), ("29.03", "lun", "Lundi de Pâques"),
              ("01.05", "sam", "Fête du Travail"), ("06.05", "jeu", "Ascension"),
              ("08.05", "sam", "Victoire 1945"), ("17.05", "lun", "Lundi de Pentecôte"),
              ("14.07", "mer", "Fête nationale"), ("15.08", "dim", "Assomption"),
              ("01.11", "lun", "Toussaint"), ("11.11", "jeu", "Armistice 1918"),
              ("25.12", "sam", "Noël")]
    for d, w, _ in feries:
        dd, mm = map(int, d.split("."))
        assert WD[dt.date(YEAR, mm, dd).weekday()] == w, d
    fr = "".join(f"<li><b>{d}</b><span class='w'>{w}</span>{n}</li>" for d, w, n in feries)
    vac = """
<table>
<tr><th></th><th>Zone A</th><th>Zone B</th><th>Zone C</th></tr>
<tr><td>Hiver</td><td>13.02 → 01.03</td><td>20.02 → 08.03</td><td>06.02 → 22.02</td></tr>
<tr><td>Printemps</td><td>10.04 → 26.04</td><td>17.04 → 03.05</td><td>03.04 → 19.04</td></tr>
<tr><td>Été</td><td colspan="3">à partir du 03.07, toutes zones</td></tr>
<tr><td>Toussaint</td><td colspan="3">23.10 → 08.11, toutes zones</td></tr>
<tr><td>Noël</td><td colspan="3">18.12 → 03.01.2028, toutes zones</td></tr>
</table>
<p class="small">Fin des vacances de Noël 2026 : lundi 04.01. Rentrée 2027 : jeudi 02.09.<br>
Zone A : Besançon, Bordeaux, Clermont-Ferrand, Dijon, Grenoble, Limoges, Lyon, Poitiers. Zone B : Aix-Marseille, Amiens, Lille, Nancy-Metz, Nantes, Nice, Normandie, Orléans-Tours, Reims, Rennes, Strasbourg. Zone C : Créteil, Montpellier, Paris, Toulouse, Versailles.</p>
<div class="extra">
  <div><b>Changement d'heure</b>28.03 heure d'été<br>31.10 heure d'hiver</div>
  <div><b>Saisons</b>20.03 printemps · 21.06 été<br>23.09 automne · 22.12 hiver</div>
</div>"""
    big = [("07.02", "Grammy Awards"), ("14.02", "Super Bowl LXI"), ("14.03", "Cérémonie des Oscars"),
           ("18.04 + 02.05", "Élection présidentielle"), ("11 → 22.05", "Festival de Cannes, 80e"),
           ("15.05", "Finale de l'Eurovision"), ("05.06", "Finale de la Ligue des champions"),
           ("24.06 → 25.07", "Coupe du monde féminine de football"), ("02 → 25.07", "Tour de France"),
           ("02.08", "Éclipse totale de Soleil"), ("01.10 → 13.11", "Coupe du monde de rugby"),
           ("26.11", "Black Friday")]
    bg = "".join(f"<li><b>{d}</b>{n}</li>" for d, n in big)
    return f"""
<section class="page recap">
  <div class="rtitle">{ov("L’essentiel de 2027")}</div>
  <div class="rgrid">
    <div class="rc"><div class="lbl">Jours fériés</div><ul class="fer">{fr}</ul></div>
    <div class="rc"><div class="lbl">Vacances scolaires 2026-2027</div>{vac}</div>
    <div class="rc"><div class="lbl">Les grands rendez-vous</div><ul class="big">{bg}</ul></div>
  </div>
</section>"""


CSS = r"""
@import url('https://fonts.googleapis.com/css2?family=Bagel+Fat+One&family=Schibsted+Grotesk:ital,wght@0,400;0,500;0,600;0,700;0,800;1,400&family=Martian+Mono:wdth,wght@87.5,400;87.5,600;87.5,700&display=block');
@page { size: 297mm 210mm; margin: 0; }
:root { --blue:#3255A4; --pink:#FF48B0; --pinkt:#FFE2F1; --paper:#FFFFFF; --soft:#7D90C4; }
* { box-sizing: border-box; margin: 0; padding: 0; }
html, body { font-family: 'Schibsted Grotesk', sans-serif; color: var(--blue); -webkit-print-color-adjust: exact; print-color-adjust: exact; }
.page { width: 297mm; height: 210mm; position: relative; overflow: hidden; page-break-after: always; background: var(--paper); }
/* surimpression riso */
.ov { position: relative; display: inline-block; font-family: 'Bagel Fat One', sans-serif; font-weight: 400; line-height: .9; }
.ov .b { color: var(--blue); }
.ov .p { position: absolute; left: 0; top: 0; color: var(--pink); mix-blend-mode: multiply; transform: translate(.08em, -.05em); }
.lbl { font-family: 'Martian Mono', monospace; font-size: 2.2mm; font-weight: 700; letter-spacing: .3mm; text-transform: uppercase; color: var(--pink); margin-bottom: 1.6mm; }
sup.ast { color: var(--pink); font-weight: 800; font-size: 1.15em; vertical-align: 0; }
/* ---- mois ---- */
.vt { position: absolute; left: 7mm; top: 10mm; bottom: 10mm; width: 36mm; display: flex; align-items: flex-end; justify-content: center; }
.vt .ov { writing-mode: vertical-rl; transform: rotate(180deg); white-space: nowrap; }
.vt .ov .p { transform: translate(-.06em, .08em); }
.info { position: absolute; left: 47mm; top: 11mm; bottom: 10mm; width: 56mm; display: flex; flex-direction: column; }
.meta { font-family: 'Martian Mono', monospace; font-size: 2.3mm; line-height: 1.7; color: var(--blue); margin-bottom: 8mm; }
.blk { margin-bottom: 7mm; }
.tip { font-size: 2.9mm; line-height: 1.42; }
.tip b { font-weight: 800; }
.perle { background: var(--pinkt); padding: 4mm 4.2mm 4.4mm; }
.pdate { font-size: 13mm; margin: 1mm 0 2mm; }
.pname { font-weight: 800; font-size: 3.1mm; line-height: 1.25; margin-bottom: 1.6mm; }
.perle p { font-size: 2.8mm; line-height: 1.42; }
.legend { margin-top: auto; display: flex; flex-direction: column; gap: 1.8mm; font-family: 'Martian Mono', monospace; font-size: 2.1mm; }
.legend span { display: flex; align-items: center; gap: 2mm; }
.dot { display: inline-block; width: 1.6mm; height: 1.6mm; border-radius: 50%; background: var(--pink); }
.legend .fr, .num.fer { background: var(--pink); color: #fff; border-radius: 50%; }
.legend .fr { font-style: normal; font-weight: 700; font-size: 1.9mm; width: 4.4mm; height: 4.4mm; display: inline-flex; align-items: center; justify-content: center; }
.cols { position: absolute; left: 110mm; right: 9mm; top: 9mm; bottom: 9mm; display: grid; grid-template-columns: repeat(3, 1fr); gap: 4.5mm; }
.col { display: flex; flex-direction: column; min-height: 0; overflow: hidden; }
.wk { font-family: 'Martian Mono', monospace; font-size: 1.8mm; color: var(--soft); letter-spacing: .2mm; text-transform: uppercase; padding: 1.3mm 0 .6mm 1.4mm; }
.day { flex: 1 0 auto; display: grid; grid-template-columns: 10mm 1fr; column-gap: 1.2mm; padding: 1.1mm 1.4mm .6mm; min-height: 9mm; }
.day.we { background: var(--pinkt); }
.dn { display: flex; flex-direction: column; align-items: flex-start; }
.num { font-family: 'Martian Mono', monospace; font-weight: 700; font-size: 3.7mm; line-height: 1; }
.num.fer { width: 6.6mm; height: 6.6mm; display: flex; align-items: center; justify-content: center; font-size: 3.1mm; margin: -.8mm 0 0 -.9mm; }
.wd { font-family: 'Martian Mono', monospace; font-size: 1.8mm; text-transform: uppercase; color: var(--soft); margin-top: .8mm; }
.day.we .wd { color: var(--pink); }
.evs p { font-size: calc(2.25mm * var(--k, 1)); line-height: 1.2; font-weight: 500; margin-bottom: .75mm; }
.evs p i { font-style: normal; color: var(--soft); }
.evs p.fun, .evs p.perso { padding-left: 2.3mm; position: relative; }
.evs p.perso { font-weight: 700; }
.evs p.perso::before { content: ""; position: absolute; left: .1mm; top: .8mm; width: 1.1mm; height: 1.1mm; background: var(--blue); transform: rotate(45deg); }
.dia { display: inline-block; width: 1.4mm; height: 1.4mm; margin: 0 .1mm; background: var(--blue); transform: rotate(45deg); }
.evs p.fun::before { content: ""; position: absolute; left: 0; top: .75mm; width: 1.25mm; height: 1.25mm; border-radius: 50%; background: var(--pink); }
/* ---- couverture ---- */
.cyear { position: absolute; left: 8mm; top: 6mm; font-size: 96mm; display: flex; flex-direction: column; }
.cyear .l2 { margin-left: 24mm; margin-top: -4mm; }
.cright { position: absolute; left: 184mm; top: 0; bottom: 0; width: 96mm; display: flex; flex-direction: column; justify-content: center; }
.cright .lbl { font-size: 2.8mm; margin-bottom: 4mm; }
.cright h1 { font-weight: 800; font-size: 8.6mm; line-height: 1.08; letter-spacing: -.2mm; margin-bottom: 5mm; }
.cright p { font-size: 3.8mm; line-height: 1.45; margin-bottom: 7mm; }
.cright ul { list-style: none; font-family: 'Martian Mono', monospace; font-size: 2.6mm; line-height: 2.1; }
.cright li::before { content: "→ "; color: var(--pink); }
/* ---- dos ---- */
.bmsg { position: absolute; left: 20mm; top: 40mm; font-size: 40mm; }
.bmsg .ov { line-height: 1; }
.bfoot { position: absolute; left: 20mm; bottom: 16mm; font-family: 'Martian Mono', monospace; font-size: 2.6mm; }
/* ---- récap ---- */
.rtitle { position: absolute; left: 10mm; top: 10mm; font-size: 17mm; }
.rgrid { position: absolute; left: 10mm; right: 10mm; top: 38mm; bottom: 10mm; display: grid; grid-template-columns: 66mm 1fr 84mm; gap: 9mm; }
.rc { display: flex; flex-direction: column; }
.rc ul { list-style: none; flex: 1; display: flex; flex-direction: column; }
.rc li { flex: 1; }
.rc li { font-size: 3.5mm; padding: 0; display: flex; align-items: center; font-weight: 500; }
.rc li:nth-child(odd) { background: var(--pinkt); }
.rc li b { font-family: 'Martian Mono', monospace; font-weight: 700; font-size: 2.8mm; min-width: 15mm; padding-left: 1.5mm; }
.rc li .w { font-family: 'Martian Mono', monospace; color: var(--soft); min-width: 10mm; font-size: 2.3mm; text-transform: uppercase; }
.big li b { min-width: 31mm; }

table { width: 100%; border-collapse: collapse; font-size: 3.1mm; margin-top: 1mm; }
.rc td { height: 17mm; }
th { font-family: 'Martian Mono', monospace; font-size: 2.4mm; text-transform: uppercase; color: var(--pink); padding: 2mm 1mm; text-align: center; }
td { padding: 3.2mm 1mm; text-align: center; font-weight: 500; font-family: 'Martian Mono', monospace; font-size: 2.6mm; }
tr:nth-child(even) td { background: var(--pinkt); }
td:first-child { text-align: left; font-family: 'Schibsted Grotesk'; font-weight: 800; font-size: 3.1mm; padding-left: 1.5mm; }
.small { margin-top: auto; padding-top: 5mm; font-size: 2.4mm; line-height: 1.5; color: var(--soft); }
.extra { display: flex; gap: 8mm; margin-top: 5mm; background: var(--pinkt); padding: 4mm 5mm; font-family: 'Martian Mono', monospace; font-size: 2.5mm; line-height: 1.8; }
.extra b { display: block; font-family: 'Schibsted Grotesk'; font-weight: 800; font-size: 3mm; }
"""

pages = [cover()] + [month_page(m) for m in range(1, 13)] + [recap(), back()]
doc = f"""<!doctype html><html lang="fr"><head><meta charset="utf-8"><title>Calendrier social media {YEAR}</title>
<style>{CSS}</style></head><body>{''.join(pages)}</body></html>"""
(ROOT / "build").mkdir(exist_ok=True)
(ROOT / "build" / "calendrier-social-media-2027.html").write_text(doc, encoding="utf-8")
print("ok", count_all())

# ======================= GÉNÉRATEUR INTERACTIF =======================
import json
data = {
    "YEAR": YEAR,
    "events": {f"{m}-{d}": items for (m, d), (items, _) in sorted(E.items())},
    "tips": TIPS,
    "perles": [[list(md), n, i] for md, n, i in PERLES],
    "recap": recap(),
}
tpl = (HERE / "app_template.html").read_text(encoding="utf-8")
app = tpl.replace("/*CSS*/", CSS).replace("/*DATA*/", json.dumps(data, ensure_ascii=False).replace("</", "<\\/"))
(ROOT / "index.html").write_text(app, encoding="utf-8")
print("app ok", len(app) // 1024, "Ko")
