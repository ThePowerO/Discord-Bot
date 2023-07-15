import webbrowser

def open_roblox_profile(username):
    profile_url = f"https://www.roblox.com/users/profile?username={username}"
    webbrowser.open(profile_url)

while True:
    username = input("Insert the roblox player username: ")
    open_roblox_profile(username)
