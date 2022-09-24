from flask import Flask, request
from flask_cors import CORS
from flask_restx import Resource, Api
from flask_pymongo import PyMongo
from pymongo.collection import Collection

from .model import Company

# Configure Flask & Flask-PyMongo:
app = Flask(__name__)
# allow access from everywhere
cors = CORS()
cors.init_app(app, resources={r"*": {"origins": "*"}})
app.config["MONGO_URI"] = "mongodb://localhost:27017/companiesdatabase"
pymongo = PyMongo(app)

# Get a reference to the companies collection.
companies: Collection = pymongo.db.companies

api = Api(app)


class CompaniesList(Resource):
    def get(self, args=None):
        args = request.args.to_dict()
        print(args)
        if args['category'] == 'All':
            cursor = companies.find()
        else:
            cursor = companies.find(args)
        return [Company(**doc).to_json() for doc in cursor]


class Companies(Resource):
    def get(self, id):
        import pandas as pd
        from statsmodels.tsa.ar_model import AutoReg
        # search for the company by ID
        cursor = companies.find_one_or_404({"id": id})
        company = Company(**cursor)
        # retrieve args
        args = request.args.to_dict()
        # retrieve the profit
        profit = company.profit
        # add to df
        profit_df = pd.DataFrame(profit).iloc[::-1]

        if args['algorithm'] == 'random':
            # retrieve the profit value from 2021
            prediction_value = int(profit_df["value"].iloc[-1])
            # add the value to profit list at position 0
            company.profit.insert(0, {'year': 2022, 'value': prediction_value})
        elif args['algorithm'] == 'regression':
            # create model
            model_ag = AutoReg(endog=profit_df['value'], lags=1, trend='c', seasonal=False, exog=None, hold_back=None,
                               period=None, missing='none')
            # train the model
            fit_ag = model_ag.fit()
            # predict for 2022 based on the profit data
            prediction_value = fit_ag.predict(start=len(profit_df), end=len(profit_df), dynamic=False).values[0]
            # add the value to profit list at position 0
            company.profit.insert(0, {'year': 2022, 'value': prediction_value})
        return company.to_json()


api.add_resource(CompaniesList, '/companies')
api.add_resource(Companies, '/companies/<int:id>')
