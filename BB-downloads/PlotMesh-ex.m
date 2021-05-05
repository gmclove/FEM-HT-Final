Ne=8;                            %number of nodes per element

df=3;                            %degrees of freedom per node

ex1=importdata('CO.txt');

ex2=importdata('CM.txt');

CO=ex1(:,2:4);

CM=ex2(:,6:13); %the CM file obtained from GMSH includes some other information in the first 5 columns. Thus the meshing info we need starts from the 6th column (i.e., the 6th column is the first global ID in the CO file within an element).

PlotMesh(CO,CM)

axis image

axis off
