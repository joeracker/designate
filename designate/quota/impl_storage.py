# Copyright 2013 Hewlett-Packard Development Company, L.P.
#
# Author: Kiall Mac Innes <kiall@hp.com>
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.
from designate.openstack.common import log as logging
from designate.quota.base import Quota
from designate import storage

LOG = logging.getLogger(__name__)


class StorageQuota(Quota):
    def __init__(self):
        super(StorageQuota, self).__init__()

        # Get a storage connection
        self.storage = storage.get_storage()

    def _get_tenant_quotas(self, context, tenant_id):
        criterion = dict(
            tenant_id=tenant_id
        )

        quotas = self.storage.find_quotas(context, criterion)

        return dict((q['resource'], q['hard_limit']) for q in quotas)
