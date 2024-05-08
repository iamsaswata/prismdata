:py:mod:`prismdata.core`
========================

.. py:module:: prismdata.core


Module Contents
---------------


Functions
~~~~~~~~~

.. autoapisummary::

   prismdata.core.download_prism



.. py:function:: download_prism(start: str = None, end: Optional[str] = None, variable: str = None, freq: Optional[str] = 'daily', download_dir: Optional[str] = None, unzip: Optional[bool] = True, remove_zip: Optional[bool] = True) -> None

   Downloads PRISM data within a specified time range and frequency.

   Args:
       start (str): The start date of the data range in 'YYYYMMDD' | 'YYYYMM' | 'YYYY' format. Defaults to None.  

       end (str, optional): The end date of the data range in 'YYYYMMDD' | 'YYYYMM' | 'YYYY' format. Defaults to None.  

       variable (str): The PRISM variable to be downloaded. Options are: "ppt", "tmin", "tmax", "tmean", "tdmean", "vpdmin" and "vpdmax". 

       freq (str, optional): The frequency of the data to be downloaded. Options: daily, monthly and annual. Defaults to "daily".  

       download_dir (str, optional): The directory where the downloaded data will be saved. Defaults to "data" under current directory.  

       unzip (bool, optional): If True, the downloaded zip files will be unzipped. Defaults to True.  

       remove_zip (bool, optional): If True, the downloaded zip files will be removed. Defaults to True.  



