from utils.db import connect_db


class EmissionModel:
    '''
    This layer handles all interaction between service layer and database
    '''

    __table_name__ = "emission"
    __table_name__additional__ = "emission_source"

    # get emission data based on emission source
    @classmethod
    def get_data_by_source(cls, source):
        connection = connect_db()
        with connection:
            with connection.cursor() as cursor:
                cursor.execute(
                    ''' SELECT emission_source, CONCAT('0',`month`, '-',`year`) AS date, amount, carbon_emission
                         FROM successgy.emission WHERE emission_source = %s''', source)
                emission_data = cursor.fetchall()
        return emission_data

    # get all emission data
    @classmethod
    def get_all_data(cls):
        connection = connect_db()
        with connection:
            with connection.cursor() as cursor:
                cursor.execute(
                    ''' SELECT emission_source, CONCAT('0',`month`, '-',`year`) AS date, amount, carbon_emission FROM successgy.emission''')
                emission_data = cursor.fetchall()
        return emission_data

    # add new emision to the database
    @classmethod
    def add_new_emission_data(cls, emission_data):
        connection = connect_db()
        with connection:
            with connection.cursor() as cursor:
                cursor.execute('''INSERT INTO successgy.emission (emission_source, month , year, amount, carbon_emission)
                                    VALUES (%s, %s, %s, %s, %s);''', (emission_data['emission_source'], emission_data['month'],
                                                                      emission_data['year'], emission_data['amount'], emission_data['carbon_emission']))
                connection.commit()

    # get conversion rate based on source requested
    @classmethod
    def get_rate_by_source(cls, source):
        connection = connect_db()
        with connection:
            with connection.cursor() as cursor:
                cursor.execute(
                    ''' SELECT conversion_rate FROM successgy.emission_source WHERE emission_source = %s''', source)
                conversion_rate = cursor.fetchone()
        return conversion_rate
