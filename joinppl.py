import PySimpleGUI as sg
import webbrowser

def open_roblox_profile(username):
    profile_url = f"https://www.roblox.com/users/profile?username={username}"
    webbrowser.open(profile_url)

layout = [
    [sg.Text("Roblox username: "), sg.InputText(key='username')],
    [sg.Button("Find"), sg.Button("Exit")]
]

while True:
    username = input("Insert the roblox player username: ")
    open_roblox_profile(username)

    repeat = input("Want to find someone else? (y/n): ")
    if repeat.lower() in ['n', 'no']:
        break
