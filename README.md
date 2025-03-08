# BlenderStruct

BlenderStruct is a Blender add-on that automatically creates a folder structure for your Blender projects and saves the Blender file in the appropriate folder. This add-on is designed to help you stay organized and save time by creating a consistent folder structure for your projects.

## Features

- Automatically creates a folder structure based on the chosen file name.
- Saves the Blender file in the 'project' subfolder.
- Creates the following subfolders:
  - `assets/3D models`
  - `assets/textures`
  - `assets/references/images`
  - `project`
  - `storyboard`
  - `scripts`
  - `addons`
  - `render/viewport render`
  - `render/render`
- Binds the custom save operator to `Ctrl + Alt + S`.

## Installation

1. Download the `create_folders.py` file.
2. Open Blender and go to `Edit > Preferences > Add-ons`.
3. Click on `Install...` and select the `create_folders.py` file.
4. Enable the add-on by checking the box next to `BlenderStruct`.

## Usage

1. Press `Ctrl + Alt + S` to open the file selector.
2. Choose the save location and file name for your Blender project.
3. The add-on will create the folder structure based on the chosen file name and save the Blender file in the 'project' subfolder.

## Example

If you choose to save your Blender file as `MyProject.blend` in the `/home/user/BlenderProjects` directory, the following folder structure will be created:
