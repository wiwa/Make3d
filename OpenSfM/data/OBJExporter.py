import sys
import json

def parse(file_directory):
    json_data=open(file_directory).read()

    geometry = json.loads(json_data)

    output = ""
    for i in range(len(geometry["vertices"])):
        vertex = geometry['vertices'][i]
        output += "v " + vertex['x'] + " " + vertex['y'] + ' ' + vertex['z'] + '\n'



    for i in range(len(geometry['faceVertexUvs'][ 0 ])):
        vertexUvs = geometry['faceVertexUvs'][ 0 ][ i ];
        for j in range(len(vertexUvs)):
            uv = vertexUvs[ j ];
            output += 'vt ' + uv['x'] + ' ' + uv['y'] + '\n';
 
# +
# +       // normals
# +
    for i in range(len(geometry['faces'])):
        normals = geometry['faces'][ i ]['vertexNormals']
        for j in range(len(normals)):
            normal = normals[j]
            output += 'vn ' + normal['x'] + ' ' + normal['y'] + ' ' + normal['x']['z'] + '\n';
#       // map

        count = 1; #// OBJ values start by 1
        map = [ count ]

        for i in range(len(geometry['faces'])):
      
            face = geometry['faces'][ i ]

            if ( face['a'] and face['b'] and face['c'] and face['normal'] and face['color'] and face['materialIndex']):

                if (face['d']):
                   count += 4;

                else:
                   count += 3;

            map.push( count );

        
       # faces

        for i in range(len(geometry['faces'])) :

            face = geometry['faces'][ i ]

            output += 'f '

            if (face['a'] and face['b'] and face['c'] and face['normal'] and face['color'] and face['materialIndex']):
               if face['d']:
                    output += ( face['a'] + 1 ) + '/' + ( map[ i ] ) + '/' + ( map[ i ] ) + ' '
                    output += ( face['b'] + 1 ) + '/' + ( map[ i ] + 1 ) + '/' + ( map[ i ] + 1 ) + ' '
                    output += ( face['c'] + 1 ) + '/' + ( map[ i ] + 2 ) + '/' + ( map[ i ] + 2 ) + '\n'
            else:
                   output += ( face['a'] + 1 ) + '/' + ( map[ i ] ) + '/' + ( map[ i ] ) + ' '
                   output += ( face['b'] + 1 ) + '/' + ( map[ i ] + 1 ) + '/' + ( map[ i ] + 1 ) + ' '
                   output += ( face['c'] + 1 ) + '/' + ( map[ i ] + 2 ) + '/' + ( map[ i ] + 2 ) + ' '
                   output += ( face['d'] + 1 ) + '/' + ( map[ i ] + 3 ) + '/' + ( map[ i ] + 3 ) + '\n'

        return output

   


if __name__ == "__main__":
    jsonname = sys.argv[0]
    obj = parse(jsonname)

    f = open('test.obj', 'r+')
    f.write(obj)
    f.close()