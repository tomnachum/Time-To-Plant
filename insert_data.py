from plant import Plant
import db_manager


plants = [
    Plant(
        "Succulent",
        "succulent plants, also known as succulents, are plants with parts that are thickened, fleshy, and engorged, usually to retain water in arid climates or soil conditions. The word succulent comes from the Latin word sucus, meaning 'juice' or 'sap'",
        "Succulent.jfif",
        3,
    ),
    Plant(
        "Olive Tree",
        "The olive, botanical name Olea europaea, meaning 'European olive' in Latin, is a species of small tree or shrub in the family Oleaceae, found traditionally in the Mediterranean Basin.",
        "Olive Tree.png",
        3,
    ),
    Plant(
        "Rose",
        "A rose is either a woody perennial flowering plant of the genus Rosa, in the family Rosaceae, or the flower it bears. There are over three hundred species and tens of thousands of cultivars.",
        "Rose.jpg",
        3,
    ),
    Plant(
        "Orchid",
        "orchid flowers have three sepals, three petals and a three-chambered ovary. The three sepals and two of the petals are often similar to each other but one petal is usually highly",
        "Orchid.png",
        3,
    ),
    Plant(
        "Cactus",
        "cacti generally have thick herbaceous or woody chlorophyll-containing stems. Cacti can be distinguished from other succulent plants by the presence of areoles",
        "Cactus.jpeg",
        3,
    ),
    Plant(
        "Aglaonema",
        "Aglaonema is a genus of flowering plants in the arum family, Araceae. They are native to tropical and subtropical regions of Asia and New Guinea. They are known commonly as Chinese evergreens.",
        "aglaonema.jpg",
        3,
    ),
    Plant(
        "aloe vera",
        "Aloe vera is a succulent plant species of the genus Aloe. It is widely distributed, and is considered an invasive species in many world regions.",
        "aloevera.jpg",
        3,
    ),
    Plant(
        "Diepenbachia",
        "Dieffenbachia, commonly known as dumb cane or leopard lily, is a genus of tropical flowering plants in the family Araceae. It is native to the New World Tropics from Mexico and the West Indies south to Argentina. Some species are widely cultivated as ornamental plants, especially as houseplants, and have become naturalized on a few tropical islands.",
        "Dieffenbachia_.jpg",
        3,
    ),
    Plant(
        "Philodendron",
        "Philodendron is a large genus of flowering plants in the family Araceae. As of September 2015, the World Checklist of Selected Plant Families accepted 489 species; other sources accept different numbers. Regardless of number of species, the genus is the second-largest member of the family Araceae, after genus Anthurium. Taxonomically, the genus Philodendron is still poorly known, with many undescribed species. Many are grown as ornamental and indoor plants.",
        "pilo.jpg",
        3,
    ),
]
db_manager.add_plants(plants)

users = [
    {"name": "Itai", "email": "email@gmail.com", "phone_number": "0525645751"},
    {"name": "Tom", "email": "tom@gmail.com", "phone_number": "0545400958"},
    {"name": "Matan", "email": "matan@gmail.com", "phone_number": "0504448908"},
    {"name": "Adi", "email": "email@gmail.com", "phone_number": "0547659131"},
]

for user in users:
    db_manager.add_user(user["name"], user["email"], user["phone_number"])

users_plants = [
    {"user_id": 1, "plants_id": [], "note": ""},
    {"user_id": 2, "plants_id": [2, 3], "note": "need more water!"},
    {"user_id": 3, "plants_id": [1, 3], "note": "need new one"},
]
for user_plants in users_plants:
    db_manager.add_plants_to_user(
        user_plants["user_id"], user_plants["plants_id"], user_plants["note"]
    )

user_notifications = [
    {"user_id": 2, "plant_id": 2, "time_in_UNIX_TIMESTAMP": 12345678},
    {"user_id": 2, "plant_id": 3, "time_in_UNIX_TIMESTAMP": 12345678},
    {"user_id": 3, "plant_id": 1, "time_in_UNIX_TIMESTAMP": 12345678},
    {"user_id": 3, "plant_id": 3, "time_in_UNIX_TIMESTAMP": 12345678},
]
for notification in user_notifications:
    db_manager.add_notification(
        notification["user_id"],
        notification["plant_id"],
        notification["time_in_UNIX_TIMESTAMP"],
    )
