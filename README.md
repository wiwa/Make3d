# Make3d

Much credit to https://github.com/mapillary/OpenSfM for providing us with a wonderfully packaged, open source, actually working structure from motion implementation. Will give them proper credit with a submodule or something when there's time.

Docker commands:  
Setup (from ~/Make3d/OpenSfM)  

    docker build -t opensfm .

Run computation  

    docker run --rm -it -v /srcimagepath:/imgfoldername opensfm bin/run_all /imgfoldername

Run viewer  

    docker run --rm -it -v /srcimagepath:data/imgfoldername -p 8000:8000 openfsm bin/run_all data/imgfoldername

