# Make3d

Docker commands:
Setup (from ~/Make3d/OpenSfM)  
    docker build -t opensfm .

Run computation  
    docker run --rm -it -v /srcimagepath:/imgfoldername opensfm bin/run_all /imgfoldername

Run viewer  
    docker run --rm -it -v /srcimagepath:data/imgfoldername -p 8000:8000 openfsm bin/run_all data/imgfoldername

