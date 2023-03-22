"""Module containing models representing patients and their data.

The Model layer is responsible for the 'business logic' part of the software.

Patients' data is held in an inflammation table (2D array) where each row contains 
inflammation data for a single patient taken over a number of days 
and each column represents a single day across all patients.
"""

import numpy as np

def dail_above_threshold(data, threshold, patient_num):
    """Determine whether a patient's data exceeds a threshold.
    using map and lambda functions

    Parameters
    ----------
    data: np.array
        Array of patient data
    threshold: int
        Threshold value
    patient_num: int
        Patient number

    Returns
    -------
    bool
        True if patient data exceeds threshold, False otherwise
    """

    return list(map(lambda x: x > threshold, data[patient_num]))


def patient_normalise(data):
    """
    Normalise patient data from a 2D inflammation data array.

    NaN values are ignored, and normalised to 0.

    Negative values are rounded to 0.
    """

    if np.any(data < 0):
        raise ValueError('Inflammation values should not be negative')

    max_data = np.nanmax(data, axis=1)
    with np.errstate(invalid='ignore', divide='ignore'):
        normalised = data / max_data[:, np.newaxis]
    normalised[np.isnan(normalised)] = 0
    normalised[normalised < 0] = 0
    return normalised

def load_csv(filename):
    """Load a Numpy array from a CSV

    Parameters
    ----------
    filename: string
        Filename of CSV to load

    Returns
    -------
    np.array
        array of inflammation data
    """
    return np.loadtxt(fname=filename, delimiter=",")


def daily_mean(data):
    """Calculate the daily mean of a 2D inflammation data array.

    Parameters
    ----------
    data: float
        2D array of inflammation data

    Returns
    -------
    np.array
        1D array of daily mean inflammation values

    """
    return np.mean(data, axis=0)

def daily_std(data):
    """Calculate the daily standard deviation of a 2D inflammation data array.

    Parameters
    ----------
    data: float
        2D array of inflammation data

    Returns
    -------
    np.array
        1D array of daily standard deviation inflammation values

    """
    return np.std(data, axis=0)


def daily_max(data):
    """Calculate the daily max of a 2D inflammation data array.

    Parameters
    ----------
    data: float
        2D array of inflammation data

    Returns
    -------
    np.array
        1D array of daily max inflammation values

    """
    return np.max(data, axis=0)


def daily_min(data):
    """Calculate the daily min of a 2D inflammation data array.

    Parameters
    ----------
    data: float
        2D array of inflammation data

    Returns
    -------
    np.array
        1D array of daily min inflammation values

    """
    return np.min(data, axis=0)
