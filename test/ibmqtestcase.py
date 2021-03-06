# -*- coding: utf-8 -*-

# This code is part of Qiskit.
#
# (C) Copyright IBM 2017, 2019.
#
# This code is licensed under the Apache License, Version 2.0. You may
# obtain a copy of this license in the LICENSE.txt file in the root directory
# of this source tree or at http://www.apache.org/licenses/LICENSE-2.0.
#
# Any modifications or derivative works of this code must retain this
# copyright notice, and modified files need to carry a notice indicating
# that they have been altered from the originals.

"""Custom TestCase for IBMQProvider."""

from qiskit.test import QiskitTestCase


class IBMQTestCase(QiskitTestCase):
    """Custom TestCase for use with the IBMQProvider."""

    def tearDown(self):
        # Reset the default providers, as in practice they acts as a singleton
        # due to importing the wrapper from qiskit.
        from qiskit.providers.ibmq import IBMQ
        IBMQ._v1_provider._accounts.clear()
        IBMQ._providers.clear()
        IBMQ._credentials = None

        from qiskit.providers.basicaer import BasicAer
        BasicAer._backends = BasicAer._verify_backends()
