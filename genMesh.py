import gmsh
import sys

def genMesh():
    projName = 'hex_box'

    room_dx = 1
    room_dy = 1
    room_dz = 1

    meshSize = 1
    # meshSF = 0.4
    ####################################################################################################################
    # Before using any functions in the Python API, Gmsh must be initialized:
    gmsh.initialize()
    #gmsh.clear()
    # By default Gmsh will not print out any messages: in order to output messages
    # on the terminal, just set the "General.Terminal" option to 1:
    gmsh.option.setNumber("General.Terminal", 0)
    # Next we add a new model (if gmsh.model.add() is not called a new
    # unnamed model will be created on the fly, if necessary):
    gmsh.model.add(projName)
    # We can log all messages for further processing with:
    gmsh.logger.start()
    ####################################################################################################################
    # Make sure "Recombine all triangular meshes" is unchecked so only triangular elements are produced
    gmsh.option.setNumber('Mesh.RecombineAll', 1)
    # Mesh.Hexahedra = 1
    # gmsh.option.setNumber('Mesh.Hexahedra', 1)
    # Mesh.SubdivisionAlgorithm = 2
    # gmsh.option.setNumber('Mesh.SubdivisionAlgorithm', 2)
    # Mesh.MshFileVersion = 1
    # gmsh.option.setNumber('Mesh.MshFileVersion', 1)
    ####################################################################################################################
    # create room rectangle
    domTag = gmsh.model.occ.addBox(0, 0, 0, room_dx, room_dy, room_dz)
    # print('room tag: %i' % roomTag)

    # We finish by synchronizing the data from OpenCASCADE CAD kernel with the Gmsh model:
    gmsh.model.occ.synchronize()
    ####################################################################################################################
    #################################
    #    Physical Group Naming      #
    #################################
    # print(gmsh.model.getBoundary([(2, domainTag)]))
    # domBWall = 1
    # domRWall = 2
    # domTWall = 3
    # domLWall = 4
    # cylWall = 5
    #
    # grpTag = 1
    # gmsh.model.addPhysicalGroup(2, [domainTag])
    #
    # grpTag += 1
    # gmsh.model.addPhysicalGroup(1, [domLWall])
    # gmsh.model.setPhysicalName(1, grpTag, 'x0')
    # grpTag += 1
    # gmsh.model.addPhysicalGroup(1, [domRWall])
    # gmsh.model.setPhysicalName(1, grpTag, 'x1')
    # grpTag += 1
    # gmsh.model.addPhysicalGroup(1, [domTWall])
    # gmsh.model.setPhysicalName(1, grpTag, 'y0')
    # grpTag += 1        # self.output.append('Best Drag [N]', algorithm.pop.get("F")[:, 0].min())
    #     # self.output.append('Best Drag [N]', np.mean(algorithm.pop.get("F")[:, 1].min()))
    #     # if
    # gmsh.model.addPhysicalGroup(1, [domBWall])
    # gmsh.model.setPhysicalName(1, grpTag, 'y1')
    # grpTag += 1
    # gmsh.model.addPhysicalGroup(1, [cylWall])
    # gmsh.model.setPhysicalName(1, grpTag, 'cyl')
    ####################################################################################################################
    #################################
    #           MESHING             #
    #################################
    # Set minimum and maximum mesh size
    # gmsh.option.setNumber('Mesh.MeshSizeMin', meshSizeMin)
    # gmsh.option.setNumber('Mesh.MeshSizeMax', meshSizeMax)

    # Set size of mesh at every point in model
    gmsh.model.mesh.setSize(gmsh.model.getEntities(0), meshSize)

    # We can then generate a 2D mesh...
    # gmsh.model.mesh.generate(1)
    # gmsh.model.mesh.generate(2)
    gmsh.model.mesh.generate(3)
    ####################################################################################################################
    # ... and save it to disk
    gmsh.write(projName + '.msh22')

    # Inspect the log:
    log = gmsh.logger.get()
    print("Logger has recorded " + str(len(log)) + " lines")
    gmsh.logger.stop()

    # To visualize the model we can run the graphical user interface with
    # `gmsh.fltk.run()'.
    gmsh.fltk.run()
    # This should be called when you are done using the Gmsh Python API:
    gmsh.finalize()


# genMesh('base_case/meshes', 0.01517)  # 0.05 , 0.01517 -> Re=150
# genMesh('base_case/meshes', 0.05)  # 0.05 , 0.01517 -> Re=150
genMesh()
