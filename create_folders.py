import bpy
import os

# Global list to store keymap references for proper cleanup on unregister.
addon_keymaps = []

class SaveWithFolderCreationOperator(bpy.types.Operator):
    """Operator to save the Blender file with multimedia folder creation.
    
    This operator opens the file selector so the user can choose the save location
    and file name. It then creates a multimedia folder structure based on the chosen
    name (folder name) and saves the file in the 'project' subfolder.
    """
    bl_idname = "wm.save_with_folder_creation"
    bl_label = "Save with Folder Creation"

    # The filepath property will be populated by the file selector.
    filepath: bpy.props.StringProperty(subtype="FILE_PATH")

    def execute(self, context):
        # Determine the root folder from the chosen file path.
        root_folder = os.path.dirname(self.filepath)
        # Get the chosen file name; remove any extension if present.
        project_filename = os.path.basename(self.filepath)
        folder_name = project_filename.rsplit('.', 1)[0]

        # Debug: Log the root folder and folder name.
        self.report({'INFO'}, f"Root folder: {root_folder}, Folder name: {folder_name}")

        # Define the base path where the multimedia folders will be created.
        base_path = os.path.join(root_folder, folder_name)
        # Define all required sub-folders in the multimedia structure.
        folders = [
            os.path.join(base_path, 'assets', '3D models'),
            os.path.join(base_path, 'assets', 'textures'),
            os.path.join(base_path, 'assets', 'references', 'images'),
            os.path.join(base_path, 'project'),
            os.path.join(base_path, 'storyboard'),
            os.path.join(base_path, 'scripts'),
            os.path.join(base_path, 'addons'),
            os.path.join(base_path, 'render', 'viewport render'),
            os.path.join(base_path, 'render', 'render')
            # Additional subfolders:
            # os.path.join(base_path, 'additional_subfolder')
        ]

        # Create each folder (if it doesn't exist already) and report status.
        for folder in folders:
            try:
                os.makedirs(folder, exist_ok=True)
                self.report({'INFO'}, f"Created folder: {folder}")
            except Exception as e:
                self.report({'ERROR'}, f"Error creating folder '{folder}': {e}")
                return {'CANCELLED'}

        # Define the path for saving the blend file.
        # The file is saved in the 'project' subfolder using the folder name with a .blend extension.
        project_folder = os.path.join(base_path, 'project')
        new_blend_path = os.path.join(project_folder, f"{folder_name}.blend")

        # Attempt to save the file.
        try:
            bpy.ops.wm.save_as_mainfile(filepath=new_blend_path)
            self.report({'INFO'}, f"Saved blend file at: {new_blend_path}")
        except Exception as e:
            self.report({'ERROR'}, f"Error saving blend file: {e}")
            return {'CANCELLED'}

        return {'FINISHED'}

    def invoke(self, context, event):
        # Always show the file selector so that you can choose a location and file name.
        context.window_manager.fileselect_add(self)
        return {'RUNNING_MODAL'}

class MultimediaFoldersPanel(bpy.types.Panel):
    """Panel to expose the operator for developers and users.
    
    The panel shows a single button to invoke the Save with Folder Creation operator.
    """
    bl_label = "Multimedia Folders"
    bl_idname = "PT_multimedia_folders"
    bl_space_type = 'VIEW_3D'  # Shows in the 3D View sidebar.
    bl_region_type = 'UI'
    bl_category = 'Multimedia'

    def draw(self, context):
        layout = self.layout
        scene = context.scene
        # Display properties for folder location and folder name.
        layout.prop(scene, "root_folder")
        layout.prop(scene, "folder_name")
        # Add a button to invoke the custom save operator.
        layout.operator("wm.save_with_folder_creation", text="Create Folders & Save")

def register():
    # Register operator and panel.
    bpy.utils.register_class(SaveWithFolderCreationOperator)
    bpy.utils.register_class(MultimediaFoldersPanel)

    # Register scene properties for manual input.
    bpy.types.Scene.root_folder = bpy.props.StringProperty(
        name="Root Folder",
        description="Select the root folder",
        subtype='DIR_PATH'
    )
    bpy.types.Scene.folder_name = bpy.props.StringProperty(
        name="Folder Name",
        description="Name of the new folder"
    )

    # Override Ctrl+S in the Window context.
    wm = bpy.context.window_manager
    kc = wm.keyconfigs.addon
    if kc:
        # Create a new keymap for the 'Window' area.
        km = kc.keymaps.new(name='Window', space_type='EMPTY')
        # Bind the custom operator to Ctrl+S.
        kmi = km.keymap_items.new("wm.save_with_folder_creation", "S", "PRESS", ctrl=True)
        addon_keymaps.append((km, kmi))

def unregister():
    # Remove keymap entries added in register().
    for km, kmi in addon_keymaps:
        km.keymap_items.remove(kmi)
    addon_keymaps.clear()

    # Unregister the operator and panel.
    bpy.utils.unregister_class(SaveWithFolderCreationOperator)
    bpy.utils.unregister_class(MultimediaFoldersPanel)
    del bpy.types.Scene.root_folder
    del bpy.types.Scene.folder_name

if __name__ == "__main__":
    register()