bl_info = {
    "name": "CgBookCase Addon",
    "author": "Dhanushka",
    "version": (1, 0),
    "blender": (2, 80, 0),
    "location": "View3D > Toolshelf",
    "description": "Adds a new shader to the object",
    "warning": "",
    "wiki_url": "",
    "category": "Add Texture",
}

import bpy
from bpy.utils import previews
from bpy.types import Panel, Operator, PropertyGroup
from bpy.props import EnumProperty, PointerProperty, StringProperty

#image preview path 
p_image_path = r"C:\Texture\clay-shingles1-unity\clay-shingles1_preview.jpg"
p_image_path2 = r"C:\Texture\space-cruiser-panels2-unity\space-cruiser-panels2_preview.jpg"


preview_collection = previews.new()
preview = preview_collection.load("custom_image", p_image_path, "IMAGE")
preview2 = preview_collection.load("custom_image2", p_image_path2, "IMAGE")


class MyTextures(PropertyGroup):
    
        my_enum : EnumProperty(
        name = "Texture",
        description = "Shader Collector",
        items = [('OP1', "CLAY", ""),
                 ('OP2', "SPACE", "")  
        ]
    
    )



class AddonMainPanel(Panel):
    bl_label = "CgBookCase Addon"
    bl_idname = "SHADER_PT_MAINPANEL"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'CgBookCase'

    def draw(self, context):
        layout = self.layout
        scene = context.scene
        mytool = scene.my_tool
        enum = mytool.my_enum
        
        
        row = layout.row()
        row.label(text = "CgBookCase")
        row = layout.row()
        row.label(text = "Select a Texture: ")
        row = layout.row()
        
        #enum
        layout.prop(mytool, "my_enum")
        
        # Display the image
        
        if enum == 'OP1':
          
                img = preview.icon_id
                layout.template_icon(icon_value=img, scale=5)
                row = layout.row()
                                  
        elif enum == 'OP2':           
            
                img = preview2.icon_id
                layout.template_icon(icon_value=img, scale=5)
                row = layout.row()
    
        
        row = layout.row()
        row.operator('shader.texture_pbr_operator')
        
        
        
class SHADER_OT_TEXTURE(Operator):
    bl_label = "Load Texture"
    bl_idname = 'shader.texture_pbr_operator'
    
    def execute(self, context):
        scene = context.scene
        mytool = scene.my_tool
        enum = mytool.my_enum

        
        if enum == 'OP1':
          
            tName = "Clay"
            image_filepath1 = r"C:\Texture\clay-shingles1-unity\clay-shingles1_albedo.png"
            image_filepath2 = r"C:\Texture\clay-shingles1-unity\clay-shingles1_metallic.psd"
            image_filepath3 = r"C:\Texture\clay-shingles1-unity\clay-shingles1_normal-ogl.png"
            image_filepath4 = r"C:\Texture\clay-shingles1-unity\clay-shingles1_height.png"
                                  
        elif enum == 'OP2':           
            
            tName = "Space"
            image_filepath1 = r"C:\Texture\space-cruiser-panels2-unity\space-cruiser-panels2_albedo.png"
            image_filepath2 = r"C:\Texture\space-cruiser-panels2-unity\space-cruiser-panels2_metallic.psd"
            image_filepath3 = r"C:\Texture\space-cruiser-panels2-unity\space-cruiser-panels2_normal-ogl.png"
            image_filepath4 = r"C:\Texture\space-cruiser-panels2-unity\space-cruiser-panels2_height.png"
        
        else:
            
            tName = ""
            image_filepath1 = r""
            image_filepath2 = r""
            image_filepath3 = r""
            image_filepath4 = r""
        
        
        
            #Creating a new shader and callling it Diamond
        material_wood = bpy.data.materials.new(name= tName)
            #Enabling use Node
        material_wood.use_nodes = True  
        
        
        
        
        ####Creating material node and PBSDF                             
            #Create a refernce to the Material Output
        material_output = material_wood.node_tree.nodes.get('Material Output')
            #Set Location of the Node
        material_output.location = (500,0)
            #Deselect the Node
        material_output.select = False
        
        #Create a refernce to the PBSDF
        princ_bsdf = material_wood.node_tree.nodes.get('Principled BSDF')
            #Set Location of the Node
        princ_bsdf.location = (50,0)
            #Deselect the Node
        princ_bsdf.select = False
        
        
        
        
        #### Imgae Texture Node        
            #Adding textimage Nodes
        tex_image_1_node = material_wood.node_tree.nodes.new('ShaderNodeTexImage')        
            # Set the image node's image file
        tex_image_1_node.image = bpy.data.images.load(image_filepath1)
            #Set location of the Node
        tex_image_1_node.location = (-600,0)
            #Deselect the Node
        tex_image_1_node.select = False
        
            #Adding textimage Nodes
        tex_image_2_node = material_wood.node_tree.nodes.new('ShaderNodeTexImage')        
            # Set the image node's image file
        tex_image_2_node.image = bpy.data.images.load(image_filepath2)
            #Set location of the Node
        tex_image_2_node.location = (-600,-300)
            #Deselect the Node
        tex_image_2_node.select = False
            #Change color space
        tex_image_2_node.image.colorspace_settings.name = "Non-Color"
               
            #Adding textimage Nodes
        tex_image_3_node = material_wood.node_tree.nodes.new('ShaderNodeTexImage')        
            # Set the image node's image file
        tex_image_3_node.image = bpy.data.images.load(image_filepath3)
            #Set location of the Node
        tex_image_3_node.location = (-600,-600)
            #Deselect the Node
        tex_image_3_node.select = False
            #Change color space
        tex_image_3_node.image.colorspace_settings.name = "Non-Color"
                   
            #Adding textimage Nodes
        tex_image_4_node = material_wood.node_tree.nodes.new('ShaderNodeTexImage')        
            # Set the image node's image file
        tex_image_4_node.image = bpy.data.images.load(image_filepath4)
            #Set location of the Node
        tex_image_4_node.location = (-600,-900)
            #Deselect the Node
        tex_image_4_node.select = False
            #Change color space
        tex_image_4_node.image.colorspace_settings.name = "Non-Color"
        
       
       
       
       #### Normal Map Node & Displacment Node
            #Adding normalmap Nodes
        normal_map1 = material_wood.node_tree.nodes.new('ShaderNodeNormalMap')        
            #Set location of the Node
        normal_map1.location = (-230,-600)
            #Deselect the Node
        normal_map1.select = False
        
            #Adding displacement Nodes
        displace_node = material_wood.node_tree.nodes.new('ShaderNodeDisplacement')        
            #Set location of the Node
        displace_node.location = (100,-900)
            #Deselect the Node
        displace_node.select = False
        
        
        
        
        #### Texture Coordinate & Mapping Node        
            #Adding texture coordinate Nodes
        tex_coord = material_wood.node_tree.nodes.new('ShaderNodeTexCoord')        
            #Set location of the Node
        tex_coord.location = (-1000,-200)
            #Deselect the Node
        tex_coord.select = False
        
            #Adding mapping Nodes
        map_node = material_wood.node_tree.nodes.new('ShaderNodeMapping')        
            #Set location of the Node
        map_node.location = (-800,-200)
            #Deselect the Node
        map_node.select = False




        ####linking the nodes
        
        link = material_wood.node_tree.links.new
        
        #linking texture coordinate and mapping nodes
        link(tex_coord.outputs['UV'], map_node.inputs['Vector'])
        link(map_node.outputs['Vector'], tex_image_1_node.inputs['Vector'])
        link(map_node.outputs['Vector'], tex_image_2_node.inputs['Vector'])
        link(map_node.outputs['Vector'], tex_image_3_node.inputs['Vector'])
        link(map_node.outputs['Vector'], tex_image_4_node.inputs['Vector'])
        
        #Rough or Metal        
        
        if enum == 'OP1':        
            link(tex_image_2_node.outputs['Color'], princ_bsdf.inputs['Metallic'])
                                  
        elif enum == 'OP2':           
            link(tex_image_2_node.outputs['Color'], princ_bsdf.inputs['Metallic'])
        
        
        #linking the image textures
        link(tex_image_1_node.outputs['Color'], princ_bsdf.inputs['Base Color'])
        link(tex_image_3_node.outputs['Color'], normal_map1.inputs['Color'])
        link(tex_image_4_node.outputs['Color'], displace_node.inputs['Height']) 
       
        
        #linking displacment and normal map nodes
        link(normal_map1.outputs['Normal'], princ_bsdf.inputs['Normal'])
        link(displace_node.outputs['Displacement'], material_output.inputs['Displacement'])
       
       
       
       
        bpy.context.object.active_material = material_wood
        
        return{'FINISHED'}
        
        
        
        
        
        
        
        
def register():
    bpy.utils.register_class(MyTextures)
    bpy.utils.register_class(AddonMainPanel)
    bpy.utils.register_class(SHADER_OT_TEXTURE)
    
    bpy.types.Scene.my_tool = PointerProperty(type= MyTextures)

def unregister():
    bpy.utils.unregister_class(MyTextures)
    bpy.utils.unregister_class(AddonMainPanel)
    bpy.utils.unregister_class(SHADER_OT_TEXTURE) 
    
    del bpy.types.Scene.my_tool

if __name__ == "__main__":
    register()
    
