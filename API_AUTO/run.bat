cd ./testCase
pytest -vs --alluredir ../report/reportallure --clean-alluredir
allure serve ../report/reportallure