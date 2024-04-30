# Simple directory tree
# replicate this tree of directories and subdirectories
# ├── draft_code
# |   ├── pending
# |   └── complete
# ├── includes
# ├── layouts
# |   ├── default
# |   └── post
# |       └── posted
# └── site
# 1. Using the os.system or os.mkdirs replicate this simple directory tree
# 2. Delete the directory tree without deleting your entire hard drive

# import os and create folder in root directory
import os

# create draft_code folder in root directory
file_path_draft_code = r"C:\NRS 528\NRS_528_Python\draft_code"
os.mkdir(file_path_draft_code)

# create pending subdirectory in draft code folder
file_path_draft_code_pending = r"C:\NRS 528\NRS_528_Python\draft_code\pending"
os.mkdir(file_path_draft_code_pending)

# create complete subdirectory in draft_code folder
file_path_draft_code_complete = r"C:\NRS 528\NRS_528_Python\draft_code\complete"
os.mkdir(file_path_draft_code_complete)

# create includes directory in root directory
file_path_includes = r"C:\NRS 528\NRS_528_Python\includes"
os.mkdir(file_path_includes)

# create layouts directory in root directory
file_path_layouts = r"C:\NRS 528\NRS_528_Python\layouts"
os.mkdir(file_path_layouts)

# create default subdirectory in layouts directory folder
file_path_layouts_default = r"C:\NRS 528\NRS_528_Python\layouts\default"
os.mkdir(file_path_layouts_default)

# create post subdirectory in layouts directory folder
file_path_layouts_post = r"C:\NRS 528\NRS_528_Python\layouts\post"
os.mkdir(file_path_layouts_post)

# create subdirectory posted in post subdirectory folder
file_path_layouts_post_posted = r"C:\NRS 528\NRS_528_Python\layouts\post\posted"
os.mkdir(file_path_layouts_post_posted)

# create site directory in root directory
file_path_site = r"C:\NRS 528\NRS_528_Python\site"
os.mkdir(file_path_site)

# remove pending subdirectory in draft_code directory
os.rmdir(file_path_draft_code_pending)

# remove complete subdirectory from draft_code directory
os.rmdir(file_path_draft_code_complete)

# remove draft_code directory in root directory
os.rmdir(file_path_draft_code)

# remove includes directory in root directory
os.rmdir(file_path_includes)

# remove posted subdirectory from post subdirectory
os.rmdir(file_path_layouts_post_posted)

# remove post subdirectory from layouts directory
os.rmdir(file_path_layouts_post)

# remove default subdirectory from layouts directory
os.rmdir(file_path_layouts_default)

# remove layouts directory in root directory
os.rmdir(file_path_layouts)

# remove site directory in root directory
os.rmdir(file_path_site)

