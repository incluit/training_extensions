# INTEL CONFIDENTIAL
#
# Copyright (C) 2021 Intel Corporation
#
# This software and the related documents are Intel copyrighted materials, and
# your use of them is governed by the express license under which they were provided to
# you ("License"). Unless the License provides otherwise, you may not use, modify, copy,
# publish, distribute, disclose or transmit this software or the related documents
# without Intel's prior written permission.
#
# This software and the related documents are provided as is,
# with no express or implied warranties, other than those that are expressly stated
# in the License.

import numpy as np
import pytest

from ote_sdk.entities.tensor import TensorEntity
from ote_sdk.tests.constants.ote_sdk_components import OteSdkComponent
from ote_sdk.tests.constants.requirements import Requirements

RANDOM_NUMPY = np.random.randint(low=0, high=255, size=(16, 32, 3))


@pytest.mark.components(OteSdkComponent.OTE_SDK)
class TestTensorEntity:
    @staticmethod
    def tensor_params():
        return {"name": "Test Tensor", "numpy": RANDOM_NUMPY}

    def tensor(self):
        return TensorEntity(**self.tensor_params())

    @pytest.mark.priority_medium
    @pytest.mark.component
    @pytest.mark.reqids(Requirements.REQ_1)
    def test_tensor_initialization(self):
        """
        <b>Description:</b>
        Check TensorEntity class object initialization

        <b>Input data:</b>
        TensorEntity class object with specified "name" and "numpy" parameters

        <b>Expected results:</b>
        Test passes if attributes of initialized TensorEntity class object are equal to expected
        """
        tensor_params = self.tensor_params()
        tensor = TensorEntity(**tensor_params)
        assert tensor.name == tensor_params.get("name")
        assert np.array_equal(tensor.numpy, tensor_params.get("numpy"))

    @pytest.mark.priority_medium
    @pytest.mark.component
    @pytest.mark.reqids(Requirements.REQ_1)
    def test_tensor_shape(self):
        """
        <b>Description:</b>
        Check TensorEntity class object "shape" property

        <b>Input data:</b>
        TensorEntity class object with specified "name" and "numpy" parameters

        <b>Expected results:</b>
        Test passes if value returned by "shape" property is equal to expected

        <b>Steps</b>
        1. Check value returned by "shape" property for initialized TensorEntity object
        2. Manually set new value of "numpy" property and check re-check "numpy" and "shape" properties
        """
        # Checking values returned by "shape" property for initialized TensorEntity object
        tensor = self.tensor()
        assert tensor.shape == (16, 32, 3)
        # Manually setting new value of "numpy" property and re-checking "numpy and "shape" properties
        new_numpy = np.random.uniform(low=0.0, high=255.0, size=(8, 16, 3))
        tensor.numpy = new_numpy
        assert np.array_equal(tensor.numpy, new_numpy)
        assert tensor.shape == (8, 16, 3)

    @pytest.mark.priority_medium
    @pytest.mark.component
    @pytest.mark.reqids(Requirements.REQ_1)
    def test_tensor_eq(self):
        """
        <b>Description:</b>
        Check TensorEntity class object __eq__ method

        <b>Input data:</b>
        TensorEntity class objects with specified "name" and "numpy" parameters

        <b>Expected results:</b>
        Test passes if value returned by __eq__ method is equal to expected

        <b>Steps</b>
        1. Check value returned by __eq__ method for comparing equal TensorEntity objects
        2. Check value returned by __eq__ method for comparing TensorEntity objects with unequal "name" parameters:
        expected equality
        3. Check value returned by __eq__ method for comparing TensorEntity objects with unequal "numpy" parameters -
        expected inequality
        4. Check value returned by __eq__ method for comparing TensorEntity with different type object
        """
        initialization_params = self.tensor_params()
        tensor = TensorEntity(**initialization_params)
        # Comparing equal TensorEntity objects
        equal_tensor = TensorEntity(**initialization_params)
        assert tensor == equal_tensor
        # Comparing TensorEntity objects with unequal "name" parameter, expected equality
        unequal_params = dict(initialization_params)
        unequal_params["name"] = "Unequal_name"
        equal_tensor = TensorEntity(**unequal_params)
        assert tensor == equal_tensor
        # Comparing TensorEntity objects with unequal "numpy" parameter, expected inequality
        unequal_params = dict(initialization_params)
        unequal_params["numpy"] = np.random.uniform(low=0.0, high=255.0, size=(1, 2, 3))
        unequal_tensor = TensorEntity(**unequal_params)
        assert tensor != unequal_tensor
        # Comparing TensorEntity with different type object
        assert tensor != str

    @pytest.mark.priority_medium
    @pytest.mark.component
    @pytest.mark.reqids(Requirements.REQ_1)
    def test_tensor_str(self):
        """
        <b>Description:</b>
        Check TensorEntity class object __str__ method

        <b>Input data:</b>
        TensorEntity class object with specified "name" and "numpy" parameters

        <b>Expected results:</b>
        Test passes if value returned by __str__ method is equal to expected
        """
        tensor = self.tensor()
        assert str(tensor) == "TensorEntity(name=Test Tensor, shape=(16, 32, 3))"

    @pytest.mark.priority_medium
    @pytest.mark.component
    @pytest.mark.reqids(Requirements.REQ_1)
    def test_tensor_repr(self):
        """
        <b>Description:</b>
        Check TensorEntity class object __repr__ method

        <b>Input data:</b>
        TensorEntity class object with specified "name" and "numpy" parameters

        <b>Expected results:</b>
        Test passes if value returned by __repr__ method is equal to expected
        """
        tensor = self.tensor()
        assert repr(tensor) == f"TensorEntity(name=Test Tensor, numpy={tensor.numpy})"
