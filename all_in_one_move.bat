echo 0

python .\functions\remove_n_move.py
echo 1

.\share\subdir-batch-face-detector-for-spoof-dataset.exe -f="C:\vs2015shareddata\dataset\MY Profiles\temp" -p=1
echo 2

python .\functions\run_through_folders.py -c "python .\dl\face_clustering_extract.py -i [path] -e [path\result]#python .\dl\face_clustering_output_2.py -e [path\result]" -p "C:\vs2015shareddata\dataset\MY Profiles\temp-cropped" -w 0
echo 3
