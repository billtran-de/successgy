from repo.emission import EmissionModel
from utils.db import log

log = log


class EmissionServices:
    '''
      This layer handles all logical interaction between handler layer and repo layer
    '''

    # get data for each emission source table in the UI
    @classmethod
    def get_emission_table(cls, source):
      if source:
        emission_data = EmissionModel.get_data_by_source(source)
      else:
        emission_data = EmissionModel.get_all_data()
      for row in emission_data:
        row['amount'] = float(row['amount'])
        row['carbon_emission'] = float(row['carbon_emission'])
      return emission_data

    # add new emision to the database 
    @classmethod
    def add_emission_record(cls, emission_data):
        emission_data['month'] = int(emission_data['date'].split('-')[0])
        emission_data['year'] = int(emission_data['date'].split('-')[1])
        emission_data.pop('date')
        conversion_rate = EmissionModel.get_rate_by_source(emission_data['emission_source'])['conversion_rate']
        emission_data['carbon_emission'] = emission_data['amount'] * conversion_rate
        EmissionModel.add_new_emission_data(emission_data)
