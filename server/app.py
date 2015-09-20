from flask import Flask, request
import uuid
from time import sleep
app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def relay_data():
    if request.method == 'GET':
        # TODO implement?
        #return "get not implemented"
        f = [i.strip() for i in open('roots').readlines()]
        fname = f[int(random.random()*len(f))]
        json = open('%s/%s' % (fname, 'reconstruction.meshed.json')).read()
        return convert(json)
        
        
    elif request.method == 'POST':
        #return "200 OK"
        # assume i have imgs = [...]
        foldername = str(uuid.uuid4())
        root_dir = '/root/%s' % foldername
        f = open('roots', 'w+')
        f.write(root_dir + '\n')
        f.close()
        imgs = request.get_json(force=True)
        print('json received: ' + imgs)
        for filename in imgs:
            f = open('%s/%s' % (root_dir, filename), 'w')
            f.write(imgs[filename])
            f.close()
        stem = 'docker run --rm -it -v '
        imgpathmap = '%s:%s ' % (root_dir, filename)
        binpath = 'openfsm bin/run_all '
        output = foldername
        command = stem + imagepathmap + binpath + output
        f = open('%s/config.yaml', 'w')
        f.write("Processes: 64")
        os.system(command)
        while not any(['reconstruction.meshed.json' in os.listdir(root_dir)]):
            sleep(1)
	# do alicia's conversion thing
        return convert(open('%s/%s' % (root_dir, 'reconstruction.meshed.json')))
        #cs = "docker run --rm -it -v /srcimagepath:/imgfoldername opensfm bin/run_all /imgfoldername"
    else:
        print("watNaNNaNNaNNaNNaNNaN")

def convert(json):
    # supposed to convert to obj
    return json

    # loop checking for whether the thing is done processing
    # when it is, produce dictionary response


if __name__ == '__main__':
    app.run(port=9000)
