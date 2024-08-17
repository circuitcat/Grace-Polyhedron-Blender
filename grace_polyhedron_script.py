import bpy

# Ensure we're in Object Mode before starting
if bpy.context.object and bpy.context.object.mode != 'OBJECT':
    bpy.ops.object.mode_set(mode='OBJECT')

# Clear existing mesh objects
# This section ensures that any pre-existing mesh objects are deleted to start fresh.
bpy.ops.object.select_all(action='SELECT')
bpy.ops.object.delete()

# Define the unique vertices based on the corrected coordinates
# These vertices correspond to Grace's 8-Vertex Polyhedron, a shape that maximizes volume
# for a polyhedron with eight vertices inscribed in a unit sphere.
vertices = [
    (0, -0.569, 0.822),
    (0, 0.970, -0.243),
    (-0.970, 0, 0.243),
    (-0.569, 0, -0.822),
    (0, -0.970, -0.243),
    (0.569, 0, -0.822),
    (0.970, 0, 0.243),
    (0, 0.569, 0.822)
]

# Create a new mesh and object
# A new mesh is created to hold the vertices, and an object is created to manage this mesh in the scene.
mesh = bpy.data.meshes.new("Grace_Polyhedron_Vertices")
obj = bpy.data.objects.new("Grace_Polyhedron_Vertices", mesh)

# Link the object to the current scene
# The object is linked to the current scene so it becomes visible and editable in Blender.
bpy.context.collection.objects.link(obj)

# Add vertices to the mesh
# The vertices are added to the mesh, but no faces or edges are created at this point.
mesh.from_pydata(vertices, [], [])
mesh.update()

# Set the object as active
# This sets the new object as the active selection in Blender, allowing further operations on it.
bpy.context.view_layer.objects.active = obj

# Switch to Edit Mode
# The script switches to Edit Mode, enabling mesh editing features like adding faces.
bpy.ops.object.mode_set(mode='EDIT')

# Select all vertices
# All vertices are selected so that the Convex Hull operation can be applied to them.
bpy.ops.mesh.select_all(action='SELECT')

# Generate the Convex Hull
# The Convex Hull operation creates the smallest convex polyhedron that encloses all the selected vertices.
bpy.ops.mesh.convex_hull()

# Triangulate all faces to ensure they are triangular
# This converts any non-triangular faces into triangles.
bpy.ops.mesh.quads_convert_to_tris()

# Switch back to Object Mode
# After generating the convex hull, the script switches back to Object Mode for further manipulations if needed.
bpy.ops.object.mode_set(mode='OBJECT')

# Center the object and adjust the origin
# The object's origin is set to its center of mass, and its location is cleared for better alignment in the scene.
bpy.ops.object.origin_set(type='ORIGIN_CENTER_OF_MASS', center='BOUNDS')
bpy.ops.object.location_clear()

# Add a r=1 ico_sphere to visualize the vertices being on it
bpy.ops.mesh.primitive_ico_sphere_add(subdivisions=4, enter_editmode=False, align='WORLD', location=(0, 0, 0), scale=(1, 1, 1))

# Switch to Edit Mode and delete faces of the ico_sphere for a clear view of Grace's Polyhedron
bpy.ops.object.editmode_toggle()
bpy.ops.mesh.delete(type='ONLY_FACE')
bpy.ops.object.editmode_toggle()

# Deselect all objects
bpy.ops.object.select_all(action='DESELECT')

# ------------------------------------------------------------------------------
# Grace's 8-Vertex Polyhedron:
# ------------------------------------------------------------------------------
# This shape was discovered by Donald W. Grace in 1962 and is known for being 
# the polyhedron with eight vertices that maximizes the volume when inscribed 
# in a unit sphere. This polyhedron is often referred to as "Grace's Polyhedron".
#
# Video Reference:
# 1. [YouTube Video](https://www.youtube.com/watch?v=XZy3rXr2yeM&t=387s) - Stand-up Maths' Video explaining the background and significance of Grace's Polyhedron.
#
# Useful Links:
# 1. [Grace's Polyhedron](https://www.jstor.org/stable/2003517) - Reference to the original discovery.
# 2. [Convex Hull in Geometry](https://en.wikipedia.org/wiki/Convex_hull) - Explanation of convex hulls.
# 3. [Platonic and Archimedean Solids](https://mathworld.wolfram.com/PlatonicSolid.html) - Related geometric shapes.
# ------------------------------------------------------------------------------
