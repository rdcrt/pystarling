import os

import dateutil
import responses

from pystarling.api_objects.DirectDebitMandate import DirectDebitMandateStatus, DirectDebitMandateSource
from pystarling.api_services.DirectDebitMandateService import DirectDebitMandateService


class TestDirectDebitMandateService(object):
    @responses.activate
    def test_list_mandates_returns_correct_number_of_mandates(self):
        test_file = os.path.dirname(os.path.realpath(__file__)) + '/responses/v1-list-directdebit_mandates.json'
        file_contents = open(test_file, 'r').read()
        config = {'api_url': 'https://starling_base_url/', 'auth_token': 'stub'}
        responses.add(responses.GET, 'https://starling_base_url/direct-debit/mandates', body=file_contents, status=200)

        direct_debit_mandate_service = DirectDebitMandateService(config)
        test_mandate_list = direct_debit_mandate_service.list()

        assert len(test_mandate_list) == 2

    @responses.activate
    def test_list_mandates_returns_correct_mandate_details(self):
        test_file = os.path.dirname(os.path.realpath(__file__)) + '/responses/v1-list-directdebit_mandates.json'
        file_contents = open(test_file, 'r').read()
        config = {'api_url': 'https://starling_base_url/', 'auth_token': 'stub'}
        responses.add(responses.GET, 'https://starling_base_url/direct-debit/mandates', body=file_contents, status=200)

        direct_debit_mandate_service = DirectDebitMandateService(config)
        test_mandate_list = direct_debit_mandate_service.list()

        assert test_mandate_list[1].uid == "a16445a6-7aa3-4ed8-9dd0-275f200c461c"
        assert test_mandate_list[1].reference == "2134589234"
        assert test_mandate_list[1].status == DirectDebitMandateStatus.LIVE
        assert test_mandate_list[1].source == DirectDebitMandateSource.ELECTRONIC
        assert test_mandate_list[1].created == dateutil.parser.parse("2017-03-15T10:44:21.111Z")
        assert test_mandate_list[1].cancelled == dateutil.parser.parse("2017-04-26T11:55:22.234Z")
        assert test_mandate_list[1].originator_name == "SSE ENERGY LTD"
        assert test_mandate_list[1].originator_uid == "fb679c77-5e60-4f80-9074-eb8fa7754875"

    @responses.activate
    def test_list_mandates_returns_correct_mandate_details(self):
        test_file = os.path.dirname(os.path.realpath(__file__)) + '/responses/v1-get-directdebit_mandate.json'
        file_contents = open(test_file, 'r').read()
        config = {'api_url': 'https://starling_base_url/', 'auth_token': 'stub'}
        responses.add(responses.GET, 'https://starling_base_url/direct-debit/mandates/dfdf686e-551c-4c16-bd06'
                                     '-aee9be00d31e',
                      body=file_contents, status=200)

        direct_debit_mandate_service = DirectDebitMandateService(config)
        get_mandate = direct_debit_mandate_service.get("dfdf686e-551c-4c16-bd06-aee9be00d31e")

        assert get_mandate.uid == "dfdf686e-551c-4c16-bd06-aee9be00d31e"
        assert get_mandate.reference == "5128749125"
        assert get_mandate.status == DirectDebitMandateStatus.LIVE
        assert get_mandate.source == DirectDebitMandateSource.PAPER
        assert get_mandate.created == dateutil.parser.parse("2017-01-10T10:22:24.324Z")
        assert get_mandate.cancelled == dateutil.parser.parse("2017-04-12T10:33:24.362Z")
        assert get_mandate.originator_name == "THAMES WATER LTD"
        assert get_mandate.originator_uid == "0a552c73-6f29-493e-89d4-2714fb403995"
