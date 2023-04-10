
PYTHONPATH="config:device:network:system:web:dummy"
export PYTHONPATH
echo "TESTSUITE is executed ..."
echo $PYTHONPATH
echo "-----------------------------------------------------------------"
# python3 -c "from app import App; App.test_system()" app.py
echo "-----------------------------------------------------------------"
# python3 -c "from app import App; App.test_config()" app.py
echo "-----------------------------------------------------------------"
# python3 -c "from app import App; App.test_device()" app.py
echo "-----------------------------------------------------------------"
python3 -c "from app import App; App.test_network()" app.py
echo "-----------------------------------------------------------------"

