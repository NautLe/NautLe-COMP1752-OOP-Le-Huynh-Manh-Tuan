from library_item import LibraryItem


library = {}
library["01"] = LibraryItem("Tom and Jerry", "Fred Quimby", 4, 94, "Tom and Jerry is an American animated media franchise and series of comedy short films created in 1940 by William Hanna and Joseph Barbera. Best known for its 161 theatrical short films by Metro-Goldwyn-Mayer, the series centers on the rivalry between the titular characters of a cat named Tom and a mouse named Jerry.")
library["02"] = LibraryItem("Breakfast at Tiffany's", "Blake Edwards", 5, 106, "Breakfast at Tiffany's is a classic novella by Truman Capote. It tells the story of a young writer who becomes infatuated with his eccentric neighbor, Holly Golightly, and their unconventional friendship in New York City.")
library["03"] = LibraryItem("Casablanca", "Michael Curtiz", 2, 102, "Step into the intrigue of wartime Casablanca, where love and politics collide. Humphrey Bogart and Ingrid Bergman's timeless performances make this film a cinematic masterpiece.")
library["04"] = LibraryItem("The Sound of Music", "Robert Wise", 1, 175, "The musical tells the story of Maria, who takes a job as governess to a large family while she decides whether to become a nun. She falls in love with the children and their widowed father, Captain von Trapp. He is ordered to accept a commission in the German navy, but he opposes the Nazis. He and Maria decide to flee from Austria with the children.")
library["05"] = LibraryItem("Gone with the Wind", "Victor Fleming", 3, 238, "Gone with the Wind is a historical novel written by American author Margaret Mitchell and published in 1936. In summary, Gone with the Wind offers a romanticized view of the American Civil War from the perspective of the Confederacy. It focuses on Scarlett O'Hara, the beautiful daughter of a wealthy planter, following her romantic trials during the war and into the Reconstruction period.")


def list_all(): #a function whose main perpose is to list all the videos in the library
    output = ""
    for key in library:
        item = library[key]
        output += f"{key} {item.info()}\n"
    return output


def get_name(key):
    try:
        item = library[key]
        return item.name
    except KeyError:
        return None
    
def get_duration(key):
    try:
        item = library[key]
        return item.duration
    except KeyError:
        return -1

def get_short_description(key):
    try:
        item = library[key]
        return item.short_description
    except KeyError:
        return None


def get_director(key):
    try:
        item = library[key]
        return item.director
    except KeyError:
        return None


def get_rating(key):
    try:
        item = library[key]
        return item.rating
    except KeyError:
        return -1


def set_rating(key, rating):
    try:
        item = library[key]
        item.rating = rating
    except KeyError:
        return


def get_play_count(key):
    try:
        item = library[key]
        return item.play_count
    except KeyError:
        return -1


def increment_play_count(key):
    try:
        item = library[key]
        item.play_count += 1
    except KeyError:
        return

