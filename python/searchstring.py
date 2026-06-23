def main():
    collections = ["skyrim", "tomb raider", "minecraft" , "ori and the blind forest", "gta v"]
    search = input(" search : ").lower()
    found = False

    for collection in collections:
        if search == collection.lower():
            print(f"search result : found {collection}", end="")
            found = True
    if not found:
        print("search result : "+ search +" not found")

main()