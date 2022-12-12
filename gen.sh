
if [ $# -eq 0 ]
  then
    echo "No arguments supplied"
    exit 1
fi

mkdir "day-$1"
cd "day-$1"
touch input
touch part-1.py
touch part-2.py
echo "Finished."
