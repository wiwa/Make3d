from flask import Flask
import uuid
app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def relay_data():
    if request.method == 'GET':
        # TODO implement?
        pass
    elif request.method == 'POST':
        return "200 OK"
        # assume i have imgs = [...]
        foldername = str(uuid.uuid4())
        root_dir = '/root/%s' % foldername
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

        #cs = "docker run --rm -it -v /srcimagepath:/imgfoldername opensfm bin/run_all /imgfoldername"
    else:
        print("watNaNNaNNaNNaNNaNNaN")



    # loop checking for whether the thing is done processing
    # when it is, produce dictionary response


if __name__ == '__main__':
    app.run()
