from face import Face


f = open('bed_0001.off', 'r')

#read in starting file data
f.readline()
num_vertices, num_faces, _ = list(map(int,(f.readline().split(" "))))



# make a list of the vertices
# for each triangle, make a face object tokeep track of the vertices and calculate area, add to total area, and later generate the appropriate amount of points.

vertex_list = []
# populate vertex_list
for i in range(num_vertices):
   point = list(map(float,(f.readline()).split(" ")))
   vertex_list.append(point)

total_area = 0
face_list = []
# populate face_list
for i in range(num_faces):
   _, v1, v2, v3 = list(map(float,(f.readline()).split(" ")))
   face = Face(v1, v2, v3)
   face_list.append(face)
   total_area += face.area

print(face_list)      
   
f.close()

