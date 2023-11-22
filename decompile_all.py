from Utilities import extract_folder
from settings import *

ea_folder = 'My Script Mods'
if not os.path.exists(ea_folder):
    os.mkdir(ea_folder)

game_folder = r'C:\Users\Owner\PycharmProjects\Sims 4 Python Script Workspace\My Script Mods\move objects'
gameplay_folder_data = os.path.join(game_folder, 'Tmex-AlwaysMOO.ts4script')
# gameplay_folder_data = os.path.join(game_folder, 'Data', 'Simulation', 'Gameplay')
# gameplay_folder_game = os.path.join(game_folder, 'Game', 'Bin', 'Python')
#
# extract_folder(ea_folder,gameplay_folder_data)
# extract_folder(ea_folder,gameplay_folder_game)

extract_folder(ea_folder, gameplay_folder_data)