artist = {
    "first": "Neil",
    "last": "Young",
}
 
# concat first and last name with a space
full_name = artist["first"] + " " + artist["last"]



artist = {
    "first": "Neil",
    "last": "Young",
}
 
full_name = "{} {}".format(artist["first"],artist["last"])

artist = {
    "first": "Neil",
    "last": "Young",
}
 
full_name = f"{artist['first']} {artist['last']}"