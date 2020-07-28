set -e 

# sentistrength
mkdir -p data/sentistrength
pushd data/sentistrength
# downlad
wget http://sentistrength.wlv.ac.uk/SentiStrength5.jar # HTTP 403 sophos!!!
wget http://sentistrength.wlv.ac.uk/SentStrength_Data_Sept2011.zip
# extract
unzip -d SentStrength_Data SentStrength_Data_Sept2011.zip

popd