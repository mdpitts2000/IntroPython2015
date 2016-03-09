#!/usr/bin/env python3

"""
test code for testing the budget application 
"""
import pytest

from BudgetApp import SumFundingResources


def test_SumFundingResources():
    '''
    tests income sources summation
    '''
    total = SumFundingResources(10, 20, 100,10,10)
    assert total == 150

