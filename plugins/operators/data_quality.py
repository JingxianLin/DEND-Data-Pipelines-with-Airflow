from airflow.hooks.postgres_hook import PostgresHook
from airflow.models import BaseOperator
from airflow.utils.decorators import apply_defaults

class DataQualityOperator(BaseOperator):

    ui_color = '#89DA59'

    @apply_defaults
    def __init__(self,
                 # Define your operators params (with defaults) here
                 # Example:
                 # conn_id = your-connection-name
                 redshift_conn_id='',
                 test_query='',
                 expected_result='',
                 *args, **kwargs):

        super(DataQualityOperator, self).__init__(*args, **kwargs)
        # Map params here
        # Example:
        # self.conn_id = conn_id
        self.redshift_conn_id=redshift_conn_id
        self.test_query=test_query
        self.expected_result=expected_result

    def execute(self, context):
        self.log.info('DataQualityOperator implemented')
        redshift_hook=PostgresHook(postgres_conn_id=redshift_conn_id)
        
        self.log.info('DataQuality testing...')
        record=redshift_hook.get_records(self.test_query)
        if record[0][0] == self.expected_result:
            self.log.info('DataQuality check passed!')
        else:
            raise ValueError(f'DataQuality check failed!')