from repo.emission import EmissionModel
from utils.db import log

log = log


class EmissionServices:
    '''
      This layer handles all logical interaction between handler layer and repo layer
    '''

    # add new emision to the database 
    @classmethod
    def add_emission_record(cls, emission_data):
        emission_data['month'] = int(emission_data['date'].split('-')[0])
        emission_data['year'] = int(emission_data['date'].split('-')[1])
        emission_data.pop('date')
        conversion_rate = EmissionModel.get_rate_by_source(emission_data['emission_source'])['conversion_rate']
        emission_data['carbon_emission'] = emission_data['amount'] * conversion_rate
        EmissionModel.add_new_emission_data(emission_data)
