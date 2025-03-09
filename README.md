# 🗂️ **BlenderStruct** 📂

**BlenderStruct** is a Blender add-on that automatically creates a folder structure for your Blender projects and saves the Blender file in the appropriate folder. This add-on is designed to help you stay organized and save time by creating a consistent folder structure for your projects. ⚙️

> **⚠️ Warning**
> 
> The Blender file will be saved in the 'project' subfolder within the created folder structure. Ensure that you choose the correct file name and location when using the add-on. 📁

> **ℹ️ Note**
> Press `Ctrl + Alt + S` to open the file selector. ⌨️

## 🔑 **Features**

- Automatically creates a folder structure based on the chosen file name. 🏗️
- Saves the Blender file in the 'project' subfolder. 💾
- Creates the following subfolders:
  - `assets/3D models` 🏗️
  - `assets/textures` 🎨
  - `assets/references/images` 🖼️
  - `project` 📁
  - `storyboard` 📝
  - `scripts` 💻
  - `addons` 🔧
  - `render/viewport render` 🎥
  - `render/render` 🖥️
- Binds the custom save operator to `Ctrl + Alt + S`. 🖱️

## 🛠️ **Installation**

1. Download the `create_folders.py` file from the [Releases](https://github.com/PatrickIndran/BlenderStruct/releases/tag/Main) page. 📥
2. Open Blender and go to **Edit > Preferences > Extensions**. ⚙️
3. In the Extensions panel, click the drop-down menu in the top-right corner and select **Install from Disk**. 💽
4. In the file browser that appears, navigate to and select the `create_folders.py` file. 📂
5. Once the add-on is installed, enable it by checking the box next to its name (e.g., *BlenderStruct*). ✅
6. If the add-on does not activate, check the Console window for any error messages. 💬

### ℹ️ **Note**

- The custom save operator is bound to `Ctrl + Alt + S`. Pressing this key combination will invoke the file selector and create the folder structure. 🔑

## 📝 **Example**

If you choose to save your Blender file as `MyProject.blend` in the `/home/user/BlenderProjects` directory, the following folder structure will be created: 📁

